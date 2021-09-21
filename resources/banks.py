import requests
import json

from .helper import Helper


class Banks(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_banks_list(self, page=1):
        """ Get the banks list """

        route = 'v1/banks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_bank_details(self, pk):
        """ Get the bank details

        Keyword arguments:

        pk -- pk of the bank
        """

        route = 'v1/banks/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_bank(self, data):
        """ Create a bank

        Keyword arguments:

        data -- data to be created:
            {
                "name": "string",
                "currency": 0,
                "country": "string",
                "iban": "string",
                "bic": "string",
                "rib": "string",
                "teams": ["string"]
                "projects": ["string"]
            }
        """
        route = 'v1/banks/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_bank(self, pk, data):
        """ Update a bank

        Keyword arguments:

        data -- data to be created:
            {
                "name": "string",
                "currency": 0,
                "country": "string",
                "iban": "string",
                "bic": "string",
                "rib": "string",
                "teams": ["string"]
                "projects": ["string"]
            }
        """
        route = 'v1/banks/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_bank(self, pk):
        """ Create a bank

        Keyword arguments:

        pk -- pk of the bank
        """
        route = 'v1/banks/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)