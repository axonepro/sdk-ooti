import requests
import json

from .helper import Helper


class Inbound_emails(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_inbound_emails_list(self, page=1):
        """ Get the list of inbound emails """

        route = 'v1/inbound_emails/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_inbound_email(self, data):
        """ Create a new inbound email

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

        route = 'v1/inbound_emails/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_inbound_email_details(self, id):
        """ Get the inbound email details

        Keywords arguments:
        id -- id of the inbound email
        """

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_inbound_email_details(self, id, data):
        """ Update the inbound email details

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

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_inbound_email(self, id):
        """ Delete the inbound email

        Keywords arguments:
        id -- id of the inbound email
        """

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)