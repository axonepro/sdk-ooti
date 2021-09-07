import requests
import json

from .helper import Helper


class Notifications(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_notifications_config(self):
        """ Get the notifications config of the organization """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_notifications_config(self, data):  # "off"/? - "on" and "active" rejected
        """ Update the notifications config of the organization 

        Keywords arguments:
        data -- content of the update
        {
            daily_time": "18:00:00",
            "weekly_time": null,
            "weekday": 5,
            "expense_reports_submissions": "off",
            "expense_reports_submissions_email": false,
            "expense_reports_validations": "off",
            "expense_reports_validations_email": false,
            "expense_reports_reimbursal": "off",
            "expense_reports_reimbursal_email": false,
            "time_off_submissions": "off",
            "time_off_submissions_email": false,
            "time_off_validations": "off",
            "time_off_validations_email": false,
            "time_entry_refusals": "off",
            "time_entry_refusals_email": false,
            "invoices_sent": "off",
            "invoices_sent_email": false,
            "invoices_paid": "off",
            "invoices_paid_email": false,
            "post_posted": "off",
            "post_posted_email": false,
            "project_fees_changed": "off",
            "project_fees_changed_email": false,
            "project_dates_changed": "off",
            "project_dates_changed_email": false,
            "invitations_accepted": "off",
            "invitations_accepted_email": false,
            "permissions_changed": "off",
            "permissions_changed_email": false
        }
        """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)