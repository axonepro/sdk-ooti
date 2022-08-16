import json

import requests

from .helper import Helper


class Defaults(Helper):
    def __init__(
        self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
    ):
        super().__init__(
            base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination
        )

    def duplicate_defaults_phase(self, pk):
        """Duplicate defaults phase

        Keyword arguements:

        pk -- pk of the phase
        """

        data = {"phase": pk}

        route = "v1/defaults/defaults/phase/duplicate/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phase_org_list(self, page=1):
        """Get defaults phase list for organization"""

        route = f"v1/defaults/defaults/phases/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_phase_org(self, data):
        """Create default phase for organization

        Keyword arguments:

        data -- data create :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true,
                "team": 0 (R)
            }
        """

        route = f"v1/defaults/defaults/phases/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phase_team_list(self, team_pk, page=1):
        """Get defaults phase list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/defaults/defaults/phases/list/{self.org_pk}/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_phase_team(self, team_pk, data):
        """Create default phase for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true
            }
        """

        route = f"v1/defaults/defaults/phases/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phase_details(self, pk):
        """Get default phase details

        Keyword arguments:

        pk -- the pk of the default phase
        """

        route = f"v1/defaults/defaults/phases/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_defaults_phase(self, pk, data):
        """Update default phase details

        Keyword arguments:

        pk -- the pk of the default phase
        data -- data update :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true
            }
        """

        route = f"v1/defaults/defaults/phases/{pk}/"
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

    def delete_defaults_phase(self, pk):
        """Delete default phase

        Keyword arguments :

        pk -- pk of the phase
        """
        route = f"v1/defaults/defaults/phases/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def apply_defaults_phasesets(self, data):
        """Apply default phase sets

        data = {
            'library': phaseset_pk,
            'fee_project': fee_project_pk,
        }
        """

        route = "v1/defaults/defaults/phasesets/apply/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def duplicate_defaults_phasesets(self, pk):
        """Duplicate default phase sets

        Keyword arguements:

        pk -- pk of the phasesets
        """

        data = {"library": pk}

        route = "v1/defaults/defaults/phasesets/duplicate/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phasesets_org_list(self, page=1):
        """Get defaults phase sets list for organization"""

        route = f"v1/defaults/defaults/phasesets/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_phasesets_org(self, data):
        """Create default phase sets for organization

        Keyword arguments:

        data -- data create :
            {
                "is_main": true,
                "title": "string",
                "team": 0 (R)
            }
        """

        route = f"v1/defaults/defaults/phasesets/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phasesets_team_list(self, team_pk, page=1):
        """Get defaults phase sests list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/defaults/defaults/phasesets/list/{self.org_pk}/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_phasesets_team(self, team_pk, data):
        """Create default phase sets for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "is_main": true,
                "title": "string",
                "team": 0 (R)
            }
        """

        route = f"v1/defaults/defaults/phasesets/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_phasesets_details(self, pk):
        """Get default phase sets details

        Keyword arguments:

        pk -- the pk of the default phase set
        """

        route = f"v1/defaults/defaults/phasesets/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_defaults_phasesets(self, pk, data):
        """Update default phase sets

        Keyword arguments:

        pk -- the pk of the default phase sets
        data -- data update :
            {
                "is_main": true,
                "title": "string"
            }
        """

        route = f"v1/defaults/defaults/phasesets/{pk}/"
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

    def delete_defaults_phasesets(self, pk):
        """Delete default phase sets

        Keyword arguments :

        pk -- pk of the phase sets
        """
        route = f"v1/defaults/defaults/phasesets/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def duplicate_defaults_plan(self, pk):
        """Duplicate defaults plan

        Keyword arguments :

        pk -- pk of the plan
        """

        data = {"plan": pk}

        route = "v1/defaults/defaults/plan/duplicate/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plans_org_list(self, page=1):
        """Get defaults plans list for organization"""

        route = f"v1/defaults/defaults/plans/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_plan_org(self, data):
        """Create default plan for organization

        Keyword arguments:

        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0
            }
        """

        route = f"v1/defaults/defaults/plans/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plans_team_list(self, team_pk, page=1):
        """Get defaults plans list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/defaults/defaults/plans/list/{self.org_pk}/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_plan_team(self, team_pk, data):
        """Create default plan for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0
            }
        """

        route = f"v1/defaults/defaults/plans/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plan_details(self, pk):
        """Get default plan details

        Keyword arguments:

        pk -- the pk of the default plan
        """

        route = f"v1/defaults/defaults/plans/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_defaults_plan(self, pk, data):
        """Update default plan

        Keyword arguments:

        pk -- the pk of the default plan
        data -- data update :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0,
                "team": 0
            }
        """

        route = f"v1/defaults/defaults/plans/{pk}/"
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

    def delete_defaults_plan(self, pk):
        """Delete default plan

        Keyword arguments :

        pk -- pk of the plan
        """
        route = f"v1/defaults/defaults/plans/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def apply_defaults_plansets(self, data):
        """Apply default plan sets"""

        route = "v1/defaults/defaults/plansets/apply/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def duplicate_defaults_plansets(self, pk):
        """Duplicate default plan sets

        Keyword arguements:

        pk -- pk of the phasesets
        """

        data = {"library": pk}

        route = "v1/defaults/defaults/plansets/duplicate/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plansets_org_list(self, page=1):
        """Get defaults plan sets list for organization"""

        route = f"v1/defaults/defaults/plansets/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_plansets_org(self, data):
        """Create default plan sets for organization

        Keyword arguments:

        data -- data create :
            {
                "title": "string"
            }
        """

        route = f"v1/defaults/defaults/plansets/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plansets_team_list(self, team_pk, page=1):
        """Get defaults plan sests list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/defaults/defaults/plansets/list/{self.org_pk}/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_defaults_plansets_team(self, team_pk, data):
        """Create default plan sets for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "title": "string"
            }
        """

        route = f"v1/defaults/defaults/plansets/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_defaults_plansets_details(self, pk):
        """Get default plan sets details

        Keyword arguments:

        pk -- the pk of the default plan set
        """

        route = f"v1/defaults/defaults/plansets/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_defaults_plansets(self, pk, data):
        """Update default plan sets

        Keyword arguments:

        pk -- the pk of the default plan sets
        data -- data update :
            {
                "title": "string"
            }
        """

        route = f"v1/defaults/defaults/plansets/{pk}/"
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

    def delete_defaults_plansets(self, pk):
        """Delete default plan sets

        Keyword arguments :

        pk -- pk of the plan sets
        """
        route = f"v1/defaults/defaults/plansets/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
