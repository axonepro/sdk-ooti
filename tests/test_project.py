import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import OrguserFactory, ProjectFactory, TeamFactory
from requests.api import delete

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

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestProject(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()["id"]
        cls.orguser_pk = OrguserFactory()["pk"]

    def test_get_project_details(self):
        response = sdk.Projects.get_project_details(self.project_id)
        self.assertEqual(response["status"], 200)

    def test_get_projects_list(self):
        response = sdk.Projects.get_projects_list()
        self.assertEqual(response["status"], 200)

    def test_export_projects_list(self):
        response = sdk.Projects.export_projects_list()
        self.assertEqual(response["status"], 200)

    def test_create_project(self):
        payload = {
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [self.orguser_pk],
            "city": "Paris",
            "country": "FR",
        }
        response = sdk.Projects.create_project(payload)
        self.assertEqual(response["status"], 400)
        payload = {
            "project_title": "New project",
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [self.orguser_pk],
            "city": "Paris",
            "country": "FR",
        }
        response = sdk.Projects.create_project(payload)
        self.assertEqual(response["status"], 201)

    def test_update_project_details(self):

        payload = {"surface_area": 730}
        response = sdk.Projects.update_project_details(self.project_id, payload)
        self.assertEqual(response["status"], 200)

    def test_get_project_fee_summary(self):

        response = sdk.Projects.get_project_fee_summary(self.project_id)
        self.assertEqual(response["status"], 200)

    def test_get_projects_list_deliverables(self):

        response = sdk.Projects.get_projects_list_deliverables()
        self.assertEqual(response["status"], 200)

    def test_get_project_available_clients(self):

        response = sdk.Projects.get_project_available_clients(self.project_id)
        self.assertEqual(response["status"], 200)

    def test_get_project_users_list(self):

        response = sdk.Projects.get_project_users_list(self.project_id)
        self.assertEqual(response["status"], 200)

    def test_add_project_user(self):
        payload = {
            "orguser": self.orguser_pk,
            "project": self.project_id,
            "is_visible": True,
        }
        response = sdk.Projects.add_project_user(self.project_id, payload)
        project_user_pk = response["data"]["pk"]
        self.assertEqual(response["status"], 201)
        payload = {"is_billable": True}
        update = sdk.Projects.update_project_user_details(project_user_pk, payload)
        self.assertEqual(update["status"], 200)
        delete = sdk.Projects.delete_project_user(project_user_pk)
        self.assertEqual(delete["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)
        sdk.Orgusers.delete_orguser(cls.orguser_pk)


if __name__ == "__main__":
    unittest.main()
