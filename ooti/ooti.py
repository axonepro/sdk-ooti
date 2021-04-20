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

###### Invoice ######

    def get_invoice_details(self, pk):
        """Get the invoice details
        Keyword arguments:
        pk -- the pk of the invoice
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def get_invoices_list(self):
        """Get the invoice list"""

        route = 'v1/invoices/list/{0}/?page_size=200'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def update_invoice(self, pk, data):
        """Create an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        data -- data to create
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def create_invoice(self, team_pk, data):
        """Create an invoice
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data to create
        """

        route = 'v1/invoices/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))

        return {'status': response.status_code, 'data': "Invoice created"}

##### Payment #####

    def get_payment_details(self, pk):
        """Get the payment details
        Keyword arguments:
        pk -- the pk of the payment
        """

        route = 'v1/payments/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def get_payments_list(self):
        """Get the payment list"""

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def update_payment(self, pk, data):
        """Create an payment
        Keyword arguments:
        pk -- the pk of the payment
        data -- data to create
        """

        route = 'v1/payments/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return json.loads(response.content)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def create_payment(self, team_pk, data):
        """Create an payment
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data to create
        """

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

###### Project ######

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


##### Phase #####


    def get_phase_details(self, pk):
        """Get the phase details
        Keyword arguments:
        pk -- the pk of the phase
        data -- data to update
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def update_phase_details(self, pk, data):
        """Update the phase details
        Keyword arguments:
        pk -- the pk of the phase
        data -- data to update
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def get_phases_list(self, project_pk):
        """Get the phase list
        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/phases/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

###### Currency ######

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
        if(response.status_code == 201):
            return {"status": 201, "data": "Currency created"}

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

    ###### Clients ######

    def get_clients_list(self, team_pk):
        """Get the clients list

        Keyword arguments:

        pk -- the pk of the team

        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)
        parameters = '?page_size=50&team={0}'.format(team_pk)

        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return {"status": response.status_code, "data": json.loads(response.content)}

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


##### Task #####

    def get_tasks_list(self):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}


##### Annexe #####


    def get_annexes_list(self, project_pk):
        """Get the annexes list

        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_annexe_details(self, pk):
        """Get the annexe details

        Keyword arguments:
        pk -- the pk of the annexe
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def create_annexe(self, project_pk, data):
        """Create an payment

        Keyword arguments:
        project_pk -- the pk of the project
        data -- data to create
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        parameters = '?phase='
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))

    def update_annexe(self, pk, data):
        """Update the annexe details

        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}


##### Organization #####


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


##### Token #####


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
