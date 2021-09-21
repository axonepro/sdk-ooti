
# To read .env variables
import os
from dotenv import load_dotenv
from test_helper import TestHelper
import sys

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

testHelper = TestHelper(sdk)
team_pk = testHelper._get_selected_team()


def UserFactory():
    response = sdk.Profiles.get_profile_details()
    return response['data']['user']


def OrguserFactory():
    payload = {
        "email": "test@test.fr",
        "first_name": "Julie",
        "last_name": "TEST",
    }
    response = sdk.Orgusers.create_orguser(payload)
    if response['status'] == 201:
        return response['data']
    else:
        print(response)
        return None


def TeamFactory():
    response = sdk.Profiles.get_profile_details()
    return response['data']['selected_team']


def OrguserPkFactory(org_pk=None):
    response = sdk.Organizations.get_user_organization_details()
    organizations = response['data']['organizations']
    if org_pk is not None:
        organization = next((org for org in organizations if org.get('id') == org_pk), None)
    else:
        organization = organizations[0]
    return organization['orguser']['pk']


def ProjectFactory(team_pk=None):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    payload = {
        'project_title': 'project test',
    }
    response = sdk.Projects.create_project(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def CostFactory(team_pk=None):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    payload = {
        'amount_actual': 10,
        'amount_budgeted': 0,
        'description': 'string',
        'type': 'monthly',
        'title': 'string',
        'year': 0,
        'team': team_pk,
        'months': []
    }
    response = sdk.Costs.create_cost(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def CostMonthFactory(team_pk=None, cost_id=None):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
        cost_id = CostFactory(team_pk)['id']
    elif not cost_id:
        cost_id = CostFactory(team_pk)
    payload = {
        'fixed_cost': cost_id,
        'team': team_pk,
        'amount_budgeted': 120,
        'amount_actual': 100,
        'year': 2020,
        'month': 3
    }
    response = sdk.Costs.create_costs_month(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def EmployeeContractFactory(orguser_pk=None, team_pk=None):
    if not orguser_pk:
        orguser_pk = OrguserFactory()['pk']
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    payload = {
        'orguser': orguser_pk,
        'team': team_pk,
        'status': 'active',
        'end_date': '20-10-2022',
    }
    response = sdk.Employees.create_employees_contract(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def EmployeePeriodFactory(employee_contract_pk=None):
    if not employee_contract_pk:
        employee_contract_pk = EmployeeContractFactory()['id']
    payload = {
        'contract': employee_contract_pk,
        'notes': 'some notes',
        'start_date': '09-05-2021',
        'end_date': '20-05-2021',
        'status': 'active',
        'salary_daily_gross': 100,
        'salary_hourly_gross': 10,
        'salary_gross_coefficent': 1,
        'salary_monthly_net': 1200,
        'salary_monthly_gross': 1500,
        'salary_loaded_coefficent': 0,
        'weekly_hours_limit': 30,
        'daily_hours_limit': 5,
        'overtime_enabled': True,
        'overtime_hours_limit': 5,
        'days_per_week': 6
    }
    response = sdk.Employees.create_employees_period(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def FreelancerFactory():
    payload = {
        'name': 'test freelancer'
    }
    response = sdk.Employees.create_freelancer(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def ExpenseGroupFactory(team_pk):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    payload = {
        'description': 'expense group test'
    }
    response = sdk.Expenses.create_expenses_group(payload, team_pk=team_pk)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def JobFactory(project_pk=None):
    if not project_pk:
        project_pk = ProjectFactory()['id']
    payload = {
        'title': 'job test',
        'project': project_pk,
    }
    response = sdk.Jobs.create_job(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def JobInvoiceFactory(team_pk=None, contractor_id=None):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    if not contractor_id:
        contractor_id = ContractorFactory()['id']
    payload = {
        'contractor': contractor_id,
        'team': team_pk,
        'date': '19-03-2020',
        'amount': '10',
    }
    response = sdk.Jobs.create_jobs_invoice(payload)
    if response['status'] == 201:
        return response['data']
    else:
        print(response)
        return None


def TaskFactory():
    payload = {'title': 'task test'}
    response = sdk.Tasks.create_task(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def PostFactory():
    payload = {
        "title": "post test",
    }
    response = sdk.Posts.create_post(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def AlbumFactory(post_pk=None):
    if not post_pk:
        post_pk = PostFactory()['pk']
    payload = {
        "post": post_pk,
        "title": "album test",
    }
    response = sdk.Posts.create_posts_album(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def GoalFactory(team_pk=None):
    if not team_pk:
        team_pk = testHelper._get_selected_team()
    payload = {
        'team': team_pk,
        'name': 'goal test'
    }
    response = sdk.Goals.create_goal(payload)
    if response['status'] == 201:
        return response['data']
    else:
        return None


def ContractorFactory():
    payload = {
        'name': 'contractor test',
        'tags': [],
    }
    response = sdk.Contracts.create_contractors(payload)
    if response['status'] == 201:
        return response['data']
    else:
        print(response)
        return None
