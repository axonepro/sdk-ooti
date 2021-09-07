import requests
import json

from .helper import Helper


class Jobs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def generate_jobs_invoices_items(self, data):
        """ Generate invoice items based on the job invoice contractor

        Keywords arguments:
        data -- :
        {
            "invoice": job_invoice_id
        }
        """
        route = 'v1/jobs/invoices/items/generate/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_jobs_invoices_items_list(self, page=1):
        """ Get the list of jobs invoices items """

        route = 'v1/jobs/invoices/items/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_jobs_invoices_item_details(self, job_invoice_item_pk):
        """ Get the jobs invoices item details

        Keywords arguments:
        job_invoice_item_pk -- pk of the item
        """

        route = 'v1/jobs/invoices/items/{0}/'.format(job_invoice_item_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_jobs_invoices_item(self, job_invoice_item_pk):
        """ Delete the jobs invoices item 

        Keywords arguments:
        job_invoice_item_pk -- pk of the item
        """

        route = 'v1/jobs/invoices/items/{0}/'.format(job_invoice_item_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_jobs_invoices_list(self, page=1):
        """ Get the list of jobs invoices """

        route = 'v1/jobs/invoices/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_jobs_invoice_details(self, job_invoice_pk):
        """ Get the jobs invoice details

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_jobs_invoice(self, job_invoice_pk):
        """ Delete the jobs invoice

        Keywords arguments:
        job_invoice_pk -- pk of the invoice
        """

        route = 'v1/jobs/invoices/{0}/'.format(job_invoice_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_jobs_list(self, page=1):
        """ Get the list of jobs """

        route = 'v1/jobs/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_jobs_months_list(self, page=1):
        """ Get the list of jobs months """

        route = 'v1/jobs/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_jobs_month_details(self, month_id):
        """ Get the jobs month details

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(month_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_jobs_month(self, month_id):
        """ Delete the jobs month 

        Keywords arguments:
        month_id -- id of the jobs month
        """

        route = 'v1/jobs/month/{0}/'.format(month_id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_job_details(self, id):
        """ Get the job details

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_job(self, id):
        """ Delete the job

        Keywords arguments:
        id -- id of the job
        """

        route = 'v1/jobs/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)
