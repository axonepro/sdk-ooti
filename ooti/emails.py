import requests
import json

from .helper import Helper


class Emails(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_emails_list(self, page=1):
        """ Get the emails list """

        route = 'v1/emails/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_email_details(self, pk):
        """ Get the email details

        Keyword arguments:

        pk -- the pk of the email
        """
        route = 'v1/emails/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_email(self, data):
        """ Create an email

        Keyword arguments:

        data -- data create, fields:
            {
                "team": 0,
                "name": "string", (name of the template)
                "type": "", ('invoice', 'followup' or 'contractor_notification')
                "email_to": "string",
                "email_from": "string",
                "name_from": "string",
                "email_cc": "string",
                "email_bcc": "string",
                "email_subject": "string",
                "email_body": "string",
                "smtp_setting": 0,
                "projects": [],
                "invoices": []
            }

        Note that there is no required fields to create the email template.
        """

        route = 'v1/emails/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_email(self, pk, data):
        """ Update an email

        Keyword arguments:

        pk -- the pk of the email template
        data -- data create, fields:
            {
                "team": 0,
                "name": "string", (name of the template)
                "type": "", ('invoice', 'followup' or 'contractor_notification')
                "email_to": "string",
                "email_from": "string",
                "name_from": "string",
                "email_cc": "string",
                "email_bcc": "string",
                "email_subject": "string",
                "email_body": "string",
                "smtp_setting": 0,
                "projects": [],
                "invoices": []
            }

        Note that there is no required fields to create the email template.
        """

        route = 'v1/emails/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_email(self, pk):
        """Delete an email

        Keyword arguments:

        pk -- pk of the email
        """
        route = 'v1/emails/{0}'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def send_test_email(self, pk):
        """ Send test email to the email of the account

        Keyword arguments:

        pk -- the pk of the email template
        """

        route = 'v1/emails/{0}/send-test/'.format(pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def apply_email(self, pk):
        """ Apply the template to related projects and unsent invoices

        Keyword arguments:

        pk -- pk of the email template
        """
        route = 'v1/emails/{0}/apply/'.format(pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_emails_smtp_list(self, page=1):
        """ Get the emails smtp list """

        route = 'v1/emails/smtp/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_email_smtp_details(self, pk):
        """ Get the email smtp details

        Keyword arguments:

        pk -- the pk of the email smtp
        """

        route = 'v1/emails/smtp/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_email_smtp(self, data):
        """ Create an email smtp

        Keyword Arguments:

        data -- data create: fields:
           {
               "from_name": "string",
               "from_email": "string",
               "username": "string",
               "password": "string",
               "protocol": "TLS" or "SSL",
               "host": "string",
               "port": 0
           }
        """
        route = 'v1/emails/smtp/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_email_smtp(self, pk, data):
        """ Update an email smtp

        Keyword arguments:

        pk -- the pk of the email smtp
        data -- data create: fields:
           {
               "from_name": "string",
               "from_email": "string",
               "username": "string",
               "password": "string",
               "protocol": "TLS" or "SSL",
               "host": "string",
               "port": 0
           }
        """

        route = 'v1/emails/smtp/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_email_smtp(self, pk):
        """ Delete an email smtp

        Keyword arguments:

        pk -- pk of the email smtp
        """
        route = 'v1/emails/smtp/{0}'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def send_test_email_smtp(self, pk):
        """ Verify the status of the smtp

        Keyword arguments:

        pk -- the pk of the email template
        """

        route = 'v1/emails/smtp/{0}/send-test/'.format(pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)