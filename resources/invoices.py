import requests
import json

from .helper import Helper


class Invoices(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_invoice_details(self, pk):
        """ Get the invoice details

        Keyword arguments:

        pk -- the pk of the invoice
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_invoices_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_invoices_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def update_invoice(self, pk, data):
        """Create an invoice

        Keyword arguments:

        pk -- the pk of the invoice
        data -- data create:
            {
                "invoice_date": "DD-MM-YYYY",
                "billing_option": 0,
                "bank": 0,
                "purchase_order": "string",
                "references": "string",
                "is_valid": Boolean,
                "is_sent": Boolean,
                "multi_tax_enabled": Boolean(if invoice items have multi tax rates)
            }
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def create_invoice(self, team_pk, data):
        """Create an invoice
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data create:
            {
                "project": 0,
                "type": 0,
                "invoice_date": "DD-MM-YYYY",
                "due_date": "DD-MM-YYYY"
                "client_name": "string",
                "client_address": "string",
                "references": "string"
                "team": 0
            }

            Note that for type 4 (other), project is not mandatory
        """

        route = 'v1/invoices/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, parameters, json.dumps(data))
        return self.process_response(response)

    def validate_invoice(self, pk):
        """Validate an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_valid": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def send_invoice(self, pk):
        """Send an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_sent": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def cancel_invoice(self, pk):
        """Cancel an invoice and create a credit note
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_closed": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))

        if(response.status_code == 200):
            response_data = json.loads(response.content)
            credit_note_pk = response_data['credit_note_url'].split('/')[4]
            return {'status': response.status_code, 'data': credit_note_pk}

        return self.process_response(response)

    def get_invoice_items(self, pk, page=1):
        """ Get invoice's items

        Keyword arguments:

        pk -- invoice pk
        """

        route = 'v1/invoices/items/{0}/?page_size={1}&page={2}'.format(pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_invoice_item(self, pk, data):
        """ Create invoice's item

        Keyword Arguments:

        pk -- pk of the invoice
        data -- data create:
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0,
                "tax_rate": 0.0 (if invoice.multi_tax_rate=True)
                "tax": 0.0 (tax amount, if invoice.multi_tax_rate=True)
            }
        """

        route = 'v1/invoices/items/{0}/'.format(pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    # TODO DELETE on /api/v1/invoices/{id}/

    # TODO GET on /api/v1/invoices/item/{id}/

    def update_invoice_item(self, pk, data):
        """ Update invoice's item

        Keyword Arguments:

        pk -- pk of the item
        data -- data update:
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0
            }
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_invoice_item(self, pk):
        """ Update invoice's item

        Keyword Arguments:

        pk -- pk of the item
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_credit_notes_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}&type=9'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_credit_notes_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true&type=9'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    # TODO GET on /api/v1/invoices/accounting-dashboard/{team_pk}/

    # TODO GET on /api/v1/invoices/accounting_periods/{org_pk}/

    # TODO GET on /api/v1/invoices/accounting_periods_per_project/{org_pk}/

    # TODO POST on /api/v1/invoices/action/{org_pk}/

    # TODO GET on /api/v1/invoices/billable-summary/{team_pk}/

    # TODO GET on /api/v1/invoices/billable_items/{project_pk}

    # TODO POST on /api/v1/invoices/contract/item/generate/{id}/

    # TODO GET on /api/v1/invoices/contract/item/{id}/

    # TODO PATCH on /api/v1/invoices/contract/item/{id}/

    # TODO DELETE on /api/v1/invoices/contract/item/{id}/

    # TODO GET on /api/v1/invoices/contract/items/{invoice_pk}/

    # TODO POST on /api/v1/invoices/contract/items/{invoice_pk}/

    # TODO GET on /api/v1/invoices/count/{org_pk}/

    # TODO POST on /api/v1/invoices/followup/action/

    # TODO GET on /api/v1/invoices/followup/list/{org_pk}/

    # TODO POST on /api/v1/invoices/followup/list/{org_pk}/

    # TODO GET on /api/v1/invoices/followup/list/{org_pk}/generate/

    # TODO POST on /api/v1/invoices/followup/list/{org_pk}/generate/

    # TODO GET on /api/v1/invoices/followup/rule/list/{org_pk}/

    # TODO POST on /api/v1/invoices/followup/rule/list/{org_pk}/

    # TODO GET on /api/v1/invoices/followup/rule/{id}/

    # TODO PATCH on /api/v1/invoices/followup/rule/{id}/

    # TODO DELETE on /api/v1/invoices/followup/rule/{id}/

    # TODO GET on /api/v1/invoices/followup/{id}/

    # TODO PATCH on /api/v1/invoices/followup/{id}/

    # TODO DELETE on /api/v1/invoices/followup/{id}/

    # TODO GET on /api/v1/invoices/followup/{id}/send/

    # TODO POST on /api/v1/invoices/followup/{id}/send/

    # TODO POST on /api/v1/invoices/generage-auto-draft-invoices/{org_pk}/

    # TODO GET on /api/v1/invoices/get_invoice_pdf_count/{id}/

    # TODO GET on /api/v1/invoices/invoice/items/deliverable/{project_pk}/

    # TODO GET on /api/v1/invoices/invoicing-metrics/{team_pk}/{project_pk}/

    # TODO POST on v1/invoices/item/actions/

    # TODO GET on /api/v1/invoices/item/job/list/{org_pk}/

    # TODO POST on /api/v1/invoices/item/job/list/{org_pk}/

    # TODO GET on /api/v1/invoices/item/job/{id}/

    # TODO PATCH on /api/v1/invoices/item/job/{id}/

    # TODO DELETE on /api/v1/invoices/item/job/{id}/

    # TODO GET on /api/v1/invoices/item/revisions/{id}/

    # TODO GET on /api/v1/invoices/item/update/{id}/

    # TODO GET on /api/v1/invoices/metrics/{org_pk}/

    # TODO GET on /api/v1/invoices/recently-imported-invoices/{org_pk}/

    # TODO DELETE on /api/v1/invoices/recently-imported-invoices/{org_pk}/

    # TODO GET on /api/v1/invoices/revenue-composition-charts/{team_pk}/

    # TODO GET on /api/v1/invoices/unpaid-composition-charts/{team_pk}/

    # TODO POST on /api/v1/invoices/{id}/notify-contractors/

    # TODO POST on /api/v1/invoices/{id}/remove-fee-project-titles/

    # TODO POST on /api/v1/invoices/{id}/reset-orders/

    # TODO POST on /api/v1/invoices/{id}/sync-contract-invoice-progress/

    # TODO POST on /api/v1/invoices/{invoice_pk}/sync-clients/