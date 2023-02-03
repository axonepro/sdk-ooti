import json

import requests

from .helper import Helper


class Prescriptions(Helper):

    def get_prescriptions_list(self, project_pk, page=1):
        """Get prescription list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = f"v1/prescriptions/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_prescription(self, project_pk, data):
        """Create prescription

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create :
            {
                "fee_pct": "string",
                "fee": 0,
                "date": "string",
                "description": "string",
                "supplier": "string",
                "supplier_contact": "string",
                "supplier_phone": "string",
                "supplier_email": "string",
                "notes": "string",
                "is_valid": true,
                "is_ordered": true,
                "is_invoiced": true,
                "file": "string",
                "area": 0,
                "type": "string"
            }
        """

        route = f"v1/prescriptions/list/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_prescriptions_details(self, pk):
        """Get prescription details

        Keyword arguments:

        pk -- the pk of the prescription
        """

        route = f"v1/prescriptions/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_prescriptions(self, pk, data):
        """Update prescriptions

        Keyword arguments:

        pk -- the pk of the prescription
        data -- data create :
            {
                "fee_pct": "string",
                "fee": 0,
                "date": "string",
                "description": "string",
                "supplier": "string",
                "supplier_contact": "string",
                "supplier_phone": "string",
                "supplier_email": "string",
                "notes": "string",
                "is_valid": true,
                "is_ordered": true,
                "is_invoiced": true,
                "file": "string",
                "area": 0,
                "type": "string"
            }
        """

        route = f"v1/prescriptions/{pk}/"
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

    def delete_prescription(self, pk):
        """Delete prescription

        Keyword arguments:

        pk -- the pk of the prescription
        """

        route = f"v1/prescriptions/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
