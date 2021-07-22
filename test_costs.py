from requests.api import delete
from ooti import ooti
import unittest
from factories import EmployeeContractFactory, EmployeePeriodFactory, ExpenseGroupFactory, FreelancerFactory, JobFactory, JobInvoiceFactory, OrguserFactory, ProjectFactory, TeamFactory, CostFactory, CostMonthFactory

OOTI_USERNAME = 'root@root.com'
OOTI_PASSWORD = 'root'

sdk = ooti.Auth(OOTI_USERNAME, OOTI_PASSWORD)
sdk.connect()


class TestFreelancers(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.freelancer = FreelancerFactory()

    def test_get_freelancer_details(self):
        response = sdk.Costs.get_freelancer_details(self.freelancer['pk'])
        self.assertEqual(response['status'], 200)

    def test_get_freelancers_list(self):
        response = sdk.Costs.get_freelancers_list()
        self.assertEqual(response['status'], 200)

    def test_delete_freelancer(self):
        freelancer = FreelancerFactory()
        response = sdk.Costs.delete_freelancer(freelancer['pk'])
        self.assertEqual(response['status'], 204)

    def test_create_freelancer(self):
        payload = {
            'name': 'freelancer test'
        }
        response = sdk.Costs.create_freelancer(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_freelancer(response['data']['pk'])
        self.assertEqual(delete['status'], 204)


class TestEmployees(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.orguser = OrguserFactory()
        cls.team_pk = TeamFactory()
        cls.employee_contract = EmployeeContractFactory()

    def test_create_employee_contract(self):
        payload = {
            'orguser': self.orguser['id'],
            'team': self.team_pk,
            'status': 'active',
            'end_date': '20-10-2022',
        }
        response = sdk.Costs.create_employees_contract(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_employees_contract(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_delete_employee_contract(self):
        employee_contract = EmployeeContractFactory()
        response = sdk.Costs.delete_employees_contract(employee_contract['id'])
        self.assertEqual(response['status'], 204)

    def test_create_employees_period(self):
        payload = {
            "contract": self.employee_contract['id'],
            "notes": "some notes",
            "start_date": "09-05-2021",
            "end_date": "20-05-2021",
            "status": "active",
            "salary_daily_gross": 100,
            "salary_hourly_gross": 10,
            "salary_gross_coefficent": 1,
            "salary_monthly_net": 1200,
            "salary_monthly_gross": 1500,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 30,
            "daily_hours_limit": 5,
            "overtime_enabled": True,
            "overtime_hours_limit": 5,
            "days_per_week": 6
        }
        response = sdk.Costs.create_employees_period(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_employees_period(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_delete_employees_period(self):
        employee_period = EmployeePeriodFactory()
        response = sdk.Costs.delete_employees_period(employee_period['id'])
        self.assertEqual(response['status'], 204)


class TestExpenses(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.expense_group = ExpenseGroupFactory(team_pk=cls.team_pk)

    def test_create_expenses_category(self):
        payload = {
            'name': 'expense category test'
        }
        response = sdk.Costs.create_expenses_category(payload)
        self.assertEqual(response['status'], 201)

    def test_create_expenses_group(self):
        payload = {
            'description': 'expense group test'
        }
        response = sdk.Costs.create_expenses_group(payload, team_pk=self.team_pk)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_expenses_group(response['data']['id'])
        self.assertEqual(delete['status'], 204)
        response = sdk.Costs.create_expenses_group(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_expenses_group(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_expenses_group_action(self):
        payload = {
            'team': self.team_pk,
            'is_validated': True,
        }
        response = sdk.Costs.create_expenses_group_action(payload)
        self.assertEqual(response['status'], 200)

    def test_create_expense(self):
        payload = {
            'amount': '10',
            'date': '10-10-2021',
        }
        response = sdk.Costs.create_expense(payload)

        self.assertEqual(response['status'], 400)

        payload['expense_group'] = self.expense_group['id']
        response = sdk.Costs.create_expense(payload)
        self.assertEqual(response['status'], 201)
        payload = {
            'amount': '10',
            'date': '10-10-2021',
        }
        response = sdk.Costs.create_expense(payload, team_pk=self.team_pk, expense_group_id=self.expense_group['id'])
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_expense(response['data']['id'])
        self.assertEqual(delete['status'], 204)
    """
    def test_add_multiple_expenses(self):
        payload = {}
        response = sdk.Costs.add_multiple_expenses(payload, expense_group_id=self.expense_group['id'])
        self.assertEqual(response['status'], 201)
    """


class TestCosts(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.cost = CostFactory(cls.team_pk)
        cls.cost_month = CostMonthFactory(team_pk=cls.team_pk, cost_id=cls.cost['id'])

    def test_create_cost(self):
        payload = {
            "amount_actual": 10,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "title": "string",
            "year": 0,
            "team": self.team_pk,
            "months": []
        }
        response = sdk.Costs.create_cost(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_cost(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_get_costs_list(self):
        response = sdk.Costs.get_costs_list()
        self.assertEqual(response['status'], 200)

    def test_create_costs_month(self):
        payload = {
            "fixed_cost": self.cost['id'],
            "team": self.team_pk,
            "amount_budgeted": 120,
            "amount_actual": 100,
            "year": 2020,
            "month": 3
        }
        response = sdk.Costs.create_costs_month(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_costs_month(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_delete_cost(self):
        cost = CostFactory(self.team_pk)
        response = sdk.Costs.delete_cost(cost['id'])
        self.assertEqual(response['status'], 204)

    def test_delete_costs_month(self):
        cost_month = CostMonthFactory(self.team_pk, self.cost['id'])
        response = sdk.Costs.delete_costs_month(cost_month['id'])
        self.assertEqual(response['status'], 204)

    def test_update_costs_month_details(self):
        payload = {
            "fixed_cost": self.cost['id'],
            "team": self.team_pk,
            "amount_budgeted": 150,
            "amount_actual": 130,
            "year": 2019,
            "month": 6
        }
        response = sdk.Costs.update_costs_month_details(self.cost_month['id'], payload)
        self.assertEqual(response['status'], 200)

    def test_update_cost_details(self):
        payload = {
            "amount_actual": 12,
            "amount_budgeted": 10,
            "description": "new description",
            "type": "monthly",
            "month": 10,
            "title": "updated cost",
            "year": 2020,
            "team": self.team_pk,
            "months": []
        }
        response = sdk.Costs.update_cost_details(self.cost['id'], payload)
        self.assertEqual(response['status'], 200)

    def test_get_costs_months_list(self):
        response = sdk.Costs.get_costs_months_list()
        self.assertEqual(response['status'], 200)


class TestJobs(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.project = ProjectFactory()
        cls.job = JobFactory()
        cls.job_invoice = JobInvoiceFactory()

    def test_create_job(self):
        payload = {
            'title': 'job test',
        }
        response = sdk.Costs.create_job(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'title': 'job test',
            'project': self.project['id'],
        }
        response = sdk.Costs.create_job(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_job(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_job_invoice(self):
        payload = {
            'team': self.team_pk,
            'date': '19-03-2020',
            'amount': '10',
        }
        response = sdk.Costs.create_jobs_invoice(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_jobs_invoice(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_jobs_invoices_item(self):
        payload = {
            'project': self.project['id'],
        }
        response = sdk.Costs.create_jobs_invoices_item(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'invoice': self.job_invoice['id'],
            'project': self.project['id'],
        }
        response = sdk.Costs.create_jobs_invoices_item(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_jobs_invoices_item(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_job_month(self):
        payload = {
            'job': self.job['id'],
            'year': '2021',
        }
        response = sdk.Costs.create_jobs_month(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Costs.delete_jobs_month(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_generate_jobs_invoices_items(self):
        payload = {}
        response = sdk.Costs.generate_jobs_invoices_items(payload)
        self.assertEqual(response['status'], 404)
        payload = {
            'invoice': self.job_invoice['id']
        }
        response = sdk.Costs.generate_jobs_invoices_items(payload)
        self.assertEqual(response['status'], 200)


if __name__ == '__main__':
    unittest.main()
