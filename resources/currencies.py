import requests
import json

from .helper import Helper


class Currencies(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_currencies_list(self, page=1):
        """Get the currencies list """

        route = 'v1/currencies/list/?page_size={0}&page={1}'.format(self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_currency(self, data):
        """ Create a currency

        Keyword arguments:

        data -- data create, required fields:
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }
        """

        route = 'v1/currencies/list/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    # TODO POST on /api/v1/currencies/list/actions/{org_pk}/

    def get_currency_details(self, pk):
        """ Get the currency details

        Keyword arguments:

        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_currency(self, pk, data):
        """ Update a currency

        Keyword arguments:

        data -- data create, required fields:
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }

        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_currency(self, pk):
        """ Delete a currency
        Keyword arguments:
        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)