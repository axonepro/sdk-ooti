import requests

from .resource import Resource


class Billing(Resource):

    def cancel_subscription(self):  # return 200
        """Cancel subscription"""

        route = f"v1/billing/cancel-subscription/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_billing_card(self):
        """Update payment method"""

        route = f"v1/billing/card/{self.org_pk}/"
        response = self.process_request(
            requests, "PATCH", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def delete_billing_card(self):
        """Delete payment method"""

        route = f"v1/billing/card/{self.org_pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def reactivate_subscription(self):  # return 200
        """Reactivate subscription"""

        route = f"v1/billing/reactivate-subscription/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_subscription(self):
        """Change subscription"""

        route = f"v1/billing/update-subscription/{self.org_pk}/"
        response = self.process_request(
            requests, "PATCH", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
