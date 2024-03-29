import json

import requests

from .resource import Resource


class Styleguides(Resource):

    # TODO POST on /api/v1/styleguides/duplicate/{org_pk}/

    def get_styleguides_list(self, page=1):
        """Get the styleguide list"""

        route = f"v1/styleguides/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_styleguide_details(self, pk):
        """Get the styleguide details

        Keyword arguments:

        pk -- pk of the styleguide
        """

        route = f"v1/styleguides/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_styleguide(self, data):
        """Create a styleguide

        Keyword arguments:

        data -- data create:
            {
                "name": "string"
            }
        """

        route = f"v1/styleguides/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def update_styleguide(self, pk, data):
        """Update a styleguide

        Keyword arguments:

        pk -- pk of the styleguide
        data -- data create:
            {
                "name": "string",
                "type": "string" ("all", "report", "invoice", "proposal"),
                "font_color": "string",
                "font": "string",
                "font_size": "string",
                "margin_left": 0,
                "margin_right": 0
            }
        """

        route = f"v1/styleguides/{pk}/"
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

    def delete_styleguide(self, pk):
        """Delete a styleguide

        Keyword arguments:

        pk -- pk of the styleguide
        """

        route = f"v1/styleguides/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
