import os
import unittest

from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestProfile(unittest.TestCase):
    def test_get_profile_preferences(self):
        response = sdk.Profiles.get_profile_preferences()
        self.assertEqual(response["status"], 200)

    def test_get_profile_details(self):
        response = sdk.Profiles.get_profile_details()
        self.assertEqual(response["status"], 200)

    def test_update_profile_details(self):
        payload = {"locale": "en"}
        response = sdk.Profiles.update_profile_details(payload)
        self.assertEqual(response["status"], 200)


if __name__ == "__main__":
    unittest.main()
