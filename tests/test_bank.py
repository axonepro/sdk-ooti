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

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

class TestBanks(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.project_pk = my_account.Projects.get_projects_list()['data'][0]['id']
        cls.bank_pk = cls.testHelper._create_bank_return_pk(cls.team_pk, cls.project_pk, cls.currency_pk)

    def test_get_banks_list(self):
        """ Test that 200 is returned """

        res = my_account.Banks.get_banks_list()

        self.assertEqual(res['status'], 200)

    def test_get_banks_details(self):
        """ Test that 200 is returned """

        res = my_account.Banks.get_bank_details(self.bank_pk)
        self.assertEqual(res['status'], 200)

    def test_create_bank(self):
        """ Test that 201 is returned """

        name = self.testHelper.create_name()

        data = {
            "name": name,
            "currency": self.currency_pk,
            "country": "FR",
            "iban": f"XXX-{name}",
            "bic": f"XXX-{name}",
            "rib": f"XXX-{name}",
            "teams": [str(self.team_pk)],
            "projects": [str(self.project_pk)]
        }

        res = my_account.Banks.create_bank(data)
        my_account.Banks.delete_bank(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_update_bank(self):
        """ Test that 200 is returned """

        name = self.testHelper.create_name()

        update = {
            "name": name
        }

        res = my_account.Banks.update_bank(self.bank_pk, update)
        my_account.Banks.delete_bank(self.bank_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_bank(self):
        """ Test that 204 is returned """

        res = my_account.Banks.delete_bank(self.bank_pk)
        self.assertEqual(res['status'], 204)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)
        my_account.Banks.delete_bank(cls.bank_pk)

if __name__ == '__main__':
    unittest.main()