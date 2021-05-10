import requests
import json

from .helper import Helper
from .invoicing import Invoicing
from .deliverables import Deliverables
from .time import Time


class Auth(Helper):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://ooti-staging-3.herokuapp.com/api/'  # "https://app.ooti.co/api/"
        self.org_pk = None
        self.teams_pk = None
        self.access_token = None
        self._csrf_token = None
        self.headers = None
        self.Invoicing = None

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_org()
        self.Invoicing = Invoicing(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers)

        self.Deliverables = Deliverables(self.base_url, self.org_pk, self.teams_pk,
                                         self.access_token, self._csrf_token, self.headers)

        self.Time = Time(self.base_url, self.org_pk, self.teams_pk,
                         self.access_token, self._csrf_token,  self.headers)


##### AUTH #####

    ##### Projects #####

    def get_project_details(self, pk):
        """Get the project details
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def update_project_details(self, pk, data):
        """Update the project details
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def get_projects_list(self):
        """Get the project list"""

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    #### Organizations ####

    def get_organization_details(self):
        """ Get organization details """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def __get_org(self):
        """ Set the organization id of the user """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        self.org_pk = json.loads(response.content)['organizations'][0]['id']
        teams = json.loads(response.content)['organizations'][0]['teams']
        self.teams_pk = []
        for team in range(len(teams)):
            self.teams_pk.append({key: teams[team][key] for key in ('id', 'title')})
        return response.status_code

    #### Token ####

    def __get_token(self):
        route = 'v1/token-auth/'
        headers = {
            'Accept': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=headers, data=data)
        self.access_token = json.loads(response.content)['token']
        self.headers = {
            'Authorization': 'JWT {0}'.format(self.access_token),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRF-Token': self._csrf_token
        }
        return response.status_code

    def __get_csrf_token(self):
        client = requests.session()
        # Retrieve the CSRF token first
        client.get("https://app.ooti.co/accounts/login/")  # sets cookie
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']

        self._csrf_token = csrftoken

    def __refresh_token(self):
        """ Refresh the access token """

        route = 'v1/token-refresh/'
        data = {
            'token': self.access_token
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if response == 201:
            self.headers['Authorization'] = 'JWT {0}'.format(self.access_token)
        return response.status_code

    def __verify_token(self):
        """ Verify if the access token is still valid """

        route = 'v1/token-verify/'
        data = {
            'token': self.access_token
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return response.status_code


##### COSTS #####

    #### Expenses ####

    def get_expenses_list(self):
        """ Get the expenses list """

        route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_expenses_details(self, pk):
        """Get the expense details

        Keyword arguments:

        pk - - the pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}


##### COLLABORATION #####

    #### Contact ####

    def get_contacts_list(self, project_pk=None):
        """ Get the contacts list

        project_pk - - the pk of the contacts' project(optional)
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_contact_details(self, pk):
        """ Get the contact details

        Keywords arguments:
        pk - - the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def update_contact_details(self, pk, data):
        """ Update the contact details

        Keywords arguments:
        pk - - the pk of the contact
        data - - data to update, example value:
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
            "client": [(ids of the clients associated with this contact)
                "string"
            ]
        }
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def create_contact(self, data, project_pk=None):
        """ Create contact

        Keywords arguments:
        project_pk - - the pk of the contact's project(optional)
        data - - data to create:
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
        pk - - the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {'status': response.status_code, 'data': 'Contact deleted'}
        else:
            return {'status': response.status_code, 'data': json.loads(response.content)}

    #### Task ####

    def get_tasks_list(self):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}
