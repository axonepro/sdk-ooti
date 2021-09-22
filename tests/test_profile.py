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

class TestProfile(unittest.TestCase):
    def test_get_profile_preferences(self):
        response = sdk.Profiles.get_profile_preferences()
        self.assertEqual(response['status'], 200)

    def test_get_profile_details(self):
        response = sdk.Profiles.get_profile_details()
        self.assertEqual(response['status'], 200)

    def test_update_profile_details(self):
        payload = {
            "locale": "en"
        }
        response = sdk.Profiles.update_profile_details(payload)
        self.assertEqual(response['status'], 200)

if __name__ == '__main__':
    unittest.main()