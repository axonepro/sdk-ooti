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
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
        return self.process_response(response)

    def get_invoices_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
        return self.process_response(response, True)

    def get_invoices_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, None, self.headers, json.dumps(data))
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
        response = self.process_request(requests, 'POST', self.base_url, route, parameters, self.headers, json.dumps(data))
        return self.process_response(response)

    def validate_invoice(self, pk):
        """Validate an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_valid": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, None, self.headers, json.dumps(data))
        return self.process_response(response)

    def send_invoice(self, pk):
        """Send an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_sent": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, None, self.headers, json.dumps(data))
        return self.process_response(response)

    def cancel_invoice(self, pk):
        """Cancel an invoice and create a credit note
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_closed": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, None, self.headers, json.dumps(data))

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
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, None, self.headers, json.dumps(data))
        return self.process_response(response)

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
        response = self.process_request(requests, 'PATCH', self.base_url, route, None, self.headers, json.dumps(data))
        return self.process_response(response)

    def delete_invoice_item(self, pk):
        """ Update invoice's item

        Keyword Arguments:

        pk -- pk of the item
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, None, self.headers, None)
        return self.process_response(response)

    def get_credit_notes_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}&type=9'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
        return self.process_response(response, True)

    def get_credit_notes_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true&type=9'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, None, self.headers, None)
        return self.process_response(response, True)