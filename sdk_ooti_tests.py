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
currency_pk = my_account.Invoicing.get_currencies_list()['data'][0]['pk']
project_pk = my_account.get_projects_list()['data'][0]['id']


class Tests(unittest.TestCase):
    def _create_invoice_return_pk(self):
        """ Create and return the pk of an invoice """

        client_info = my_account.Invoicing.get_clients_list(team_pk)['data'][0]

        invoice = {
            "client": client_info['pk'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": "UNITTEST ref",
            "type": 4
        }

        invoice_pk = my_account.Invoicing.create_invoice(team_pk, invoice)['data']['pk']
        return invoice_pk

##### INVOICING #####

    #### Invoices #####

    def test_get_invoices_list(self):
        """ Test that 200 is returned """
        # * OK

        res_get = my_account.Invoicing.get_invoices_list()

        self.assertEqual(res_get['status'], 200)

    def test_get_invoice_details(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = my_account.Invoicing.get_invoices_list()['data'][0]['pk']
        res_details = my_account.Invoicing.get_invoice_details(invoice_pk)

        self.assertEqual(res_details['status'], 200)

    def test_get_invoices_sent_valid_list(self):
        """ Test that 200 is returned """
        # * OK

        res_sent_valid = my_account.Invoicing.get_invoices_sent_valid_list(team_pk)

        self.assertEqual(res_sent_valid['status'], 200)

    def test_create_invoice(self):
        """ Test that 201 is returned """
        # * OK

        client_info = my_account.Invoicing.get_clients_list(team_pk)['data'][0]

        invoice = {
            "client": client_info['pk'],
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.Invoicing.create_invoice(team_pk, invoice)

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
        res_update = my_account.Invoicing.update_invoice(invoice_pk, invoice_updated)

        self.assertEqual(res_update['status'], 200)

    def test_validate_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_validate = my_account.Invoicing.validate_invoice(invoice_pk)

        self.assertEqual(res_validate['status'], 200)

    def test_send_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_send = my_account.Invoicing.send_invoice(invoice_pk)

        self.assertEqual(res_send['status'], 200)

    def test_close_invoice(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()

        res_close = my_account.Invoicing.cancel_invoice(invoice_pk)

        self.assertEqual(res_close['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """
        # * OK

        invoice_pk = self._create_invoice_return_pk()
        res_items = my_account.Invoicing.get_invoice_items(invoice_pk)

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

        res_creation = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)

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

        invoice_item_pk = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)['data']['pk']

        invoice_item_updated = {
            "amount": 1200
        }

        res_update = my_account.Invoicing.update_invoice_item(invoice_item_pk, invoice_item_updated)

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

        invoice_item_pk = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)['data']['pk']

        res_delete = my_account.Invoicing.delete_invoice_item(invoice_item_pk)

        self.assertEqual(res_delete['status'], 204)

    #### Credit notes ####

    def test_get_credit_notes(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_credit_notes_list()

        self.assertEqual(res['status'], 200)

    def test_get_credit_notes_sent_valid(self):
        """ Test that 200 is returned """
        res = my_account.Invoicing.get_credit_notes_sent_valid_list(team_pk)

        self.assertEqual(res['status'], 200)

    ##### Payments #####

    def test_get_payments_list(self):
        """ Test that 200 is returned """
        # * OK

        res_payments = my_account.Invoicing.get_payments_list()

        self.assertEqual(res_payments['status'], 200)

    def test_get_payments_details(self):
        """ Test that 200 is returned """
        # * OK

        payment_pk = my_account.Invoicing.get_payments_list()['data'][0]['pk']
        res_details = my_account.Invoicing.get_payment_details(payment_pk)

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

        res_creation_item = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)
        my_account.Invoicing.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        res_creation_payment = my_account.Invoicing.create_payment(team_pk, payment)

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

        res_creation_item = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)
        my_account.Invoicing.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        payment_pk = my_account.Invoicing.create_payment(team_pk, payment)['data']['pk']
        payment['date'] = '20-04-2021'

        res_update_payment = my_account.Invoicing.update_payment(payment_pk, payment)

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

        res_creation_item = my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)
        my_account.Invoicing.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": "11833",
            "invoice": invoice_pk,
            "team": team_pk
        }

        payment_pk = my_account.Invoicing.create_payment(team_pk, payment)['data']['pk']

        update = {
            "amount": 200
        }

        my_account.Invoicing.update_payment(payment_pk, update)
        res_update_amount_invoice = my_account.Invoicing.update_payment_invoice(payment_pk, update)

        self.assertEqual(res_update_amount_invoice['status'], 200)

    ##### Currencies #####

    def test_get_currencies_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_currencies_list()
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

        res = my_account.Invoicing.create_currency(currency)
        self.assertEqual(res['status'], 201)

    def test_get_currency_details(self):
        """ Test that 200 is returned """
        # * OK

        # get an id
        res_get = my_account.Invoicing.get_currencies_list()
        id_currency = res_get["data"][0]['pk']

        # get details
        res_details = my_account.Invoicing.get_currency_details(id_currency)
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

        pk_currency = my_account.Invoicing.create_currency(currency)['data']['pk']
        currency["decimal_points"] = 2

        res_update = my_account.Invoicing.update_currency(pk_currency, currency)
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

        pk_currency = my_account.Invoicing.create_currency(currency)['data']['pk']
        res_del = my_account.Invoicing.delete_currency(pk_currency)

        self.assertEqual(res_del['status'], 204)

    ##### Clients #####

    def test_get_clients_list(self):
        """ Test that 200 is returned """
        # * OK

        res_get = my_account.Invoicing.get_clients_list(team_pk)

        self.assertEqual(res_get['status'], 200)

    def test_get_client_details(self):
        """ Test that 200 is returned """
        # * OK

        res_get_list = my_account.Invoicing.get_clients_list(team_pk)

        client_pk = res_get_list['data'][0]['pk']
        res_get = my_account.Invoicing.get_clients_details(client_pk)

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

        res_creation = my_account.Invoicing.create_client(client)

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

        client_pk = my_account.Invoicing.create_client(client)['data']['pk']

        client["billing_address"] = "Update unittest address"

        res_update = my_account.Invoicing.update_client(client_pk, client)

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

        client_pk = my_account.Invoicing.create_client(client)['data']['pk']
        res_delete = my_account.Invoicing.delete_client(client_pk)
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

        email_pk = my_account.Invoicing.create_email(my_account.Invoicing.teams_pk, email)['data']['id']
        return email_pk

    def test_get_emails_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_emails_list()

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

        res_creation = my_account.Invoicing.create_email(my_account.Invoicing.teams_pk, email)
        my_account.Invoicing.delete_email(res_creation['data']['id'])

        self.assertEqual(res_creation['status'], 201)

    def test_get_emails_details(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.get_email_details(email_pk)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()

        data = {'name': 'UNITTEST - update'}
        res = my_account.Invoicing.update_email(email_pk, data)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_email(self):
        """ Test that 204 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 204)

    def test_send_test_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.send_test_email(email_pk)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_apply_email(self):
        """ Test that 200 is returned """
        # * OK

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.apply_email(email_pk)

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

        smtp_pk = my_account.Invoicing.create_email_smtp(data)['data']['id']
        return smtp_pk

    def test_get_emails_smtp(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_emails_smtp_list()

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

        res = my_account.Invoicing.create_email_smtp(data)
        my_account.Invoicing.delete_email_smtp(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_email_smtp_details(self):
        """ Test that 200 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()

        res = my_account.Invoicing.get_email_smtp_details(smtp_pk)
        my_account.Invoicing.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email_smtp(self):
        """ Test that 200 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()

        data = {"from_name": "UNITTEST - Update"}
        res = my_account.Invoicing.update_email_smtp(smtp_pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_email_smtp(self):
        """ Test that 204 is returned """
        # * OK

        smtp_pk = self._create_email_smtp_return_pk()
        res = my_account.Invoicing.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 204)

    def test_send_test_email_smtp(self):
        """ Test that 200 is returned """

        smtp_pk = self._create_email_smtp_return_pk()
        res = my_account.Invoicing.send_test_email_smtp(smtp_pk)

        my_account.Invoicing.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 200)

    #### Files ####

    ### Folders ###
    def _create_folder_return_pk(self):
        """ Create a folder and return the pk """

        folder = {
            "name": "UNITTEST"
        }

        folder_pk = my_account.Invoicing.create_folder(project_pk, folder)['data']['pk']
        return folder_pk

    def test_get_folders_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_folder_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_folder_details(self):
        """ Test that 200 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()

        res = my_account.Invoicing.get_folder_details(folder_pk)
        my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_create_folder(self):
        """ Test that 201 is returned """
        # * OK

        folder = {
            "name": "UNITTEST"
        }

        res = my_account.Invoicing.create_folder(project_pk, folder)
        my_account.Invoicing.delete_folder(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_update_folder(self):
        """ Test that 201 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()

        folder_updated = {
            "name": "UNITTEST - UPDATE"
        }

        res = my_account.Invoicing.update_folder(folder_pk, folder_updated)
        my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_folder(self):
        """ Test that 200 is returned """
        # * OK

        folder_pk = self._create_folder_return_pk()
        res = my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 204)

    ### Files ###
    def test_get_files_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_files_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_files_details(self):
        """ Test that 200 is returned """
        # * OK

        file_pk = my_account.Invoicing.get_files_list(project_pk)['data'][0]['pk']
        res = my_account.Invoicing.get_file_details(file_pk)

        self.assertEqual(res['status'], 200)

    #### Banks ####
    def test_get_banks_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_banks_list()

        self.assertEqual(res['status'], 200)

    def test_get_banks_details(self):
        """ Test that 200 is returned """
        # * OK

        bank_pk = my_account.Invoicing.get_banks_list()['data'][0]['id']
        res = my_account.Invoicing.get_bank_details(bank_pk)

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

        res = my_account.Invoicing.create_bank(data)
        my_account.Invoicing.delete_bank(res['data']['id'])

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

        bank_pk = my_account.Invoicing.create_bank(bank)['data']['id']

        updated_bank = {
            "name": "UNITTEST - update"
        }

        res = my_account.Invoicing.update_bank(bank_pk, updated_bank)
        my_account.Invoicing.delete_bank(bank_pk)

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

        bank_pk = my_account.Invoicing.create_bank(bank)['data']['id']
        res = my_account.Invoicing.delete_bank(bank_pk)

        self.assertEqual(res['status'], 204)

    ##### Reports ####

    ### Reports ###
    def _create_report_return_pk(self):
        """ Create a report and return the pk """
        # * OK

        report = {
            "name": "UNITTEST",
            "project": project_pk,
            "type": "billed_progress_report",
            "lang": "fr"
        }

        res = my_account.Invoicing.create_report(report)['data']['pk']
        return res

    def test_get_reports_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_reports_list()

        self.assertEqual(res['status'], 200)

    def test_get_reports_project_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_reports_project_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_reports(self):
        """ Test that 201 is returned """
        # * OK

        report = {
            "name": "UNITTEST_billed_progress",
            "project": project_pk,
            "type": "billed_progress_report",
            "lang": "fr"
        }

        res = my_account.Invoicing.create_report(report)

        self.assertEqual(res['status'], 201)

    def test_get_report_details(self):
        """ Test that 200 is returned """
        # * OK

        report_pk = self._create_report_return_pk()
        res = my_account.Invoicing.get_report_details(report_pk)
        my_account.Invoicing.delete_report(report_pk)

        self.assertEqual(res['status'], 200)

    def update_report(self):
        """ Test that 200 is returned """
        # * OK

        report_pk = self._create_report_return_pk()

        report_up = {
            "name": "UPDATED UNITTEST"
        }

        res = my_account.Invoicing.update_report(report_pk, report_up)
        my_account.Invoicing.delete_report(report_pk)

        self.assertEqual(res['status'], 200)

    def generate_report(self):
        """ Test that 200 is returned """
        # * OK

        report_pk = self._create_report_return_pk()

        data = {
            "pk": report_pk,
            "project": project_pk
        }

        res = my_account.Invoicing.generate_report(data)

        self.assertEqual(res['status'], 200)

    ### Templates ###
    def _create_template_return_pk(self):
        """ Create a template and return the pk """
        # * OK

        template = {
            "name": "UNITTEST",
            "type": "progress",
            "lang": "fr",
            "orientation": "portrait"
        }

        return my_account.Invoicing.create_template(team_pk, template)['data']['pk']

    def test_get_templates_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Invoicing.get_templates_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_get_template_details(self):
        """ Test that 200 is returned """
        # * OK

        template_pk = self._create_template_return_pk()

        res = my_account.Invoicing.get_template_details(template_pk)

        self.assertEqual(res['status'], 200)

    def test_create_template(self):
        """ Test that 201 is returned """
        # * OK

        template = {
            "name": "UNITTEST",
            "type": "progress",
            "lang": "fr",
            "orientation": "portrait"
        }

        res = my_account.Invoicing.create_template(team_pk, template)

        self.assertEqual(res['status'], 201)

    def test_update_template(self):
        """ Test that 200 is returned """
        # * OK

        template_pk = self._create_template_return_pk()

        template_up = {
            "name": "UPDATED"
        }

        res = my_account.Invoicing.update_template(template_pk, template_up)
        my_account.Invoicing.delete_template(template_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_template(self):
        """ Test that 204 is returned """
        # * OK

        template_pk = self._create_template_return_pk()
        res = my_account.Invoicing.delete_template(template_pk)

        self.assertEqual(res['status'], 204)

    def test_duplicate_template(self):
        """ Test that 201 is returned """
        # * OK

        template_pk = self._create_template_return_pk()
        res = my_account.Invoicing.duplicate_template(template_pk)

        my_account.Invoicing.delete_template(template_pk)
        my_account.Invoicing.delete_template(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    #### Styleguides ####
    def _create_styleguide_return_pk(self):
        """ Create a styleguide and return pk """
        # * OK

        data = {
            "name": "UNITTEST"
        }

        return my_account.Invoicing.create_styleguide(data)['data']['id']

    def test_get_styleguides_list(self):
        """ Test that 200 is returned"""
        # * OK

        res = my_account.Invoicing.get_styleguides_list()

        self.assertEqual(res['status'], 200)

    def test_create_styleguide(self):
        """ Test that 201 is returned """
        # * OK

        data = {
            "name": "UNITTEST"
        }

        res = my_account.Invoicing.create_styleguide(data)
        my_account.Invoicing.delete_styleguide(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_styleguide_details(self):
        """ Test that 200 is returned """
        # * OK

        styleguide_pk = self._create_styleguide_return_pk()
        res = my_account.Invoicing.get_styleguide_details(styleguide_pk)
        my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 200)

    def test_update_styleguide(self):
        """ Test that 200 is returned """
        # * OK

        styleguide_pk = self._create_styleguide_return_pk()

        data_up = {
            "name": "UNITTEST - UPDATED"
        }
        res = my_account.Invoicing.update_styleguide(styleguide_pk, data_up)
        my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_styleguide(self):
        """ Test that 204 is returned """
        # * OK

        styleguide_pk = self._create_styleguide_return_pk()
        res = my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 204)

##### DELIVERABLES #####

    #### Zones ####
    def _create_zone_return_pk(self):
        """ Create a zone and return the pk 

        :return: {"pk": zone_pk, "area_pk": area_pk}
        """

        area_pk = self._create_area_return_pk()

        data = {
            "name": "UNITTEST",
            "area": area_pk,
            "progress": 0,
            "is_annex": True,
            "internal_code": "string",
            "client_code": "string",
            "surface_area": 0,
            "default_surface_price": 0,
            "num_units": 0
        }

        res = my_account.Deliverables.create_zone(area_pk, data)
        return {"pk": res['data']['id'], "area_pk": area_pk}

    def test_export_zones(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.export_phase(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_zones_list(self):
        """ Test that 200 is returned """
        area_pk = self._create_area_return_pk()

        res = my_account.Deliverables.get_zones_list(area_pk)
        my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 200)

    def test_create_zone(self):
        """ Test that 201 is returned """

        area_pk = self._create_area_return_pk()

        data = {
            "name": "string",
            "area": area_pk,
            "progress": 0,
            "is_annex": True,
            "internal_code": "string",
            "client_code": "string",
            "surface_area": 0,
            "default_surface_price": 0,
            "num_units": 0
        }

        res = my_account.Deliverables.create_zone(area_pk, data)

        self.assertEqual(res['status'], 201)

    def test_get_zone_details(self):
        """ Test that 200 is returned """
        res_create = self._create_zone_return_pk()

        res = my_account.Deliverables.get_zone_details(res_create['pk'])

        my_account.Deliverables.delete_zone(res_create['pk'])
        my_account.Deliverables.delete_area(res_create['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_update_zone(self):
        """ Test that 200 is returned """
        res_create = self._create_zone_return_pk()

        data_up = {
            "name": "update"
        }

        res = my_account.Deliverables.update_zone(res_create['pk'], data_up)

        my_account.Deliverables.delete_zone(res_create['pk'])
        my_account.Deliverables.delete_area(res_create['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_delete_zone(self):
        """ Test that 204 is returned """
        area_pk = self._create_area_return_pk()

        data = {
            "name": "string",
            "area": area_pk,
            "progress": 0,
            "is_annex": True,
            "internal_code": "string",
            "client_code": "string",
            "surface_area": 0,
            "default_surface_price": 0,
            "num_units": 0
        }

        zone_pk = my_account.Deliverables.create_zone(area_pk, data)['data']['id']
        res = my_account.Deliverables.delete_zone(zone_pk)

        my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 204)

    #### Areas ####

    def _create_area_return_pk(self):
        """ Create an area and return the pk """

        area = {
            "name": "test",
            "project": project_pk,
            "surface_area": 30
        }

        return my_account.Deliverables.create_areas(project_pk, area)['data']['id']

    def test_get_areas_list(self):
        """ Test that 200 is returned """
        # * OK
        res = my_account.Deliverables.get_areas_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_area(self):
        """ Test that 201 is returned """
        # * OK

        area = {
            "name": "UNITTEST",
            "project": project_pk,
            "surface_area": 30
        }

        res = my_account.Deliverables.create_areas(project_pk, area)
        my_account.Deliverables.delete_area(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_area_details(self):
        """ Test that 200 is returned """
        # * OK

        area_pk = self._create_area_return_pk()

        res = my_account.Deliverables.get_areas_details(area_pk)
        my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 200)

    # def test_update_area(self):
    #     """ Test that 200 is returned """
    #     #! Do not pass (403)

    #     area_pk = self._create_area_return_pk()

    #     area_up = {
    #         "name": "UPDATE",
    #     }

    #     res = my_account.Deliverables.create_areas(area_pk, area_up)
    #     my_account.Deliverables.delete_area(area_pk)

    #     self.assertEqual(res['status'], 200)

    def test_delete_area(self):
        """ Test that 204 is returned """
        # * OK

        area_pk = self._create_area_return_pk()
        res = my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 204)

    #### Phases ####
    def test_get_phases_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Deliverables.get_phases_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_phases_projections_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Deliverables.get_phases_projections_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_export_phase(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Deliverables.export_phase(project_pk)

        self.assertEqual(res['status'], 200)

    #### Milestone ####
    def _create_milestone_return_pk(self):
        """ Create a milestone and return the pk """

        data = {
            "title": "UNITTEST",
            "project": project_pk,
            "date": "30-04-2021",
            "description": "string",
            "in_timeline": True
        }

        return my_account.Deliverables.create_milestone(data)['data']['pk']

    def test_get_milestones_list(self):
        """ Test that 200 is returned """
        # * OK

        res = my_account.Deliverables.get_milestones_list()

        self.assertEqual(res['status'], 200)

    # def test_get_milestone_details(self):
    #     """ Test that 200 is returned """
    #     #! Do not pass, 403

    #     milestone_pk = self._create_milestone_return_pk()
    #     res = my_account.Deliverables.get_milestone_details(milestone_pk)

    #     self.assertEqual(res['status'], 200)

    def test_create_milestone(self):
        """ Test that 201 is returned """
        # * OK

        data = {
            "title": "UNITTEST",
            "project": project_pk,
            "date": "30-04-2021",
            "description": "string",
            "in_timeline": True
        }

        res = my_account.Deliverables.create_milestone(data)

        self.assertEqual(res['status'], 201)

    def test_update_milestone(self):
        """ Test that 200 is returned """
        # * OK

        milestone_pk = self._create_milestone_return_pk()

        data = {
            "title": "UPDATE"
        }

        res = my_account.Deliverables.update_milestone(milestone_pk, data)

        self.assertEqual(res['status'], 200)

    #### Fees ####
    def _create_fee_return_pk(self):
        """ Create a fee and return pk """

        data = {
            "title": "string",
            "amount_base": 0,
            "amount_current": 0,
            "progress": 0,
            "in_timeline": True
        }

        return my_account.Deliverables.create_fee(project_pk, data)['data']['pk']

    def test_get_fees_bracket_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_bracket_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_export_project_fees(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.export_project_fees(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_fee_project_version_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fee_project_version_list()

        self.assertEqual(res['status'], 200)

    def test_get_fees_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_fee(self):
        """ Test that 201 is returned """

        data = {
            "title": "string",
            "amount_base": 0,
            "amount_current": 0,
            "progress": 0,
            "in_timeline": True
        }

        res = my_account.Deliverables.create_fee(project_pk, data)

        self.assertEqual(res['status'], 201)

    def test_get_fees_projection_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_projection_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_fees_project_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_project_list()

        self.assertEqual(res['status'], 200)

    def test_validate_fees_costs(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.validation_fees_costs(project_pk)

        self.assertEqual(res['status'], 200)

    def test_validate_fees_ffne(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.validation_fees_ffne(project_pk)

        self.assertEqual(res['status'], 200)

    def test_validate_fees_production(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.validation_fees_production(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_fees_zones_list(self):
        """ Test that 200 is returend """
        res = my_account.Deliverables.get_fees_zones_list()

        self.assertEqual(res['status'], 200)

    #### Plans ####
    # def _create_plan_return_pk(self):
    #     """ Create plan and return pk """

    #     zone_pk = self._create_zone_return_pk()

    #     data = {
    #         "zone": zone_pk['pk'],
    #         "name_fr": "string",
    #         "name_en": "string",
    #         "plan_format": "string",
    #         "scale": "string",
    #         "level": "string",
    #         "lot": 0,
    #         "is_default": True,
    #         "progress": 0,
    #         "sub_zone_code": "string",
    #         "plan_code": "string",
    #         "project": project_pk,
    #         "area": zone_pk['area_pk'],
    #         "code": "string",
    #         "custom_field_1": "string",
    #         "custom_field_2": "string",
    #         "custom_field_3": "string"
    #     }

    #     res = my_account.Deliverables.create_plan(project_pk, data)['data']['id']

    #     return {"pk": res, "area_pk": area_pk, "zone_pk": zone_pk}

    def test_get_plans_list_action(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_plans_list_action(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_plans_list_action(self):
        """ Test that 201 is returned """
        res = my_account.Deliverables.create_plans_list_action(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_plans_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_plans_list(project_pk)

        self.assertEqual(res['status'], 200)

    # def test_create_plan(self):
    #     """ Test that 201 is returned """

    #     zone_pk = self._create_zone_return_pk()

    #     data = {
    #         "zone": zone_pk['pk'],
    #         "name_fr": "string",
    #         "name_en": "string",
    #         "plan_format": "string",
    #         "scale": "string",
    #         "level": "string",
    #         "lot": 0,
    #         "is_default": True,
    #         "progress": 0,
    #         "sub_zone_code": "string",
    #         "plan_code": "string",
    #         "project": project_pk,
    #         "area": zone_pk['area_pk'],
    #         "code": "client"
    #     }

    #     res = my_account.Deliverables.create_plan(project_pk, data)

    #     my_account.Deliverables.delete_zone(zone_pk['pk'])
    #     my_account.Deliverables.delete_area(zone_pk['area_pk'])
    #     # my_account.Deliverables.delete_plan(res['data']['pk'])

    #     self.assertEqual(res['status'], 201)

    #### Prescription ####
    def _create_prescription_return_pk(self):
        """ Create a prescription and return pk 

        :return: {"pk": pk, "area_pk": area_pk, "fee_pk": fee_pk}

        """

        fee_pk = self._create_fee_return_pk()
        area_pk = self._create_area_return_pk()

        data = {
            "fee_pct": "10",
            "fee": fee_pk,
            "date": "04-05-2021",
            "description": "UNITTEST",
            "area": area_pk,
        }

        pk = my_account.Deliverables.create_prescription(project_pk, data)['data']['id']
        return {"pk": pk, "area_pk": area_pk, "fee_pk": fee_pk}

    def test_get_prescription_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_prescriptions_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_prescription(self):
        """ Test that 201 is returned """

        fee_pk = self._create_fee_return_pk()
        area_pk = self._create_area_return_pk()

        data = {
            "fee_pct": "10",
            "fee": fee_pk,
            "date": "04-05-2021",
            "description": "UNITTEST",
            "area": area_pk,
        }

        res = my_account.Deliverables.create_prescription(project_pk, data)
        my_account.Deliverables.delete_prescription(res['data']['id'])
        my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 201)

    def test_get_prescription_details(self):
        """ Test that 200 is returned """

        res_creation = self._create_prescription_return_pk()

        res = my_account.Deliverables.get_prescriptions_details(res_creation['pk'])
        my_account.Deliverables.delete_prescription(res_creation['pk'])
        my_account.Deliverables.delete_area(res_creation['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_update_prescription(self):
        """ Test that 200 is returned """

        res_creation = self._create_prescription_return_pk()

        data = {
            "description": "UPDATED"
        }

        res = my_account.Deliverables.update_prescriptions(res_creation['pk'], data)
        my_account.Deliverables.delete_prescription(res_creation['pk'])
        my_account.Deliverables.delete_area(res_creation['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_delete_prescription(self):
        """ Test that 204 is returned """

        res_creation = self._create_prescription_return_pk()

        res = my_account.Deliverables.delete_prescription(res_creation['pk'])

        my_account.Deliverables.delete_area(res_creation['area_pk'])

        self.assertEqual(res['status'], 204)


if __name__ == '__main__':
    unittest.main()
