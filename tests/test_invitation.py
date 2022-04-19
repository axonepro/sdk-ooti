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
class TestInvitation(unittest.TestCase):
    def test_get_invitations_list(self):
        response = sdk.get_invitations_list()
        self.assertEqual(response['status'], 200)

    def test_get_team_invitations_list(self):
        response = sdk.get_team_invitations_list(1689)
        self.assertEqual(response['status'], 200)

    def test_get_invitation_details(self):
        response = sdk.get_invitation_details(71)
        self.assertEqual(response['status'], 200)

    def test_create_invitation(self):
        payload = {
            "team": 1689,
            "invitor": 5042,
            "invitee": 9868,
            "email": "test@mail.com",
        }
        response = sdk.create_invitation(0, payload)
        self.assertEqual(response['status'], 201)

    def test_update_invitation(self):
        payload = {
            "email": "mailchanged@mail.com"
        }
        response = sdk.update_invitation_details(71, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_invitation(self):
        response = sdk.delete_invitation(71)
        self.assertEqual(response['status'], 204)
"""

if __name__ == '__main__':
    unittest.main()