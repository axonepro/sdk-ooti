from requests.api import delete
from factories.factories import OrguserFactory, ProjectFactory, TeamFactory
import unittest
import os
import sys
from dotenv import load_dotenv

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ooti import ooti # noqa E402


# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

""" Not cleanup yet
class TestPermissions(unittest.TestCase):
    def test_get_permissions_list(self):
        response = sdk.get_permissions_list()
        self.assertEqual(response['status'], 200)

    def test_get_permissions_details(self):
        response = sdk.get_permissions_details(16466)
        self.assertEqual(response['status'], 200)

    def test_get_permissions_map(self):
        response = sdk.get_permissions_map()
        self.assertEqual(response['status'], 200)

    def test_create_permissions(self):
        payload = {
            "name": "Lead Architect",
            "name_en": "Lead Architect",
            "name_fr": "Architecte en chef",
            "level": "project",
            "all_permissions": True
        }
        response = sdk.create_permissions(payload)
        self.assertEqual(response['status'], 201)

    def test_update_permissions_details(self):
        payload = {
            "name_fr": "Membre d'équipe",
            "all_permissions": True
        }
        response = sdk.update_permissions_details(16459, payload)
        return self.assertEqual(response['status'], 200)

    def test_delete_permissions(self):
        response = sdk.delete_permissions(35750)
        self.assertEqual(response['status'], 204)
"""

if __name__ == '__main__':
    unittest.main()