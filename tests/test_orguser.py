import os
import time
import unittest

from factories.factories import OrguserFactory, ProjectFactory, TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestOrguser(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()["id"]
        cls.orguser_pk = OrguserFactory()["pk"]

    def test_get_orguser_details(self):
        response = sdk.Orgusers.get_orguser_details(self.orguser_pk)
        self.assertEqual(response["status"], 200)

    def test_get_orgusers_list(self):
        response = sdk.Orgusers.get_orgusers_list()
        self.assertEqual(response["status"], 200)

    def test_export_orgusers_list(self):
        response = sdk.Orgusers.export_orgusers_list()
        self.assertEqual(response["status"], 200)

    def test_create_orguser(self):  # Error 500
        response = sdk.Orgusers.create_orguser({
            "email": f"test{int(time.time() * 1000)}@test.fr",
            "first_name": "Julie",
            "last_name": "TEST",
        })
        self.assertEqual(response["status"], 201)
        delete = sdk.Orgusers.delete_orguser(response["data"]["pk"])
        self.assertEqual(delete["status"], 204)

    def test_update_orguser_details(self):
        payload = {"mobile": "0777777777", "birthday": "28-06-1989"}

        response = sdk.Orgusers.update_orguser_details(self.orguser_pk, payload)
        self.assertEqual(response["status"], 200)

    def test_invite_orguser(self):

        response = sdk.Orgusers.invite_orguser(self.orguser_pk, self.team_pk)
        self.assertEqual(response["status"], 200)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)
        sdk.Orgusers.delete_orguser(cls.orguser_pk)


if __name__ == "__main__":
    unittest.main()
