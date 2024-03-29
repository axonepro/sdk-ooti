import json

import requests

from .resource import Resource


class Revenue(Resource):

    def get_revenue_list(self, page=1):
        """Get the revenue list"""

        route = (
            f"v1/revenue/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        )
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_revenue_details(self, pk):
        """Get the revenue details

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = f"v1/revenue/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_revenue(self, data):
        """Create a revenue

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

        route = f"v1/revenue/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_revenue_month_list(self, page=1):
        """Get the revenue month list"""

        route = f"v1/revenue/month/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_revenue_month(self, data):
        """Create a revenue month

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

        route = f"v1/revenue/month/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_revenue_month_details(self, pk):
        """Get the revenue month details

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = f"v1/revenue/month/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_revenue_month(self, pk, data):
        """Update a revenue month

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

        route = f"v1/revenue/month/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_revenue_month(self, pk):
        """Delete the revenue month

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = f"v1/revenue/month/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_revenue(self, pk, data):
        """Update a revenue

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

        route = f"v1/revenue/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_revenue(self, pk):
        """Delete the revenue

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = f"v1/revenue/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    # TODO POST on /api/v1/revenue/set-annual-budget/{id}/
