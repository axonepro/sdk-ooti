import os
import random
import string
import sys
import time
import unittest

from dotenv import load_dotenv
from factories.factories import TeamFactory
from requests.models import Response
from test_helper import HelperTest

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

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()["data"][0]["pk"]
project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]


class TestEmails(unittest.TestCase):
    @classmethod
    def setUp(cls):
        testHelper = HelperTest(my_account)
        cls.email_pk = testHelper._create_email_return_pk()
        cls.smtp_pk = testHelper._create_email_smtp_return_pk()

    ### Classic ###

    def test_get_emails_list(self):
        """Test that 200 is returned"""

        res = my_account.Emails.get_emails_list()
        self.assertEqual(res["status"], 200)

    def test_create_email(self):
        """Test that 201 is returned"""

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "vdebande@ooti.co",
            "email_from": "vdebande@ooti.co",
            "name_from": "Vincent de OOTI",
        }

        res_creation = my_account.Emails.create_email(email)
        my_account.Emails.delete_email(res_creation["data"]["id"])

        self.assertEqual(res_creation["status"], 201)

    def test_get_emails_details(self):
        """Test that 200 is returned"""

        res = my_account.Emails.get_email_details(self.email_pk)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res["status"], 200)

    def test_update_email(self):
        """Test that 200 is returned"""

        data = {"name": "UNITTEST - update"}
        res = my_account.Emails.update_email(self.email_pk, data)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res["status"], 200)

    def test_delete_email(self):
        """Test that 204 is returned"""

        res = my_account.Emails.delete_email(self.email_pk)
        self.assertEqual(res["status"], 204)

    def test_send_test_email(self):
        """Test that 200 is returned"""

        res = my_account.Emails.send_test_email(self.email_pk)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res["status"], 200)

    def test_apply_email(self):
        """Test that 200 is returned"""

        res = my_account.Emails.apply_email(self.email_pk)
        self.assertEqual(res["status"], 200)

    ### smtp ###
    def test_get_emails_smtp(self):
        """Test that 200 is returned"""

        res = my_account.Emails.get_emails_smtp_list()
        self.assertEqual(res["status"], 200)

    def test_create_email_smtp(self):
        """Test that 201 is returned"""

        data = {
            "from_name": "UNITTEST",
            "from_email": "UNITTEST",
            "username": "UNITTEST",
            "password": "UNITTEST",
            "protocol": "TLS",
            "host": "UNITTEST",
            "port": 0,
        }

        res = my_account.Emails.create_email_smtp(data)
        my_account.Emails.delete_email_smtp(res["data"]["id"])

        self.assertEqual(res["status"], 201)

    def test_get_email_smtp_details(self):
        """Test that 200 is returned"""

        res = my_account.Emails.get_email_smtp_details(self.smtp_pk)
        my_account.Emails.delete_email_smtp(self.smtp_pk)

        self.assertEqual(res["status"], 200)

    def test_update_email_smtp(self):
        """Test that 200 is returned"""

        data = {"from_name": "UNITTEST - Update"}
        res = my_account.Emails.update_email_smtp(self.smtp_pk, data)

        self.assertEqual(res["status"], 200)

    def test_delete_email_smtp(self):
        """Test that 204 is returned"""

        res = my_account.Emails.delete_email_smtp(self.smtp_pk)
        self.assertEqual(res["status"], 204)

    def test_send_test_email_smtp(self):
        """Test that 200 is returned"""

        res = my_account.Emails.send_test_email_smtp(self.smtp_pk)
        self.assertEqual(res["status"], 200)

    @classmethod
    def tearDown(cls):
        my_account.Emails.delete_email(cls.email_pk)
        my_account.Emails.delete_email_smtp(cls.smtp_pk)


if __name__ == "__main__":
    unittest.main()
