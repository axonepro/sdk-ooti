import requests
import json

from .helper import Helper


class Trips(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_trips_list(self, page=1):
        """ Get trips list """

        route = 'v1/trips/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_trip(self, data):
        """ Create trip  

        Keyword arguments:

        data -- data create:
        {
            "team": 0,
            "project": 0,
            "orguser": 0,
            "start_date": "string",
            "end_date": "string",
            "notes": "string"
        }
        """

        route = 'v1/trips/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_trips_details(self, pk):
        """ Get trip details 

        Keyword arguments:

        pk -- pk of the rtrip
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_trip(self, pk, data):
        """ Update trip 

        Keyword arguments:

        pk -- pk of the trip
        data -- data create:
        {
            "team": 0,
            "project": 0,
            "orguser": 0,
            "start_date": "string",
            "end_date": "string",
            "notes": "string"
        }
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_trip(self, pk):
        """ Delete trip 

        Keyword arguments:

        pk -- pk of the trip
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)