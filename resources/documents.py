import requests
import json

from .helper import Helper


class Documents(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_documents_list(self, project_pk, page=1):
        """ Get docuemnts list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/documents/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_document(self, project_pk, data):
        """ Create a docuemnt

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create : 
            {
                "progress": 0,
                "name": "string", (R)
                "doc_category": "string",
                "price_weight": 0,
                "price": 0, (R)
                "weight": 0,
                "progress_weighted": 0,
                "phase": 0,
                "is_mockup": true,
                "is_additional": true,
                "in_contract": true,
                "annexes": [
                    "string"
                ],
                "zone": 0
            }
        """

        route = 'v1/documents/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def set_price_documents(self, project_pk):
        """ Set price document

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/documents/set-price/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_document_details(self, pk):
        """ Get document details

        Keyword arguments:

        pk -- the pk of the document
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_document(self, pk, data):
        """ Update a docuemnt

        Keyword arguments:

        pk -- the pk of the document
        data -- data update : 
            {
                "progress": 0,
                "name": "string",
                "doc_category": "string",
                "price_weight": 0,
                "price": 0,
                "weight": 0,
                "progress_weighted": 0,
                "phase": 0,
                "is_mockup": true,
                "is_additional": true,
                "in_contract": true,
                "annexes": [
                    "string"
                ],
                "zone": 0
            }
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_document(self, pk):
        """ Delete document

        Keyword arguments:

        pk -- the pk of the document
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)