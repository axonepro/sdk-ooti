import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import TeamFactory
from test_helper import HelperTest

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()["data"][0]["pk"]
project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
fee_project = my_account.Fees.get_fees_project_list_projects(project_pk)["data"][0][
    "id"
]


class TestDefaults(unittest.TestCase):
    """
    test_duplicate_defaults_plan not working
    """

    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.client_pk = cls.testHelper._create_client_return_pk(team_pk, currency_pk)
        cls.project_pk = cls.testHelper._create_project_return_pk(
            cls.client_pk, cls.currency_pk
        )
        # cls.project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

        cls.area_pk = cls.testHelper._create_area_return_pk(cls.project_pk)
        cls.zone_pk = cls.testHelper._create_zone_return_pk(cls.area_pk)

        cls.phaseset_pk = cls.testHelper._create_phaseset_return_pk(cls.team_pk)
        cls.default_phase_pk = cls.testHelper._create_defaults_phase_return_pk(
            cls.team_pk, cls.phaseset_pk
        )
        cls.planset_pk = cls.testHelper._create_plansets_return_pk()
        cls.default_plan_pk = cls.testHelper._create_defaults_plan_return_pk(
            cls.planset_pk, cls.zone_pk
        )

    ## Phasesets ### #     # noqa: E266

    def test_apply_defaults_phasesets(self):
        """Test that 200 is returned"""

        data = {
            "library": self.phaseset_pk,
            "project": self.project_pk,
        }

        res = my_account.Defaults.apply_defaults_phasesets(data)
        self.assertEqual(res["status"], 200)

    def test_duplicate_defaults_phasesets(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.duplicate_defaults_phasesets(self.phaseset_pk)
        self.assertEqual(res["status"], 200)

    def test_get_defaults_phasesets_org_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phasesets_org_list()
        self.assertEqual(res["status"], 200)

    def test_create_defaults_phasesets_org(self):
        """Test that 201 is returned"""
        data = {
            "is_main": False,
            "title": self.testHelper.create_name(),
            "team": self.team_pk,
        }

        res = my_account.Defaults.create_defaults_phasesets_org(data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_phasesets_team_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phasesets_team_list(self.team_pk)
        self.assertEqual(res["status"], 200)

    def test_create_defaults_phasesets_team(self):
        """Test that 200 is returned"""

        data = {
            "is_main": False,
            "title": self.testHelper.create_name(),
        }

        res = my_account.Defaults.create_defaults_phasesets_team(self.team_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_phasesets_details(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phasesets_details(self.phaseset_pk)
        my_account.Defaults.delete_defaults_phasesets(self.phaseset_pk)

        self.assertEqual(res["status"], 200)

    def test_update_defaults_phasesets(self):
        """Test that 200 is returned"""

        data = {
            "title": self.testHelper.create_name(),
        }

        res = my_account.Defaults.update_defaults_phasesets(self.phaseset_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_defaults_phasesets(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.delete_defaults_phasesets(self.phaseset_pk)
        self.assertEqual(res["status"], 204)

    ### Phases #### noqa: E266

    def test_duplicate_defaults_phase(self):
        """Test that 201 is returned"""

        res = my_account.Defaults.duplicate_defaults_phase(self.default_phase_pk)

        my_account.Defaults.delete_defaults_phase(self.default_phase_pk)
        my_account.Defaults.delete_defaults_phasesets(self.phaseset_pk)

        self.assertEqual(res["status"], 200)

    def test_get_defaults_phase_org_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phase_org_list()
        self.assertEqual(res["status"], 200)

    def test_get_defaults_phase_team_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phase_team_list(self.team_pk)
        self.assertEqual(res["status"], 200)

    def test_create_defaults_phase_org(self):
        """Test that 201 is returned"""

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "pct": 10,
            "library": self.phaseset_pk,
            "team": self.team_pk,
        }

        res = my_account.Defaults.create_defaults_phase_org(data)

        self.assertEqual(res["status"], 201)

    def test_create_defaults_phase_team(self):
        """Test that 200 is returned"""

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "pct": 10,
            "library": self.phaseset_pk,
            "team": self.team_pk,
        }

        res = my_account.Defaults.create_defaults_phase_team(self.team_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_phase_details(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_phase_details(self.default_phase_pk)
        self.assertEqual(res["status"], 200)

    def test_update_defaults_phase(self):
        """Test that 200 is returned"""

        data = {"name": self.testHelper.create_name()}

        res = my_account.Defaults.update_defaults_phase(self.default_phase_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_defaults_phase(self):
        """Test that 204 is returned"""

        res = my_account.Defaults.delete_defaults_phase(self.default_phase_pk)

        self.assertEqual(res["status"], 204)

    ### Plansets #### noqa: E266

    def test_apply_defaults_plansets(self):
        """Test that 200 is returned"""

        data = {
            "library": self.planset_pk,
            "area": self.area_pk,
            "zone_pk": self.zone_pk,
        }

        res = my_account.Defaults.apply_defaults_plansets(data)
        self.assertEqual(res["status"], 200)

    def test_duplicate_defaults_plansets(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.duplicate_defaults_plansets(self.planset_pk)
        self.assertEqual(res["status"], 200)

    def test_get_defaults_plansets_org_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plansets_org_list()
        self.assertEqual(res["status"], 200)

    def test_create_defaults_plansets_org(self):
        """Test that 201 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Defaults.create_defaults_plansets_org(data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_plansets_team_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plansets_team_list(self.team_pk)
        self.assertEqual(res["status"], 200)

    def test_create_defaults_plansets_team(self):
        """Test that 201 is returned"""

        data = {"is_main": False, "title": self.testHelper.create_name()}

        res = my_account.Defaults.create_defaults_plansets_team(self.team_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_plansets_details(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plansets_details(self.planset_pk)
        self.assertEqual(res["status"], 200)

    def test_update_defaults_plansets(self):
        """Test that 200 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Defaults.update_defaults_plansets(self.planset_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_defaults_plansets(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.delete_defaults_plansets(self.planset_pk)
        self.assertEqual(res["status"], 204)

    ### Plans #### noqa: E266

    def test_duplicate_defaults_plan(self):
        """Test that 200 is returned"""
        # !500

        res = my_account.Defaults.duplicate_defaults_plan(self.default_plan_pk)
        self.assertEqual(res["status"], 200)

    def test_get_defaults_plan_org_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plans_org_list()
        self.assertEqual(res["status"], 200)

    def test_get_defaults_plan_team_list(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plans_team_list(self.team_pk)
        self.assertEqual(res["status"], 200)

    def test_create_defaults_plan_org(self):
        """Test that 201 is returned"""

        data = {
            "zone": self.zone_pk,
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": self.testHelper.create_name(),
            "library": self.planset_pk,
        }

        res = my_account.Defaults.create_defaults_plan_org(data)
        self.assertEqual(res["status"], 201)

    def test_create_defaults_plan_team(self):
        """Test that 201 is returned"""

        data = {
            "zone": self.zone_pk,
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": self.testHelper.create_name(),
            "library": self.planset_pk,
        }

        res = my_account.Defaults.create_defaults_plan_team(self.team_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_defaults_plan_details(self):
        """Test that 200 is returned"""

        res = my_account.Defaults.get_defaults_plan_details(self.default_plan_pk)
        self.assertEqual(res["status"], 200)

    def test_update_defaults_plan(self):
        """Test that 200 is returned"""

        data = {"name": self.testHelper.create_name()}

        res = my_account.Defaults.update_defaults_plan(self.default_plan_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_defaults_plan(self):
        """Test that 204 is returned"""

        res = my_account.Defaults.delete_defaults_plan(self.default_plan_pk)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)
        my_account.Clients.delete_client(cls.client_pk)
        my_account.Projects.delete_project(cls.project_pk)
        my_account.Areas.delete_area(cls.area_pk)
        my_account.Zones.delete_zone(cls.zone_pk)
        my_account.Defaults.delete_defaults_phasesets(cls.phaseset_pk)
        my_account.Defaults.delete_defaults_phase(cls.default_phase_pk)
        my_account.Defaults.delete_defaults_plansets(cls.planset_pk)
        my_account.Defaults.delete_defaults_plan(cls.default_plan_pk)


if __name__ == "__main__":
    unittest.main()
