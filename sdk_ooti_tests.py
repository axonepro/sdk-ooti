import unittest
from ooti import ooti

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
project_pk = my_account.get_projects_list()['data'][0]['id']


class Tests(unittest.TestCase):
    def _create_invoice_return_pk(self):
        """ Create and return the pk of an invoice """

        client_info = my_account.get_clients_list(team_pk)['data'][0]

        invoice = {
            "client": client_info['pk'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": "UNITTEST ref",
            "type": 4
        }

        invoice_pk = my_account.create_invoice(team_pk, invoice)['data']['pk']
        return invoice_pk

##### INVOICING #####

    #### Invoices #####

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

    def test_get_invoices_sent_valid_list(self):
        """ Test that 200 is returned """
        # * OK

        res_sent_valid = my_account.get_invoices_sent_valid_list()

        self.assertEqual(res_sent_valid['status'], 200)

    def test_create_invoice(self):
        """ Test that 201 is returned """
        # * OK

        client_info = my_account.get_clients_list(team_pk)['data'][0]

        invoice = {
            "client": client_info['pk'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.create_invoice(team_pk, invoice)

        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        invoice_updated = {
            "invoice_date": "20-04-2021",
            "references": "This is my new reference!!!",
            "purchase_order": "Hey this is the purchase order"
        }
        res_update = my_account.update_invoice(invoice_pk, invoice_updated)

        self.assertEqual(res_update['status'], 200)

    def test_validate_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_validate = my_account.validate_invoice(invoice_pk)

        self.assertEqual(res_validate['status'], 200)

    def test_send_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_send = my_account.send_invoice(invoice_pk)

        self.assertEqual(res_send['status'], 200)

    def test_close_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_close = my_account.cancel_invoice(invoice_pk)

        self.assertEqual(res_close['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()
        res_items = my_account.get_invoice_items(invoice_pk)

        self.assertEqual(res_items['status'], 200)

    def test_create_invoice_item(self):
        """ Test that 201 is returned """
        # * OK

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
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        invoice_item_pk = my_account.create_invoice_item(invoice_pk, invoice_item)['data']['pk']

        invoice_item_updated = {
            "amount": 1200
        }

        res_update = my_account.update_invoice_item(invoice_item_pk, invoice_item_updated)

        self.assertEqual(res_update['status'], 200)

    def test_delete_invoice_item(self):
        """ Test that 204 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()
        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        invoice_item_pk = my_account.create_invoice_item(invoice_pk, invoice_item)['data']['pk']

        res_delete = my_account.delete_invoice_item(invoice_item_pk)

        self.assertEqual(res_delete['status'], 204)

    #### Credit notes ####

    def test_get_credit_notes(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_credit_notes_list()

        self.assertEqual(res['status'], 200)

    def test_get_sent_valid_credit_notes(self):
        """ Test that 200 is returned """
        res = my_account.get_credit_notes_sent_valid_list()

        self.assertEqual(res['status'], 200)

    ##### Payments #####

    def test_get_payments_list(self):
        """ Test that 200 is returned """
        # * OK

        res_payments = my_account.get_payments_list()

        self.assertEqual(res_payments['status'], 200)

    def test_get_payments_details(self):
        """ Test that 200 is returned """
        # * OK

        payment_pk = my_account.get_payments_list()['data'][0]['pk']
        res_details = my_account.get_payment_details(payment_pk)

        self.assertEqual(res_details['status'], 200)

    def test_create_payment(self):
        """ Test that 201 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = my_account.create_invoice_item(invoice_pk, invoice_item)
        my_account.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        res_creation_payment = my_account.create_payment(team_pk, payment)

        self.assertEqual(res_creation_payment['status'], 201)

    def test_update_payment(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()
        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = my_account.create_invoice_item(invoice_pk, invoice_item)
        my_account.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        payment_pk = my_account.create_payment(team_pk, payment)['data']['pk']
        payment['date'] = '20-04-2021'

        res_update_payment = my_account.update_payment(payment_pk, payment)

        self.assertEqual(res_update_payment['status'], 200)

    def test_update_amount_payment_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()
        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = my_account.create_invoice_item(invoice_pk, invoice_item)
        my_account.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        payment_pk = my_account.create_payment(team_pk, payment)['data']['pk']

        update = {
            "amount": 200
        }

        my_account.update_payment(payment_pk, update)
        res_update_amount_invoice = my_account.update_payment_invoice(payment_pk, update)

        self.assertEqual(res_update_amount_invoice['status'], 200)

    ##### Currencies #####

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

        pk_currency = my_account.create_currency(currency)['data']['pk']
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

        pk_currency = my_account.create_currency(currency)['data']['pk']
        res_del = my_account.delete_currency(pk_currency)

        self.assertEqual(res_del['status'], 204)

    ##### Clients #####

    def test_get_clients_list(self):
        """ Test that 200 is returned """
        # * OK

        res_get = my_account.get_clients_list(team_pk)

        self.assertEqual(res_get['status'], 200)

    def test_get_client_details(self):
        """ Test that 200 is returned """
        # * OK

        res_get_list = my_account.get_clients_list(team_pk)

        client_pk = res_get_list['data'][0]['pk']
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

        client_pk = my_account.create_client(client)['data']['pk']

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

        client_pk = my_account.create_client(client)['data']['pk']
        res_delete = my_account.delete_client(client_pk)
        self.assertEqual(res_delete['status'], 204)

    #### Emails ####

    ### Classic ###
    def _create_email_return_pk(self):
        """ Create an email template and return the pk """
        # * OK

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "vdebande@ooti.co",
            "email_from": "vdebande@ooti.co",
            "name_from": "Vincent de OOTI"
        }

        email_pk = my_account.create_email(my_account.teams_pk, email)['data']['id']
        return email_pk

    def test_get_emails_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_emails_list()

        self.assertEqual(res['status'], 200)

    def test_create_email(self):
        """ Test that 201 is returned """
        # * OK

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "vdebande@ooti.co",
            "email_from": "vdebande@ooti.co",
            "name_from": "Vincent de OOTI"
        }

        res_creation = my_account.create_email(my_account.teams_pk, email)
        my_account.delete_email(res_creation['data']['id'])

        self.assertEqual(res_creation['status'], 201)

    def test_get_emails_details(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.get_email_details(email_pk)
        my_account.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()

        data = {'name': 'UNITTEST - update'}
        res = my_account.update_email(email_pk, data)
        my_account.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_email(self):
        """ Test that 204 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.delete_email(email_pk)

        self.assertEqual(res['status'], 204)

    def test_send_test_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.send_test_email(email_pk)
        my_account.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_apply_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.apply_email(email_pk)

        self.assertEqual(res['status'], 200)

    ### smtp ###
    def _create_email_smtp_return_pk(self):
        """ Create email smtp and return pk """
        # * OK

        data = {
            "from_name": "UNITTEST",
            "from_email": "UNITTEST",
            "username": "UNITTEST",
            "password": "UNITTEST",
            "protocol": "TLS",
            "host": "UNITTEST",
            "port": 0
        }

        smtp_pk = my_account.create_email_smtp(data)['data']['id']
        return smtp_pk

    def test_get_emails_smtp(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_emails_smtp_list()

        self.assertEqual(res['status'], 200)

    def test_create_email_smtp(self):
        """ Test that 201 is returned """
        # * OK

        data = {
            "from_name": "UNITTEST",
            "from_email": "UNITTEST",
            "username": "UNITTEST",
            "password": "UNITTEST",
            "protocol": "TLS",
            "host": "UNITTEST",
            "port": 0
        }

        res = my_account.create_email_smtp(data)
        my_account.delete_email_smtp(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_email_smtp_details(self):
        """ Test that 200 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()

        res = my_account.get_email_smtp_details(smtp_pk)
        my_account.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email_smtp(self):
        """ Test that 200 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()

        data = {"from_name": "UNITTEST - Update"}
        res = my_account.update_email_smtp(smtp_pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_email_smtp(self):
        """ Test that 204 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()
        res = my_account.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 204)

    def test_send_test_email_smtp(self):
        """ Test that 200 is returned """

        smtp_pk = self._create_email_smtp_return_pk()
        res = my_account.send_test_email_smtp(smtp_pk)

        my_account.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 200)

    #### Files ####

    ### Folders ###
    def _create_folder_return_pk(self):
        """ Create a folder and return the pk """

        folder = {
            "name": "UNITTEST"
        }

        folder_pk = my_account.create_folder(project_pk, folder)['data']['pk']
        return folder_pk

    def test_get_folders_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_folder_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_folder_details(self):
        """ Test that 200 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()

        res = my_account.get_folder_details(folder_pk)
        my_account.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_create_folder(self):
        """ Test that 201 is returned """
        # * OK

        folder = {
            "name": "UNITTEST"
        }

        res = my_account.create_folder(project_pk, folder)
        my_account.delete_folder(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_update_folder(self):
        """ Test that 201 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()

        folder_updated = {
            "name": "UNITTEST - UPDATE"
        }

        res = my_account.update_folder(folder_pk, folder_updated)
        my_account.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_folder(self):
        """ Test that 200 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()
        res = my_account.delete_folder(folder_pk)

        self.assertEqual(res['status'], 204)

    ### Files ###
    def test_get_files_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_files_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_files_details(self):
        """ Test that 200 is returned """
        # * OK

        file_pk = my_account.get_files_list(project_pk)['data'][0]['pk']
        res = my_account.get_file_details(file_pk)

        self.assertEqual(res['status'], 200)

    #### Banks ####
    def test_get_banks_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.get_banks_list()

        self.assertEqual(res['status'], 200)

    def test_get_banks_details(self):
        """ Test that 200 is returned """
        # * OK

        bank_pk = my_account.get_banks_list()['data'][0]['id']
        res = my_account.get_bank_details(bank_pk)

        self.assertEqual(res['status'], 200)

    def test_create_bank(self):
        """ Test that 201 is returned """
        # * OK

        data = {
            "name": "UNITTEST",
            "currency": 11833,
            "country": "FR",
            "iban": "XXX",
            "bic": "XXX",
            "rib": "XXX",
            "teams": [str(team_pk)],
            "projects": [str(project_pk)]
        }

        res = my_account.create_bank(data)
        my_account.delete_bank(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_update_bank(self):
        """ Test that 200 is returned """
        # * OK

        bank = {
            "name": "UNITTEST",
            "currency": 11833,
            "country": "FR",
            "iban": "XXX",
            "bic": "XXX",
            "rib": "XXX",
            "teams": [str(team_pk)],
            "projects": [str(project_pk)]
        }

        bank_pk = my_account.create_bank(bank)['data']['id']

        updated_bank = {
            "name": "UNITTEST - update"
        }

        res = my_account.update_bank(bank_pk, updated_bank)
        my_account.delete_bank(bank_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_bank(self):
        """ Test that 204 is returned """
        # * OK

        bank = {
            "name": "UNITTEST",
            "currency": 11833,
            "country": "FR",
            "iban": "XXX",
            "bic": "XXX",
            "rib": "XXX",
            "teams": [str(team_pk)],
            "projects": [str(project_pk)]
        }

        bank_pk = my_account.create_bank(bank)['data']['id']
        res = my_account.delete_bank(bank_pk)

        self.assertEqual(res['status'], 204)


if __name__ == '__main__':
    unittest.main()
