import requests
import json

from .helper import Helper


class Revisions(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def delete_revisions_annexe_detail(self, pk):
        """ Delete revision annexe detail
        Keyword arguments:

        pk -- the pk of the annex revision
        """

        route = 'v1/revisions/annexes/detail/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_revisions_annexes_team_project(self, team_pk, project_pk, page=1):
        """ Get annexes revisions team project 

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = 'v1/revisions/annexes/{0}/{1}/?page_size={2}&page={3}'.format(
            team_pk, project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_annexe_revision(self, team_pk, project_pk, data):
        """ Create an annexe revision team project

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

        route = 'v1/revisions/annexes/{0}/{1}/'.format(team_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revisions_document_detail(self, pk):
        """ Delete revision document details
        Keyword arguments:

        pk -- the pk of the document revision
        """

        route = 'v1/revisions/documents/detail/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_revisions_documents_team_project(self, team_pk, project_pk, page=1):
        """ Get documents revisions team project 

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = 'v1/revisions/documents/{0}/{1}/?page_size={2}&page={3}'.format(
            team_pk, project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_document_revision(self, team_pk, project_pk, data):
        """ Create a documents revision team project

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

        route = 'v1/revisions/documents/{0}/{1}/'.format(team_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revisions_fee_items_detail(self, pk):
        """ Delete revision fee_items detail

        Keyword arguments:

        pk -- the pk of the fee_items revision
        """

        route = 'v1/revisions/fee_items/detail/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_revisions_fee_items_team_project(self, team_pk, project_pk, page=1):
        """ Get fee_items revisions team project 

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = 'v1/revisions/fee_items/{0}/{1}/?page_size={2}&page={3}'.format(
            team_pk, project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fee_items_revision(self, team_pk, project_pk, data):
        """ Create an fee_items revision team project

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

        route = 'v1/revisions/fee_items/{0}/{1}/'.format(team_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revisions_phases_detail(self, pk):
        """ Delete revision phases detail

        Keyword arguments:

        pk -- the pk of the phases revision
        """

        route = 'v1/revisions/phases/detail/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_revisions_phases_team_project(self, team_pk, project_pk, page=1):
        """ Get phases revisions team project 

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = 'v1/revisions/phases/{0}/{1}/?page_size={2}&page={3}'.format(team_pk, project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_phase_revision(self, team_pk, project_pk, data):
        """ Create a phase revision team project

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

        route = 'v1/revisions/phases/{0}/{1}/'.format(team_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_revisions_plan_detail(self, pk):
        """ Delete revision plans detail

        Keyword arguments:

        pk -- the pk of the plans revision
        """

        route = 'v1/revisions/plans/detail/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_revisions_plans_team_project(self, team_pk, project_pk, page=1):
        """ Get plans revisions team project 

        Keyword arguments:

        team_pk -- pk of the team
        project_pk -- pk of the project

        """

        route = 'v1/revisions/plans/{0}/{1}/?page_size={2}&page={3}'.format(team_pk, project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_plan_revision(self, team_pk, project_pk, data):
        """ Create a plans revision team project

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

        route = 'v1/revisions/plans/{0}/{1}/'.format(team_pk, project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)