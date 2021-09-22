import requests
import json

from .helper import Helper


class Zones(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def export_zones(self, project_pk):
        """ Export zone

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/zones/export/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_zones_list(self, area_pk, page=1):
        """ Get zones list

        Keyword arguments:

        area_pk -- the pk of the area
        """

        route = 'v1/zones/list/{0}/?page_size={1}&page={2}'.format(area_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_zone(self, area_pk, data):
        """ Create zone

        Keyword arguments:

        area_pk -- the pk of the project
        data -- data create :
        {
            "name": "string" (in UI),
            "area": 0 (required),
            "progress": 0,
            "is_annex": true,
            "internal_code": "string" (in UI),
            "client_code": "string" (in UI),
            "surface_area": 0 (in UI),
            "default_surface_price": 0 (in UI),
            "num_units": 0 (in UI)
        }
        """

        route = 'v1/zones/list/{0}/'.format(area_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_zone_details(self, pk):
        """ Get the zone details

        Keyword arguments:

        pk -- pk of the zone
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_zone(self, pk, data):
        """ Update zone

        Keyword arguments:

        pk -- the pk of the zone
        data -- data create :
        {
            "name": "string",
            "area": 0,
            "progress": 0,
            "is_annex": true,
            "internal_code": "string",
            "client_code": "string",
            "surface_area": 0,
            "default_surface_price": 0,
            "num_units": 0
        }
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_zone(self, pk):
        """ Delete zone

        Keyword arguments:

        pk -- pk of the zone
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)