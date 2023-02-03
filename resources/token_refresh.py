import json

import requests

from .helper import Helper


class TokenRefresh(Helper):

    def __refresh_token(self):
        """Refresh the access token"""

        route = "v1/token-refresh/"
        data = {"token": self.access_token}
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        if response == 201:
            self.headers["Authorization"] = f"JWT {self.access_token}"
        return response.status_code
