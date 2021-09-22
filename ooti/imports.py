import requests
import json

from .helper import Helper

"""
- ERROR 403 : GET v1/imports/counts/
- ERROR 400 ("Type is required"): GET & POST v1/imports/import/{org_pk}/
- POST on v1/imports/{id}/map-columns/ ?

"""

class Imports(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_imports_count(self):  # Error 403
        """ Get the number of imports """

        route = 'v1/imports/counts/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_exports_list(self, page=1):
        """ Get the list of exports """

        route = 'v1/imports/export/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_export(self, data):
        """ Get imports list

        Keywords arguments
        data -- data of the new import to be created:
        {
            "orguser": orguser_pk,
            "team": team_pk,
            "project": project_id,
            "type": "string",
            "items": 0,
            "started_processing_at": "string",
            "ended_processing_at": "string",
            "include_documents": true
        }
        """

        route = 'v1/imports/export/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_export_details(self, export_pk):
        """ Get the export details 

        Keywords arguments:
        export_pk -- pk of the export
        """

        route = 'v1/imports/export/{0}/'.format(export_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def delete_export(self, export_pk):
        """ Delete the export

        Keywords arguments:
        export_pk -- pk of the export
        """

        route = 'v1/imports/export/{0}/'.format(export_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/imports/import/{org_pk}/

    # TODO POST on /api/v1/imports/import/{org_pk}/

    def get_imports_list(self, page=1):
        """ Get the list of imports """

        route = 'v1/imports/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_import(self, data):
        """ Create a new import

        Keywords arguments:
        data -- data of the new import to be created:
        {
            "data": {

            } 
            "type":
        }
        """

        route = 'v1/imports/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_import_details(self, id):
        """ Get the import details

        Keywords arguments:
        id -- id of the import
        """

        route = 'v1/imports/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_import_details(self, id, data):
        """ Update the import details

        Keywords arguments:
        id -- id of the import
        data -- content of the update
        """

        route = 'v1/imports/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_import(self, id):
        """ Delete the import 

        Keywords arguments:
        id -- id of the import
        """

        route = 'v1/imports/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO POST on /api/v1/imports/{id}/map-columns/