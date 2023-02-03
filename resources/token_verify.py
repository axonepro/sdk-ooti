import json

import requests

from .resource import Resource


class TokenVerify(Resource):

    def __verify_token(self):
        """Verify if the access token is still valid"""

        route = "v1/token-verify/"
        data = {"token": self.access_token}
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return response.status_code
