import json

import requests

from .resource import Resource


class Milestones(Resource):

    def get_milestones_list(self, page=1):
        """Get milestones list"""
        route = (
            f"v1/milestones/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        )
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_milestone(self, data):
        """Create a milestone

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "title": "string",
                "project": 0,
                "date": "string",
                "phases": [
                    "string"
                ],
                "annexes": [
                    "string"
                ],
                "description": "string",
                "in_timeline": true
            }
        """
        route = f"v1/milestones/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_milestone_details(self, pk):
        """Get melistone details

        Keyword arguments:

        pk -- pk of the milestone
        """
        route = f"v1/milestones/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_milestone(self, pk, data):
        """Update a milestone

        Keyword arguments:

        pk -- pk of the milestone
        data -- data update:
            {
                "title": "string",
                "project": 0,
                "date": "string",
                "phases": [
                    "string"
                ],
                "annexes": [
                    "string"
                ],
                "description": "string",
                "in_timeline": true
            }
        """
        route = f"v1/milestones/{pk}/"
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

    def delete_milestone(self, pk):
        """Delete milestone

        Keyword arguments:

        pk -- pk of the milestone
        """
        route = f"v1/milestones/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
