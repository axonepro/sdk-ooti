import unittest
from ooti import ooti

# To read .env variables
import os
from dotenv import load_dotenv

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.Auth(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = my_account.teams_pk[0]['id']
currency_pk = my_account.Invoicing.get_currencies_list()['data'][0]['pk']
project_pk = my_account.get_projects_list()['data'][0]['id']

orguser = my_account.get_organization_details()['data']['organizations'][0]['orguser']['pk']

week_pk = my_account.Time.get_timelogs_week_list()['data'][0]['id']


class Tests(unittest.TestCase):
    # def test_copy_previous_week(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass {'status': 405, 'data': {'detail': 'Method "GET" not allowed.'}}

    #     res = my_account.Time.copy_previous_week()

    #     self.assertEqual(res['status'], 201)

    def test_get_timelogs_analytics_team(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_analytics_team(team_pk)

        self.assertEqual(res['status'], 200)

    def test_get_timelogs_calendar(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_calendar()

        self.assertEqual(res['status'], 200)

    # def test_create_timelogs_comments(self):
    #     """ Test that 201 is returned """
    #     #! what is the pk
    #     res = my_account.Time.create_timelogs_comments()

    #     self.assertEqual(res['status'], 201)

    def test_get_timelogs_delete_imported_worklogs_project(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_delete_imported_worklogs_project(project_pk)

        self.assertEqual(res['status'], 200)

    # def test_create_timelogs_delete_imported_worklogs_project():
    #     """ Test that 201 is returned """
    #     #! Do not pass Returns a 204 status code
    #     res = my_account.Time.create_timelogs_delete_imported_worklogs_project(project)

    #     self.assertEqual(res['status'], 201)

    # def test_get_timelogs_monthly_summary(self):
    #     """ Test that 200 is returned """
    #     #! Do not pass 403 : "detail": "You do not have permission to perform this action."
    #     res = my_account.Time.get_timelogs_monthly_summary()

    #     self.assertEqual(res['status'], 200)

    def test_get_recently_worked_on(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_recently_worked_on(team_pk)

        self.assertEqual(res['status'], 200)

    # def test_validate_timelogs(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass : 500

    #     res = my_account.Time.validate_timelogs(team_pk)

    #     self.assertEqual(res['status'], 201)

    ### Holidays ###
    def _create_timelogs_holidays_org(self):
        """ Test that 201 is returned """

        data = {
            "teams": [
                team_pk
            ],
            "date": "07-05-2021",
            "name": "UNITTEST",
        }

        return my_account.Time.create_timelogs_holidays_org(data)['data']['id']

    def test_get_timelogs_holidays_org(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_holidays_org()

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_holidays_org(self):
        """ Test that 201 is returned """

        data = {
            "teams": [
                team_pk
            ],
            "date": "07-05-2021",
            "name": "UNITTEST",
        }

        res = my_account.Time.create_timelogs_holidays_org(data)
        my_account.Time.delete_timelogs_holidays(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_holidays_team(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_holidays_team(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_holidays_team(self):
        """ Test that 201 is returned """

        data = {
            "teams": [
                team_pk
            ],
            "date": "07-05-2021",
            "name": "UNITTEST",
        }

        res = my_account.Time.create_timelogs_holidays_team(team_pk, data)
        my_account.Time.delete_timelogs_holidays(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_holidays_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_holidays_org()

        res = my_account.Time.get_timelogs_holidays_details(pk)
        my_account.Time.delete_timelogs_holidays(pk)

        self.assertEqual(res['status'], 200)

    def test_update_timelogs_holidays(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_holidays_org()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Time.update_timelogs_holidays(pk, data)
        my_account.Time.delete_timelogs_holidays(pk)

    def test_delete_timelogs_holidays(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_holidays_org()
        res = my_account.Time.delete_timelogs_holidays(pk)

        self.assertEqual(res['status'], 204)

    ### Hourslogs ###
    def _create_timelogs_hourslogs_return_pk(self):
        """ Create hourslogs and return pk """

        data = {
            "monday": 0,
            "type": 6605,
            "week": week_pk,
            "is_draft": False
        }

        return my_account.Time.create_timelogs_hourslogs_list(team_pk, data)['data']['id']

    def get_timelogs_hourslogs_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_hourslogs_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_hourslogs_list(self):
        """ Test that 201 is returned """

        data = {
            "monday": 0,
            "type": 6605,
            "week": week_pk,
            "is_draft": False
        }

        res = my_account.Time.create_timelogs_hourslogs_list(team_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_timelogs_hourslogs_my_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_hourslogs_my_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_hourslogs_my_list(self):
        """ Test that 201 is returned """
        data = {
            "monday": 0,
            "type": 6605,
            "week": week_pk,
            "is_draft": False
        }

        res = my_account.Time.create_timelogs_hourslogs_my_list(team_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_timelogs_hourslogs_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_hourslogs_return_pk()

        res = my_account.Time.get_timelogs_hourslogs_details(pk)

        self.assertEqual(res['status'], 200)

    def test_get_timelogs_hourslogs_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_hourslogs_return_pk()

        data = {
            "project_pk": project_pk
        }

        res = my_account.Time.update_timelogs_hourslogs(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_timelogs_hourslogs(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_hourslogs_return_pk()

        res = my_account.Time.delete_timelogs_hourslogs(pk)

        self.assertEqual(res['status'], 204)

    ### Timeoff ###
    def _create_timelogs_timeoff_requests(self):
        """ Create timeoff requests and return pk """

        data = {
            "start_date": "11-05-2021",
            "end_date": "12-05-2021",
            "is_paid": True,
            "orguser": orguser
        }

        return my_account.Time.create_timelogs_my_timeoff_requests(team_pk, data)['data']['id']

    def test_get_timelogs_my_timeoff_requests(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_my_timeoff_requests_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_my_timeoff_requests(self):
        """ Test that 201 is returned """

        data = {
            "start_date": "11-05-2021",
            "end_date": "12-05-2021",
            "is_paid": True,
            "orguser": orguser
        }

        res = my_account.Time.create_timelogs_my_timeoff_requests(team_pk, data)

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_timeoff_requests(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_timeoff_requests_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_timeoff_requests(self):
        """ Test that 201 is returned """

        data = {
            "start_date": "11-05-2021",
            "end_date": "12-05-2021",
            "is_paid": True,
            "orguser": orguser
        }

        res = my_account.Time.create_timelogs_timeoff_requests(team_pk, data)

        self.assertEqual(res['status'], 201)

    # def test_create_timeoff_balance_list(self):
    #     #! 200
    #     """ Test that 201 is returned """

    #     data = {
    #         "orguser": orguser,
    #         "start_date": "01-05-2021",
    #         "end_date": "10-05-2021"
    #     }

    #     res = my_account.Time.create_timeoff_balance_list(team_pk, data)
    #     print(res)

    #     self.assertEqual(res['status'], 201)

    # def test_create_timeoff_requests_action(self):
    #     #! 200
    #     """ Test that 201 is returned """

    #     data = {
    #         "orguser": orguser,
    #         "start_date": "01-05-2021",
    #         "end_date": "10-05-2021"
    #     }

    #     res = my_account.Time.create_timeoff_requests_action(team_pk, data)
    #     print(res)

    #     self.assertEqual(res['status'], 201)

    def test_get_timelogs_timeoff_requests_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_timeoff_requests()

        res = my_account.Time.get_timelogs_timeoff_requests_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_timelogs_timeoff_requests(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_timeoff_requests()

        data = {
            "start_date": "10-05-2021"
        }

        res = my_account.Time.update_timelogs_timeoff_requests(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_timelogs_timeoff_requests(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_timeoff_requests()

        res = my_account.Time.delete_timelogs_timeoff_requests(pk)

        self.assertEqual(res['status'], 204)

    ### Types ###

    def _create_timelogs_types_list_return_pk(self):
        """ Create timelogs type and return pk """

        data = {
            "name": "UNITTEST"
        }

        return my_account.Time.create_timelogs_types_list(data)['data']['id']

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_types_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_types_list()

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_types_list(self):
        """ Test that 201 is returned """

        data = {
            "name": "UNITTEST"
        }

        res = my_account.Time.create_timelogs_types_list(data)

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_types_timeoff_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_types_timeoff_list()

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_types_timeoff(self):
        """ Test that 201 is returned """

        data = {
            "name": "UNITTEST"
        }

        res = my_account.Time.create_timelogs_types_timeoff(data)

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_types_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_types_list_return_pk()

        res = my_account.Time.get_timelogs_types_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_timelogs_types(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_types_list_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Time.update_timelogs_types(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_timelogs_types(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_types_list_return_pk()

        res = my_account.Time.delete_timelogs_types(pk)

        self.assertEqual(res['status'], 204)

    ### Week-config ###
    def _create_timelogs_week_config_return_pk(self):
        """ Create timelogs week config and return pk """

        data = {
            "team": team_pk,
            "name": "UNITTEST",
            "orgusers": [orguser]
        }

        return my_account.Time.create_timelogs_week_config(data)['data']['id']

    def test_get_timelogs_week_config_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_week_config_list()

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_week_config(self):
        """ Test that 201 is returned """

        data = {
            "team": team_pk,
            "name": "UNITTEST",
            "orgusers": [orguser]
        }

        res = my_account.Time.create_timelogs_week_config(data)

        self.assertEqual(res['status'], 201)

    def test_get_timelogs_week_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_week_config_return_pk()

        res = my_account.Time.get_timelogs_week_config_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_timelogs_week_config(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_week_config_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Time.update_timelogs_week_config(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_timelogs_week_config(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_week_config_return_pk()
        res = my_account.Time.delete_timelogs_week_config(pk)

        self.assertEqual(res['status'], 204)

    ### Weeks ####

    # def test_get_timelogs_week_away(self):
    #! Do not pass : 404
    #     """ Test that 200 is returned """

    #     res = my_account.Time.get_timelogs_week_away()

    #     self.assertEqual(res['status'], 200)

    def test_get_timelogs_week_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_week_list()

        self.assertEqual(res['status'], 200)

    def test_get_timelogs_week_details(self):
        """ Test that 200 is returned """

        pk = res = my_account.Time.get_timelogs_week_list("03-05-2021")['data'][0]['id']
        res = my_account.Time.get_timelogs_week_details(pk)

        self.assertEqual(res['status'], 200)

    def update_timelogs_week(self):
        """ Test that 200 is returned """

        pk = res = my_account.Time.get_timelogs_week_list("03-05-2021")['data'][0]['id']

        data = {
            "team": team_pk
        }

        res = my_account.Time.update_timelogs_week(pk, data)

        self.assertEqual(res['status'], 200)

    ### Worklogs ###
    def _create_timelogs_worklogs_return_pk(self):
        """ Create worklogs and return pk """

        data = {
            "description": "string",
            "is_imported": True,
            "cost": 0,
            "base_cost": 0,
            "date": "05-05-2021"
        }

        return my_account.Time.create_timelogs_worklogs(team_pk, data)['data']['id']

    def test_get_timelogs_worklogs_list(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timelogs_worklogs_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_timelogs_worklogs_list(self):
        """ Test that 200 or 201 is returned """

        data = {
            "description": "string",
            "is_imported": True,
            "cost": 0,
            "base_cost": 0,
            "date": "09-05-2021"
        }

        res = my_account.Time.create_timelogs_worklogs(team_pk, data)

        self.assertIn(res['status'], [201, 200])

    def test_get_timelogs_worklogs_details(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_worklogs_return_pk()
        res = my_account.Time.get_timelogs_worklogs_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_timelogs_worklogs_list(self):
        """ Test that 200 is returned """

        pk = self._create_timelogs_worklogs_return_pk()

        data = {
            "cost": 1
        }

        res = my_account.Time.update_timelogs_worklogs(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_timelogs_worklogs(self):
        """ Test that 204 is returned """

        pk = self._create_timelogs_worklogs_return_pk()
        res = my_account.Time.delete_timelogs_worklogs(pk)

        self.assertEqual(res['status'], 204)

    #### Timeperiods ####
    def _create_annexe_return_pk(self):
        """ Create annexe and return pk """

        data = {
            "title": "UNITTEST",
            "annex_type": "time",
            "total_fees": 1,
            "description": "UNITTEST",
            "date": "06-05-2021"
        }

        return my_account.Deliverables.create_annexe(project_pk, data)['data']['id']

    def _create_role_annex_period_return_pk(self):
        """ Create role annex period and return pk """

        pk_annex = self._create_annexe_return_pk()

        data = {
            "orgusers": [
                orguser
            ],
            "annex": pk_annex
        }

        return my_account.Time.create_timeperiods_role_annex_periods(data)['data']['pk']

    def _create_user_period_return_pk(self):
        """ Create user period and return pk """

        data = {
            "orguser": orguser,
            "team": team_pk,
            "project": project_pk,
            "description": "string",
        }

        return my_account.Time.create_user_period_list(data)['data']['pk']

    def test_get_timeperiods_dashboard_scheduling_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timeperiods_dashboard_scheduling_timeline()

        self.assertEqual(res['status'], 200)

    # def test_get_timeperiods_resource_planning_timeline(self):
    #     #! 500
    #     """ Test that 200 is returned """

    #     res = my_account.Time.get_timeperiods_resource_planning_timeline()

    #     self.assertEqual(res['status'], 200)

    # def test_create_timeperiods_resource_planning_timeline(self):
    #     #! 403
    #     """ Test that 201 is returned """

    #     res = my_account.Time.create_timeperiods_resource_planning_timeline()

    #     self.assertEqual(res['status'], 201)

    def test_get_timeperiods_resources_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timeperiods_resources_timeline(project_pk)

        self.assertEqual(res['status'], 200)

    # def test_get_timeperiods_role_annex_periods(self):
    #     """ Test that 200 is returned """
    #     #! 403

    #     res = my_account.Time.get_timeperiods_role_annex_periods()

    #     self.assertEqual(res['status'], 200)

    def test_create_timeperiods_role_annex_periods(self):
        """ Test that 201 is returned """

        pk_annex = self._create_annexe_return_pk()

        data = {
            "orgusers": [
                orguser
            ],
            "annex": pk_annex
        }

        res = my_account.Time.create_timeperiods_role_annex_periods(data)

        self.assertEqual(res['status'], 201)

    def test_get_timeperiods_role_annex_period_details(self):
        """ Test that 200 is returned """

        pk_role_annex_period = self._create_role_annex_period_return_pk()

        res = my_account.Time.get_timeperiods_role_annex_period_details(pk_role_annex_period)

        self.assertEqual(res['status'], 200)

    def test_update_timeperiods_role_annex_period(self):
        """ Test that 200 is returned """

        pk = self._create_role_annex_period_return_pk()

        data = {
            "budget_pct": 1
        }

        res = my_account.Time.update_timeperiods_role_annex_period(pk, data)

        self.assertEqual(res['status'], 200)

    # def test_delete_timeperiods_role_annex_period(self):
    #     #! 500
    #     """ Test that 204 is returned """

    #     pk = self._create_role_annex_period_return_pk()

    #     res = my_account.Time.delete_timeperiods_role_annex_period(pk)
    #     self.assertEqual(res['status'], 204)

    # def test_create_timeperiods_scheduling_timeline_actions(self):
    #     #! 200 no body
    #     """ Test that 201 is returned """

    #     res = my_account.Time.create_timeperiods_scheduling_timeline_actions(project_pk)

    #     self.assertEqual(res['status'], 201)

    def test_get_timeperiods_scheduling_timeline_actions(self):
        """ Test that 200 is returned """

        res = my_account.Time.get_timeperiods_scheduling_timeline_actions(project_pk)

        self.assertEqual(res['status'], 200)

    # def test_create_user_period_action(self):
    #     #! 200 no body
    #     """ Test that 201 is returned """

    #     res = my_account.Time.create_user_period_action()

    #     self.assertEqual(res['status'], 201)

    # def test_get_user_period_list(self):
    #     #! 403
    #     """ Test that 200 is returned """

    #     res = my_account.Time.get_user_period_list()

    #     self.assertEqual(res['status'], 200)

    def test_create_user_period_list(self):
        """ Test that 201 is returned """

        data = {
            "orguser": orguser,
            "team": team_pk,
            "project": project_pk,
            "description": "string",
        }

        res = my_account.Time.create_user_period_list(data)

        self.assertEqual(res['status'], 201)

    def test_get_user_period_details(self):
        """ Test that 200 is returned """

        pk = self._create_user_period_return_pk()

        res = my_account.Time.get_user_period_details(pk)

        self.assertEqual(res['status'], 200)

    # def test_update_user_period_list(self):
    #     #! 500
    #     """ Test that 200 is returned """

    #     pk = self._create_user_period_return_pk()

    #     data = {
    #         "description": "UPDATED"
    #     }

    #     res = my_account.Time.update_user_period_list(pk, data)

    #     self.assertEqual(res['status'], 200)

    # def test_delete_user_period(self):
    #     #! 500
    #     """ Test that 204 is returned """

    #     pk = self._create_user_period_return_pk()

    #     res = my_account.Time.delete_user_period(pk)

    #     self.assertEqual(res['status'], 204)

    # def test_get_users_scheduling_timeline(self):
    #     #! 500
    #     """ Test that 200 is returned """

    #     res = my_account.Time.get_users_scheduling_timeline()

    #     self.assertEqual(res['status'], 200)


if __name__ == '__main__':
    unittest.main()
