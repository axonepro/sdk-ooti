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

class TestTags(unittest.TestCase):
    @ classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.orguser_pk = OrguserFactory()['pk']

    def test_get_tags_list(self):
        response = sdk.Tags.get_tags_list()
        self.assertEqual(response['status'], 200)

    def test_create_tag(self):
        payload = {
            "name": "tag test",
        }
        response = sdk.Tags.create_tag(payload)
        self.assertEqual(response['status'], 201)
        created_id = response['data']['id']
        payload = {
            "orgusers": [
                self.orguser_pk,
            ]
        }
        update = sdk.Tags.update_tag_details(created_id, payload)
        self.assertEqual(update['status'], 200)
        get = sdk.Tags.get_tag_details(created_id)
        self.assertEqual(get['status'], 200)
        delete = sdk.Tags.delete_tag(created_id)
        self.assertEqual(delete['status'], 204)

    @classmethod
    def tearDown(cls):
        sdk.Orgusers.delete_orguser(cls.orguser_pk)

if __name__ == '__main__':
    unittest.main()