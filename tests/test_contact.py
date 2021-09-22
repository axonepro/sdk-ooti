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


class TestContacts(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.post_pk = PostFactory()["pk"]
        cls.album_pk = AlbumFactory()["pk"]

    def test_create_contact(self):
        payload = {"name": "contact test"}
        response = sdk.Contacts.create_contact(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Contacts.delete_contact(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_create_contact_category(self):
        payload = {"name": "contact category test"}
        response = sdk.Contacts.create_contact_category(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Contacts.delete_contact_category(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Posts.delete_post(cls.post_pk)
        sdk.Posts.delete_posts_album(cls.album_pk)


if __name__ == "__main__":
    unittest.main()
