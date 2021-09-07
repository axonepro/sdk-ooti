import requests
import json

from .helper import Helper


class Goals(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_goals_list(self, page=1):
        """ Get the list of goals """

        route = 'v1/goals/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_goal(self, data):
        """ Create a new goal

        Keywords arguments:
        data -- data of the new goal to be created:
        {
            "team": team_pk,
            "name": "string",
            "value": 0,
            "year": 0
        }
        """

        route = 'v1/goals/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_goal_details(self, id):
        """ Get the goal details

        Keywords arguments:
        id -- id of the goal
        """

        route = 'v1/goals/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_goal_details(self, id, data):
        """ Update the goal details

        Keywords arguments:
        id -- id of the goal
        data -- content of the update:
        {
            "team": team_pk,
            "name": "string",
            "value": 0,
            "year": 0
        }
        """

        route = 'v1/goals/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_goal(self, id):
        """ Delete the goal

        Keywords arguments:
        id -- id of the goal
        """

        route = 'v1/goals/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)