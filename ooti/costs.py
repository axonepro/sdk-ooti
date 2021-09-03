import requests
import json

from .helper import Helper


class Costs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Costs ####

    def copy_costs_fee_allocations_from_contract_hours(self, project_id):  # ?
        """ Copy cost fee allocations from contract hours

        Keywords arguments:
        project_id -- id of the project
        data -- fee project to be copied
        {
            "fee_project": fee_project_pk
        }
        """
        route = 'v1/costs/copy-fee-allocations-from-contract-hours/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def copy_costs_fee_allocations_from_subcontractor_fees(self, project_id):  # ?
        """ Copy cost fee allocations from subcontractor fees

        Keywords arguments:
        project_id -- id of the project
        data -- fee project to be copied
        {
            "fee_project": fee_project_pk
        }
        """
        route = 'v1/costs/copy-fee-allocations-from-subcontractor-fees/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def copy_costs_previous_year(self):
        """ Copy costs from a previous year

        Keywords arguments:
        data -- year of the costs to be copied
        {
            "year": 0
        }
        """
        route = 'v1/costs/copy-prev-year/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_costs_months_list(self, page=1):
        """ Get the list of costs month """

        route = 'v1/costs/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_costs_month(self, data):
        """ Create a new costs month

        Keywords arguments:
        data -- data of the new cost month to be created:
        {
            "fixed_cost": cost_id, # REQUIRED
            "team": team_pk, # REQUIRED
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/costs/month/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_costs_month_details(self, month_id):
        """ Get the costs month details

        Keywords arguments:
        month_id -- id of the month
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_costs_month_details(self, month_id, data):
        """ Update the costs month details

        Keywords arguments:
        month_id -- id of the month
        data -- content of the update:
        {
            "fixed_cost": cost_id,
            "team": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_costs_month(self, month_id):
        """ Delete the costs month

        Keywords arguments:
        month_id -- id of the month
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def set_costs_annual_budget(self, cost_id, data):
        """ Set the cost annual budget

        Keywords arguments:
        cost_id -- id of the cost
        data -- annual amount budgeted to be set:
        {
            "amount_budgeted": 0
        }
        """
        route = 'v1/costs/set-annual-budget/{0}/'.format(cost_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=data)
        return self.process_response(response)

    def get_costs_list(self, page=1):
        """ Get the list of costs """

        route = 'v1/costs/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_cost(self, data):
        """ Create a new cost

        Keywords arguments:
        data -- data of the new cost to be created:
        {
            "team": team_pk, # REQUIRED
            "amount_actual": 0,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "month": 0,
            "title": "string",
            "year": 0,
            "months": [
                month_id,
                ...
            ]
        }
        """

        route = 'v1/costs/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_cost_details(self, id):
        """ Get the cost details

        Keywords arguments:
        id -- id of the cost
        """

        route = 'v1/costs/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_cost_details(self, id, data):
        """ Update costs month

        Keywords arguments:
        id -- id of the cost
        data -- content of the update:
        {
            "amount_actual": 0,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "month": 0,
            "title": "string",
            "year": 0,
            "team": team_pk,
            "months": [
                month_id,
                ...
            ]
        }
        """

        route = 'v1/costs/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_cost(self, id):
        """ Delete the cost

        Keywords arguments:
        id -- id of the cost
        """

        route = 'v1/costs/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Employees ####

    def get_employees_contracts_list(self, page=1):
        """ Get the employees contracts """

        route = 'v1/employees/contracts/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_employees_contract(self, data):
        """ Create a new employees 

        Keywords arguments:
        data -- data of the new contract to be created:
        {
            "team": team_pk,
            "orguser": orguser_pk,
            "status": "string",
            "start_date": "string",
            "end_date": "string",
            "cancel_date": "string",
            "notes": "string",
            "currency": currency_pk,
            "pay_type": "string",
            "admin_only": true,
            "contract_type": "string",
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0,
            "file": "string",
            "salary_monthly_gross": 0,
            "salary_hourly_gross": 0,
            "salary_loaded_coefficent": 0,
            "salary_daily_gross": 0
        }
        """

        route = 'v1/employees/contracts/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_employees_contracts_details(self, contract_id):
        """ Get employees contract details 

        Keywords arguments:
        contract_id -- id of the employees contract
        """

        route = 'v1/employees/contracts/{0}/'.format(contract_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_employees_contracts_details(self, contract_id, data):
        """ Get employees contract details 

        Keywords arguments:
        contract_id -- id of the employees contract
        data -- content of the update:
        {
            "team": team_pk,
            "orguser": orguser_pk,
            "status": "string",
            "start_date": "string",
            "end_date": "string",
            "cancel_date": "string",
            "notes": "string",
            "currency": currency_pk,
            "pay_type": "string",
            "admin_only": true,
            "contract_type": "string",
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0,
            "file": "string",
            "salary_monthly_gross": 0,
            "salary_hourly_gross": 0,
            "salary_loaded_coefficent": 0,
            "salary_daily_gross": 0
        }
        """

        route = 'v1/employees/contracts/{0}/'.format(contract_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_employees_contract(self, contract_id):
        """ Delete employees contract

        Keywords arguments:
        contract_id -- id of the employees contract
        """

        route = 'v1/employees/contracts/{0}/'.format(contract_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_employees_period_list(self, page=1):
        """ Get the list of employees periods """

        route = 'v1/employees/period/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_employees_period(self, data):
        """ Create a new employees period

        Keywords arguments:
        data -- data of the new period to be created:
        {
            "contract": contract_id, # REQUIRED
            "notes": "string",
            "start_date": "string",
            "end_date": "string",
            "status": "string",
            "salary_daily_gross": 0,
            "salary_hourly_gross": 0,
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "salary_monthly_gross": 0,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0
        }
        """

        route = 'v1/employees/period/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_employees_period_details(self, period_id):
        """ Get employees period details

        Keywords arguments:
        period_id -- id of the period
        """

        route = 'v1/employees/period/{0}/'.format(period_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_employees_period_details(self, period_id, data):
        """ Update the employees period details 

        Keywords arguments:
        period_id -- id of the period
        data -- content of the update:
        {
            "contract": contract_id,
            "notes": "string",
            "start_date": "string",
            "end_date": "string",
            "status": "string",
            "salary_daily_gross": 0,
            "salary_hourly_gross": 0,
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "salary_monthly_gross": 0,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0
        }
        """

        route = 'v1/employees/period/{0}/'.format(period_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_employees_period(self, period_id):
        """ Delete the employees period

        Keywords arguments:
        period_id -- id of the period
        """

        route = 'v1/employees/period/{0}/'.format(period_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Expenses ####

    # DELETE on v1/expenses/{expense_group_pk}/versions/{version_pk}/delete/ ?

    def get_expenses_categories_list(self, page=1):
        """ Get the list of expenses categories """

        route = 'v1/expenses/category/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_expenses_category(self, data):
        """ Create a new expenses category 

        Keywords arguments:
        data -- data of the new expenses category to be created:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "accounting_code": "string",
            "vat": "string"
        }
        """

        route = 'v1/expenses/category/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_expenses_category_details(self, category_pk):
        """ Get the expenses category details

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_expenses_category_details(self, category_pk, data):
        """ Update the expense details

        Keyword arguments:
        category_pk -- pk of the expense category
        data -- content of the update:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "accounting_code": "string",
            "vat": "string"
        }
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_expenses_category(self, category_pk):
        """ Delete the expenses category

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_expenses_groups_list(self, team_pk=None, page=1):
        """ Get the list of expenses groups

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        if team_pk is None:
            route = 'v1/expenses/groups/v2/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        else:
            route = 'v1/expenses/groups/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_expenses_group(self, data, team_pk=None):
        """ Create a new group of expenses

        Keyword arguments:
        data -- data of the new group of expenses to be created
        """

        if team_pk is None:
            route = 'v1/expenses/groups/v2/list/{0}/'.format(self.org_pk)
        else:
            route = 'v1/expenses/groups/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def create_expenses_group_action(self, data):
        """ Create an action

        Keyword arguments:
        {
            'team': team_pk # REQUIRED
            'is_treated': bool
            'is_validated': bool
        }
        """

        route = 'v1/expenses/groups/list/action/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_expenses_group_details(self, expense_group_id):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_expenses_group_details(self, expense_group_id, data):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_expenses_group(self, expense_group_id):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_expenses_list(self, team_pk=None, expense_group_id=None, page=1):
        """ Get the expenses list """

        if team_pk is not None and expense_group_id is not None:
            route = 'v1/expenses/list/{0}/{1}/?page_size={2}&page={3}'.format(
                team_pk, expense_group_id, self.pagination, page)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        else:
            route = 'v1/expenses/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_expense(self, data, team_pk=None, expense_group_id=None):
        """ Create a new expense

        Keywords arguments:
        data -- data of the new expense to be created:
        {
            "expense_group": 0,
            "description": "string",
            "amount": 0,
            "vat": 0,
            "file": "string",
            "date": "string",
            "is_paid": true,
            "is_billed": true,
            "comments": "string",
            "local_amount": 0,
            "currency": 0,
            "currency_rate": 0,
            "has_duplicate_receipt": true,
            "distance": 0,
            "rate_per_km": 0,
            "phase": 0
        }
        """

        if team_pk is not None and expense_group_id is not None:
            route = 'v1/expenses/list/{0}/{1}/'.format(team_pk, expense_group_id)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/'.format(team_pk)
        else:
            route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def add_multiple_expenses(self, expense_group_id, files):

        route = 'v1/expenses/groups/create-multiple-expenses/{0}/'.format(expense_group_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=files)
        return self.process_response(response)

    def get_expenses_pdf_count(self, expense_group_id):

        route = 'v1/expenses/pdf_count/{0}/'.format(expense_group_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_expenses_details(self, pk):
        """Get the expense details

        Keyword arguments:
        pk -- pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_expense_details(self, pk, data):
        """Update the expense details

        Keyword arguments:
        pk -- pk of the expense
        data -- content of the update:
        {
            "expense_group": group_id,
            "description": "string",
            "amount": 0,
            "vat": 0,
            "file": "string",
            "date": "string",
            "is_paid": true,
            "is_billed": true,
            "comments": "string",
            "local_amount": 0,
            "currency": 0,
            "currency_rate": 0,
            "has_duplicate_receipt": true,
            "distance": 0,
            "rate_per_km": 0,
            "phase": phase_id
        }
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_expense(self, pk):
        """Delete the expense

        Keyword arguments:
        pk -- pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Freelancers ####

    def get_freelancers_list(self, page=1):
        """ Get the list of freelancers """

        route = 'v1/freelancers/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_freelancer(self, data):
        """ Create a new freelancer

        Keywords arguments:
        data -- data of the new freelancer to be created
        {
            "photo": "string",
            "name": "string",
            "is_company": true,
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "telephone": "string",
            "mobile": "string",
            "teams": [
                team_pk,
                ...
            ],
            "projects": [
                project_id,
                ...
            ],
            "address": "string"
        }
        """

        route = 'v1/freelancers/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_freelancer_details(self, pk):
        """ Get the freelancer details 

        Keywords arguments:
        pk -- pk of the freelancer
        """

        route = 'v1/freelancers/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_freelancer_details(self, pk, data):
        """ Update the freelancer details 

        Keywords arguments:
        pk -- pk of the freelancer
        data -- content of the update:
        {
            "photo": "string",
            "name": "string",
            "is_company": true,
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "telephone": "string",
            "mobile": "string",
            "teams": [
                team_pk,
                ...
            ],
            "projects": [
                project_id,
                ...
            ],
            "address": "string"
        }
        """

        route = 'v1/freelancers/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_freelancer(self, pk):
        """ Delete the freelancer 

        Keywords arguments:
        pk -- pk of the freelancer
        """

        route = 'v1/freelancers/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Jobs ####

    def get_jobs_invoices_items_list(self, page=1):
        """ Get the list of jobs invoices items """

        route = 'v1/jobs/invoices/items/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_invoices_item(self, data):
        """ Create a new jobs invoices item 

        Keywords arguments:
        data -- data of the new jobs invoices item to be created:
        {
            "invoice": invoice_id, # REQUIRED
            "project": project_id,
            "phases": [
                phase_id,
                ...
            ],
            "annexes": [
                annexe_pk,
                ...
            ],
            "tax": 0,
            "subtotal": 0,
            "amount": 0,
            "description": "string"
        }
        """

        route = 'v1/jobs/invoices/items/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_jobs_invoices_item_details(self, job_invoice_item_pk):
        """ Get the jobs invoices item details

        Keywords arguments:
        job_invoice_item_pk -- pk of the item
        """

        route = 'v1/jobs/invoices/items/{0}/'.format(job_invoice_item_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_jobs_invoices_item_details(self, job_invoice_item_pk, data):
        """ Update the jobs invoices item

        Keywords arguments:
        job_invoice_item_pk -- pk of the item
        data -- content of the update:
        {
            "invoice": invoice_id, # REQUIRED
            "project": project_id, 
            "phases": [
                phase_id,
                ...
            ],
            "annexes": [
                annexe_pk,
                ...
            ],
            "tax": 0,
            "subtotal": 0,
            "amount": 0,
            "description": "string"
        }
        """

        route = 'v1/jobs/invoices/items/{0}/'.format(job_invoice_item_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_jobs_invoices_item(self, job_invoice_item_pk):
        """ Delete the jobs invoices item 

        Keywords arguments:
        job_invoice_item_pk -- pk of the item
        """

        route = 'v1/jobs/invoices/items/{0}/'.format(job_invoice_item_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_jobs_invoices_list(self, page=1):
        """ Get the list of jobs invoices """

        route = 'v1/jobs/invoices/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_invoice(self, data):
        """ Create a new jobs invoice

        Keywords arguments:
        data -- data of the new jobs invoice to be created:
        {
            "date": "string", # REQUIRED
            "contractor": 0, # REQUIRED
            "job": job_pk,
            "orguser": orguser_pk,
            "team": team_pk,
            "freelancer": 0,
            "project": project_id,
            "phases": [
                phase_id,
                ...
            ],
            "annexes": [
                annexe_pk,
                ...
            ],
            "client_amount": 0,
            "currency": currency_pk,
            "currency_rate": 0,
            "amount": 0,
            "file": "string",
            "is_validated": "string",
            "is_paid": true,
            "date_paid": "string",
            "tax": 0,
            "description": "string",
            "number": "string",
            "due_date": "string",
            "type": "string"
        }
        """

        route = 'v1/jobs/invoices/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_jobs_invoice_details(self, job_invoice_pk):
        """ Get the jobs invoice details

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_jobs_invoice_details(self, job_invoice_pk, data):
        """ Get the jobs invoice details

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        data -- content of the update:
        {
            "job": job_pk,
            "orguser": orguser_pk,
            "team": team_pk,
            "freelancer": 0,
            "contractor": 0,
            "project": project_id,
            "phases": [
                phase_id,
                ...
            ],
            "annexes": [
                annexe_pk,
                ...
            ],
            "client_amount": 0,
            "currency": currency_pk,
            "currency_rate": 0,
            "amount": 0,
            "file": "string",
            "is_validated": "string",
            "is_paid": true,
            "date_paid": "string",
            "date": "string",
            "tax": 0,
            "description": "string",
            "number": "string",
            "due_date": "string",
            "type": "string"
        }
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_jobs_invoice(self, job_invoice_pk):
        """ Delete the jobs invoice

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_jobs_list(self, page=1):
        """ Get the list of jobs """

        route = 'v1/jobs/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_job(self, data):
        """ Create a new job 

        Keywords arguments:
        data -- data of the new job to be created:
        {
            "title": "string",
            "orguser": orguser_pk,
            "project": project_id,
            "freelancer": 0,
            "contractor": 0,
            "budget": 0,
            "budget_ref": 0,
            "currency": currency_pk,
            "currency_rate": 0,
            "amount": 0,
            "amount_ref": 0,
            "annexes": [
                annexe_id,
                ...
            ],
            "phases": [
                phase_id,
                ...
            ],
            "type": "string",
            "doc": 0,
            "lot": 0,
            "description": "string",
            "is_annex": true,
            "file": "string",
            "subtotal": 0,
            "forecast_type": "string",
            "date": "string",
            "start_date": "string",
            "end_date": "string",
            "tax": 0,
            "balance": 0
        }
        """

        route = 'v1/jobs/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_jobs_months_list(self, page=1):
        """ Get the list of jobs months """

        route = 'v1/jobs/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_month(self, data):
        """ Create a new jobs month 

        Keywords arguments:
        data -- data of the jobs month to be created:
        {
            "job": job_id, # REQUIRED
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": true,
            "is_present": true,
            "is_future": true,
            "budget": 0,
            "actual": 0,
            "pct": 0
        }
        """

        route = 'v1/jobs/month/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_jobs_month_details(self, month_id):
        """ Get the jobs month details

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(month_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_jobs_month_details(self, month_id, data):
        """ Update the jobs month details

        Keywords arguments:
        month_id -- id of the jobs month
        data -- content of the update:
        {
            "job": job_id,
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": true,
            "is_present": true,
            "is_future": true,
            "budget": 0,
            "actual": 0,
            "pct": 0
        }
        """

        route = 'v1/jobs/month/{0}/'.format(month_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_jobs_month(self, month_id):
        """ Delete the jobs month 

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(month_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_job_details(self, id):
        """ Get the job details

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_job_details(self, id, data):
        """ Update the job details

        Keywords arguments:
        id -- id of the job
        data -- content of the update:
        {
            "title": "string",
            "orguser": 0,
            "project": 0,
            "freelancer": 0,
            "contractor": 0,
            "budget": 0,
            "budget_ref": 0,
            "currency": 0,
            "currency_rate": 0,
            "amount": 0,
            "amount_ref": 0,
            "annexes": [
                "string"
            ],
            "phases": [
                "string"
            ],
            "type": "string",
            "doc": 0,
            "lot": 0,
            "description": "string",
            "is_annex": true,
            "file": "string",
            "subtotal": 0,
            "forecast_type": "string",
            "date": "string",
            "start_date": "string",
            "end_date": "string",
            "tax": 0,
            "balance": 0
        }
        """

        route = 'v1/jobs/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_job(self, id):
        """ Delete the job

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def generate_jobs_invoices_items(self, data):
        """ Generate invoice items based on the job invoice contractor

        Keywords arguments:
        data -- :
        {
            "invoice": job_invoice_id
        }
        """
        route = 'v1/jobs/invoices/items/generate/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)
