import requests
import json

from .helper import Helper


class Costs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def copy_costs_fee_allocations_from_contract_hours(self, project_id):  # ?
        """ Copy cost fee allocations from contract hours

        Keywords arguments:
        project_id -- id of the project
        data -- fee project to be copied
        {
            "fee_project": fee_project_pk
        }
        """
        route = 'v1/costs/copy-fee-allocations-from-contract-hours/{0}/'.format(project_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def copy_costs_fee_allocations_from_subcontractor_fees(self, project_id):  # ?
        """ Copy cost fee allocations from subcontractor fees

        Keywords arguments:
        project_id -- id of the project
        data -- fee project to be copied
        {
            "fee_project": fee_project_pk
        }
        """
        route = 'v1/costs/copy-fee-allocations-from-subcontractor-fees/{0}/'.format(project_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def copy_costs_previous_year(self):
        """ Copy costs from a previous year

        Keywords arguments:
        data -- year of the costs to be copied
        {
            "year": 0
        }
        """
        route = 'v1/costs/copy-prev-year/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/costs/cost-composition-charts/{team_pk}/

    # TODO GET on /api/v1/costs/cost-summary/{team_pk}/

    def get_costs_list(self, page=1):
        """ Get the list of costs """

        route = 'v1/costs/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_cost(self, data):
        """ Create a new cost

        Keywords arguments:
        data -- data of the new cost to be created:
        {
            "team": team_pk, # REQUIRED
            "amount_actual": 0,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "month": 0,
            "title": "string",
            "year": 0,
            "months": [
                month_id,
                ...
            ]
        }
        """

        route = 'v1/costs/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_costs_months_list(self, page=1):
        """ Get the list of costs month """

        route = 'v1/costs/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_costs_month(self, data):
        """ Create a new costs month

        Keywords arguments:
        data -- data of the new cost month to be created:
        {
            "fixed_cost": cost_id, # REQUIRED
            "team": team_pk, # REQUIRED
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/costs/month/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_costs_month_details(self, month_id):
        """ Get the costs month details

        Keywords arguments:
        month_id -- id of the month
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_costs_month_details(self, month_id, data):
        """ Update the costs month details

        Keywords arguments:
        month_id -- id of the month
        data -- content of the update:
        {
            "fixed_cost": cost_id,
            "team": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_costs_month(self, month_id):
        """ Delete the costs month

        Keywords arguments:
        month_id -- id of the month
        """

        route = 'v1/costs/month/{0}/'.format(month_id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)
  
    def set_costs_annual_budget(self, cost_id, data):
        """ Set the cost annual budget

        Keywords arguments:
        cost_id -- id of the cost
        data -- annual amount budgeted to be set:
        {
            "amount_budgeted": 0
        }
        """
        route = 'v1/costs/set-annual-budget/{0}/'.format(cost_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, data)
        return self.process_response(response) 

    def get_cost_details(self, id):
        """ Get the cost details

        Keywords arguments:
        id -- id of the cost
        """

        route = 'v1/costs/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_cost_details(self, id, data):
        """ Update costs month

        Keywords arguments:
        id -- id of the cost
        data -- content of the update:
        {
            "amount_actual": 0,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "month": 0,
            "title": "string",
            "year": 0,
            "team": team_pk,
            "months": [
                month_id,
                ...
            ]
        }
        """

        route = 'v1/costs/{0}/'.format(id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_cost(self, id):
        """ Delete the cost

        Keywords arguments:
        id -- id of the cost
        """

        route = 'v1/costs/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)
