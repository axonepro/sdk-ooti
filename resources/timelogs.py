import json

import requests

from .resource import Resource


class Timelogs(Resource):

    def copy_previous_week(self):
        """Copy previous week"""

        route = f"v1/timelogs/actions/copy-previous-week/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_analytics_team(self, team_pk):
        """Hours per year/month/weer per teamuser.orguser

        Keyword arguments :

        team_pk : pk of the team
        """

        route = f"v1/timelogs/analytics/{team_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_calendar(self):
        """Get the calendar"""

        route = f"v1/timelogs/calendar/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_timelogs_comments(self, pk):
        """No documentation
        #! what is the pk
        Keyword argument :

        pk -- pk of what ?
        """

        route = f"v1/timelogs/comments/{pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    # TODO GET on /api/v1/timelogs/dash_calendar/{org_pk}/

    def get_timelogs_delete_imported_worklogs_project(self, project_pk):
        """Get the deleted/imported worklogs of a project

        Keyword arguments :

        project_pk -- pk of the project

        """

        route = f"v1/timelogs/delete-imported-worklogs/{project_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def create_timelogs_delete_imported_worklogs_project(self, project_pk):
        """Create deleted/imported worklogs of a project

        Keyword arguments :

        project_pk -- pk of the project

        """

        route = f"v1/timelogs/delete-imported-worklogs/{project_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_monthly_summary(self):
        """Get mothnly summary"""

        route = f"v1/timelogs/monthly-summary/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_recently_worked_on(self, team_pk):
        """Get recently worked on projects, areas, zones, plans and annexes"""

        route = f"v1/timelogs/recently-worked-on/{team_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def validate_timelogs(self, team_pk):
        """Validate timelog

        Keyword arguments :

        team_pk -- pk of the team

        """

        route = f"v1/timelogs/validation/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_holidays_org(self, page=1):
        """Get the holidays list"""

        route = f"v1/timelogs/holidays/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_holidays_org(self, data):
        """Create holidays

        Keyword arguments :

        data -- data create :
        {
            "teams": [
                "string"
            ],
            "date": "string",
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "is_default": true
        }

        """

        route = f"v1/timelogs/holidays/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_holidays_team(self, team_pk, page=1):
        """Get the holidays list for a team

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/holidays/list/{self.org_pk}/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_holidays_team(self, team_pk, data):
        """Create holidays for a team

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create :
        {
            "teams": [
                "string"
            ],
            "date": "string",
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "is_default": true
        }

        """

        route = f"v1/timelogs/holidays/list/{self.org_pk}/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_holidays_details(self, pk):
        """Get the holidays details

        pk -- pk of the holidays
        """

        route = f"v1/timelogs/holidays/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_timelogs_holidays(self, pk, data):
        """Update holidays for a team

         Keyword arguments :

        pk -- pk of the holidays
         data -- data create :
         {
             "teams": [
                 "string"
             ],
             "date": "string",
             "name": "string",
             "name_en": "string",
             "name_fr": "string",
             "is_default": true
         }
        """

        route = f"v1/timelogs/holidays/{pk}/"
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

    def delete_timelogs_holidays(self, pk):
        """Delete holidays for a team

        Keyword arguments :

        pk -- pk of the holidays
        """

        route = f"v1/timelogs/holidays/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_hourslogs_list(self, team_pk, page=1):
        """Get the hourslogs list

        Keyword argument :

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/hourslogs/list/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_hourslogs_list(self, team_pk, data):
        """Create hourslogs

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create :
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
            "total_hours": 0,
            "monday_notes": "string",
            "tuesday_notes": "string",
            "wednesday_notes": "string",
            "thursday_notes": "string",
            "friday_notes": "string",
            "saturday_notes": "string",
            "sunday_notes": "string",
            "weekly_notes": "string",
            "project": 0,
            "is_draft" False,
            "week": 0

        """

        route = f"v1/timelogs/hourslogs/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_hourslogs_my_list(self, team_pk, page=1):
        """Get the hourslogs list

        Keyword argument :

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/hourslogs/my-list/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_hourslogs_my_list(self, team_pk, data):
        """Create hourslogs

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create :
        {
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
            "total_hours": 0,
            "monday_notes": "string",
            "tuesday_notes": "string",
            "wednesday_notes": "string",
            "thursday_notes": "string",
            "friday_notes": "string",
            "saturday_notes": "string",
            "sunday_notes": "string",
            "weekly_notes": "string",
            "project": 0,
            "is_draft" False,
            "week": 0
        }

        """

        route = f"v1/timelogs/hourslogs/my-list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_hourslogs_details(self, pk):
        """Get timelogs hourslogs details

        Keyword arguments :

        pk -- pk of the hourslogs
        """
        route = f"v1/timelogs/hourslogs/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def update_timelogs_hourslogs(self, pk, data):
        """Update timelogs hourslogs

        Keyword arguments :

        pk -- pk of the hourslogs
        data -- data update :
        {
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
            "total_hours": 0,
            "monday_notes": "string",
            "tuesday_notes": "string",
            "wednesday_notes": "string",
            "thursday_notes": "string",
            "friday_notes": "string",
            "saturday_notes": "string",
            "sunday_notes": "string",
            "weekly_notes": "string"
        }
        """
        route = f"v1/timelogs/hourslogs/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response, True)

    def delete_timelogs_hourslogs(self, pk):
        """Delete timelogs hourslogs

        Keyword arguments :

        pk -- pk of the hourslogs
        """
        route = f"v1/timelogs/hourslogs/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    # TODO GET on /api/v1/timelogs/my-timeoff-request/list/{team_pk}/

    # TODO POST on /api/v1/timelogs/my-timeoff-request/list/{team_pk}/

    # TODO GET on /api/v1/timelogs/time-summary/{org_pk}/

    # TODO GET on /api/v1/timelogs/time-summary/{org_pk}/{team_pk}/

    # TODO GET on /api/v1/timelogs/timelogs-charts/{org_pk}/{team_pk}/

    def get_timelogs_my_timeoff_requests_list(self, team_pk, page=1):
        """Get my timeoff requests

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/my-timeoff-requests/list/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_my_timeoff_requests(self, team_pk, data, page):
        """Create my timeoff requests

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create:
        {
            "start_date_is_half": true,
            "end_date_is_half": true,
            "start_date": "string",
            "end_date": "string",
            "type": 0
            "is_draft": True,
            "notes": "string",
            "validation_notes": "string",
            "is_recuperation": true,
            "manual_days_paid": true,
            "paid_days": 0,
            "unpaid_days": 0,
            "recuperation_days": 0,
            "recuperation_hours": 0,
            "is_uncounted": true,
            "is_treated": true,
            "orguser" 0,
            "is_paid": true
        }
        """

        route = f"v1/timelogs/my-timeoff-requests/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response, True)

    def get_timelogs_timeoff_requests_list(self, team_pk, page=1):
        """Get timeoff requests

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/timeoff-requests/list/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_timeoff_requests(self, team_pk, data):
        """Create timeoff requests

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create:
        {
            "start_date_is_half": true,
            "end_date_is_half": true,
            "start_date": "string",
            "end_date": "string",
            "type": 0
            "is_draft": True,
            "notes": "string",
            "validation_notes": "string",
            "is_recuperation": true,
            "manual_days_paid": true,
            "paid_days": 0,
            "unpaid_days": 0,
            "recuperation_days": 0,
            "recuperation_hours": 0,
            "is_uncounted": true,
            "is_treated": true,
            "orguser" 0
        }
        """

        route = f"v1/timelogs/timeoff-requests/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response, True)

    def create_timeoff_balance_list(self, team_pk, data):
        """Create timeoff balance list

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create :
        {
            "orguser": 0,
            "start_date": "string",
            "end_date": "string"
        }
        """

        route = f"v1/timelogs/timeoff-balance/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    # TODO POST on /api/v1/timelogs/timeoff-requests/action/{team_pk}/

    def create_timeoff_requests_action(self, team_pk, data):
        """Create timeoff request action

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create :
        {
            "orguser": 0,
            "start_date": "string",
            "end_date": "string"
        }
        """

        route = f"v1/timelogs/timeoff-balance/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_timeoff_requests_details(self, pk):
        """Get timeoff requests details

        Keyword arguments:

        pk -- pk of the timeoff requests
        """

        route = f"v1/timelogs/timeoff-requests/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_timelogs_timeoff_requests(self, pk, data):
        """Update tiemoff requests

        Keyword arguments:

        pk -- pk of the timeoff requests
        data -- data update :
            {
                "start_date_is_half": true,
                "end_date_is_half": true,
                "start_date": "string",
                "end_date": "string",
                "type": 0
                "is_draft": True,
                "notes": "string",
                "validation_notes": "string",
                "is_recuperation": true,
                "manual_days_paid": true,
                "paid_days": 0,
                "unpaid_days": 0,
                "recuperation_days": 0,
                "recuperation_hours": 0,
                "is_uncounted": true,
                "is_treated": true,
                "orguser" 0
            }
        """

        route = f"v1/timelogs/timeoff-requests/{pk}/"
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

    def delete_timelogs_timeoff_requests(self, pk):
        """Delete timeoff requests details

        Keyword arguments:

        pk -- pk of the timeoff requests
        """

        route = f"v1/timelogs/timeoff-requests/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_types_list(self):
        """Get timelogs type list"""

        route = f"v1/timelogs/types/list/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_types_list(self, data):
        """Create timelogs type

        data -- data create:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "is_recuperation": true,
            "is_billable": true
            "project_option": "string",
            "deliverable_option": "string",
            "exclude_from_limit": true
        }
        """

        route = f"v1/timelogs/types/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response, True)

    def get_timelogs_types_timeoff_list(self, page=1):
        """Get timelogs types timeoff list"""

        route = f"v1/timelogs/types/timeoff/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_types_timeoff(self, data):
        """Create timelogs types timeoff list

        Keyword arguments:

        data -- data create:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "is_default": true,
            "is_recuperation": true,
            "deduct_from_balance": true
        }
        """

        route = f"v1/timelogs/types/timeoff/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response, True)

    # TODO GET on /api/v1/timelogs/types/timeoff/{id}/

    # TODO PATCH on /api/v1/timelogs/types/timeoff/{id}/

    # TODO DELETE on /api/v1/timelogs/types/timeoff/{id}/

    def get_timelogs_types_details(self, pk):
        """Get timelogs type details

        Keyword arguments:

        pk -- pk of the timelog
        """

        route = f"v1/timelogs/types/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def update_timelogs_types(self, pk, data):
        """Update timelogs types timeoff

        Keyword arguments:

        pk -- pk of the timelog
        data -- data create:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "is_default": true,
            "is_recuperation": true,
            "deduct_from_balance": true
        }
        """

        route = f"v1/timelogs/types/{pk}/"
        response = self.process_request(
            requests,
            "PATCH",
            self.base_url,
            route,
            self.headers,
            None,
            json.dumps(data),
        )
        return self.process_response(response, True)

    def delete_timelogs_types(self, pk):
        """Delete timelogs type

        Keyword arguments:

        pk -- pk of the timelog
        """

        route = f"v1/timelogs/types/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def get_timelogs_week_config_list(self, page=1):
        """Get week config list"""

        route = f"v1/timelogs/week-config/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_week_config(self, data):
        """Create week config

        Keyword arguments:

        data -- data to create:
            {
                "team": 0,
                "is_default": true,
                "orgusers": [
                    "string"
                ],
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "entry_mode": "string",
                "week_start_day": "string",
                "show_monday": true,
                "show_tuesday": true,
                "show_wednesday": true,
                "show_thursday": true,
                "show_friday": true,
                "show_saturday": true,
                "show_sunday": true,
                "use_daily_limits": true,
                "weekly_hours_limit": 0,
                "weekly_overtime_limit": 0,
                "hours_per_monday": 0,
                "hours_per_tuesday": 0,
                "hours_per_wednesday": 0,
                "hours_per_thursday": 0,
                "hours_per_friday": 0,
                "hours_per_saturday": 0,
                "hours_per_sunday": 0,
                "monday_overtime_limit": 0,
                "tuesday_overtime_limit": 0,
                "wednesday_overtime_limit": 0,
                "thursday_overtime_limit": 0,
                "friday_overtime_limit": 0,
                "saturday_overtime_limit": 0,
                "sunday_overtime_limit": 0,
                "overtime_enabled": true
            }
        """

        route = f"v1/timelogs/week-config/list/{self.org_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_week_config_details(self, pk):
        """Get week config details

        Keyword arguments:

        pk -- pk of the week config
        """

        route = f"v1/timelogs/week-config/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_timelogs_week_config(self, pk, data):
        """Update week config

        Keyword arguments:

        pk -- pk of the week config
        data -- data to create:
            {
                "team": 0,
                "is_default": true,
                "orgusers": [
                    "string"
                ],
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "entry_mode": "string",
                "week_start_day": "string",
                "show_monday": true,
                "show_tuesday": true,
                "show_wednesday": true,
                "show_thursday": true,
                "show_friday": true,
                "show_saturday": true,
                "show_sunday": true,
                "use_daily_limits": true,
                "weekly_hours_limit": 0,
                "weekly_overtime_limit": 0,
                "hours_per_monday": 0,
                "hours_per_tuesday": 0,
                "hours_per_wednesday": 0,
                "hours_per_thursday": 0,
                "hours_per_friday": 0,
                "hours_per_saturday": 0,
                "hours_per_sunday": 0,
                "monday_overtime_limit": 0,
                "tuesday_overtime_limit": 0,
                "wednesday_overtime_limit": 0,
                "thursday_overtime_limit": 0,
                "friday_overtime_limit": 0,
                "saturday_overtime_limit": 0,
                "sunday_overtime_limit": 0,
                "overtime_enabled": true
            }
        """

        route = f"v1/timelogs/week-config/{pk}/"
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

    def delete_timelogs_week_config(self, pk):
        """Delete week config details

        Keyword arguments:

        pk -- pk of the week config
        """

        route = f"v1/timelogs/week-config/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_week_away(self):
        """Get days current user is away for given week"""

        route = f"v1/timelogs/weeks/away/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_timelogs_week_list(self, page=1, start_date=None):
        """Get weeks list

        Keyword arguments:

        start_date -- start date of the week
        """

        route = f"v1/timelogs/weeks/list/{self.org_pk}/"
        parameters = f"?page={page}&page_size={self.pagination}"
        if start_date:
            parameters += f"&start_date={start_date}"

        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, parameters, None
        )
        return self.process_response(response, True)

    def get_timelogs_week_details(self, pk):
        """Get weeks details

        Keyword arguments:

        pk -- pk of the week
        """

        route = f"v1/timelogs/weeks/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def update_timelogs_week(self, pk, data):
        """Update week

        Keyword arguments:

        pk -- pk of the week
        data -- data to create:
            {
                "start_date": "string",
                "end_date": "string",
                "is_open": false,
                "team": 0;
                "has_hourslogs": false
            }

        """

        route = f"v1/timelogs/weeks/{pk}/"
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

    def get_timelogs_worklogs_list(self, team_pk, page=1):
        """Get worklogs list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = f"v1/timelogs/worklogs/list/{team_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response, True)

    def create_timelogs_worklogs(self, team_pk, data):
        """Create worklogs

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create:
            {
                "project": 0,
                "phase": 0,
                "task": 0,
                "annex": 0,
                "date": "string",
                "type": 0,
                "is_draft": false,
                "orguser": 0,
                "week": 0,
                "day": 0,
                "hourslog": 0,
                "team": 0,
                "area": 0,
                "zone": 0,
                "plan": 0,
                "hours": 0,
                "hours_pct": 0,
                "is_validated": "string",
                "description": "string",
                "is_imported": true,
                "cost": 0,
                "base_cost": 0
            }
        """

        route = f"v1/timelogs/worklogs/list/{team_pk}/"
        response = self.process_request(
            requests, "POST", self.base_url, route, self.headers, None, json.dumps(data)
        )
        return self.process_response(response)

    def get_timelogs_worklogs_details(self, pk):
        """Get worklogs details

        Keyword arguments:

        pk -- pk of the worklogs
        """

        route = f"v1/timelogs/worklogs/{pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def update_timelogs_worklogs(self, pk, data):
        """Update worklogs

        Keyword arguments:

        pk -- pk of the worklogs
        data -- data create:
            {
                "project": 0,
                "phase": 0,
                "task": 0,
                "annex": 0,
                "date": "string",
                "type": 0,
                "is_draft": false,
                "orguser": 0,
                "week": 0,
                "day": 0,
                "hourslog": 0,
                "team": 0,
                "area": 0,
                "zone": 0,
                "plan": 0,
                "hours": 0,
                "hours_pct": 0,
                "is_validated": "string",
                "description": "string",
                "is_imported": true,
                "cost": 0,
                "base_cost": 0
            }
        """

        route = f"v1/timelogs/worklogs/{pk}/"
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

    def delete_timelogs_worklogs(self, pk):
        """Delete worklogs

        Keyword arguments:

        pk -- pk of the worklogs
        """

        route = f"v1/timelogs/worklogs/{pk}/"
        response = self.process_request(
            requests, "DELETE", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
