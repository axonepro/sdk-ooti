import unittest
from ooti import ooti

from datetime import datetime
from uuid import uuid4

# To read .env variables
import os
from dotenv import load_dotenv

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.Auth(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = my_account.teams_pk[0]['id']
currency_pk = my_account.get_currencies_list()['data'][0]['pk']


class Tests(unittest.TestCase):
    def _get_item_id(self, results, attribute_name, value_attribute):
        """ Returns the pk of a given object based on value of attribute

        Keyword arguments:

        results -- array of object
        attribute_name -- name of the attribute you're looking for
        value_attribute -- value of the attribute you're looking for
        """
        for data_object in results:
            if(attribute_name in data_object):
                if(data_object[attribute_name] == value_attribute):
                    return data_object['pk']

    def _create_invoice_return_pk(self):
        """ Create and return the pk of an invoice """

        client_info = my_account.get_clients_list(team_pk)['data']['results'][0]

        reference = "{0}{1}".format(datetime.now().strftime('%Y%m-%d%H-%M%S-'), uuid4())

        invoice = {
            "client_name": client_info['name'],
            "client_address": client_info['address'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": reference,
            "type": 4
        }

        my_account.create_invoice(team_pk, invoice)
        res_get_invoices = my_account.get_invoices_list()['data']

        invoice_pk = self._get_item_id(res_get_invoices, 'references', invoice['references'])
        return invoice_pk

    ##### Invoices ######

    def test_get_invoices_list(self):
        """ Test that 200 is returned """
        # * OK

        res_get = my_account.get_invoices_list()

        self.assertEqual(res_get['status'], 200)

    def test_get_invoice_details(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = my_account.get_invoices_list()['data'][0]['pk']
        res_details = my_account.get_invoice_details(invoice_pk)

        self.assertEqual(res_details['status'], 200)

    def test_create_invoice(self):
        """ Test that 201 is returned """
        # * OK

        client_info = my_account.get_clients_list(team_pk)['data']['results'][0]

        invoice = {
            "client_name": client_info['name'],
            "client_address": client_info['address'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.create_invoice(team_pk, invoice)

        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()

        invoice_updated = {
            "invoice_date": "20-04-2021",
            "references": "This is my new reference!!!",
            "purchase_order": "Hey this is the purchase order"
        }
        res_update = my_account.update_invoice(invoice_pk, invoice_updated)

        self.assertEqual(res_update['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()
        res_items = my_account.get_invoice_items(invoice_pk)

        self.assertEqual(res_items['status'], 200)

    def test_create_invoice_item(self):
        """ Test that 201 is returned """

        invoice_pk = self._create_invoice_return_pk()

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation = my_account.create_invoice_item(invoice_pk, invoice_item)

        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice_item(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        my_account.create_invoice_item(invoice_pk, invoice_item)
        invoice_item_pk = my_account.get_invoice_items(invoice_pk)['data']['results'][0]['pk']

        invoice_item_updated = {
            "amount": 1200
        }

        res_update = my_account.update_invoice_item(invoice_item_pk, invoice_item_updated)

        self.assertEqual(res_update['status'], 200)

    def test_delete_invoice_item(self):
        """ Test that 204 is returned """

        invoice_pk = self._create_invoice_return_pk()
        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        my_account.create_invoice_item(invoice_pk, invoice_item)
        invoice_item_pk = my_account.get_invoice_items(invoice_pk)['data']['results'][0]['pk']

        res_delete = my_account.delete_invoice_item(invoice_item_pk)

        self.assertEqual(res_delete['status'], 204)

    ###### Currencies ######

    def test_get_currencies_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_currencies_list()
        self.assertEqual(res['status'], 200)

    def test_create_currency(self):
        """ Test that 201 is returned """
        # * OK

        currency = {
            "name": "MYCURR",
            "longname": "unittest",
            "decimal_points": 3,
            "symbol": "^"
        }

        res = my_account.create_currency(currency)
        self.assertEqual(res['status'], 201)

    def test_get_currency_details(self):
        """ Test that 200 is returned """
        # * OK

        # get an id
        res_get = my_account.get_currencies_list()
        id_currency = res_get["data"][0]['pk']

        # get details
        res_details = my_account.get_currency_details(id_currency)
        self.assertEqual(res_details["status"], 200)

    def test_update_currency(self):
        """ Test that 200 is returned """
        # * OK

        currency = {
            "name": "MYUPD",
            "longname": "myCurrency",
            "decimal_points": 3,
            "symbol": "^"
        }

        my_account.create_currency(currency)
        res_currencies_list = my_account.get_currencies_list()["data"]
        pk_currency = self._get_item_id(res_currencies_list, 'name', currency['name'])
        currency["decimal_points"] = 2

        res_update = my_account.update_currency(pk_currency, currency)
        self.assertEqual(res_update['status'], 200)

    def test_delete_currency(self):
        """ Test that 204 is returned """
        # * OK

        currency = {
            "name": "MYDEL",
            "longname": "myCurrency",
            "decimal_points": 3,
            "symbol": "^"
        }

        my_account.create_currency(currency)
        res_currencies_list = my_account.get_currencies_list()['data']
        pk_currency = self._get_item_id(res_currencies_list, 'name', currency['name'])
        res_del = my_account.delete_currency(pk_currency)

        self.assertEqual(res_del['status'], 204)

    ###### Clients ######

    def test_get_clients_list(self):
        """ Test that 200 is returned """
        # * OK

        res_get = my_account.get_clients_list(team_pk)

        self.assertEqual(res_get['status'], 200)

    def test_get_client_details(self):
        """ Test that 200 is returned """
        # * OK

        res_get_list = my_account.get_clients_list(team_pk)

        client_pk = res_get_list['data']['results'][0]['pk']
        res_get = my_account.get_clients_details(client_pk)

        self.assertEqual(res_get['status'], 200)

    def test_create_client(self):
        """ Test that 201 is returned """
        # * OK

        client = {
            "name": "UNITTEST",
            "number": "000",
            "currency": currency_pk,
            "billing_address": "Unittest address",
            "team": team_pk,
            "tags": []
        }

        res_creation = my_account.create_client(client)

        self.assertEqual(res_creation['status'], 201)

    def test_update_client(self):
        """ Test that 200 is returned """
        # * OK

        client = {
            "name": "UNITTEST_UPDATE",
            "number": "000",
            "currency": currency_pk,
            "billing_address": "Unittest address",
            "team": team_pk,
            "tags": []
        }

        res_creation = my_account.create_client(client)

        res_clients_list = my_account.get_clients_list(team_pk)
        client_pk = self._get_item_id(res_clients_list["data"]["results"], "name", "UNITTEST_UPDATE")

        client["billing_address"] = "Update unittest address"

        res_update = my_account.update_client(client_pk, client)

        self.assertEqual(res_update['status'], 200)

    def test_delete_client(self):
        """ Test that 204 is returned """
        # * OK

        client = {
            "name": "UNITTEST_DELETE",
            "number": "000",
            "currency": currency_pk,
            "billing_address": "Unittest address",
            "team": team_pk,
            "tags": []
        }

        res_creation = my_account.create_client(client)
        res_clients_list = my_account.get_clients_list(team_pk)
        client_pk = self._get_item_id(res_clients_list["data"]["results"], "name", "UNITTEST_DELETE")

        res_delete = my_account.delete_client(client_pk)
        self.assertEqual(res_delete['status'], 204)

    ###### Exepenses ######


if __name__ == '__main__':
    unittest.main()
