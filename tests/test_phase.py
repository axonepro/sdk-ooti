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


class TestPhases(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(
            cls.project_pk
        )
        cls.phase_pk = cls.testHelper._create_phase_return_pk(
            cls.project_pk, cls.fee_project_pk
        )
        cls.plan_pk = cls.testHelper._create_plan_return_pk(cls.project_pk)

    def test_pagination(self):
        my_account.update_pagination(1)

        # phase_pk1 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)
        # phase_pk2 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)
        # phase_pk3 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)

        res = my_account.Phases.get_phases_list(self.project_pk)
        self.assertEqual(res["status"], 200)
        self.assertEqual(len(res["data"]), 1)
        obj = res["data"][0]

        res = my_account.Phases.get_phases_list(self.project_pk, page=2)
        self.assertEqual(res["status"], 200)
        self.assertEqual(len(res["data"]), 1)
        self.assertNotEqual(obj, res["data"][0])

        my_account.update_pagination(5)
        res = my_account.Phases.get_phases_list(self.project_pk)
        self.assertEqual(res["status"], 200)
        self.assertLessEqual(len(res["data"]), 5)

    def test_get_phases_list(self):
        """Test that 200 is returned"""

        res = my_account.Phases.get_phases_list(self.project_pk)
        self.assertEqual(res["status"], 200)

    def test_get_phases_list_fee_project(self):
        """Test that 200 is returned"""

        res = my_account.Phases.get_phases_list_fee_project(
            self.project_pk, self.fee_project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_get_phases_projections_list(self):
        """Test that 200 is returned"""

        res = my_account.Phases.get_phases_projections_list(self.project_pk)
        self.assertEqual(res["status"], 200)

    def test_export_phase(self):
        """Test that 200 is returned"""
        currency_pk = self.testHelper._create_currency_if_none()
        client_pk = self.testHelper._create_client_return_pk(team_pk, currency_pk)
        project_pk = self.testHelper._create_project_return_pk(client_pk, currency_pk)

        # fee_project_pk = self.testHelper._create_fee_project_return_pk(project_pk)
        # phase_pk = self.testHelper._create_phase_return_pk(project_pk, fee_project_pk)

        res = my_account.Phases.export_phase(project_pk)
        self.assertEqual(res["status"], 200)

    def test_create_phase(self):
        """Test that 201 is returned"""

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "fee_project": self.fee_project_pk,
            "pct": 10,
            "dependants": [],
        }

        res = my_account.Phases.create_phase(self.project_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_phase_details(self):
        """Test that 200 is returned"""

        res = my_account.Phases.get_phase_details(self.phase_pk)
        self.assertEqual(res["status"], 200)

    def test_update_phase(self):
        """Test that 200 is returned"""

        data = {"name": self.testHelper.create_name()}

        res = my_account.Phases.update_phase(self.phase_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_phase(self):
        """Test that 204 is returned"""

        res = my_account.Phases.delete_phase(self.phase_pk)
        self.assertEqual(res["status"], 204)

    def test_reset_phase_order(self):
        """Test that 200 is returned"""
        res = my_account.Phases.reset_phases_order(self.project_pk)

        self.assertEqual(res["status"], 200)

    def test_get_phase_planphase_details(self):
        """Test that 200 is returned"""

        planphase_pk = my_account.Plans.get_plan_details(self.plan_pk)["data"][
            "plan_phases"
        ][0]["id"]
        res = my_account.Phases.get_phase_planphase_details(planphase_pk)

        self.assertEqual(res["status"], 200)

    def test_update_phase_planphase(self):
        """Test that 200 is returned"""

        planphase_pk = my_account.Plans.get_plan_details(self.plan_pk)["data"][
            "plan_phases"
        ][0]["id"]

        data = {"progress": 20}

        res = my_account.Phases.update_phase_planphase(planphase_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_phase_planphase(self):
        """Test that 204 is returned"""

        planphase_pk = my_account.Plans.get_plan_details(self.plan_pk)["data"][
            "plan_phases"
        ][0]["id"]

        res = my_account.Phases.delete_phase_planphase(planphase_pk)

        my_account.Plans.delete_plan(self.plan_pk)
        self.assertEqual(res["status"], 204)

    def test_update_phases_progress(self):
        """Test that 200 is returned"""

        res = my_account.Phases.update_phases_progress()
        self.assertEqual(res["status"], 200)

    @classmethod
    def tearDown(cls):
        my_account.Fees.delete_fee_project(cls.fee_project_pk)
        my_account.Phases.delete_phase(cls.phase_pk)
        my_account.Plans.delete_plan(cls.plan_pk)


if __name__ == "__main__":
    unittest.main()
