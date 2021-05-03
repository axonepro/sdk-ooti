import requests
import json

from .helper import Helper


class Collaboration(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Contact ####

    def get_contacts_list(self, project_pk=None):
        """ Get the contacts list

        project_pk -- the pk of the contacts' project (optional)
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_contact_details(self, pk):
        """ Get the contact details

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contact_details(self, pk, data):
        """ Update the contact details

        Keywords arguments:
        pk -- the pk of the contact
        data -- data to update, example value:
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def create_contact(self, data, project_pk=None):
        """ Create a new contact

        Keywords arguments:
        project_pk -- the pk of the contact's project (optional)
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
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if(response.status_code != 500):
            return {'status': response.status_code, 'data': json.loads(response.content)['results']}
        else:
            return {'status': response.status_code}

    def delete_contact(self, pk):
        """ Delete the contact

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {'status': response.status_code, 'data': 'Contact deleted'}
        else:
            return self.process_response(response)

    #### Task ####

    def get_tasks_list(self):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
