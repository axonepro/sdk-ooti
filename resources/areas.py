import requests
import json

from .helper import Helper


class Areas(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)
    
    def get_areas_list(self, project_pk, page=1):
        """ Get the areas list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/areas/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_areas(self, project_pk, data):
        """ Create an area

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "name": "string" (in UI),
                "project": 0,
                "internal_code": "string" (in UI),
                "client_code": "string" (in UI)
            }
        """
        route = 'v1/areas/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_areas_details(self, pk):
        """ Get the area details

        Keyword arguments:

        pk -- pk of the area
        """

        route = 'v1/areas/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_areas(self, pk, data):
        """ Update an area

        Keyword arguments:

        pk -- pk of the project
        data -- data update:
            {
                "name": "string",
                "project": 0,
                "internal_code": "string",
                "client_code": "string"
            }
        """
        route = 'v1/areas/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_area(self, pk):
        """ Delete an area

        Keyword arguments:

        pk -- pk of the project
        """
        route = 'v1/areas/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)