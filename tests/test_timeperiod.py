import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import OrguserPkFactory, TeamFactory
from test_helper import HelperTest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

orguser = OrguserPkFactory(my_account.org_pk)
week_pk = my_account.Timelogs.get_timelogs_week_list()['data'][0]['id']
res = my_account.Orgusers.update_orguser_details(orguser, {'trips_enabled': True})
print(res.get('status'))

class TestTimeperiods(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.orguser_pk = OrguserPkFactory(my_account.org_pk)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

        cls.annex_pk = cls.testHelper._create_annex_return_pk(cls.project_pk)

    def test_get_timeperiods_dashboard_scheduling_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_timeperiods_dashboard_scheduling_timeline()
        self.assertEqual(res['status'], 200)

    def test_get_timeperiods_resource_planning_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_timeperiods_resource_planning_timeline()
        self.assertEqual(res['status'], 200)

    def test_create_timeperiods_resource_planning_timeline(self):
        """ Test that 200 is returned """

        data = {
            "team": self.team_pk
        }

        res = my_account.Timeperiods.create_timeperiods_resource_planning_timeline(data)
        self.assertEqual(res['status'], 200)

    def test_get_timeperiods_resources_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_timeperiods_resources_timeline(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_timeperiods_scheduling_timeline_actions(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.create_timeperiods_scheduling_timeline_actions(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_get_timeperiods_scheduling_timeline_actions(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_timeperiods_scheduling_timeline_actions(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_user_period_action(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.create_user_period_action()
        self.assertEqual(res['status'], 200)

    def test_get_user_period_list(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_user_period_list(self.team_pk)
        self.assertEqual(res['status'], 200)

    def test_create_user_period_list(self):
        """ Test that 201 is returned """

        data = {
            "orguser": self.orguser_pk,
            "team": self.team_pk,
            "project": self.project_pk,
            "description": "string",
        }

        res = my_account.Timeperiods.create_user_period_list(data)
        self.assertEqual(res['status'], 201)

    def test_get_user_period_details(self):
        """ Test that 200 is returned """

        user_period_pk = self.testHelper._create_user_period_return_pk(self.orguser_pk, self.team_pk, self.project_pk)
        res = my_account.Timeperiods.get_user_period_details(user_period_pk)
        self.assertEqual(res['status'], 200)

    def test_update_user_period_list(self):
        """ Test that 200 is returned """

        data = {
            "description": "UPDATED"
        }

        user_period_pk = self.testHelper._create_user_period_return_pk(self.orguser_pk, self.team_pk, self.project_pk)
        res = my_account.Timeperiods.update_user_period_list(user_period_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_user_period(self):
        """ Test that 204 is returned """

        user_period_pk = self.testHelper._create_user_period_return_pk(self.orguser_pk, self.team_pk, self.project_pk)
        res = my_account.Timeperiods.delete_user_period(user_period_pk)
        self.assertEqual(res['status'], 204)

    def test_get_users_scheduling_timeline(self):
        """ Test that 200 is returned """

        res = my_account.Timeperiods.get_users_scheduling_timeline()
        self.assertEqual(res['status'], 200)

    @classmethod
    def tearDown(cls):
        my_account.Annexes.delete_annexe(cls.annex_pk)

if __name__ == '__main__':
    unittest.main()