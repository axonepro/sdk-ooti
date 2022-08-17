import json

import requests

from .helper import Helper


class Invitations(Helper):
    def __init__(
        self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
    ):
        super().__init__(
            base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
        )

    def get_invitations_list(self):
        """Get the list of invitations"""

        route = f"v1/invitations/list/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_team_invitations_list(self, team_pk):
        """Get the list of invitations of a specific team

        Keywords arguments:
        team_pk -- pk of the team
        """

        route = f"v1/invitations/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_invitation_details(self, pk):
        """Get the invitation details

        Keywords arguments:
        pk -- pk of the invitation
        """
        route = f"v1/invitations/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_invitation(
        self, pk, data
    ):  # which pk ? already tested with orguser_pk and team_pk
        """Create a new invitation"""

        route = f"v1/invitations/{pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def update_invitation_details(self, pk, data):
        """Update invitation informations

        Keywords arguments:
        pk -- pk of the invitation
        data -- content of the update:
        {
            "email": "emailchanged@mail.com
        }
        """

        route = f"v1/invitations/{pk}/"
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

    def delete_invitation(self, pk):
        """Delete the invitation

        Keywords arguments:
        pk -- pk of the invitation
        """
        route = f"v1/invitations/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
