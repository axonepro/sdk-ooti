import requests
import json

from .helper import Helper


class Teams(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_teams_access_list(self):
        """ Get teams orguser has or has not access to """

        route = 'v1/teams/list/access/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_teams_list(self):
        """ Get the list of teams """

        route = 'v1/teams/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)  # no 'results' key

    def create_team(self, data):
        """ Create a new team 

        Keywords arguments:
        data -- content of the team to be created:
        {
            "name": "Beta", (required)
            "currency": currency_pk,
            "city": "Paris",
            "address": "6 Rue de la rue",
            "banks": [
                bank_id
            ]
        }
        """

        route = 'v1/teams/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    # TODO POST on /api/v1/teams/staff/{id}/

    # TODO GET on /api/v1/teams/team-summary/{team_pk}/

    def add_team_user_to_multiple_projects(self, data):  # Error 500
        """ Add a user to multiple teams at once

        Keywords arguments:
        data -- pk of the projects and pk of the orguser to add :
        {
            "orguser": orguser_pk,
            "teams": [

            ]
            "projects": [
                project_id,
                ...
            ]
        }
        """

        route = 'v1/teams/users/bulk/add/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def remove_team_user_to_multiple_projects(self, data):  # Error 500
        """ Remove a user from multiple teams at once

        Keywords arguments:
        data -- pks of the projects and pk of the orguser to remove :
        {
            "orguser": orguser_pk,
            "projects": [
                project_id,
                ...
            ]
        }
        """

        route = 'v1/teams/users/bulk/delete/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_team_users_list(self, pk):
        """ Get the list of users in the team 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/users/list/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def add_team_user(self, pk, data):
        """ Add a user to a team

        Keywords arguments:
        pk -- pk of the team where to add the user
        data -- details about the user to add (pk, permissionsset, role, ...):
        {
            "orguser": orguser_pk,
            "permissionsset: permissionsset_pk,
            "role": role_pk
            "team": team_pk
        }
        """

        route = 'v1/teams/users/list/{0}/'.format(pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_team_user_details(self, user_pk):  # same thing as get_orguser_details ?
        """ Get the orguser details related to the team he is in

        Keywords arguments:
        user_pk -- pk of the team user
        """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_team_user_details(self, user_pk, data):
        """ Update the orguser details related to the team he is in

        Keywords arguments:
        user_pk -- pk of the team user
        data -- content of the update:
        {
            "permissionsset": 16464,
            "team": team_pk
        }
        """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def remove_team_user(self, user_pk):
        """ Delete a user from the team """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_team_details(self, pk):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_team_details(self, pk, data):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        data -- content of the update:
        {
            "city": "Lyon",
            "address": "2 Avenue du Trône"
        }
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)