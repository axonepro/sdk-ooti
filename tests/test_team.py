import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import OrguserFactory, ProjectFactory, TeamFactory
from requests.api import delete

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

""" Not cleanup yet
class TestTeam(unittest.TestCase):
    def test_get_teams_list(self):
        response = sdk.get_teams_list()
        self.assertEqual(response['status'], 200)

    def test_get_team_users_list(self):
        response = sdk.get_team_users_list(1689)
        self.assertEqual(response['status'], 200)

    def test_get_team_user_details(self):
        response = sdk.get_team_user_details(5042)
        self.assertEqual(response['status'], 200)

    def test_update_team_user_details(self):
        payload = {
            "permissionsset": 16464,
            "team": 1689
        }
        response = sdk.update_team_user_details(5042, payload)
        self.assertEqual(response['status'], 200)

    def test_get_team_details(self):
        response = sdk.get_team_details(1689)
        self.assertEqual(response['status'], 200)

    def test_update_team_details(self):
        payload = {
            "city": "Lyon",
            "address": "14 Avenue de France"
        }
        response = sdk.update_team_details(1689, payload)
        self.assertEqual(response['status'], 200)

    def test_create_team(self):
        payload = {
            "name": "Beta"
        }
        response = sdk.create_team(payload)
        self.assertEqual(response['status'], 201)

    def test_add_team_user(self):

        payload = {
            "orguser": 5042,
            "role": 6487,
            "permissionsset": 16462
        }
        response = sdk.add_team_user(3237, payload)
        self.assertEqual(response['status'], 201)

    def test_add_team_user_to_multiple_projects(self):

        payload = {
            "orguser": 11585,
            "teams": [
                1689
            ],
            "projects": [
                11702,
                11678,
                11707
            ]
        }
        response = sdk.add_team_user_to_multiple_projects(payload)
        self.assertEqual(response['status'], 201)

    def test_delete_team_user_to_multiple_projects(self):

        payload = {
            "orguser": 11585,
            "projects": [
                11702,
                11678,
                11707
            ]
        }
        response = sdk.remove_team_user_to_multiple_projects(payload)
        self.assertEqual(response['status'], 204)
"""

if __name__ == '__main__':
    unittest.main()