import json

import requests

from .resource import Resource


class Revisions(Resource):

    def delete_revisions_annexe_detail(self, pk):
        """Delete revision annexe detail
        Keyword arguments:

        pk -- the pk of the annex revision
        """

        route = f"v1/revisions/annexes/detail/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_revisions_annexes_team_project(self, team_pk, project_pk, page=1):
        """Get annexes revisions team project

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = f"v1/revisions/annexes/{team_pk}/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_annexe_revision(self, team_pk, project_pk, data):
        """Create an annexe revision team project

        Keyword arguments:

        data -- data create :
            {
                "progress": 0,
                "date": "string",
                "annex": 0,
                "reviewer": 0,
                "validator": 0,
                "is_valid": true
            }
        """

        route = f"v1/revisions/annexes/{team_pk}/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_revisions_document_detail(self, pk):
        """Delete revision document details
        Keyword arguments:

        pk -- the pk of the document revision
        """

        route = f"v1/revisions/documents/detail/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_revisions_documents_team_project(self, team_pk, project_pk, page=1):
        """Get documents revisions team project

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = f"v1/revisions/documents/{team_pk}/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_document_revision(self, team_pk, project_pk, data):
        """Create a documents revision team project

        Keyword arguments:

        data -- data create :
            {
                "progress": 0,
                "date": "string",
                "doc": 0,
                "reviewer": 0,
                "validator": 0
            }
        """

        route = f"v1/revisions/documents/{team_pk}/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_revisions_fee_items_detail(self, pk):
        """Delete revision fee_items detail

        Keyword arguments:

        pk -- the pk of the fee_items revision
        """

        route = f"v1/revisions/fee_items/detail/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_revisions_fee_items_team_project(self, team_pk, project_pk, page=1):
        """Get fee_items revisions team project

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = f"v1/revisions/fee_items/{team_pk}/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_fee_items_revision(self, team_pk, project_pk, data):
        """Create an fee_items revision team project

        Keyword arguments:

        data -- data create :
            {
                "fee_item": 0,
                "progress": 0,
                "date": "string",
                "reviewer": 0,
                "validator": 0,
                "is_valid": true
            }
        """

        route = f"v1/revisions/fee_items/{team_pk}/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_revisions_phases_detail(self, pk):
        """Delete revision phases detail

        Keyword arguments:

        pk -- the pk of the phases revision
        """

        route = f"v1/revisions/phases/detail/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_revisions_phases_team_project(self, team_pk, project_pk, page=1):
        """Get phases revisions team project

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = f"v1/revisions/phases/{team_pk}/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_phase_revision(self, team_pk, project_pk, data):
        """Create a phase revision team project

        Keyword arguments:

        data -- data create :
            {
                "phase": 0,
                "progress": 0,
                "date": "string",
                "reviewer": 0,
                "validator": 0,
                "is_valid": true
            }
        """

        route = f"v1/revisions/phases/{team_pk}/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_revisions_plan_detail(self, pk):
        """Delete revision plans detail

        Keyword arguments:

        pk -- the pk of the plans revision
        """

        route = f"v1/revisions/plans/detail/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_revisions_plans_team_project(self, team_pk, project_pk, page=1):
        """Get plans revisions team project

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = f"v1/revisions/plans/{team_pk}/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_plan_revision(self, team_pk, project_pk, data):
        """Create a plans revision team project

        Keyword arguments:

        data -- data create :
            {
                "progress": 0,
                "date": "string",
                "plan_phase": 0,
                "reviewer": 0,
                "validator": 0
            }
        """

        route = f"v1/revisions/plans/{team_pk}/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)
