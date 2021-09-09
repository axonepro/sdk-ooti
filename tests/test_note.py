from factories.factories import AlbumFactory, OrguserFactory, PostFactory, ProjectFactory
from factories.factories import TaskFactory, TeamFactory
import unittest

# To read .env variables
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

class TestNotes(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.project_pk = ProjectFactory()['id']
        cls.orguser_pk = OrguserFactory()['pk']
        cls.team_pk = TeamFactory()

    def test_create_note(self):
        payload = {
            "text": "A note to see if the function works correctly",
            "title": "note tested",
            "is_pinned": True,
            "project": self.project_pk,
            "orguser": self.orguser_pk,
            "is_public": True,
            "entire_project": True,
            "followers": [
                self.orguser_pk,
            ]
        }
        response = sdk.Notes.create_note(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Notes.delete_note(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_pk)
        sdk.Orgusers.delete_orguser(cls.orguser_pk)

if __name__ == '__main__':
    unittest.main()