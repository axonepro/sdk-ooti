import os
import unittest

from factories.factories import ProjectFactory, TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestCeleryTasks(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()["id"]

    def test_get_last_celery_task(self):
        response = sdk.Celery_tasks.get_last_celery_task()
        self.assertIn(response["status"], [200, 404])

    def test_get_celery_tasks_list(self):
        response = sdk.Celery_tasks.get_celery_tasks_list()
        self.assertEqual(response["status"], 200)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)


if __name__ == "__main__":
    unittest.main()
