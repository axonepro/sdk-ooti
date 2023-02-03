import json

import requests

from .resource import Resource


class Employees(Resource):

    def get_employees_contracts_list(self, page=1):
        """Get the employees contracts"""

        route = f"v1/employees/contracts/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_employees_contract(self, data):
        """Create a new employees

        Keywords arguments:
        data -- data of the new contract to be created:
        {
            "team": team_pk,
            "orguser": orguser_pk,
            "status": "string",
            "start_date": "string",
            "end_date": "string",
            "cancel_date": "string",
            "notes": "string",
            "currency": currency_pk,
            "pay_type": "string",
            "admin_only": true,
            "contract_type": "string",
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0,
            "file": "string",
            "salary_monthly_gross": 0,
            "salary_hourly_gross": 0,
            "salary_loaded_coefficent": 0,
            "salary_daily_gross": 0
        }
        """

        route = f"v1/employees/contracts/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_employees_contracts_details(self, contract_id):
        """Get employees contract details

        Keywords arguments:
        contract_id -- id of the employees contract
        """

        route = f"v1/employees/contracts/{contract_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_employees_contracts_details(self, contract_id, data):
        """Get employees contract details

        Keywords arguments:
        contract_id -- id of the employees contract
        data -- content of the update:
        {
            "team": team_pk,
            "orguser": orguser_pk,
            "status": "string",
            "start_date": "string",
            "end_date": "string",
            "cancel_date": "string",
            "notes": "string",
            "currency": currency_pk,
            "pay_type": "string",
            "admin_only": true,
            "contract_type": "string",
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0,
            "file": "string",
            "salary_monthly_gross": 0,
            "salary_hourly_gross": 0,
            "salary_loaded_coefficent": 0,
            "salary_daily_gross": 0
        }
        """

        route = f"v1/employees/contracts/{contract_id}/"
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

    def delete_employees_contract(self, contract_id):
        """Delete employees contract

        Keywords arguments:
        contract_id -- id of the employees contract
        """

        route = f"v1/employees/contracts/{contract_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_employees_period_list(self, page=1):
        """Get the list of employees periods"""

        route = f"v1/employees/period/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_employees_period(self, data):
        """Create a new employees period

        Keywords arguments:
        data -- data of the new period to be created:
        {
            "contract": contract_id, # REQUIRED
            "notes": "string",
            "start_date": "string",
            "end_date": "string",
            "status": "string",
            "salary_daily_gross": 0,
            "salary_hourly_gross": 0,
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "salary_monthly_gross": 0,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0
        }
        """

        route = f"v1/employees/period/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_employees_period_details(self, period_id):
        """Get employees period details

        Keywords arguments:
        period_id -- id of the period
        """

        route = f"v1/employees/period/{period_id}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_employees_period_details(self, period_id, data):
        """Update the employees period details

        Keywords arguments:
        period_id -- id of the period
        data -- content of the update:
        {
            "contract": contract_id,
            "notes": "string",
            "start_date": "string",
            "end_date": "string",
            "status": "string",
            "salary_daily_gross": 0,
            "salary_hourly_gross": 0,
            "salary_gross_coefficent": 0,
            "salary_monthly_net": 0,
            "salary_monthly_gross": 0,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 0,
            "daily_hours_limit": 0,
            "overtime_enabled": true,
            "overtime_hours_limit": 0,
            "days_per_week": 0
        }
        """

        route = f"v1/employees/period/{period_id}/"
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

    def delete_employees_period(self, period_id):
        """Delete the employees period

        Keywords arguments:
        period_id -- id of the period
        """

        route = f"v1/employees/period/{period_id}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
