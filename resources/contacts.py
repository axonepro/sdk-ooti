import requests
import json

from .helper import Helper


class Contacts(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_contact_categories_list(self, project_id=None):
        """ Get the list of categories of contact

        Keywords arguments:
        project_id -- id of the project if the category is specific to a project
        """

        route = 'v1/contacts/categories/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_contact_category(self, data, project_id=None):
        """ Create a new category for contacts

        Keywords arguments:
        project_id -- id of the project if the category is specific to a project
        data -- data of the new category to be created:
        {
            "name": "new category",
            "count": 2,
            "permissionssets": [
                permissionset_pk,
                ...
            ]
        }
        """
        route = 'v1/contacts/categories/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response, True)

    def get_contact_category_details(self, category_pk):
        """ Get the contact category details

        Keywords arguments:
        category_pk -- the pk of the contact
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_contact_category_details(self, category_pk, data):
        """ Update the contact category details

        Keywords arguments:
        category_pk -- the pk of the contact category
        data -- content of the update:
        {
            "name": "new name",
            "count": 1,
            "permissionssets": [
                permissionsset_pk,
                ...
            ]
        }
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_contact_category(self, category_pk):
        """ Delete the contact

        Keywords arguments:
        category_pk -- the pk of the contact category
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_contact_list_action(self):

        route = 'v1/contacts/list-action/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO POST on /api/v1/contacts/list-action/{org_pk}/

    def get_contacts_list(self, project_id=None, page=1):
        """ Get the contacts list

        project_id -- id of the contacts' project (optional)
        """

        route = 'v1/contacts/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_contact(self, data, project_id=None):
        """ Create a new contact

        Keywords arguments:
        project_id -- id of the contact's project (optional)
        data -- data to create:
            {   
                "name": "string" (required),
                "first_name": "string" (optional),
                "last_name": "string" (optional),
                "email": "string" (optional),
                "mobile_phone": "string" (optional),
                "job_title": "string" (optional)
            }
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_number_uncategorized_contacts(self, team_pk=None, project_id=None):
        """ Return the number of uncategorized contacts """

        route = 'v1/contacts/uncategorized/count/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, parameters, None)
        return self.process_response(response)

    def get_contact_details(self, pk):
        """ Get the contact details

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_contact_details(self, pk, data):
        """ Update the contact details

        Keywords arguments:
        pk -- the pk of the contact
        data -- content of the update:
        {
            "name": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "mobile_phone": "string",
            "office_phone": "string",
            "home_phone": "string",
            "fax": "string",
            "website": "string",
            "street1": "string",
            "postal_code1": "string",
            "city1": "string",
            "province1": "string",
            "country1": "string",
            "job_title": "string",
            "client": [ (ids of the clients associated with this contact)
                "string" 
            ]
        }
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_contact(self, pk):
        """ Delete the contact

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)