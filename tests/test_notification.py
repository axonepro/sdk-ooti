# To read .env variables
import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import (
    AlbumFactory,
    OrguserFactory,
    PostFactory,
    ProjectFactory,
    TaskFactory,
    TeamFactory,
)

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


class TestNotifications(unittest.TestCase):
    def test_get_notifications_config(self):
        response = sdk.Notifications.get_notifications_config()
        self.assertEqual(response["status"], 200)

    def test_update_notifications_details(self):
        payload = {"weekday": 5, "daily_time": "19:00:00"}
        response = sdk.Notifications.update_notifications_config(payload)
        self.assertEqual(response["status"], 200)


if __name__ == "__main__":
    unittest.main()
