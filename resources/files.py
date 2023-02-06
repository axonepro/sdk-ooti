import json

import requests

from .resource import Resource


class Files(Resource):

    def get_folder_list(self, project_pk, page=1):
        """Get the folder list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = f"v1/files/folder/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_folder(self, project_pk, data):
        """Create a folder

        Keyword arguments:

        project_pk -- pk of the project
        data -- data to be created:
            {
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "parent": 0
            }
        """
        route = f"v1/files/folder/list/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_folder_details(self, pk):
        """Get the folder details

        Keyword arguments:

        pk -- pk of the folder
        """

        route = f"v1/files/folder/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_folder(self, pk, data):
        """Update a folder

        Keyword arguments:

        pk -- pk of the folder
        data -- data to be updated:
            {
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "parent": 0
            }
        """
        route = f"v1/files/folder/{pk}/"
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

    def delete_folder(self, pk):
        """Delete a folder

        Keyword arguments:

        pk -- pk of the folder
        """
        route = f"v1/files/folder/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_files_list(self, project_pk, page=1):
        """Get the files list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = f"v1/files/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_file(self, project_pk, data):
        """Create a file

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = f"v1/files/list/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response, True)

    # TODO GET on /api/v1/files/request_access/

    # TODO GET on /api/v1/files/smtp_request_access/

    def get_file_details(self, pk):
        """Get the file details

        Keyword arguments:

        pk -- pk of the file
        """

        route = f"v1/files/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    # TODO PATCH on /api/v1/files/{id}/

    def delete_file(self, pk):
        """Delete a file

        Keyword arguments:

        pk -- pk of the file
        """

        route = f"v1/files/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
