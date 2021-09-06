import requests
import json

from .helper import Helper


class Costs(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Costs ####

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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    