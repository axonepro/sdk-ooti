import requests
import json

from .helper import Helper

"""
- Help:
    - ERROR 403 POST & GET v1/help/manage/

- Pipelines:
    - ERROR 403 on all endpoints

- Projections:
    - ERROR 500 : create_projections_month_fee
    
"""


class Others(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Goals ####

    def get_goals_list(self, page=1):
        """ Get the list of goals """

        route = 'v1/goals/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
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
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_indicators_financial_incomes(self):
        """ Get financial incomes indicators list """

        route = 'v1/indicators/financial/income/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_indicators_financial_revenues(self, team_pk=None, project_id=None):
        """ Get financial revenues indicators """

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
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_indicators_revenue(self):
        """ Get the list of revenue indicators """

        route = 'v1/indicators/revenue/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Pipelines ####

    #### Projections ####

    def get_component_metrics_widget(self):
        """ """

        route = 'v1/projections/components/metrics/widget/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def export_projections_project_timeline(self, project_id):
        """ Export the project timeline into a .xls file

        Keywords arguments:
        project_id -- id of the project
        """

        route = 'v1/projections/export/{0}/'.format(project_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        xls_file = open('project_{0}_timeline.xls'.format(project_id), 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_projections_forecast_month_rule_list(self, page=1):
        """ Get the list of month rules """

        route = 'v1/projections/forecast-month-rule/list/{0}/?page_size={1}&page={2}'.format(
            self.org_pk, self.pagination, page)
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
        """ Get the month rule details

        Keywords arguments:
        month_rule_id -- id of the month rule
        """

        route = 'v1/projections/forecast-month-rule/{0}/'.format(month_rule_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_forecast_month_rule_details(self, month_rule_id, data):
        """ Update the month rule details

        Keywords arguments:
        month_rule_id -- id of the month rule
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

    def delete_projections_forecast_month_rule(self, month_rule_id):
        """ Delete the month rule

        Keywords arguments:
        month_rule_id -- id of the month rule
        """

        route = 'v1/projections/forecast-month-rule/{0}/'.format(month_rule_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_forecast_month_ruleset_list(self, page=1):
        """ Get the list of month rulesets """

        route = 'v1/projections/forecast-month-ruleset/list/{0}/?page_size={1}&page={2}'.format(
            self.org_pk, self.pagination, page)
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
        """ Get the month ruleset details

        Keyword arguments:
        month_rule_id -- id of the month rule
        """
        route = 'v1/projections/forecast-month-ruleset/{0}/'.format(month_ruleset_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_forecast_month_ruleset_details(self, month_ruleset_id, data):
        """ Update the month ruleset details

        Keywords arguments:
        month_rule_id -- id of the month rule to be created
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

    def delete_projections_forecast_month_ruleset(self, month_ruleset_id):
        """ Delete the month rule 

        Keywords arguments:
        month_ruleset_id -- id of the month ruleset
        """

        route = 'v1/projections/forecast-month-ruleset/{0}/'.format(month_ruleset_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_month_annexes_list(self, project_id, page=1):
        """ Get the project month annexes list

        Keywords arguments:
        project_id -- id of the project
        """

        route = 'v1/projections/months/annex/list/{0}/?page_size={1}&page={2}'.format(project_id, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_projections_month_annex(self, project_id, data):
        """ Create a new project month annex 

        Keywords arguments:
        project_id -- id of the project
        data -- data of the new project month annex to be created:
        {
            "annex": 0,
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": true,
            "is_present": true,
            "is_future": true,
            "pct": 0,
            "billing_pct": 0,
            "is_locked": true,
            "mockup_pct": 0,
            "mockup_is_locked": true,
            "planned_invoicing": 0,
            "actual_invoiced": 0,
            "projected_invoiced": 0,
            "cost_payroll_projected": 0
        }
        """

        route = 'v1/projections/months/annex/list/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_month_annex_details(self, month_annex_id):
        """ Get the month annex details

        Keywords arguments:
        month_annex_id -- id of the month annex
        """

        route = 'v1/projections/months/annex/{0}/'.format(month_annex_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_month_annex_details(self, month_annex_id, data):
        """ Update the month annex details

        Keywords arguments:
        month_annex_id -- id of the month annex
        data -- content of the update:
        {

        }
        """

        route = 'v1/projections/months/annex/{0}/'.format(month_annex_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_month_annex(self, month_annex_id):
        """ Delete the month annex

        Keywords arguments:
        month_annex_id -- id of the month annex
        """

        route = 'v1/projections/months/annex/{0}/'.format(month_annex_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_month_fees_list(self, project_id, page=1):
        """ Get the month fees

        Keywords arguments:
        project_id -- id of the project
        """

        route = 'v1/projections/months/fee/list/{0}/?page_size={1}&page={2}'.format(project_id, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_projections_month_fee(self, project_id, data):
        """ Create a new month fee

        Keywords arguments:
        project_id -- id of the project
        data -- data of the new month fee to be created
        {
            "fee": 0,
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": true,
            "is_present": true,
            "is_future": true,
            "pct": 0,
            "mockup_pct": 0,
            "billing_pct": 0,
            "mockup_billing_pct": 0,
            "is_locked": true,
            "mockup_is_locked": true
        }
        """

        route = 'v1/projections/months/fee/list/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_month_fee_details(self, month_fee_id):
        """ Get the month fee details

        Keywords arguments:
        month_fee_id -- id of the month fee
        """

        route = 'v1/projections/months/fee/{0}/'.format(month_fee_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_month_fee_details(self, month_fee_id, data):
        """ Update the month fee details

        Keywords arguments:
        month_fee_id -- id of the month fee
        data -- content of the update:
        {

        }
        """

        route = 'v1/projections/months/fee/{0}/'.format(month_fee_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_month_fee(self, month_fee_id):
        """ Delete the month fee

        Keywords arguments:
        month_fee_id -- id of the month fee
        """

        route = 'v1/projections/months/fee/{0}/'.format(month_fee_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_month_phases_list(self, project_id, page=1):
        """ Get the month phases list

        Keywords arguments:
        project_id -- id of the project
        """

        route = 'v1/projections/months/phase/list/{0}/?page_size={1}&page={2}'.format(project_id, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_projections_month_phase(self, project_id, data):
        """ Create a new month phase

        Keywords arguments:
        project_id -- id of the project
        data -- data of the new month phase to be created
        {
            "phase": 0,
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": true,
            "is_present": true,
            "is_future": true,
            "is_locked": true,
            "mockup_pct": 0,
            "mockup_is_locked": true,
            "pct": 0,
            "billing_pct": 0,
            "mockup_billing_pct": 0
        }
        """

        route = 'v1/projections/months/phase/list/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_month_phase_details(self, month_phase_id):
        """ Get the month phase details

        Keywords arguments:
        month_phase_id -- id of the month phase
        """

        route = 'v1/projections/months/phase/{0}/'.format(month_phase_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_month_phase_details(self, month_phase_id, data):
        """ Update the month phase details

        Keywords arguments:
        month_phase_id -- id of the month phase
        data -- content of the update:
        {

        }
        """

        route = 'v1/projections/months/phase/{0}/'.format(month_phase_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_month_phase(self, month_phase_id):
        """ Delete month phase

        Keywords arguments:
        month_phase_id -- id of the month phase
        """

        route = 'v1/projections/months/phase/{0}/'.format(month_phase_id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_projections_planning_deliverables_months_bulk_update(self):
        """ Create projections planning deliverables months bulk update """
        route = 'v1/projections/planning/deliverables/months/bulk-update/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_reset_budget(self, project_pk):
        """ Get projections reset budget
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/reset_budget/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_roles_annex_list(self, project_pk, page=1):
        """ Get projections roles annex list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/roles/annex/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_projections_roles_annex_details(self, pk):
        """ Get projections roles annex details
        Keyword argument:
        pk -- pk of the project projection role annex
        """
        route = 'v1/projections/roles/annex/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_roles_annex(self, pk, data):
        """ Update projections roles annex
        Keyword argument:
        pk -- pk of the project projection role annex
        data -- data create :
        {
            "role": 0,
            "annex": 0,
            "pct": 0,
            "hours_actual": 0,
            "hours_budgeted": 0,
            "hours_allocated": 0,
            "hours_contract": 0,
            "is_locked": true
        }
        """
        route = 'v1/projections/roles/annex/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_roles_annex(self, pk):
        """ Delete projections roles annex
        Keyword argument:
        pk -- pk of the project projection role annex
        """
        route = 'v1/projections/roles/annex/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_roles_phase_list(self, project_pk, page=1):
        """ Get projections roles phase list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/roles/phase/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_projections_roles_phase_details(self, pk):
        """ Get projections roles phase details
        Keyword argument:
        pk -- pk of the project projection role phase
        """
        route = 'v1/projections/roles/phase/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_roles_phase(self, pk, data):
        """ Update projections roles phase
        Keyword argument:
        pk -- pk of the project projection role phase
        data -- data create :
        {
            "role": 0,
            "phase": 0,
            "pct": 0,
            "hours_actual": 0,
            "hours_budgeted": 0,
            "hours_allocated": 0,
            "hours_contract": 0,
            "is_locked": true,
            "mockup_pct": 0,
            "mockup_is_locked": true
        }
        """
        route = 'v1/projections/roles/phase/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_projections_roles_phase(self, pk):
        """ Delete projections roles phase
        Keyword argument:
        pk -- pk of the project projection role phase
        """
        route = 'v1/projections/roles/phase/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_all_teamuser_months(self):
        """ Update all teamuser months (post request) """
        route = 'v1/projections/update_all_teamuser_months/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_update_project_budget(self, project_pk):
        """ Get projections update project budget 
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/update_project_budget/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_update_project_projections(self, project_pk):
        """ Get projections update project projections 
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/update_project_projections/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_update_projections(self):
        """ Get projections update projections """
        route = 'v1/projections/update_projections/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_users_annex_list(self, project_pk, page=1):
        """ Get projections users annex list  
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/users/annex/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projections_users_annex_details(self, pk):
        """ Get projections users annex details 
        Keyword argument:
        pk -- pk of the user annex 
        """
        route = 'v1/projections/users/annex/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_projections_users_annex(self, pk, data):
        """ Get projections users annex 
        Keyword argument:
        pk -- pk of the user annex 
        data -- data update :
        {
            "annex": 0,
            "project_user": 0,
            "pct": 0,
            "is_locked": true,
            "hours_actual": 0,
            "hours_budgeted": 0,
            "hours_allocated": 0
        }
        """
        route = 'v1/projections/users/annex/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_projections_users_phase_list(self, project_pk, page=1):
        """ Get projections users phase list 
        Keyword argument:
        project_pk -- pk of the project
        """
        route = 'v1/projections/users/phase/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_projections_users_phase_details(self, pk):
        """ Get projections users phase details 
        Keyword argument:
        pk -- pk of the user phase
        """
        route = 'v1/projections/users/phase/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_projections_users_phase(self, pk, data):
        """ Get projections users phase 
        Keyword argument:
        pk -- pk of the user phase 
        data -- data update :
        {
            "phase": 0,
            "project_user": 0,
            "pct": 0,
            "is_locked": true,
            "mockup_pct": 0,
            "mockup_is_locked": true,
            "hours_actual": 0,
            "hours_budgeted": 0,
            "hours_allocated": 0
        }
        """
        route = 'v1/projections/users/phase/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)
