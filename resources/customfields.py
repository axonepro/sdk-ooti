import requests
import json

from .helper import Helper


class Customfields(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_customfields_list(self, page=1):
        """ Get the list of customfields """

        route = 'v1/customfields/field/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_customfield(self, data):  # Error 500
        """ Create a new customfield 

        Keywords arguments:
        data -- data of the new field to be created:
        {
            "content_type": "project", # REQUIRED
            "name": "string",  # REQUIRED
            "field_type": "t",  # REQUIRED
            "default_value": "string",
            "is_required": false,
            "admin_only": false,
            "permissionssets": [
                permissions_pk,
                ...
            ],
            "permissionssets_can_edit": [
                permissions_pk,
                ...
            ]
        }

        field_type:
        "t" --> Text
        "i" --> Integer
        "a" --> Large Text Field
        "f" --> Floating point decimal
        "d" --> Date

        content_type
        "contact" --> Contact
        "project" --> Project
        "orguser" --> OrgUser

        """

        route = 'v1/customfields/field/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_customfield_details(self, pk):
        """ Get the customfield details 

        Keywords arguments:
        pk -- pk of the customfield
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_customfield_details(self, pk, data):
        """ Update the customfield details 

        Keywords arguments:
        pk -- pk of the customfield
        data -- data of the new field to be created:
        {
            "name": "string",
            "field_type": "t",
            "default_value": "string",
            "is_required": false,
            "admin_only": false,
            "permissionssets: [
                permissionsset_pk,
                ...
            ],
            "permissionssets_can_edit: [
                permissionsset_pk,
                ...
            ]
        }
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_customfield(self, pk):
        """ Delete the customfield 

        Keywords arguments:
        pk -- pk of the customfield
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/customfields/values/{org_pk}/

    # TODO POST on /api/v1/customfields/values/{org_pk}/