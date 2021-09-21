import requests
import json

from .helper import Helper


class Token_verify(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def __verify_token(self):
        """ Verify if the access token is still valid """

        route = 'v1/token-verify/'
        data = {
            'token': self.access_token
        }
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return response.status_code