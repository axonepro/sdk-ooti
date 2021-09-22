import unittest

from requests.models import Response
from test_helper import HelperTest
from factories.factories import TeamFactory

import random
import string
import time

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

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

class TestClients(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = testHelper._create_currency_if_none()
        cls.client_pk = testHelper._create_client_return_pk(cls.team_pk, cls.currency_pk)

    def test_get_clients_list(self):
        """ Test that 200 is returned """

        res_get = my_account.Clients.get_clients_list(self.team_pk)
        self.assertEqual(res_get['status'], 200)

    def test_get_client_details(self):
        """ Test that 200 is returned """

        res_get = my_account.Clients.get_clients_details(self.client_pk)
        self.assertEqual(res_get['status'], 200)

    def test_create_client(self):
        """ Test that 201 is returned """

        client = {
            "name": "UNITTEST",
            "number": "{0}{1}{2}{3}{4}".format(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)),
            "currency": self.currency_pk,
            "billing_address": "Unittest address",
            "team": self.team_pk,
            "tags": []
        }

        res_creation = my_account.Clients.create_client(client)
        self.assertEqual(res_creation['status'], 201)

    def test_update_client(self):
        """ Test that 200 is returned """

        update = {
            "billing_address": "Update unittest address",
        }

        res_update = my_account.Clients.update_client(self.client_pk, update)
        self.assertEqual(res_update['status'], 200)

    def test_delete_client(self):
        """ Test that 204 is returned """

        res_delete = my_account.Clients.delete_client(self.client_pk)
        self.assertEqual(res_delete['status'], 204)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)
        my_account.Clients.delete_client(cls.client_pk)

if __name__ == '__main__':
    unittest.main()