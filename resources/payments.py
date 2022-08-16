import json

import requests

from .helper import Helper


class Payments(Helper):
    def __init__(
        self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
    ):
        super().__init__(
            base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
        )

    def get_payment_details(self, pk):
        """Get the payment details

        Keyword arguments:

        pk -- the pk of the payment
        """

        route = f"v1/payments/{pk}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_payments_list(self, page=1):
        """Get the payment list"""

        route = (
            f"v1/payments/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        )
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def update_payment(self, pk, data):
        """Create an payment

        Keyword arguments:

        pk -- the pk of the payment
        data -- data create:
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "currency_rate": 0,
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk)
            }
        """

        route = f"v1/payments/{pk}/"
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

    def update_payment_invoice(self, pk, data):
        """Update payment's amount on invoice

        Please do not call this function before update_payment.
        To make an update on a payment, first use the "update_payment" method.
        Then, update the amount on the invoice with this method.

        Keyword arguments:

        pk -- pk of payment
        data -- data update:
            {
                "amount": 0
            }
        """
        route = f"v1/payments/invoice/{pk}/"
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

    def create_payment(self, team_pk, data):
        """Create an payment

        Keyword arguments:

        team_pk -- the pk of the team
        data -- data create:
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk)(no need of project for invoices of type 4)
            }
        """

        route = f"v1/payments/list/{self.org_pk}/"
        parameters = f"?team={team_pk}"
        response = self.process_request(
            requests,
            "POST",
            self.base_url,
            route,
            self.headers,
            parameters,
            json.dumps(data),
        )
        return self.process_response(response)

    # TODO DELETE on /api/v1/payments/{id}/
