import os
import unittest

from factories.factories import AlbumFactory, PostFactory, TeamFactory
from resources import ooti

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
        payload = {"name": "contact test", "tags": []}
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
