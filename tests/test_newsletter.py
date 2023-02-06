import os
import unittest

from factories.factories import OrguserFactory, TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestNewsletters(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.orguser_pk = OrguserFactory()["pk"]
        cls.team_pk = TeamFactory()

    def test_create_newsletter(self):
        payload = {
            "receivers": [self.orguser_pk],
            "name": "newsletter tested",
            "start_date": "04-05-2021",
            "end_date": "07-05-2021",
            "frequency": 1,
            "all_users_are_receivers": True,
        }
        response = sdk.Newsletters.create_newsletters(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Newsletters.delete_newsletter(response["data"]["pk"])
        self.assertEqual(delete["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Orgusers.delete_orguser(cls.orguser_pk)


if __name__ == "__main__":
    unittest.main()
