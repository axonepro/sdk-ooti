import requests
import json

from .helper import Helper


class Projects(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO POST on /api/v1/projects/actions/{org_pk}/

    def get_project_available_clients(self, id):
        """ Get the list of clients avalaible (clients that are not already participating in the project)
        Return the list of clients with their display name and pk

        Keywords arguments:
        id -- the id of the project
        """

        route = 'v1/projects/available-clients/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_projects_list_deliverables(self):
        """ Get the list of projects and their associated deliverables where the current user is a member of """

        route = 'v1/projects/deliverables/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def export_projects_list(self):
        """ Export the list of projects as a .xls file """

        route = 'v1/projects/export/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        xls_file = open('projects_list.xls', 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_project_fee_summary(self, id):
        """ Get the project fee summary

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/fee-summary/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/projects/leads2/{org_pk}/

    # TODO GET on /api/v1/projects/leads2/{org_pk}/{team_pk}/

    def get_project_list_access(self):
        """ ? """

        route = 'v1/projects/list/access/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_projects_list(self, team_pk=None):
        """ Get the projects list 

        Keywords arguments:
        team_pk -- pk of a team to get the project list of a specific team
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        if team_pk is not None:
            route += '{0}/'.format(team_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_project(self, data):
        """ Create a new project

        Keyword arguments:
        data -- content of the project to be created:
        {
            "client": client_pk,
            "currency": curency_pk,
            "project_title": "New project",
            "phases": [phase_pk, phase_pk, ...],
            "project_users": [project_user_pk, ...],
            "areas": [],
            "project_tags": [],
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [orguser_pk, orguser_pk, ...],
            "city": "Paris",
            "country": "FR"
        }
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    # TODO GET on /api/v1/projects/list/{org_pk}/{team_pk}/

    # TODO POST on /api/v1/projects/list/{org_pk}/{team_pk}/