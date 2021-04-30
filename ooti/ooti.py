import requests
import json


class Auth(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://ooti-staging-3.herokuapp.com/api/'  # "https://app.ooti.co/api/"
        self.org_pk = None
        self.teams_pk = None
        self.access_token = None
        self._csrf_token = None
        self.headers = None

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_org()

##### HELPER #####

    def process_response(self, response, results=None):
        """ Process the response and return it 
        :param: reponse is the reponse from the API
        :param: results is saying if we just want the results field of the reponse
        :return: {status, data} or {status} if data is not JSON serializable
        """
        try:
            if(results == None):
                return {'status': response.status_code, 'data': json.loads(response.content)}
            else:
                return {'status': response.status_code, 'data': json.loads(response.content)['results']}
        except ValueError:
            return {'status': response.status_code}
        except KeyError:
            return self.process_response(response)

##### AUTH #####

    ##### Projects #####

    def get_project_details(self, id):
        """ Get the project details

        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_project_details(self, id, data):
        """ Update the project details

        Keyword arguments:
        id -- the id of the project
        data -- content of the update :
        {
            "surface_area": 238,
            "surface_unit": "m",
            "notes": "some notes",
            "project_title": "New title"
        }
        """

        route = 'v1/projects/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project(self, id):
        """ Delete a project

        Keyword arguments:
        id -- the id of the project
        """
        route = 'v1/projects/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projects_list(self, team_pk=None):
        """ Get the projects list 

        Keywords arguments:
        team_pk -- pk of a team to get the project list of a specific team
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        if team_pk is not None:
            route += '{0}/'.format(team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def create_project(self, data):  # Error 500
        """ Create a new project

        Keyword arguments:
        data -- content of the project to be created :
        {
            "client": client_pk,
            "currency": curency_pk,
            "project_title": "New project",
            "phases": [phase_pk, phase_pk, ...],
            "project_users": [project_user_pk, ...],
            "areas": [],
            "project_tags": [],
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [orguser_pk, orguser_pk, ...],
            "city": "Paris",
            "country": "FR"
        }
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_project_fee_summary(self, id):
        """ Get the project fee summary

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/fee-summary/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_revenue(self, id):
        """ Get the list of project revenues by years and by months

        Keywords arguments:
        id -- the id of the project
        """
        route = 'v1/projects/revenue/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_available_clients(self, id):
        """ Get the list of clients avalaible (clients that are not already participating in the project)
        Return the list of clients with their display name and pk

        Keywords arguments:
        id -- the id of the project
        """

        route = 'v1/projects/available-clients/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projects_list_deliverables(self):
        """ Get the list of projects and their associated deliverables where the current user is a member of """

        route = 'v1/projects/deliverables/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_users_list(self, id):
        """ Get the list of users of a project 

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/users/list/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_project_user_details(self, user_pk):
        """ Get the project user details 

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def add_project_user(self, id, data):
        """ Add a new user to the project 

        Keyword arguments:
        id -- id of the project
        data -- content of the user to add to the project :
        {
            "orguser": orguser_pk,
            "permissionsset": permission_pk,
            "project": project_id,
            "is_visible": true
        }
        """

        route = 'v1/projects/users/list/{0}/'.format(id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_project_user_details(self, user_pk, data):
        """ Update the project user details 

        Keyword arguments:
        user_pk -- pk of the user
        data -- content of the update :
        {
            "hours_actual": 10,
            "is_billable": False
        }
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project_user(self, user_pk):
        """ Delete the project user

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_tags_list(self):
        """ Get the list of tags """

        route = 'v1/projects/tags/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_project_tag(self, data):
        """ Create a new tag 

        Keywords arguments:
        data -- content of the tag to be created :
        {
            "name": "new tag", (required)
            "group": group_id, (optional)
            "projects": [project_id, project_id, ...] (optional) # list of projects to add the tag
        }
        """

        route = 'v1/projects/tags/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_project_tag_details(self, tag_pk):
        """ Get project tag details 

        Keywords arguments:
        tag_pk -- pk of the tag
        """
        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_project_tag_details(self, tag_pk, data):
        """ Update project tag details 

        Keywords arguments:
        tag_pk -- pk of the tag
        data -- content of the update :
        {
            "name": "new name",
            "projects": [project_id, project_id, ...]
        }
        """

        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project_tag(self, tag_pk):
        """ Delete project tag 

        Keywords arguments:
        tag_pk -- pk of the tag to be deleted
        """

        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Orgusers ####

    def get_orgusers_list(self):
        """ Get the list of users in the organization """

        route = 'v1/orgusers/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_orguser_details(self, pk):
        """ Get the orguser details

        Keyword arguments:
        pk -- pk of the orguser
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_orguser(self, data):
        """ Create a new user in the organization 

        data -- content of the orguser to be created :
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_orguser_details(self, pk, data):
        """ Update the orguser details 

        Keywords arguments:
        pk -- pk of the orguser to update
        data -- content of the update :
        {
            "mobile": "012345678",
            "birthday": "16-04-2021"
        }
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_orguser(self, pk):
        """ Delete the orguser 

        Keyword arguments:
        pk -- pk of the orguser to update
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Organizations ####

    def get_user_organization_details(self):
        """ Returns short user information and orgs/teams/projects he is member of """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_organization_details(self, pk):
        """ Get organizations details """

        route = 'v1/organizations/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

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

    #### Profile ####

    def get_profile_preferences(self):
        """ Get profile preferences """

        route = 'v1/profiles/preferences/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_profile_details(self):
        """ Get current profile details """

        route = 'v1/profiles/profile/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_profile_details(self, data):
        """ Update current profile details 

        Keywords arguments:
        data -- content of the update :
        {
            "locale": "en",
            "show_sidemenu": False
        }
        """

        route = 'v1/profiles/profile/'
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    # post method on profile preferences ?

    #### Team #####

    def get_teams_list(self):
        """ Get the list of teams """

        route = 'v1/teams/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_team_users_list(self, pk):
        """ Get the list of users in the team 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/users/list/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_team_user_details(self, orguser_pk):  # same thing as get_orguser_details ?
        """ Get the orguser details related to the team he is in

        Keywords arguments:
        orguser_pk -- pk of the orguser
        """

        route = 'v1/teams/users/{0}/'.format(orguser_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_team_user_details(self, orguser_pk, data):
        """ Update the orguser details related to the team he is in

        Keywords arguments:
        orguser_pk -- pk of the orguser
        data -- content of the update :
        {
            "permissionsset": 16464,
            "team": team_pk
        }
        """

        route = 'v1/teams/users/{0}/'.format(orguser_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_team_details(self, pk):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_team_details(self, pk, data):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        data -- content of the update :
        {
            "city": "Lyon",
            "address": "2 Avenue du Trône"
        }
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

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


##### DELIVERABLES #####

    #### Phases ####

    def get_phase_details(self, pk):
        """Get the phase details
        Keyword arguments:
        pk -- the pk of the phase
        data -- data to update
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_phase_details(self, pk, data):
        """Update the phase details
        Keyword arguments:
        pk -- the pk of the phase
        data -- data to update
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_phases_list(self, project_pk):
        """Get the phase list
        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/phases/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    #### Annexes ####

    def get_annexes_list(self, project_pk):
        """Get the annexes list
        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_annex_details(self, pk):
        """Get the annex details
        Keyword arguments:
        pk -- the pk of the annex
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_annex(self, project_pk, data):
        """Create an annex
        Keyword arguments:
        project_pk -- the pk of the project
        data -- data to create
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        parameters = '?phase='
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_annex(self, pk, data):
        """Update the annex details
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)


##### INVOICING #####

    #### Invoices ####


    def get_invoice_details(self, pk):
        """Get the invoice details
        Keyword arguments:
        pk -- the pk of the invoice
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_invoices_list(self):
        """Get the invoice list"""

        route = 'v1/invoices/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_invoices_sent_valid_list(self):
        """ Get the sent and valid invoice list """

        route = 'v1/invoices/list/{0}/?team={1}&page_size=999999&q=&is_sent=true&is_valid=true'.format(
            self.org_pk, self.teams_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def update_invoice(self, pk, data):
        """Create an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        data -- data to create :
            {
                "invoice_date": "DD-MM-YYYY",
                "billing_option": 0,
                "bank": 0,
                "purchase_order": "string",
                "references": "string",
                "is_valid": Boolean,
                "is_sent": Boolean,
                "multi_tax_enabled": Boolean (if invoice items have multi tax rates)
            }
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if(response.status_code == 200):
            return {'status': response.status_code}
        else:
            return self.process_response(response)

    def create_invoice(self, team_pk, data):
        """Create an invoice
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data to create :
            {
                "project": 0,
                "type": 0,
                "invoice_date": "DD-MM-YYYY",
                "due_date": "DD-MM-YYYY"
                "client_name": "string",
                "client_address": "string",
                "references": "string"
                "team": 0
            }
            Note that for type 4 (other), project is not mandatory
        """

        route = 'v1/invoices/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def validate_invoice(self, pk):
        """Validate an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_valid": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def send_invoice(self, pk):
        """Send an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_sent": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def cancel_invoice(self, pk):
        """Cancel an invoice and create a credit note
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_closed": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if(response.status_code == 200):
            response_data = json.loads(response.content)
            credit_note_pk = response_data['credit_note_url'].split('/')[4]
        return {'status': response.status_code, 'data': credit_note_pk}

    def get_invoice_items(self, pk):
        """ Get invoice's items
        Keyword arguments: 
        pk -- invoice pk
        """

        route = 'v1/invoices/items/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_invoice_item(self, pk, data):
        """ Create invoice's item
        Keyword Arguments:
        pk -- pk of the invoice
        data -- data to create :
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0,
                "tax_rate": 0.0 (if invoice.multi_tax_rate = True)
                "tax": 0.0 (tax amount, if invoice.multi_tax_rate = True)
            }
        """

        route = 'v1/invoices/items/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if(response.status_code not in [500]):
            return self.process_response(response)
        else:
            return {'status': response.status_code}

    def update_invoice_item(self, pk, data):
        """ Update invoice's item
        Keyword Arguments:
        pk -- pk of the item
        data -- data to update :
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0
            }
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))

        if(response.status_code == 200):
            return {'status': response.status_code}
        else:
            return self.process_response(response)

    def delete_invoice_item(self, pk):
        """ Update invoice's item
        Keyword Arguments:
        pk -- pk of the item
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code not in [204]):
            return self.process_response(response)
        else:
            return {'status': response.status_code}

    #### Credit notes ####

    def get_credit_notes_list(self):
        """Get the invoice list"""

        route = 'v1/invoices/list/{0}/?page_size=999999&type=9'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_credit_notes_sent_valid_list(self):
        """ Get the sent and valid invoice list """

        route = 'v1/invoices/list/{0}/?team={1}&page_size=999999&q=&is_sent=true&is_valid=true&type=9'.format(
            self.org_pk, self.teams_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    #### Payments ####

    def get_payment_details(self, pk):
        """Get the payment details
        Keyword arguments:
        pk -- the pk of the payment
        """

        route = 'v1/payments/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_payments_list(self):
        """Get the payment list"""

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def update_payment(self, pk, data):
        """Create an payment
        Keyword arguments:
        pk -- the pk of the payment
        data -- data to create : 
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "currency_rate": 0,
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk)
            }
        """

        route = 'v1/payments/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_payment_invoice(self, pk, data):
        """ Update payment's amount on invoice
        Please do not call this function before update_payment. 
        To make an update on a payment, first use the "update_payment" method. 
        Then, update the amount on the invoice with this method. 
        Keyword arguments :
        pk -- pk of payment
        data -- data to update : 
            {
                "amount": 0
            }
        """
        route = 'v1/payments/invoice/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def create_payment(self, team_pk, data):
        """Create an payment
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data to create : 
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk) (no need of project for invoices of type 4)
            }
        """

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    ##### Clients #####

    def get_clients_list(self, team_pk):
        """Get the clients list
        Keyword arguments:
        pk -- the pk of the team
        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)
        parameters = '?page_size=999999&team={0}'.format(team_pk)

        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return {"status": response.status_code, "data": json.loads(response.content)['results']}

    def get_clients_details(self, pk):
        """Get the client details
        Keyword arguments:
        pk -- the pk of the client
        """

        route = 'v1/clients/{0}/'.format(pk)

        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {"status": response.status_code, "data": json.loads(response.content)}

    def create_client(self, data):
        """ Create client 
        Keyword arguments:
        data -- data to create, required fields : 
            {
                "company_name": "string",
                "number": "string",
                "currency": "string" (currency_pk)
                "billing_address": "string",
                "team": "string",
                "tags": []
            }
        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)

        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def update_client(self, pk, data):
        """ Update client
        Keyword arguments:
        pk -- pk of the client 
        data -- data to create, required fields : 
            {
                "company_name": "string",
                "currency": "string" (currency_pk),
                "number": "string",
                "business_vat_id: "string",
                "billing_address": "string",
                "group": "?"
                "address: "string"
            }
        """
        route = 'v1/clients/{0}/'.format(pk)

        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def delete_client(self, pk):
        """ Delete client
        Keyword arguments:
        pk -- pk of the client
        """
        route = 'v1/clients/{0}/'.format(pk)

        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {"status": response.status_code, "data": "Client deleted"}
        else:
            return {"status": response.status_code, "data": json.loads(response.content)}

    ##### Currencies #####

    def get_currencies_list(self):
        """Get the currencies list """

        route = 'v1/currencies/list/?page_size=200'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {"status": response.status_code, "data": json.loads(response.content)['results']}

    def get_currency_details(self, pk):
        """ Get the currency details
        Keyword arguments:
        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {"status": response.status_code, "data": json.loads(response.content)}

    def delete_currency(self, pk):
        """ Delete a currency
        Keyword arguments:
        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {"status": 204, "data": "Currency deleted"}

    def create_currency(self, data):
        """ Create a currency
        Keyword arguments:
        data -- data to create, required fields : 
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }
        """

        route = 'v1/currencies/list/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def update_currency(self, pk, data):
        """ Update a currency
        Keyword arguments:
        data -- data to create, required fields : 
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }
        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers,
                                  data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}


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
        pk -- the pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)


##### COLLABORATION #####

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
        """ Create contact
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


##### TIME #####


##### SETTINGS #####


##### RANDOM #####
