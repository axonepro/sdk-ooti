import unittest

from requests.models import Response
from test_helper import TestHelper
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

from resources import ooti # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

class TestPayments(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = testHelper._create_currency_if_none()
        cls.client_pk = testHelper._create_client_return_pk(cls.team_pk, cls.currency_pk)
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()['data'][0]['id']
        cls.invoice_pk = testHelper._create_invoice_return_pk(cls.team_pk, cls.project_pk)
        cls.payment_pk = testHelper._create_payment_return_pk(cls.team_pk, cls.invoice_pk, cls.currency_pk)

    def test_get_payments_list(self):
        """ Test that 200 is returned """

        res_payments = my_account.Payments.get_payments_list()

        self.assertEqual(res_payments['status'], 200)

    def test_get_payments_details(self):
        """ Test that 200 is returned """

        res_details = my_account.Payments.get_payment_details(self.payment_pk)

        self.assertEqual(res_details['status'], 200)

    def test_create_payment(self):
        """ Test that 201 is returned """

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = my_account.Invoices.create_invoice_item(self.invoice_pk, invoice_item)
        my_account.Invoices.validate_invoice(self.invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "team": self.team_pk,
            "project": self.project_pk,
            "invoice": self.invoice_pk,
        }

        res_creation_payment = my_account.Payments.create_payment(self.team_pk, payment)
        self.assertEqual(res_creation_payment['status'], 201)

    def test_update_payment(self):
        """ Test that 200 is returned """

        update = {
            'date': '20-04-2021',
        }

        res_update_payment = my_account.Payments.update_payment(self.payment_pk, update)
        self.assertEqual(res_update_payment['status'], 200)

    def test_update_amount_payment_invoice(self):
        """ Test that 200 is returned """

        update = {
            "amount": 10
        }

        my_account.Payments.update_payment(self.payment_pk, update)
        invoice_payment_pk = my_account.Payments.get_payment_details(self.payment_pk)['data']['invoice_payments'][0]['pk']
        res_update_amount_invoice = my_account.Payments.update_payment_invoice(invoice_payment_pk, update)
        self.assertEqual(res_update_amount_invoice['status'], 200)

    @classmethod
    def tearDown(cls):
        my_account.Currencies.delete_currency(cls.currency_pk)
        my_account.Clients.delete_client(cls.client_pk)
        # TODO Delete cls.invoice_pk when the delete function will be written
        # TODO Delete cls.payment_pk when the delete function will be written

if __name__ == '__main__':
    unittest.main()