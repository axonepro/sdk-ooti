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


class TestTasks(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.orguser_pk = OrguserFactory()["pk"]
        cls.task_pk = TaskFactory()["pk"]

    def test_create_task_label(self):
        payload = {
            "creator": self.orguser_pk,
            "team": self.team_pk,
            "title": "task label tested",
            "description": "test if the function works correctly",
        }
        response = sdk.Tasks.create_task_label(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Tasks.delete_task_label(response["data"]["pk"])
        self.assertEqual(delete["status"], 204)

    def test_create_task(self):
        payload = {
            "creator": self.orguser_pk,
            "title": "task tested",
            "due_date": "07-08-2021",
            "description": "test if the tasks creation works",
        }
        response = sdk.Tasks.create_task(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Tasks.delete_task(response["data"]["pk"])
        self.assertEqual(delete["status"], 204)

    def test_create_tasks_list(self):
        payload = {
            "title": "task list test",
        }
        response = sdk.Tasks.create_tasks_list(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Tasks.delete_tasks_list(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Orgusers.delete_orguser(cls.orguser_pk)
        sdk.Tasks.delete_task(cls.task_pk)


if __name__ == "__main__":
    unittest.main()
