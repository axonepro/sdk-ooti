import json

import requests

from .resource import Resource


class Plans(Resource):

    def get_plans_list_action(self, project_pk):
        """Get data needed to perfom actions

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = f"v1/plans/list-action/{project_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_plans_list_action(self, project_pk):
        """Create plans list action

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = f"v1/plans/list-action/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_plans_list(self, project_pk, page=1):
        """Get plans list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = f"v1/plans/list/{project_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_plan(self, project_pk, data):
        """Create plan

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "is_default": true,
                "progress": 0,
                "sub_zone_code": "string",
                "plan_code": "string",
                "project": 0,
                "area": 0,
                "code": "string", ("pln", "det", "elv", "sec")
                "custom_field_1": "string",
                "custom_field_2": "string",
                "custom_field_3": "string",
                "org": 0
            }
        """

        route = f"v1/plans/list/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_plan_details(self, plan_pk):
        """Get plans details

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = f"v1/plans/{plan_pk}/?plan_phases=true"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_plan(self, plan_pk, data):
        """Update plan

        Keyword arguments:

        plan_pk -- the pk of the plan
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "is_default": true,
                "progress": 0,
                "sub_zone_code": "string",
                "plan_code": "string",
                "project": 0,
                "area": 0,
                "code": "string",
                "custom_field_1": "string",
                "custom_field_2": "string",
                "custom_field_3": "string"
            }
        """

        route = f"v1/plans/{plan_pk}/"
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

    def delete_plan(self, plan_pk):
        """Delete plan

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = f"v1/plans/{plan_pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_plans_planphases_list(self, project_pk, page=1):
        """Get plans planphases list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = f"v1/plans/list/{project_pk}/?page_size={self.pagination}&page={page}&plan_phases=true"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)
