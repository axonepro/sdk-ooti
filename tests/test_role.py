import os
import unittest

from factories.factories import OrguserPkFactory, TeamFactory
from test_helper import HelperTest
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()["data"][0]["pk"]
project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]

orguser = OrguserPkFactory(my_account.org_pk)
week_pk = my_account.Timelogs.get_timelogs_week_list()["data"][0]["id"]
res = my_account.Orgusers.update_orguser_details(orguser, {"trips_enabled": True})


class TestRoles(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.orguser_pk = OrguserPkFactory(my_account.org_pk)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]

        cls.role_pk = cls.testHelper._create_roles_return_pk()
        cls.project_role_pk = cls.testHelper._create_roles_project_return_pk(
            cls.project_pk, cls.role_pk
        )

    def test_get_roles_list(self):
        """Test that 200 is returned"""

        res = my_account.Roles.get_roles_list()
        self.assertEqual(res["status"], 200)

    def test_create_roles(self):
        """Test that 201 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Roles.create_roles(data)
        self.assertEqual(res["status"], 201)

    def test_get_roles_project_list(self):
        """Test that 200 is returned"""

        res = my_account.Roles.get_roles_project_list()
        self.assertEqual(res["status"], 200)

    def test_create_roles_project(self):
        """Test that 201 is returned"""

        data = {
            "project": self.project_pk,
            "billable_per_hour": 1,
            "role": self.role_pk,
        }

        res = my_account.Roles.create_roles_project(data)
        self.assertEqual(res["status"], 201)

    def test_get_roles_project_details(self):
        """Test that 200 is returned"""

        res = my_account.Roles.get_roles_project_details(self.project_role_pk)
        self.assertEqual(res["status"], 200)

    def test_update_roles_project(self):
        """Test that 200 is returned"""

        data = {"billable_per_hour": 2}

        res = my_account.Roles.update_roles_project(self.project_role_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_roles_project(self):
        """Test that 204 is returned"""

        res = my_account.Roles.delete_roles_project(self.project_role_pk)
        self.assertEqual(res["status"], 204)

    def test_create_bulk_action_add_roles(self):
        """Test that 201 is returned"""

        res = my_account.Roles.create_bulk_action_add_roles(self.project_pk)
        self.assertEqual(res["status"], 201)

    def test_delete_bulk_action_add_roles(self):
        """Test that 204 is returned"""

        res = my_account.Roles.delete_bulk_action_add_roles(self.project_pk)
        self.assertEqual(res["status"], 204)

    def test_get_roles_details(self):
        """Test that 200 is returned"""

        res = my_account.Roles.get_roles_details(self.role_pk)
        self.assertEqual(res["status"], 200)

    def test_update_roles(self):
        """Test that 200 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Roles.update_roles(self.role_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_roles(self):
        """Test that 204 is returned"""

        role_pk2 = self.testHelper._create_roles_return_pk()
        res = my_account.Roles.delete_roles(role_pk2)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Roles.delete_roles(cls.role_pk)
        my_account.Roles.delete_roles_project(cls.project_role_pk)


if __name__ == "__main__":
    unittest.main()
