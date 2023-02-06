import json

import requests

from .resource import Resource


class Actions(Resource):

    def get_actions_list(self, page=1):
        """Get the list of actions"""

        route = (
            f"v1/actions/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        )
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_actions_details(self, id):
        """Get the action details

        Keywords arguments:
        id -- id of the action
        """

        route = f"v1/actions/{id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
