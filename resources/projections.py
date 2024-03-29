import json

import requests

from .resource import Resource


class Projections(Resource):

    def get_component_metrics_widget(self):
        """ """

        route = "v1/projections/components/metrics/widget/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def export_projections_project_timeline(self, project_id):
        """Export the project timeline into a .xls file

        Keywords arguments:
        project_id -- id of the project
        """

        route = f"v1/projections/export/{project_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        xls_file = open(f"project_{project_id}_timeline.xls", "wb")
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_projections_forecast_month_rule_list(self, page=1):
        """Get the list of month rules"""

        route = f"v1/projections/forecast-month-rule/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_projections_forecast_month_rule(self, data):
        """Create a new month rule

        Keywords arguments:
        data -- data of the new month rule to be created:
        {
            "ruleset": ruleset_id,
            "relative_to": "string",
            "index": 0,
            "pct": 0
        }
        """
        route = f"v1/projections/forecast-month-rule/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_projections_forecast_month_rule_details(self, month_rule_id):
        """Get the month rule details

        Keywords arguments:
        month_rule_id -- id of the month rule
        """

        route = f"v1/projections/forecast-month-rule/{month_rule_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_forecast_month_rule_details(self, month_rule_id, data):
        """Update the month rule details

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
        route = f"v1/projections/forecast-month-rule/{month_rule_id}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_projections_forecast_month_rule(self, month_rule_id):
        """Delete the month rule

        Keywords arguments:
        month_rule_id -- id of the month rule
        """

        route = f"v1/projections/forecast-month-rule/{month_rule_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_forecast_month_ruleset_list(self, page=1):
        """Get the list of month rulesets"""

        route = f"v1/projections/forecast-month-ruleset/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_projections_forecast_month_ruleset(self, data):
        """Create a new month ruleset

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
        route = f"v1/projections/forecast-month-ruleset/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_projections_forecast_month_ruleset_details(self, month_ruleset_id):
        """Get the month ruleset details

        Keyword arguments:
        month_rule_id -- id of the month rule
        """
        route = f"v1/projections/forecast-month-ruleset/{month_ruleset_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_forecast_month_ruleset_details(self, month_ruleset_id, data):
        """Update the month ruleset details

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
        route = f"v1/projections/forecast-month-ruleset/{month_ruleset_id}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_projections_forecast_month_ruleset(self, month_ruleset_id):
        """Delete the month rule

        Keywords arguments:
        month_ruleset_id -- id of the month ruleset
        """

        route = f"v1/projections/forecast-month-ruleset/{month_ruleset_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_month_annexes_list(self, project_id, page=1):
        """Get the project month annexes list

        Keywords arguments:
        project_id -- id of the project
        """

        route = f"v1/projections/months/annex/list/{project_id}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_projections_month_annex(self, project_id, data):
        """Create a new project month annex

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

        route = f"v1/projections/months/annex/list/{project_id}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_projections_month_annex_details(self, month_annex_id):
        """Get the month annex details

        Keywords arguments:
        month_annex_id -- id of the month annex
        """

        route = f"v1/projections/months/annex/{month_annex_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_month_annex_details(self, month_annex_id, data):
        """Update the month annex details

        Keywords arguments:
        month_annex_id -- id of the month annex
        data -- content of the update:
        {

        }
        """

        route = f"v1/projections/months/annex/{month_annex_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_projections_month_annex(self, month_annex_id):
        """Delete the month annex

        Keywords arguments:
        month_annex_id -- id of the month annex
        """

        route = f"v1/projections/months/annex/{month_annex_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_month_fees_list(self, project_id, page=1):
        """Get the month fees

        Keywords arguments:
        project_id -- id of the project
        """

        route = f"v1/projections/months/fee/list/{project_id}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_projections_month_fee(self, project_id, data):
        """Create a new month fee

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

        route = f"v1/projections/months/fee/list/{project_id}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_projections_month_fee_details(self, month_fee_id):
        """Get the month fee details

        Keywords arguments:
        month_fee_id -- id of the month fee
        """

        route = f"v1/projections/months/fee/{month_fee_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_month_fee_details(self, month_fee_id, data):
        """Update the month fee details

        Keywords arguments:
        month_fee_id -- id of the month fee
        data -- content of the update:
        {

        }
        """

        route = f"v1/projections/months/fee/{month_fee_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_projections_month_fee(self, month_fee_id):
        """Delete the month fee

        Keywords arguments:
        month_fee_id -- id of the month fee
        """

        route = f"v1/projections/months/fee/{month_fee_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_month_phases_list(self, project_id, page=1):
        """Get the month phases list

        Keywords arguments:
        project_id -- id of the project
        """

        route = f"v1/projections/months/phase/list/{project_id}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_projections_month_phase(self, project_id, data):
        """Create a new month phase

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

        route = f"v1/projections/months/phase/list/{project_id}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_projections_month_phase_details(self, month_phase_id):
        """Get the month phase details

        Keywords arguments:
        month_phase_id -- id of the month phase
        """

        route = f"v1/projections/months/phase/{month_phase_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_month_phase_details(self, month_phase_id, data):
        """Update the month phase details

        Keywords arguments:
        month_phase_id -- id of the month phase
        data -- content of the update:
        {

        }
        """

        route = f"v1/projections/months/phase/{month_phase_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def delete_projections_month_phase(self, month_phase_id):
        """Delete month phase

        Keywords arguments:
        month_phase_id -- id of the month phase
        """

        route = f"v1/projections/months/phase/{month_phase_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_projections_planning_deliverables_months_bulk_update(self):
        """Create projections planning deliverables months bulk update"""
        route = "v1/projections/planning/deliverables/months/bulk-update/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_reset_budget(self, project_pk):
        """Get projections reset budget
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/reset_budget/{project_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_roles_annex_list(self, project_pk, page=1):
        """Get projections roles annex list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/roles/annex/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_projections_roles_annex_details(self, pk):
        """Get projections roles annex details
        Keyword argument:
        pk -- pk of the project projection role annex
        """
        route = f"v1/projections/roles/annex/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_roles_annex(self, pk, data):
        """Update projections roles annex
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
        route = f"v1/projections/roles/annex/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_projections_roles_annex(self, pk):
        """Delete projections roles annex
        Keyword argument:
        pk -- pk of the project projection role annex
        """
        route = f"v1/projections/roles/annex/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_roles_phase_list(self, project_pk, page=1):
        """Get projections roles phase list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/roles/phase/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_projections_roles_phase_details(self, pk):
        """Get projections roles phase details
        Keyword argument:
        pk -- pk of the project projection role phase
        """
        route = f"v1/projections/roles/phase/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_roles_phase(self, pk, data):
        """Update projections roles phase
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
        route = f"v1/projections/roles/phase/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def delete_projections_roles_phase(self, pk):
        """Delete projections roles phase
        Keyword argument:
        pk -- pk of the project projection role phase
        """
        route = f"v1/projections/roles/phase/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_all_teamuser_months(self):
        """Update all teamuser months (post request)"""
        route = f"v1/projections/update_all_teamuser_months/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_update_project_budget(self, project_pk):
        """Get projections update project budget
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/update_project_budget/{project_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_update_project_projections(self, project_pk):
        """Get projections update project projections
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/update_project_projections/{project_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_update_projections(self):
        """Get projections update projections"""
        route = f"v1/projections/update_projections/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_users_annex_list(self, project_pk, page=1):
        """Get projections users annex list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/users/annex/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_projections_users_annex_details(self, pk):
        """Get projections users annex details
        Keyword argument:
        pk -- pk of the user annex
        """
        route = f"v1/projections/users/annex/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_projections_users_annex(self, pk, data):
        """Get projections users annex
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
        route = f"v1/projections/users/annex/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)

    def get_projections_users_phase_list(self, project_pk, page=1):
        """Get projections users phase list
        Keyword argument:
        project_pk -- pk of the project
        """
        route = f"v1/projections/users/phase/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_projections_users_phase_details(self, pk):
        """Get projections users phase details
        Keyword argument:
        pk -- pk of the user phase
        """
        route = f"v1/projections/users/phase/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def update_projections_users_phase(self, pk, data):
        """Get projections users phase
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
        route = f"v1/projections/users/phase/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response)
