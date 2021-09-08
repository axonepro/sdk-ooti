import requests
import json

from .helper import Helper


class Timeperiods(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_timeperiods_dashboard_scheduling_timeline(self):
        """ Get dashboard scheduling timeline """

        route = 'v1/timeperiods/dashboard/scheduling/timeline/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_timeperiods_resource_planning_timeline(self):
        """ Get resource planning timeline """

        route = 'v1/timeperiods/resource-planning-timeline/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_timeperiods_resource_planning_timeline(self, data):
        """ Create planning timeline """

        route = 'v1/timeperiods/resource-planning-timeline/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_timeperiods_resources_timeline(self, project_pk):
        """ Get resources timeline 

        Keyword arguments: 

        project_pk -- pk of the project
        """

        route = 'v1/timeperiods/resources-timeline/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_timeperiods_role_annex_periods(self, page=1):
        """ Get role annex periods list """

        route = 'v1/timeperiods/role-annex-periods/list/{0}/?page_size={1}&page={2}'.format(
            self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_timeperiods_role_annex_periods(self, data):
        """ Create week config list 

        Keyword arguments:

        data -- data create: 
        {
            "start_date": "string",
            "end_date": "string",
            "hours_per_day": 0,
            "personnel_count": 0,
            "include_saturday": true,
            "include_sunday": true,
            "hours_scheduled": 0,
            "hours_scheduled_per_user": 0,
            "annex": 0, (R) 
            "role": 0,
            "project_role": 0,
            "orgusers": [
                "string"
            ],
            "budget_pct": 0
        }

        """

        route = 'v1/timeperiods/role-annex-periods/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_timeperiods_role_annex_period_details(self, pk):
        """ Get role annex period details  

        Keyword arguments:

        pk -- pk of the role annex period
        """

        route = 'v1/timeperiods/role-annex-periods/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_timeperiods_role_annex_period(self, pk, data):
        """ Update role annex period details  

        Keyword arguments:

        pk -- pk of the role annex period
        data -- data update :
        {
            "start_date": "string",
            "end_date": "string",
            "hours_per_day": 0,
            "personnel_count": 0,
            "include_saturday": true,
            "include_sunday": true,
            "hours_scheduled": 0,
            "hours_scheduled_per_user": 0,
            "annex": 0,
            "role": 0,
            "project_role": 0,
            "orgusers": [
                "string"
            ],
            "budget_pct": 0
        }
        """

        route = 'v1/timeperiods/role-annex-periods/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_timeperiods_role_annex_period(self, pk):
        """ Delete role annex period  

        Keyword arguments:

        pk -- pk of the role annex period
        """

        route = 'v1/timeperiods/role-annex-periods/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/timeperiods/role-phase-periods/list/{org_pk}/

    # TODO POST on /api/v1/timeperiods/role-phase-periods/list/{org_pk}/

    # TODO GET on /api/v1/timeperiods/role-phase-periods/{id}/

    # TODO PATCH on /api/v1/timeperiods/role-phase-periods/{id}/

    # TODO DELETE on /api/v1/timeperiods/role-phase-periods/{id}/

    def create_timeperiods_scheduling_timeline_actions(self, project_pk):
        """
        Get scheduling timeline actions for a project

        Keyword arguments:

        pk -- pk of the project
        """

        route = 'v1/timeperiods/scheduling-timeline/actions/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_timeperiods_scheduling_timeline_actions(self, project_pk):
        """
        Get scheduling timeline actions for a project

        Keyword arguments:

        pk -- pk of the project
        """

        route = 'v1/timeperiods/scheduling-timeline/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_user_period_action(self):
        """ Create user period action """

        route = 'v1/timeperiods/user-period/list/action/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_user_period_list(self, team_pk):
        """ Get user period list"""

        route = 'v1/timeperiods/user-period/list/{0}/?team={1}'.format(self.org_pk, team_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_user_period_list(self, data):
        """ Get user period

        Keyword argument:

        data -- data create:
        {
            "orguser": 0,
            "role": 0,
            "time_type": 0,
            "team": 0,
            "project": 0,
            "phase": 0,
            "annex": 0,
            "start_date": "string",
            "end_date": "string",
            "hours_per_day": 0,
            "hours": 0,
            "pct_of_day": 0,
            "description": "string",
            "sync_with_budget": true,
            "sync_with_planning": true
        }
        """

        route = 'v1/timeperiods/user-period/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_user_period_details(self, pk):
        """ Get user period details

        Keyword arguments:

        pk -- pk of the user perdio
        """

        route = 'v1/timeperiods/user-period/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_user_period_list(self, pk, data):
        """ Update user period

        Keyword argument:

        pk -- pk of the user period
        data -- data update:
        {
            "orguser": 0,
            "role": 0,
            "time_type": 0,
            "team": 0,
            "project": 0,
            "phase": 0,
            "annex": 0,
            "start_date": "string",
            "end_date": "string",
            "hours_per_day": 0,
            "hours": 0,
            "pct_of_day": 0,
            "description": "string",
            "sync_with_budget": true,
            "sync_with_planning": true
        }
        """

        route = 'v1/timeperiods/user-period/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_user_period(self, pk):
        """ Delete user period details

        Keyword arguments:

        pk -- pk of the user perdio
        """

        route = 'v1/timeperiods/user-period/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_users_scheduling_timeline(self):
        """ Get user scheduling timeline """

        route = 'v1/timeperiods/users/scheduling-timeline/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)