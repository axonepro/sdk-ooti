import json

import requests

from .resource import Resource


class Contracts(Resource):

    def get_contractors_list(self, page=1):
        """Get contractors list"""

        route = f"v1/contracts/contractor/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_contractors(self, data):
        """Create a contractor

        Keyword arguments:

        data -- data create :
            {
                "identity_team": 0,
                "currency": 0,
                "name": "string",
                "photo": "string",
                "email": "string",
                "address": "string",
                "telephone": "string",
                "iban": "string",
                "number": "string",
                "is_company": true,
                "is_internal": true,
                "tags": [
                "string"
                ]
            }
        """

        route = f"v1/contracts/contractor/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_contractor_details(self, pk):
        """Get contractor details

        Keyword arguments:

        pk -- the pk of the contractor
        """

        route = f"v1/contracts/contractor/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_contractor(self, pk, data):
        """Update a contractor

        Keyword arguments:

        pk -- the pk of the contractor
        data -- data create :
            {
                "identity_team": 0,
                "currency": 0,
                "name": "string",
                "photo": "string",
                "email": "string",
                "address": "string",
                "telephone": "string",
                "iban": "string",
                "number": "string",
                "is_company": true,
                "is_internal": true,
                "tags": [
                "string"
                ]
            }
        """

        route = f"v1/contracts/contractor/{pk}/"
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

    def delete_contractor(self, pk):
        """Delete contractor

        Keyword arguments:

        pk -- the pk of the contractor
        """

        route = f"v1/contracts/contractor/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def generate_contracts_project(self, project_pk):
        """Copy contracts from fee projects to annexes

        Keyword arguments:

        project_pk -- pk of the project :
        """

        route = f"v1/contracts/generate/contracts/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def generate_contracts_org(self, project_pk):
        """Generate contracts"""

        route = f"v1/contracts/generate/{self.org_pk}/?project_pk={project_pk}"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_contracts_items_list(self, page=1, contract_pk=None):
        """Get contracts item list"""

        if contract_pk is not None:
            route = f"v1/contracts/item/list/{0}/?page_size={1}&page={2}&contract={3}".format(
                self.org_pk, self.pagination, page, contract_pk
            )
        else:
            route = f"v1/contracts/item/list/{0}/?page_size={1}&page={2}".format(
                self.org_pk, self.pagination, page
            )

        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_contracts_items(self, data):
        """Create a contract item

        Keyword arguments:

        data -- data create :
            {
                "contract": 0,
                "phase": 0,
                "annex": 0,
                "type": "string",
                "fee": 0,
                "amount_current": 0,
                "already_billed": 0,
                "amount_billed": 0,
                "already_paid": 0
            }
        """

        route = f"v1/contracts/item/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_contract_item_details(self, pk):
        """Get contract item details


        Keyword arguments:

        pk -- the pk of the item
        """

        route = f"v1/contracts/item/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_contract_item(self, pk, data):
        """Update a contract item

        Keyword arguments:

        pk -- pk of the item
        data -- data update :
            {
                "contract": 0,
                "phase": 0,
                "annex": 0,
                "type": "string",
                "fee": 0,
                "amount_current": 0,
                "already_billed": 0,
                "amount_billed": 0,
                "already_paid": 0
            }
        """

        route = f"v1/contracts/item/{pk}/"
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

    def delete_contract_item(self, pk):
        """Delete a contract item

        Keyword arguments:

        pk -- pk of the item
        """

        route = f"v1/contracts/item/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_contracts_list(self, page=1):
        """Get contracts list"""

        route = (
            f"v1/contracts/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        )
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_contract(self, data):
        """Create a contract
        #! A contract can be added to a fee_project under review only.

        Keyword arguments:

        data -- data create :
            {
                "contractor": 0, (R)
                "manager": 0,
                "fee_project": 0,
                "is_valid": true,
                "is_archived": true,
                "type": "string", (R) ("sub")
                "forecast_type": "string",
                "invoicing_method": "string",
                "description": "string",
                "is_mandate": true,
                "tax_rate": 0,
                "project": 0,
                "fee_project": 0
            }
        """

        route = f"v1/contracts/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_contract_details(self, pk):
        """Get contract details

        Keyword arguments:

        pk -- the pk of the contract
        """

        route = f"v1/contracts/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_contract(self, pk, data):
        """Update a contract

        Keyword arguments:

        pk -- the pk of the contract
        data -- data create :
            {
                "contractor": 0,
                "manager": 0,
                "fee_project": 0,
                "is_valid": true,
                "is_archived": true,
                "type": "string",
                "forecast_type": "string",
                "invoicing_method": "string",
                "description": "string",
                "is_mandate": true,
                "tax_rate": 0
            }
        """

        route = f"v1/contracts/{pk}/"
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

    def delete_contract(self, pk):
        """Delete contract

        Keyword arguments:

        pk -- the pk of the contract
        """

        route = f"v1/contracts/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def generate_contracts_month_org(self, contract_pk):
        """Generate contract month

        Keyword arguments:

        contract_pk -- pk of the contract
        """

        data = {"contract": contract_pk}

        route = f"v1/contracts/month/generate/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_contracts_month_list(self, page=1):
        """Get contracts month list"""

        route = f"v1/contracts/month/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_contracts_month(self, data):
        """Create a contract month

        Keyword arguments:

        data -- data create :
            {
                "contract": 0,
                "year": 0,
                "month": 0,
                "start_date": "string",
                "end_date": "string",
                "is_past": true,
                "is_present": true,
                "is_future": true,
                "budget": 0,
                "budget_projected": 0,
                "actual": 0,
                "pct": 0
            }
        """

        route = f"v1/contracts/month/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_contract_month_details(self, pk):
        """Get contract month details

        Keyword arguments:

        pk -- the pk of the contract month
        """

        route = f"v1/contracts/month/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_contracts_month(self, pk, data):
        """Create a contract month

        Keyword arguments:

        pk -- the pk of the contract month
        data -- data create :
            {
                "contract": 0,
                "year": 0,
                "month": 0,
                "start_date": "string",
                "end_date": "string",
                "is_past": true,
                "is_present": true,
                "is_future": true,
                "budget": 0,
                "budget_projected": 0,
                "actual": 0,
                "pct": 0
            }
        """

        route = f"v1/contracts/month/{pk}/"
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

    def delete_contract_month(self, pk):
        """Delete contract month

        Keyword arguments:

        pk -- the pk of the contract month
        """

        route = f"v1/contracts/month/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
