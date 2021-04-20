import requests
import json


class Auth(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.org_pk = None
        self.base_url = "https://ooti-staging-3.herokuapp.com/api/"
        self.access_token = None
        self._csrf_token = None
        self.headers = None

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_org()

    def get_invoice_details(self, pk):
        """Get the invoice details
        Keyword arguments:
        pk -- the pk of the invoice
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return json.loads(response.content)

    def get_invoices_list(self):
        """Get the invoice list"""

        route = 'v1/invoices/list/{0}/?page_size=200'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return json.loads(response.content)['results']

    def update_invoice(self, pk, data):
        """Create an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        data -- data to create
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return json.loads(response.content)

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

        return {"status": response.status_code}

    def get_payment_details(self, pk):
        """Get the payment details
        Keyword arguments:
        pk -- the pk of the payment
        """

        route = 'v1/payments/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return json.loads(response.content)

    def get_payments_list(self):
        """Get the payment list"""

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return json.loads(response.content)['results']

    def update_payment(self, pk, data):
        """Create an payment
        Keyword arguments:
        pk -- the pk of the payment
        data -- data to create
        """

        route = 'v1/payments/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return json.loads(response.content)

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
        return json.loads(response.content)

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

    def get_phases_list(self, pk):
        """Get the phase list
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/phases/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

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

        return {"status": 204, "data": json.loads(response.content)}

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

    def __get_org(self):
        """ Set the organization id of the user """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        self.org_pk = json.loads(response.content)['organizations'][0]['id']
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
        """ Return the access toke if it's still valid """

        route = 'v1/token-verify/'
        data = {
            'token': self.access_token
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return response.status_code
