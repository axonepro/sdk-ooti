import requests
import json

from .helper import Helper


class Roles(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_roles_list(self, page=1):
        """ Get roles list """

        route = 'v1/roles/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_roles(self, data):
        """ Create roles list 

        Keyword arguments:

        data -- data create:
        {
            "title": "string",
            "billable_per_hour": 0,
            "payable_per_hour": 0
        }
        """

        route = 'v1/roles/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_roles_project_list(self, page=1):
        """ Get roles project list """

        route = 'v1/roles/project/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_roles_project(self, data):
        """ Get roles project list 

        Keyword arguments:

        data -- data create:
        {
            "project": 0,
            "role": 0,
            "billable_per_hour": 0,
            "payable_per_hour": 0,
            "pay_per_hour": 0,
            "personnel_count": 0
        }
        """

        route = 'v1/roles/project/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_roles_project_details(self, pk):
        """ Get roles details 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_roles_project(self, pk, data):
        """ Update roles project 

        Keyword arguments:

        pk -- pk of the roles project
        data -- data create:
        {
            "project": 0,
            "role": 0,
            "billable_per_hour": 0,
            "payable_per_hour": 0,
            "pay_per_hour": 0,
            "personnel_count": 0
        }
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_roles_project(self, pk):
        """ Delete roles project 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_bulk_action_add_roles(self, project_pk):
        """ Create bulk action to add role to project """

        route = 'v1/roles/roles/bulk/add/{0}/?project={1}'.format(self.org_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def delete_bulk_action_add_roles(self, project_pk):
        """ Delete bulk action to add role to project """

        route = 'v1/roles/roles/bulk/delete/{0}/?project={1}'.format(self.org_pk, project_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_roles_details(self, pk):
        """ Get roles details 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_roles(self, pk, data):
        """ Update roles 

        Keyword arguments:

        pk -- pk of the roles
        data -- data create:
        {
            "title": "string",
            "billable_per_hour": 0,
            "payable_per_hour": 0
        }
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_roles(self, pk):
        """ Delete roles 

        Keyword arguments:

        pk -- pk of the roles 
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)