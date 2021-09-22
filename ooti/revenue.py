import requests
import json

from .helper import Helper


class Revenue(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_revenue_list(self, page=1):
        """ Get the revenue list """

        route = 'v1/revenue/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_revenue_details(self, pk):
        """ Get the revenue details

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_revenue(self, data):
        """ Create a revenue

        Keyword arguments:

        data -- data create:
            {
                "amount_actual": 0,
                "amount_budgeted": 0,
                "description": "string",
                "type": "string",
                "month": 0,
                "title": "string",
                "year": 0,
                "team": 0,
                "project": 0,
                "months": [
                    "string"
                ]
            }
        """

        route = 'v1/revenue/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_revenue_month_list(self, page=1):
        """ Get the revenue month list """

        route = 'v1/revenue/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_revenue_month(self, data):
        """ Create a revenue month

        Keyword arguments:

        data -- data create:
        {
            "revenue_adjustment": 0,
            "team": 0,
            "project": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/revenue/month/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_revenue_month_details(self, pk):
        """Get the revenue month details

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_revenue_month(self, pk, data):
        """ Update a revenue month

        Keyword arguments:

        pk -- pk of the revenue month
        data -- data create:
        {
            "revenue_adjustment": 0,
            "team": 0,
            "project": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revenue_month(self, pk):
        """ Delete the revenue month

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_revenue(self, pk, data):
        """ Update a revenue

        Keyword arguments:

        pk -- pk of the revenue
        data -- data update:
            {
                "amount_actual": 0,
                "amount_budgeted": 0,
                "description": "string",
                "type": "string",
                "month": 0,
                "title": "string",
                "year": 0,
                "team": 0,
                "project": 0,
                "months": [
                    "string"
                ]
            }
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revenue(self, pk):
        """ Delete the revenue

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO POST on /api/v1/revenue/set-annual-budget/{id}/