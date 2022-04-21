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

class TestCurrencies(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = cls.testHelper._create_currency_if_none()

    def test_get_currencies_list(self):
        """ Test that 200 is returned """

        res = my_account.Currencies.get_currencies_list()
        self.assertEqual(res['status'], 200)

    def test_create_currency(self):
        """ Test that 201 is returned """

        name = ''
        for i in range(6):
            name += random.choice(string.ascii_letters)
            time.sleep(0.1)

        data_currency = {
            "name": name,
            "longname": "longname",
            "symbol": "$",
        }

        res = my_account.Currencies.create_currency(data_currency)

        if 'detail' in res['data'] and res['data']['detail'] == 'Currency already exists':
            self.test_create_currency()
        else:
            self.assertEqual(res['status'], 201)

    def test_get_currency_details(self):
        """ Test that 200 is returned """

        # get details
        res_details = my_account.Currencies.get_currency_details(self.currency_pk)
        self.assertEqual(res_details["status"], 200)

    def test_update_currency(self):
        """ Test that 200 is returned """

        currency_pk = self.testHelper._create_currency_return_pk()

        update = {
            "decimal_points": 2
        }

        res_update = my_account.Currencies.update_currency(currency_pk, update)
        self.assertEqual(res_update['status'], 200)

    def test_delete_currency(self):
        """ Test that 204 is returned """

        currency_pk = self.testHelper._create_currency_return_pk()
        res_del = my_account.Currencies.delete_currency(currency_pk)
        self.assertEqual(res_del['status'], 204)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)

if __name__ == '__main__':
    unittest.main()