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
"""project_pk = my_account.Projects.get_projects_list()['data'][0]['id']
fee_project = my_account.Fees.get_fees_project_list_projects(project_pk)['data'][0]['id']"""


class TestAnnexes(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.client_pk = cls.testHelper._create_client_return_pk(team_pk, currency_pk)
        cls.project_pk = cls.testHelper._create_project_return_pk(
            cls.client_pk, cls.currency_pk
        )
        cls.annex_pk = cls.testHelper._create_annex_return_pk(cls.project_pk)

    ### Plans ### noqa: E266
    ### Annexes #### noqa: E266

    def test_get_annexes_list(self):
        """Test that 200 is returned"""

        res = my_account.Annexes.get_annexes_list(self.project_pk)
        self.assertEqual(res["status"], 200)

    def test_create_annexe(self):
        """Test that 201 is returned"""

        data = {
            "title": self.testHelper.create_name(),
            "annex_type": "time",
            "total_fees": 1,
            "description": "UNITTEST",
            "start_date": "06-05-2021",
        }

        res = my_account.Annexes.create_annexe(self.project_pk, data)
        self.assertEqual(res["status"], 201)

    def test_get_annexe_details(self):
        """Test that 200 is returned"""

        res = my_account.Annexes.get_annexe_details(self.annex_pk)
        self.assertEqual(res["status"], 200)

    def test_update_annexe(self):
        """Test that 200 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Annexes.update_annexe(self.annex_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_annexe(self):
        """Test that 204 is returned"""

        res = my_account.Annexes.delete_annexe(self.annex_pk)
        self.assertEqual(res["status"], 204)

    def test_get_annexes_projections_list(self):
        """Test that 200 is returned"""

        res = my_account.Annexes.get_annexes_projections_list(self.project_pk)
        self.assertEqual(res["status"], 200)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)
        my_account.Clients.delete_client(cls.client_pk)
        my_account.Projects.delete_project(cls.project_pk)
        my_account.Annexes.delete_annexe(cls.annex_pk)


if __name__ == "__main__":
    unittest.main()
