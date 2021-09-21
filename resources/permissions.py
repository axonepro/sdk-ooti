import requests
import json

from .helper import Helper


class Permissions(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_permissions_list(self):
        """ Get the list of permissions sets """

        route = 'v1/permissions/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_permissions(self, data):
        """ Create a new set of permissions

        Keywords arguments:
        data -- content of the permissions set to be created:
        {
            "name": "Consultant", (required)
            "name_en": "Consultant",
            "name_fr": "Consultant",
            "level": "project",
            "all_permissions": true,
            "is_default": true,
            "permissions": [
                id,
                ...
            ]
        }
        """

        route = 'v1/permissions/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_permissions_map(self):
        """ Return a dictionary with request.user permissions by level """

        route = 'v1/permissions/map/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_permissions_details(self, id):
        """ Get permissions set details

        Keywords arguments:
        id -- id of the permissions set
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_permissions_details(self, id, data):
        """ Update permissions set details

        Keywords arguments:
        id -- id of the permissions set
        data -- content of the update:
        {
            "name": "Boss",
            "name_en": "Boss",
            "name_fr": "Patron",
            "level": "organization",
            "all_permissions": true,
            "is_default": true,
            "permissions": [
                id,
                ...
            ]
        }
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_permissions(self, id):
        """ Delete permissions set

        Keywords arguments:
        id -- id of the permissions set
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)
