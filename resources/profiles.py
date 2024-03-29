import json

import requests

from .resource import Resource


class Profiles(Resource):

    # TODO GET on /api/v1/profiles/onboarding/{org_pk}/

    # TODO GET on /api/v1/profiles/permissions/

    def get_profile_preferences(self):
        """Get profile preferences"""

        route = "v1/profiles/preferences/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    # TODO POST on /api/v1/profiles/preferences/

    def get_profile_details(self):
        """Get current profile details"""

        route = "v1/profiles/profile/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_profile_details(self, data):
        """Update current profile details

        Keywords arguments:
        data -- content of the update:
        {
            "locale": "en",
            "show_sidemenu": False
        }
        """

        route = "v1/profiles/profile/"
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
