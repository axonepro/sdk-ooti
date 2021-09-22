import requests
import json

from .helper import Helper


class Indicators(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_indicators_financial_costs(self, team_pk=None, project_id=None):
        """ Get financial costs indicators list """

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
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, parameters, None)
        return self.process_response(response)

    def get_indicators_financial_incomes(self):
        """ Get financial incomes indicators list """

        route = 'v1/indicators/financial/income/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # WARNING same code than get_indicators_financial_costs
    def get_indicators_financial_revenues(self, team_pk=None, project_id=None):
        """ Get financial revenues indicators """

        route = 'v1/indicators/financial/revenue/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, parameters, None)
        return self.process_response(response)

    def get_indicators_financial_summary(self, team_pk=None, project_id=None):
        """ Get the financial indicators summary """

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
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, parameters, None)
        return self.process_response(response)

    def get_indicators_revenue(self):
        """ Get the list of revenue indicators """

        route = 'v1/indicators/revenue/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)