import requests
import json

from .helper import Helper


class Orgusers(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO GET on /api/v1/orgusers/all/

    # TODO POST on /api/v1/orgusers/all/

    def get_orgusers_count(self):
        """ Get only the number of orguser inside the organization """

        route = 'v1/orgusers/count/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/orgusers/dashboard-metrics/{project_pk}/

    def export_orgusers_list(self):
        """ Export the list of orgusers as a .xls file """

        route = 'v1/orgusers/export/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        xls_file = open('orgusers_list.xls', 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def invite_orguser(self, pk, team_pk):
        """ Send an invitation to the orguser

        Keywords arguments:
        pk -- pk of the orguser
        team_pk -- pk of the team
        """

        route = 'v1/orgusers/invite/'
        data = {
            'orguser': pk,
            'team': team_pk
        }
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_orgusers_list(self):
        """ Get the list of users in the organization """

        route = 'v1/orgusers/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_orguser(self, data):
        """ Create a new user in the organization 

        data -- content of the orguser to be created:
        {
            "email": "testk@email.com",
            "first_name": "Julien",
            "last_name": "DUPUIS",
            "role": role_pk
            "timeoff_validators": [],
            "time_validators": [],
            "expenses_validators": [],
            "tags": []
        }
        """

        route = 'v1/orgusers/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_orguser_details(self, pk):
        """ Get the orguser details

        Keyword arguments:
        pk -- pk of the orguser
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_orguser_details(self, pk, data):
        """ Update the orguser details 

        Keywords arguments:
        pk -- pk of the orguser to update
        data -- content of the update:
        {
            "mobile": "012345678",
            "birthday": "16-04-2021"
        }
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_orguser(self, pk):
        """ Delete the orguser 

        Keyword arguments:
        pk -- pk of the orguser to update
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)