import requests
import json

from .helper import Helper


class Notes(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_notes_list(self, page=1):
        """ Get the list of notes """

        route = 'v1/notes/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_note(self, data):
        """ Create a new note

        Keywords arguments:
        data -- data of the new note to be created:
        {
            "text": "string",
            "title": "string",
            "is_pinned": true,
            "project": project_pk,
            "orguser": orguser_pk,
            "is_public": true,
            "entire_project": true,
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/notes/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_note_details(self, pk):
        """ Get note details

        Keywords arguments:
        pk -- pk of the note
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_note_details(self, pk, data):
        """ Update note details

        Keywords arguments:
        pk -- pk of the note
        data -- content of the update:
        {
            "text": "string",
            "title": "string",
            "is_pinned": true,
            "project": project_pk,
            "orguser": orguser_pk,
            "is_public": true,
            "entire_project": true,
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_note(self, pk):
        """ Delete the note

        Keywords arguments:
        pk -- pk of the note
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)