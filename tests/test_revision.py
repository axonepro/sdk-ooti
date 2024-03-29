import os
import unittest

from factories.factories import TeamFactory
from test_helper import HelperTest
from resources import ooti

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


class TestRevisions(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(
            cls.project_pk
        )

        cls.annex_pk = cls.testHelper._create_annex_return_pk(cls.project_pk)
        cls.document_pk = cls.testHelper._create_document_return_pk(cls.project_pk)
        cls.fee_pk = cls.testHelper._create_fee_return_pk(cls.project_pk)
        cls.phase_pk = cls.testHelper._create_phase_return_pk(
            cls.project_pk, cls.fee_project_pk
        )
        cls.plan_pk = cls.testHelper._create_plan_return_pk(cls.project_pk)

    def test_get_revisions_annexes_team_project(self):
        """Test that 200 is returned"""

        res = my_account.Revisions.get_revisions_annexes_team_project(
            self.team_pk, self.project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_create_annex_revision(self):
        """Test that 201 is returned"""

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": self.annex_pk,
            "progress": 80,
        }

        res = my_account.Revisions.create_annexe_revision(
            self.team_pk, self.project_pk, data
        )
        self.assertEqual(res["status"], 201)

    def test_delete_annex_revision(self):
        """Test that 201 is returned"""

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": self.annex_pk,
            "progress": 80,
        }

        pk = my_account.Revisions.create_annexe_revision(
            self.team_pk, self.project_pk, data
        )["data"]["id"]
        res = my_account.Revisions.delete_revisions_annexe_detail(pk)

        self.assertEqual(res["status"], 204)

    def test_get_revisions_documents_team_project(self):
        """Test that 200 is returned"""

        res = my_account.Revisions.get_revisions_documents_team_project(
            self.team_pk, self.project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_create_document_revision(self):
        """Test that 201 is returned"""

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": self.document_pk,
            "progress": 80,
        }

        res = my_account.Revisions.create_document_revision(
            self.team_pk, self.project_pk, data
        )
        self.assertEqual(res["status"], 201)

    def test_delete_document_revision(self):
        """Test that 204 is returned"""

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": self.document_pk,
            "progress": 80,
        }

        pk = my_account.Revisions.create_document_revision(
            self.team_pk, self.project_pk, data
        )["data"]["id"]
        res = my_account.Revisions.delete_revisions_document_detail(pk)

        self.assertEqual(res["status"], 204)

    def test_get_revisions_fee_items_team_project(self):
        """Test that 200 is returned"""

        res = my_account.Revisions.get_revisions_fee_items_team_project(
            self.team_pk, self.project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_create_fee_items_revision(self):
        """Test that 201 is returned"""

        data = {
            "fee_item": self.fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Revisions.create_fee_items_revision(
            self.team_pk, self.project_pk, data
        )
        self.assertEqual(res["status"], 201)

    def test_delete_fee_items_revision(self):
        """Test that 204 is returned"""

        data = {
            "fee_item": self.fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Revisions.create_fee_items_revision(
            self.team_pk, self.project_pk, data
        )
        res = my_account.Revisions.delete_revisions_fee_items_detail(pk["data"]["id"])
        self.assertEqual(res["status"], 204)

    def test_get_revisions_phases_team_project(self):
        """Test that 200 is returned"""

        res = my_account.Revisions.get_revisions_phases_team_project(
            self.team_pk, self.project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_create_phases_revision(self):
        """Test that 201 is returned"""

        data = {
            "phase": self.phase_pk,
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Revisions.create_phase_revision(
            self.team_pk, self.project_pk, data
        )
        self.assertEqual(res["status"], 201)

    def test_delete_phase_revision(self):
        """Test that 204 is returned"""

        data = {
            "phase": self.phase_pk,
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Revisions.create_phase_revision(
            self.team_pk, self.project_pk, data
        )["data"]["id"]
        res = my_account.Revisions.delete_revisions_phases_detail(pk)

        self.assertEqual(res["status"], 204)

    def test_get_revisions_plans_team_project(self):
        """Test that 200 is returned"""

        res = my_account.Revisions.get_revisions_plans_team_project(
            self.team_pk, self.project_pk
        )
        self.assertEqual(res["status"], 200)

    def test_create_plan_revision(self):
        """Test that 201 is returned"""

        planphase_pk = my_account.Plans.get_plan_details(self.plan_pk)["data"][
            "plan_phases"
        ][0]["id"]

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80,
        }

        res = my_account.Revisions.create_plan_revision(
            self.team_pk, self.project_pk, data
        )
        self.assertEqual(res["status"], 201)

    def test_delete_plan_revision(self):
        """Test that 204 is returned"""

        planphase_pk = my_account.Plans.get_plan_details(self.plan_pk)["data"][
            "plan_phases"
        ][0]["id"]

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80,
        }

        pk = my_account.Revisions.create_plan_revision(
            self.team_pk, self.project_pk, data
        )["data"]["id"]
        res = my_account.Revisions.delete_revisions_plan_detail(pk)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Fees.delete_fee_project(cls.fee_project_pk)
        my_account.Annexes.delete_annexe(cls.annex_pk)
        my_account.Documents.delete_document(cls.document_pk)
        my_account.Fees.delete_fee(cls.fee_pk)
        my_account.Phases.delete_phase(cls.phase_pk)
        my_account.Plans.delete_plan(cls.plan_pk)


if __name__ == "__main__":
    unittest.main()
