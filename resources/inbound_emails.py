import json

import requests

from .resource import Resource


class InboundEmail(Resource):

    def get_inbound_emails_list(self, page=1):
        """Get the list of inbound emails"""

        route = f"v1/inbound_emails/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_inbound_email(self, data):
        """Create a new inbound email

        Keywords arguments:
        data -- data of the new inbound email to be created:
        {
            "project": project_id, (required)
            "invoice": invoice_pk,,
            "received_at": "string",
            "to_address": "string",
            "from_address": "string",
            "reply_to_address": "string",
            "cc_address": "string",
            "bcc_address": "string",
            "subject": "string",
            "body": "string"
        }
        """

        route = f"v1/inbound_emails/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_inbound_email_details(self, id):
        """Get the inbound email details

        Keywords arguments:
        id -- id of the inbound email
        """

        route = f"v1/inbound_emails/{id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_inbound_email_details(self, id, data):
        """Update the inbound email details

        Keywords arguments:
        id -- id of the inbound email
        data -- content of the update:
        {
            "project": project_id,
            "invoice": invoice_pk,
            "received_at": "string",
            "to_address": "string",
            "from_address": "string",
            "reply_to_address": "string",
            "cc_address": "string",
            "bcc_address": "string",
            "subject": "string",
            "body": "string"
        }
        """

        route = f"v1/inbound_emails/{id}/"
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

    def delete_inbound_email(self, id):
        """Delete the inbound email

        Keywords arguments:
        id -- id of the inbound email
        """

        route = f"v1/inbound_emails/{id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
