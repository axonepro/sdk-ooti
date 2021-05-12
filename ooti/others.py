import requests
import json

from requests.models import Response

from helper import Helper

"""
- Help:
    - ERROR 403 POST & GET v1/help/manage/ 

"""


class Others(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Goals ####

    def get_goals_list(self):
        """ Get the list of goals """

        route = 'v1/goals/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_goal_details(self, id):
        """ Get the goal details

        Keywords arguments:
        id -- id of the goal
        """

        route = 'v1/goals/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_goal(self, id):
        """ Delete the goal

        Keywords arguments:
        id -- id of the goal
        """

        route = 'v1/goals/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Help ####

    #### Indicators ####

    def get_indicators_financial_costs(self, team_pk=None, project_id=None):

        route = 'v1/indicators/financial/cost/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_indicators_financial_incomes(self):

        route = 'v1/indicators/financial/income/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_indicators_financial_revenues(self, team_pk=None, project_id=None):

        route = 'v1/indicators/financial/cost/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_indicators_financial_summary(self, team_pk=None, project_id=None):

        route = 'v1/indicators/financial/summary/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_indicators_revenue(self):

        route = 'v1/indicators/revenue/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Pipelines ####

    #### Projections ####

    def get_component_metrics_widget(self):

        route = 'v1/projections/components/metrics/widget/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def export_projections_project_fees(self, project_id):

        route = 'v1/projections/export/{0}/'.format(project_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        xls_file = open('project_{0}_timeline.xls'.format(project_id), 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_projections_forecast_month_rule_list(self):

        route = 'v1/projections/forecast-month-rule/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_projections_forecast_month_rule(self, data):
        """ Create a new month rule

        Keywords arguments:
        data -- data of the new month rule to be created:
        {
            "ruleset": ruleset_id,
            "relative_to": "string",
            "index": 0,
            "pct": 0
        }
        """
        route = 'v1/projections/forecast-month-rule/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_forecast_month_rule_details(self, month_rule_id):

        route = 'v1/projections/forecast-month-rule/{0}/'.format(month_rule_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_forecast_month_rule_details(self, month_rule_id, data):
        """ Update the month rule details

        Keywords arguments:
        month_rule_id -- id of the month rule to
        data -- content of the update:
        {
            "ruleset": ruleset_id,
            "relative_to": "string",
            "index": 0,
            "pct": 0
        }
        """
        route = 'v1/projections/forecast-month-rule/{0}/'.format(month_rule_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_forecast_month_rule_details(self, month_rule_id):

        route = 'v1/projections/forecast-month-rule/{0}/'.format(month_rule_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_forecast_month_ruleset_list(self):

        route = 'v1/projections/forecast-month-ruleset/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_projections_forecast_month_ruleset(self, data):
        """ Create a new month ruleset

        Keywords arguments:
        data -- data of the new month ruleset to be created:
        {
            "name": "string",
            "rules": [
                rule_id,
                ...
            ]
        }
        """
        route = 'v1/projections/forecast-month-ruleset/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_forecast_month_ruleset_details(self, month_ruleset_id):

        route = 'v1/projections/forecast-month-ruleset/{0}/'.format(month_ruleset_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_forecast_month_ruleset_details(self, month_ruleset_id, data):
        """ Update the month ruleset details

        Keywords arguments:
        month_rule_id -- id of the month rule to
        data -- content of the update:
        {
            "name": "string",
            "rules": [
                rule_id,
                ...
            ]
        }
        """
        route = 'v1/projections/forecast-month-ruleset/{0}/'.format(month_ruleset_id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_forecast_month_rule_details(self, month_ruleset_id):

        route = 'v1/projections/forecast-month-ruleset/{0}/'.format(month_ruleset_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
