import requests
import json

from .helper import Helper


class Time(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Timelogs ####

    def copy_previous_week(self):
        """ Copy previous week """

        route = 'v1/timelogs/actions/copy-previous-week/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timelogs_analytics_team(self, team_pk):
        """ Hours per year/month/weer per teamuser.orguser 

        Keyword arguments :

        team_pk : pk of the team
        """

        route = 'v1/timelogs/analytics/{0}/'.format(team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timelogs_calendar(self):
        """ Get the calendar """

        route = 'v1/timelogs/calendar/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_timelogs_comments(self, pk):
        """ No documentation 
        #! what is the pk
        Keyword argument : 

        pk -- pk of what ? 
        """

        route = 'v1/timelogs/comments/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timelogs_delete_imported_worklogs_project(self, project_pk):
        """ Get the deleted/imported worklogs of a project

        Keyword arguments : 

        project_pk -- pk of the project

        """

        route = 'v1/timelogs/delete-imported-worklogs/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_timelogs_delete_imported_worklogs_project(self, project_pk):
        """ Create deleted/imported worklogs of a project

        Keyword arguments : 

        project_pk -- pk of the project

        """

        route = 'v1/timelogs/delete-imported-worklogs/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timelogs_monthly_summary(self):
        """ Get mothnly summary """

        route = 'v1/timelogs/monthly-summary/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_recently_worked_on(self, team_pk):
        """ Get recently worked on projects, areas, zones, plans and annexes """

        route = 'v1/timelogs/recently-worked-on/{0}/'.format(team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def validate_timelogs(self, team_pk):
        """ Validate timelog

        Keyword arguments : 

        team_pk -- pk of the team

        """

        route = 'v1/timelogs/validation/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Holidays ###
    def get_timelogs_holidays_org(self, page=1):
        """ Get the holidays list """

        route = 'v1/timelogs/holidays/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_holidays_org(self, data):
        """ Create holidays

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

        route = 'v1/timelogs/holidays/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_holidays_team(self, team_pk, page=1):
        """ Get the holidays list for a team 

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/holidays/list/{0}/{1}/?page_size={2}&page={3}'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_holidays_team(self, team_pk, data):
        """ Create holidays for a team

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

        route = 'v1/timelogs/holidays/list/{0}/{1}/'.format(self.org_pk, team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_holidays_details(self, pk):
        """ Get the holidays details

        pk -- pk of the holidays
        """

        route = 'v1/timelogs/holidays/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_timelogs_holidays(self, pk, data):
        """ Update holidays for a team

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

        route = 'v1/timelogs/holidays/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_timelogs_holidays(self, pk):
        """ Delete holidays for a team

        Keyword arguments : 

        pk -- pk of the holidays
        """

        route = 'v1/timelogs/holidays/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Hourslogs ###
    def get_timelogs_hourslogs_list(self, team_pk, page=1):
        """ Get the hourslogs list 

        Keyword argument : 

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/hourslogs/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_hourslogs_list(self, team_pk, data):
        """ Create hourslogs

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

        route = 'v1/timelogs/hourslogs/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_hourslogs_my_list(self, team_pk, page=1):
        """ Get the hourslogs list 

        Keyword argument : 

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/hourslogs/my-list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_hourslogs_my_list(self, team_pk, data):
        """ Create hourslogs

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

        route = 'v1/timelogs/hourslogs/my-list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_hourslogs_details(self, pk):
        """ Get timelogs hourslogs details

        Keyword arguments :

        pk -- pk of the hourslogs
        """
        route = 'v1/timelogs/hourslogs/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_timelogs_hourslogs(self, pk, data):
        """ Update timelogs hourslogs

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
        route = 'v1/timelogs/hourslogs/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def delete_timelogs_hourslogs(self, pk):
        """ Delete timelogs hourslogs

        Keyword arguments :

        pk -- pk of the hourslogs
        """
        route = 'v1/timelogs/hourslogs/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    ### Timeoff ###
    def get_timelogs_my_timeoff_requests_list(self, team_pk, page=1):
        """ Get my timeoff requests 

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/my-timeoff-requests/list/{0}/?page_size={1}&page={2}'.format(
            team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_my_timeoff_requests(self, team_pk, data, page):
        """ Create my timeoff requests 

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

        route = 'v1/timelogs/my-timeoff-requests/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def get_timelogs_timeoff_requests_list(self, team_pk, page=1):
        """ Get timeoff requests 

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/timeoff-requests/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_timeoff_requests(self, team_pk, data):
        """ Create timeoff requests 

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

        route = 'v1/timelogs/timeoff-requests/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def create_timeoff_balance_list(self, team_pk, data):
        """ Create timeoff balance list 

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create : 
        {
            "orguser": 0,
            "start_date": "string",
            "end_date": "string"
        }
        """

        route = 'v1/timelogs/timeoff-balance/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def create_timeoff_requests_action(self, team_pk, data):
        """ Create timeoff request action

        Keyword arguments :

        team_pk -- pk of the team
        data -- data create : 
        {
            "orguser": 0,
            "start_date": "string",
            "end_date": "string"
        }
        """

        route = 'v1/timelogs/timeoff-balance/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_timeoff_requests_details(self, pk):
        """ Get timeoff requests details 

        Keyword arguments:

        pk -- pk of the timeoff requests
        """

        route = 'v1/timelogs/timeoff-requests/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_timelogs_timeoff_requests(self, pk, data):
        """ Update tiemoff requests

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

        route = 'v1/timelogs/timeoff-requests/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_timelogs_timeoff_requests(self, pk):
        """ Delete timeoff requests details 

        Keyword arguments:

        pk -- pk of the timeoff requests
        """

        route = 'v1/timelogs/timeoff-requests/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Types ###
    def get_timelogs_types_list(self):
        """ Get timelogs type list """

        route = 'v1/timelogs/types/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_types_list(self, data):
        """ Create timelogs type 

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

        route = 'v1/timelogs/types/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def get_timelogs_types_timeoff_list(self, page=1):
        """ Get timelogs types timeoff list """

        route = 'v1/timelogs/types/timeoff/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_types_timeoff(self, data):
        """ Create timelogs types timeoff list 

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

        route = 'v1/timelogs/types/timeoff/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def get_timelogs_types_details(self, pk):
        """ Get timelogs type details 

        Keyword arguments:

        pk -- pk of the timelog
        """

        route = 'v1/timelogs/types/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_timelogs_types(self, pk, data):
        """ Update timelogs types timeoff 

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

        route = 'v1/timelogs/types/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def delete_timelogs_types(self, pk):
        """ Delete timelogs type 

        Keyword arguments:

        pk -- pk of the timelog
        """

        route = 'v1/timelogs/types/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    ### Week-config ###
    def get_timelogs_week_config_list(self, page=1):
        """ Get week config list """

        route = 'v1/timelogs/week-config/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_week_config(self, data):
        """ Create week config 

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

        route = 'v1/timelogs/week-config/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_week_config_details(self, pk):
        """ Get week config details

        Keyword arguments:

        pk -- pk of the week config
        """

        route = 'v1/timelogs/week-config/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_timelogs_week_config(self, pk, data):
        """ Update week config 

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

        route = 'v1/timelogs/week-config/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_timelogs_week_config(self, pk):
        """ Delete week config details

        Keyword arguments:

        pk -- pk of the week config
        """

        route = 'v1/timelogs/week-config/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Weeks ###
    def get_timelogs_week_away(self):
        """ Get days current user is away for given week """

        route = 'v1/timelogs/weeks/away/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timelogs_week_list(self, page=1, start_date=None):
        """ Get weeks list 

        Keyword arguments:

        start_date -- start date of the week 
        """

        route = 'v1/timelogs/weeks/list/{0}/'.format(self.org_pk)
        parameters = "?page={0}&page_size={1}".format(page, self.pagination)
        if start_date:
            parameters += '&start_date={0}'.format(start_date)

        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response, True)

    def get_timelogs_week_details(self, pk):
        """ Get weeks details 

        Keyword arguments:

        pk -- pk of the week
        """

        route = 'v1/timelogs/weeks/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_timelogs_week(self, pk, data):
        """ Update week 

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

        route = 'v1/timelogs/weeks/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    ### Worklogs ###
    def get_timelogs_worklogs_list(self, team_pk, page=1):
        """ Get worklogs list 

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/timelogs/worklogs/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_timelogs_worklogs(self, team_pk, data):
        """ Create worklogs 

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

        route = 'v1/timelogs/worklogs/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timelogs_worklogs_details(self, pk):
        """ Get worklogs details 

        Keyword arguments:

        pk -- pk of the worklogs
        """

        route = 'v1/timelogs/worklogs/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_timelogs_worklogs(self, pk, data):
        """ Update worklogs 

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

        route = 'v1/timelogs/worklogs/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_timelogs_worklogs(self, pk):
        """ Delete worklogs 

        Keyword arguments:

        pk -- pk of the worklogs
        """

        route = 'v1/timelogs/worklogs/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Timeperiods ####
    def get_timeperiods_dashboard_scheduling_timeline(self):
        """ Get dashboard scheduling timeline """

        route = 'v1/timeperiods/dashboard/scheduling/timeline/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timeperiods_resource_planning_timeline(self):
        """ Get resource planning timeline """

        route = 'v1/timeperiods/resource-planning-timeline/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_timeperiods_resource_planning_timeline(self, data):
        """ Create planning timeline """

        route = 'v1/timeperiods/resource-planning-timeline/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timeperiods_resources_timeline(self, project_pk):
        """ Get resources timeline 

        Keyword arguments: 

        project_pk -- pk of the project
        """

        route = 'v1/timeperiods/resources-timeline/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timeperiods_role_annex_periods(self, page=1):
        """ Get role annex periods list """

        route = 'v1/timeperiods/role-annex-periods/list/{0}/?page_size={1}&page={2}'.format(
            self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_timeperiods_role_annex_period_details(self, pk):
        """ Get role annex period details  

        Keyword arguments:

        pk -- pk of the role annex period
        """

        route = 'v1/timeperiods/role-annex-periods/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_timeperiods_role_annex_period(self, pk):
        """ Delete role annex period  

        Keyword arguments:

        pk -- pk of the role annex period
        """

        route = 'v1/timeperiods/role-annex-periods/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_timeperiods_scheduling_timeline_actions(self, project_pk):
        """
        Get scheduling timeline actions for a project

        Keyword arguments:

        pk -- pk of the project
        """

        route = 'v1/timeperiods/scheduling-timeline/actions/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_timeperiods_scheduling_timeline_actions(self, project_pk):
        """
        Get scheduling timeline actions for a project

        Keyword arguments:

        pk -- pk of the project
        """

        route = 'v1/timeperiods/scheduling-timeline/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_user_period_action(self):
        """ Create user period action """

        route = 'v1/timeperiods/user-period/list/action/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_user_period_list(self, team_pk):
        """ Get user period list"""

        route = 'v1/timeperiods/user-period/list/{0}/?team={1}'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_user_period_details(self, pk):
        """ Get user period details

        Keyword arguments:

        pk -- pk of the user perdio
        """

        route = 'v1/timeperiods/user-period/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_user_period(self, pk):
        """ Delete user period details

        Keyword arguments:

        pk -- pk of the user perdio
        """

        route = 'v1/timeperiods/user-period/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_users_scheduling_timeline(self):
        """ Get user scheduling timeline """

        route = 'v1/timeperiods/users/scheduling-timeline/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Roles ####
    def get_roles_list(self, page=1):
        """ Get roles list """

        route = 'v1/roles/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_roles(self, data):
        """ Create roles list 

        Keyword arguments:

        data -- data create:
        {
            "title": "string",
            "billable_per_hour": 0,
            "payable_per_hour": 0
        }
        """

        route = 'v1/roles/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_roles_project_list(self, page=1):
        """ Get roles project list """

        route = 'v1/roles/project/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_roles_project(self, data):
        """ Get roles project list 

        Keyword arguments:

        data -- data create:
        {
            "project": 0,
            "role": 0,
            "billable_per_hour": 0,
            "payable_per_hour": 0,
            "pay_per_hour": 0,
            "personnel_count": 0
        }
        """

        route = 'v1/roles/project/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_roles_project_details(self, pk):
        """ Get roles details 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_roles_project(self, pk, data):
        """ Update roles project 

        Keyword arguments:

        pk -- pk of the roles project
        data -- data create:
        {
            "project": 0,
            "role": 0,
            "billable_per_hour": 0,
            "payable_per_hour": 0,
            "pay_per_hour": 0,
            "personnel_count": 0
        }
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_roles_project(self, pk):
        """ Delete roles project 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/project/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_bulk_action_add_roles(self, project_pk):
        """ Create bulk action to add role to project """

        route = 'v1/roles/roles/bulk/add/{0}/?project={1}'.format(self.org_pk, project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_bulk_action_add_roles(self, project_pk):
        """ Delete bulk action to add role to project """

        route = 'v1/roles/roles/bulk/delete/{0}/?project={1}'.format(self.org_pk, project_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_roles_details(self, pk):
        """ Get roles details 

        Keyword arguments:

        pk -- pk of the roles project
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_roles(self, pk, data):
        """ Update roles 

        Keyword arguments:

        pk -- pk of the roles
        data -- data create:
        {
            "title": "string",
            "billable_per_hour": 0,
            "payable_per_hour": 0
        }
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_roles(self, pk):
        """ Delete roles 

        Keyword arguments:

        pk -- pk of the roles 
        """

        route = 'v1/roles/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Trips ####
    def get_trips_list(self, page=1):
        """ Get trips list """

        route = 'v1/trips/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_trip(self, data):
        """ Create trip  

        Keyword arguments:

        data -- data create:
        {
            "team": 0,
            "project": 0,
            "orguser": 0,
            "start_date": "string",
            "end_date": "string",
            "notes": "string"
        }
        """

        route = 'v1/trips/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_trips_details(self, pk):
        """ Get trip details 

        Keyword arguments:

        pk -- pk of the rtrip
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_trip(self, pk, data):
        """ Update trip 

        Keyword arguments:

        pk -- pk of the trip
        data -- data create:
        {
            "team": 0,
            "project": 0,
            "orguser": 0,
            "start_date": "string",
            "end_date": "string",
            "notes": "string"
        }
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_trip(self, pk):
        """ Delete trip 

        Keyword arguments:

        pk -- pk of the trip
        """

        route = 'v1/trips/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
