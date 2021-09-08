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

class TestCeleryTasks(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()['id']

    def test_get_last_celery_task(self):
        response = sdk.Celery_tasks.get_last_celery_task()
        self.assertIn(response['status'], [200, 404])

    def test_get_celery_tasks_list(self):
        response = sdk.Celery_tasks.get_celery_tasks_list()
        self.assertEqual(response['status'], 200)

if __name__ == '__main__':
    unittest.main()