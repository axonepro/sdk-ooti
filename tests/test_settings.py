from factories.factories import OrguserFactory, ProjectFactory
import unittest
from test_helper import TestHelper
import os
import sys
from dotenv import load_dotenv


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ooti import ooti # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.Auth(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestCustomfields(unittest.TestCase):
    @ classmethod
    def setUpClass(self):
        testHelper = TestHelper(sdk)
        self.team_pk = testHelper._get_selected_team()

    def test_get_customfields_list(self):
        response = sdk.Settings.get_customfields_list()
        self.assertEqual(response['status'], 200)

    def test_create_customfield(self):
        payload = {
            "name": "Test custom field",
            "field_type": "t",
            "default_value": "test",
            "is_required": False,
            "admin_only": False,
            "content_type": 'project',
        }
        response = sdk.Settings.create_customfield(payload)
        self.assertEqual(response['status'], 201)
        created_id = response['data']['pk']
        update = sdk.Settings.update_customfield_details(created_id, payload)
        self.assertEqual(update['status'], 200)
        get = sdk.Settings.get_customfield_details(created_id)
        self.assertEqual(get['status'], 200)
        delete = sdk.Settings.delete_customfield(created_id)
        self.assertEqual(delete['status'], 204)


""" Not cleaned up yet
class TestImports(unittest.TestCase):
    def test_get_imports_count(self):
        response = sdk.Settings.get_imports_count()
        self.assertEqual(response['status'], 200)

    def test_get_exports_list(self):
        response = sdk.Settings.get_exports_list()
        self.assertEqual(response['status'], 200)

    def test_create_export(self):
        payload = {
            "orguser": 5042,
            "team": 1689,
            "project": 11702,
            "items": 0,
            "include_documents": True
        }
        response = sdk.Settings.create_export(payload)
        self.assertEqual(response['status'], 201)

    def test_get_export_details(self):
        response = sdk.Settings.get_export_details(16)
        self.assertEqual(response['status'], 200)

    def test_delete_export(self):
        response = sdk.Settings.delete_export(15)

    def test_get_import_list(self):
        response = sdk.Settings.get_imports_list()
        self.assertEqual(response['status'], 200)

    def test_create_import(self):
        payload = {
            "data": {}
        }
        response = sdk.Settings.create_import(payload)
        self.assertEqual(response['status'], 201)

    def test_get_import_details(self):
        response = sdk.Settings.get_import_details(66)
        self.assertEqual(response['status'], 200)

    def test_update_import_list(self):
        payload = {
            "status": 3,
            "type": 6
        }
        response = sdk.Settings.update_import_details(66, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_import(self):
        response = sdk.Settings.delete_import(71)
"""


class TestCeleryTasks(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        testHelper = TestHelper(sdk)
        cls.team_pk = testHelper._get_selected_team()
        cls.project_id = ProjectFactory()['id']

    def test_get_last_celery_task(self):
        response = sdk.Settings.get_last_celery_task()
        self.assertIn(response['status'], [200, 404])

    def test_get_celery_tasks_list(self):
        response = sdk.Settings.get_celery_tasks_list()
        self.assertEqual(response['status'], 200)


class TestInboundEmails(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        testHelper = TestHelper(sdk)
        cls.team_pk = testHelper._get_selected_team()
        cls.project_id = ProjectFactory()['id']

    def test_get_inbound_emails_list(self):
        response = sdk.Settings.get_inbound_emails_list()
        self.assertEqual(response['status'], 200)

    def test_create_inbound_email(self):
        payload = {
            "project": self.project_id,
            "subject": "test subject",
            "body": "test body"
        }
        response = sdk.Settings.create_inbound_email(payload)
        self.assertEqual(response['status'], 201)
        created_id = response['data']['id']
        payload = {
            "subject": "updated",
            "body": "body update"
        }
        update = sdk.Settings.update_inbound_email_details(created_id, payload)
        self.assertEqual(update['status'], 200)
        get = sdk.Settings.get_inbound_email_details(created_id)
        self.assertEqual(get['status'], 200)
        delete = sdk.Settings.delete_inbound_email(created_id)
        self.assertEqual(delete['status'], 204)


class TestTags(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        testHelper = TestHelper(sdk)
        cls.team_pk = testHelper._get_selected_team()
        cls.orguser_pk = OrguserFactory()['pk']

    def test_get_tags_list(self):
        response = sdk.Settings.get_tags_list()
        self.assertEqual(response['status'], 200)

    def test_create_tag(self):
        payload = {
            "name": "tag test",
        }
        response = sdk.Settings.create_tag(payload)
        self.assertEqual(response['status'], 201)
        created_id = response['data']['id']
        payload = {
            "orgusers": [
                self.orguser_pk,
            ]
        }
        update = sdk.Settings.update_tag_details(created_id, payload)
        self.assertEqual(update['status'], 200)
        get = sdk.Settings.get_tag_details(created_id)
        self.assertEqual(get['status'], 200)
        delete = sdk.Settings.delete_tag(created_id)
        self.assertEqual(delete['status'], 204)


if __name__ == '__main__':
    unittest.main()
