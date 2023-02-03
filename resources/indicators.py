import requests

from .helper import Helper


class Indicators(Helper):

    def get_indicators_financial_costs(self, team_pk=None, project_id=None):
        """Get financial costs indicators list"""

        route = f"v1/indicators/financial/cost/{self.org_pk}/"
        parameters = ""
        if team_pk is not None or project_id is not None:
            parameters = "?"
            if team_pk is not None:
                parameters += f"team={team_pk}"
                if project_id is not None:
                    parameters += "&"
            if project_id is not None:
                parameters += f"project={team_pk}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, parameters, None
        )
        return self.process_response(response)

    def get_indicators_financial_incomes(self):
        """Get financial incomes indicators list"""

        route = f"v1/indicators/financial/income/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    # WARNING same code than get_indicators_financial_costs
    def get_indicators_financial_revenues(self, team_pk=None, project_id=None):
        """Get financial revenues indicators"""

        route = f"v1/indicators/financial/revenue/{self.org_pk}/"
        parameters = ""
        if team_pk is not None or project_id is not None:
            parameters = "?"
            if team_pk is not None:
                parameters += f"team={team_pk}"
                if project_id is not None:
                    parameters += "&"
            if project_id is not None:
                parameters += f"project={team_pk}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, parameters, None
        )
        return self.process_response(response)

    def get_indicators_financial_summary(self, team_pk=None, project_id=None):
        """Get the financial indicators summary"""

        route = f"v1/indicators/financial/summary/{self.org_pk}/"
        parameters = ""
        if team_pk is not None or project_id is not None:
            parameters = "?"
            if team_pk is not None:
                parameters += f"team={team_pk}"
                if project_id is not None:
                    parameters += "&"
            if project_id is not None:
                parameters += f"project={team_pk}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, parameters, None
        )
        return self.process_response(response)

    def get_indicators_revenue(self):
        """Get the list of revenue indicators"""

        route = f"v1/indicators/revenue/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
