import json

import requests

from .helper import Helper


class TokenVerify(Helper):

    def __verify_token(self):
        """Verify if the access token is still valid"""

        route = "v1/token-verify/"
        data = {"token": self.access_token}
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return response.status_code
