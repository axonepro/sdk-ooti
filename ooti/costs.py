import requests
import json

from helper import Helper


class Costs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Costs ####

    #### Employees ####

    #### Expenses ####

    # see questions below

    def get_expenses_categories_list(self):
        """ Get the list of expenses categories """

        route = 'v1/expenses/category/list/{0}/'.format(self.org_pk)
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

    # POST on v1/expenses/groups/create-multiple-expenses/{id}/ ?

    # POST on v1/expenses/groups/list/action/{org_pk}/ ?

    def get_expenses_groups_list(self, team_pk=None):
        """ Get the list of expenses groups

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        if team_pk is None:
            route = 'v1/expenses/groups/v2/list/{0}/'.format(self.org_pk)
        else:
            route = 'v1/expenses/groups/list/{0}/'.format(team_pk)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, json=json.dumps(data))
        return self.process_response(response)

    def get_expenses_group_details(self, group_id):

        route = 'v1/expenses/groups/{group_id}/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_expenses_group_details(self, group_id, data):

        route = 'v1/expenses/groups/{group_id}/'
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, json=json.dumps(data))
        return self.process_response(response)

    def delete_expenses_group(self, group_id):

        route = 'v1/expenses/groups/{group_id}/'
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_expenses_list(self, team_pk=None, group_id=None):
        """ Get the expenses list """

        if team_pk is not None and group_id is not None:
            route = 'v1/expenses/list/{0}/{1}/'.format(team_pk, group_id)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/'.format(team_pk)
        else:
            route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_expense(self, data, team_pk=None, group_id=None):
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

        if team_pk is not None and group_id is not None:  # differences between the 3 ?
            route = 'v1/expenses/list/{0}/{1}/'.format(team_pk, group_id)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/'.format(team_pk)
        else:
            route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, json=json.dumps(data))
        return self.process_response(response)

    def get_expenses_pdf_count(self, id):  # which id ?

        route = 'v1/expenses/pdf_count/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    # DELETE on v1/expenses/{expense_group_pk}/versions/{version_pk}/delete/ ?

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

    def get_freelancers_list(self):
        """ Get the list of freelancers """

        route = 'v1/freelancers/list/{0}/'.format(self.org_pk)
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

    # POST on v1/jobs/invoices/items/generate/{org_pk}/ ?

    def get_jobs_invoices_items_list(self):
        """ Get the list of jobs invoices items """

        route = 'v1/jobs/invoices/items/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_invoices_item(self, data):
        """ Create a new jobs invoices item 

        Keywords arguments:
        data -- data of the new jobs invoices item to be created:
        {
            "invoice": invoice_id,
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
            "invoice": invoice_id,
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

    def get_jobs_invoices_list(self):
        """ Get the list of jobs invoices """

        route = 'v1/jobs/invoices/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_invoice(self, data):
        """ Create a new jobs invoice

        Keywords arguments:
        data -- data of the new jobs invoice to be created:
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

    def get_jobs_invoice_details(self, job_invoice_pk):
        """ Delete the jobs invoice

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_jobs_list(self):
        """ Get the list of jobs """

        route = 'v1/jobs/list/{0}/'.format(self.org_pk)
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

    def get_jobs_months_list(self):
        """ Get the list of jobs months """

        route = 'v1/jobs/month/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_jobs_month(self, data):
        """ Create a new jobs month 

        Keywords arguments:
        data -- data of the jobs month to be created:
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

        route = 'v1/jobs/month/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_jobs_month_details(self, month_id):
        """ Get the jobs month details

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(self.month_id)
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

        route = 'v1/jobs/month/{0}/'.format(self.month_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_jobs_month(self, month_id):
        """ Delete the jobs month 

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(self.month_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_job_details(self, id):
        """ Get the job details

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(self.id)
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

        route = 'v1/jobs/{0}/'.format(self.id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_job(self, id):
        """ Delete the job

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(self.id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
