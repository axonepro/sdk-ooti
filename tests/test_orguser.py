from requests.api import delete
from factories.factories import OrguserFactory, ProjectFactory, TeamFactory
import unittest
import os
import sys
from dotenv import load_dotenv

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti # noqa E402


# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

class TestOrguser(unittest.TestCase):
    @ classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()['id']
        cls.orguser_pk = OrguserFactory()['pk']

    def test_get_orguser_details(self):
        response = sdk.Orgusers.get_orguser_details(self.orguser_pk)
        self.assertEqual(response['status'], 200)

    def test_get_orgusers_list(self):
        response = sdk.Orgusers.get_orgusers_list()
        self.assertEqual(response['status'], 200)

    def test_export_orgusers_list(self):
        response = sdk.Orgusers.export_orgusers_list()
        self.assertEqual(response['status'], 200)

    def test_create_orguser(self):  # Error 500
        payload = {
            "email": "test13@test.fr",
            "first_name": "Julie",
            "last_name": "TEST",
        }
        response = sdk.Orgusers.create_orguser(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Orgusers.delete_orguser(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_update_orguser_details(self):
        payload = {
            "mobile": "0777777777",
            "birthday": "28-06-1989"
        }

        response = sdk.Orgusers.update_orguser_details(self.orguser_pk, payload)
        self.assertEqual(response['status'], 200)

    def test_invite_orguser(self):

        response = sdk.Orgusers.invite_orguser(self.orguser_pk, self.team_pk)
        self.assertEqual(response['status'], 200)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)
        sdk.Orgusers.delete_orguser(cls.orguser_pk)

if __name__ == '__main__':
    unittest.main()