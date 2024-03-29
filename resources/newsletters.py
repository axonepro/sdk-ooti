import json

import requests

from .resource import Resource


class Newsletters(Resource):

    def get_newsletters_list(self, page=1):
        """Get the list of newsletters"""

        route = f"v1/newsletters/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_newsletters(self, data):
        """Create a new newsletter

        Keywords arguments:
        data -- data of the new newsletter to be created:
        {
            "template": 0,
            "receivers": [
                orguser_pk,
                ...
            ],
            "name": "string",
            "start_date": "string",
            "end_date": "string",
            "time": "string",
            "type": "string",
            "frequency": 0,
            "all_users_are_receivers": true
        }
        """

        route = f"v1/newsletters/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_newsletter_details(self, pk):
        """Get newsletter details

        Keywords arguments:
        pk -- pk of the newsletter
        """

        route = f"v1/newsletters/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_newsletter_details(self, pk, data):
        """Update newsletter details

        Keywords arguments:
        pk -- pk of the newsletter
        data -- content of the update:
        {
            "template": 0,
            "receivers": [
                orguser_pk,
                ...
            ],
            "name": "string",
            "start_date": "string",
            "end_date": "string",
            "time": "string",
            "type": "string",
            "frequency": 0,
            "all_users_are_receivers": true
        }
        """

        route = f"v1/newsletters/{pk}/"
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

    def delete_newsletter(self, pk):
        """Delete the newsletter

        Keywords arguments:
        pk -- pk of the newsletter
        """

        route = f"v1/newsletters/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
