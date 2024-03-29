import json

import requests

from .resource import Resource


class Notes(Resource):

    def get_notes_list(self, page=1):
        """Get the list of notes"""

        route = f"v1/notes/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_note(self, data):
        """Create a new note

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

        route = f"v1/notes/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_note_details(self, pk):
        """Get note details

        Keywords arguments:
        pk -- pk of the note
        """

        route = f"v1/notes/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_note_details(self, pk, data):
        """Update note details

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

        route = f"v1/notes/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_note(self, pk):
        """Delete the note

        Keywords arguments:
        pk -- pk of the note
        """

        route = f"v1/notes/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
