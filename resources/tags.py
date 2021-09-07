import requests
import json

from .helper import Helper


class Tags(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_tags_list(self, page=1):
        """ Get the list of tags """

        route = 'v1/tags/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_tag(self, data):
        """ Create a new tag 

        Keywords arguments:
        data -- data of the new tag to be created:
        {
            "name": "string",
            "contacts": [
                contact_pk,
                ...
            ],
            "contractors": [
                contractor_pk
            ],
            "clients": [
                client_pk,
                ...
            ],
            "orgusers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tags/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_tag_details(self, id):
        """ Get the tag details

        Keywords arguments:
        id -- id of the tag
        """

        route = 'v1/tags/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_tag_details(self, id, data):
        """ Update the tag details

        Keywords arguments:
        id -- id of the tag
        data -- content of the update:
        {
            "name": "string",
            "contacts": [
                contact_pk,
                ...
            ],
            "contractors": [
                contractor_pk
            ],
            "clients": [
                client_pk,
                ...
            ],
            "orgusers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tags/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_tag(self, id):
        """ Delete the tag

        Keywords arguments:
        id -- id of the tag
        """

        route = 'v1/tags/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)