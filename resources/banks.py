import json

import requests

from .helper import Helper


class Banks(Helper):

    def get_banks_list(self, page=1):
        """Get the banks list"""

        route = f"v1/banks/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_bank_details(self, pk):
        """Get the bank details

        Keyword arguments:

        pk -- pk of the bank
        """

        route = f"v1/banks/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_bank(self, data):
        """Create a bank

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
        route = f"v1/banks/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def update_bank(self, pk, data):
        """Update a bank

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
        route = f"v1/banks/{pk}/"
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

    def delete_bank(self, pk):
        """Create a bank

        Keyword arguments:

        pk -- pk of the bank
        """
        route = f"v1/banks/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
