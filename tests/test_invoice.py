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
project_pk = my_account.get_projects_list()['data'][0]['id']

class TestInvoices(unittest.TestCase):
    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = testHelper._create_currency_if_none()
        cls.client_pk = testHelper._create_client_return_pk(cls.team_pk, cls.currency_pk)
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.invoice_pk = testHelper._create_invoice_return_pk(cls.team_pk, cls.project_pk)
        cls.invoice_item_pk = testHelper._create_invoice_item_return_pk(cls.invoice_pk)
        cls.payment_pk = testHelper._create_payment_return_pk(cls.team_pk, cls.invoice_pk, cls.currency_pk)

        cls.invoice_pk_not_validated = testHelper._create_invoice_return_pk(cls.team_pk, cls.project_pk)
        cls.invoice_item_pk_not_validated = testHelper._create_invoice_item_return_pk(cls.invoice_pk_not_validated)

    def test_get_invoices_list(self):
        """ Test that 200 is returned """

        res_get = my_account.Invoices.get_invoices_list()

        self.assertEqual(res_get['status'], 200)

    def test_get_invoice_details(self):
        """ Test that 200 is returned """

        res_details = my_account.Invoices.get_invoice_details(self.invoice_pk)

        self.assertEqual(res_details['status'], 200)

    def test_get_invoices_sent_valid_list(self):
        """ Test that 200 is returned """

        res_sent_valid = my_account.Invoices.get_invoices_sent_valid_list(self.team_pk)

        self.assertEqual(res_sent_valid['status'], 200)

    def test_create_invoice(self):
        """ Test that 201 is returned """

        # Test with project in paylaod
        invoice_project = {
            "project": self.project_pk,
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.Invoices.create_invoice(self.team_pk, invoice_project)
        self.assertEqual(res_creation['status'], 201)

        # Test with client in paylaod
        invoice_client = {
            "client": self.client_pk,
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.Invoices.create_invoice(self.team_pk, invoice_client)
        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice(self):
        """ Test that 200 is returned """

        invoice_updated = {
            "invoice_date": "20-04-2021",
            "references": "This is my new reference!!!",
            "purchase_order": "Hey this is the purchase order"
        }

        res_update = my_account.Invoices.update_invoice(self.invoice_pk_not_validated, invoice_updated)
        self.assertEqual(res_update['status'], 200)

    def test_validate_invoice(self):
        """ Test that 200 is returned """

        res_validate = my_account.Invoices.validate_invoice(self.invoice_pk_not_validated)
        self.assertEqual(res_validate['status'], 200)

    def test_send_invoice(self):
        """ Test that 200 is returned """

        res_send = my_account.Invoices.send_invoice(self.invoice_pk)
        self.assertEqual(res_send['status'], 200)

    def test_close_invoice(self):
        """ Test that 200 is returned """

        res_close = my_account.Invoices.cancel_invoice(self.invoice_pk)
        self.assertEqual(res_close['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """

        res_items = my_account.Invoices.get_invoice_items(self.invoice_pk)
        self.assertEqual(res_items['status'], 200)

    def test_create_invoice_item(self):
        """ Test that 201 is returned """

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation = my_account.Invoices.create_invoice_item(self.invoice_pk, invoice_item)
        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice_item(self):
        """ Test that 200 is returned """

        update = {
            "amount": 1200
        }

        res_update = my_account.Invoices.update_invoice_item(self.invoice_item_pk_not_validated, update)
        self.assertEqual(res_update['status'], 200)

    def test_delete_invoice_item(self):
        """ Test that 204 is returned """

        res_delete = my_account.Invoices.delete_invoice_item(self.invoice_item_pk)
        self.assertEqual(res_delete['status'], 204)

    def test_get_credit_notes(self):
        """ Test that 200 is returned """

        res = my_account.Invoices.get_credit_notes_list()
        self.assertEqual(res['status'], 200)

    def test_get_credit_notes_sent_valid(self):
        """ Test that 200 is returned """
        res = my_account.Invoices.get_credit_notes_sent_valid_list(self.team_pk)

        self.assertEqual(res['status'], 200)

if __name__ == '__main__':
    unittest.main()