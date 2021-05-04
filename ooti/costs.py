import requests
import json

from helper import Helper


class Costs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Costs ####

    #### Employees ####

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

    #### Freelancers ####

    #### Jobs ####
