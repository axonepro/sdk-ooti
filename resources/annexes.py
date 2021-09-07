import requests
import json

from .helper import Helper


class Annexes(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_annexes_list(self, project_pk):
        """ Get the annexes list

        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_annexe_details(self, pk):
        """ Get the annexe details

        Keyword arguments:
        pk -- the pk of the annexe
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_annexe(self, project_pk, data):
        """C reate a payment

        Keyword arguments:
        project_pk -- the pk of the project
        data -- data create : 
        {
            "phases": [
                "string"
            ],
            "zone": 0,
            "document": 0,
            "title": "string",
            "date": "string",
            "description": "string",
            "enter_hours": true,
            "progress": 0,
            "in_timeline": true,
            "in_budget": true
            "annex_time": "string" ("time", "other", "transport"),
            "total_fees": 0,
        }
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_annexe(self, pk, data):
        """ Update the annexe

        Keyword arguments:
        pk - - the pk of the project
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def delete_annexe(self, pk):
        """ Delete annexe

        Keyword arguments:

        pk -- the pk of the annexe
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_annexes_projections_list(self, project_pk):
        """ Get the annexes projection list

        Keyword arguments:
        project_pk -- the pk of the project
        """

        route = 'v1/annexes/projections/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)