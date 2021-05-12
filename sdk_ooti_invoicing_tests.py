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

"""

#* Reports of bugs or failed tests 


test_update_area -> 403
test_get_milestone_details -> 403
test_apply_defaults_phasesets -> 404
test_apply_defaults_plansets -> 404
test_duplicate_defaults_plan -> 500
test_delete_defaults_plan -> 500
test_generate_contracts_org -> 403
test_update_contract_item -> 500
test_delete_file -> Cannot create file with SDK
test_generate_report -> 200

"""


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

        res_get = my_account.Invoicing.get_invoices_list()

        self.assertEqual(res_get['status'], 200)

    def test_get_invoice_details(self):
        """ Test that 200 is returned """

        invoice_pk = my_account.Invoicing.get_invoices_list()['data'][0]['pk']
        res_details = my_account.Invoicing.get_invoice_details(invoice_pk)

        self.assertEqual(res_details['status'], 200)

    def test_get_invoices_sent_valid_list(self):
        """ Test that 200 is returned """

        res_sent_valid = my_account.Invoicing.get_invoices_sent_valid_list(team_pk)

        self.assertEqual(res_sent_valid['status'], 200)

    def test_create_invoice(self):
        """ Test that 201 is returned """

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

        invoice_pk = self._create_invoice_return_pk()

        res_validate = my_account.Invoicing.validate_invoice(invoice_pk)

        self.assertEqual(res_validate['status'], 200)

    def test_send_invoice(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()

        res_send = my_account.Invoicing.send_invoice(invoice_pk)

        self.assertEqual(res_send['status'], 200)

    def test_close_invoice(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()

        res_close = my_account.Invoicing.cancel_invoice(invoice_pk)

        self.assertEqual(res_close['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """

        invoice_pk = self._create_invoice_return_pk()
        res_items = my_account.Invoicing.get_invoice_items(invoice_pk)

        self.assertEqual(res_items['status'], 200)

    def test_create_invoice_item(self):
        """ Test that 201 is returned """

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

        res = my_account.Invoicing.get_credit_notes_list()

        self.assertEqual(res['status'], 200)

    def test_get_credit_notes_sent_valid(self):
        """ Test that 200 is returned """
        res = my_account.Invoicing.get_credit_notes_sent_valid_list(team_pk)

        self.assertEqual(res['status'], 200)

    ##### Payments #####

    def test_get_payments_list(self):
        """ Test that 200 is returned """

        res_payments = my_account.Invoicing.get_payments_list()

        self.assertEqual(res_payments['status'], 200)

    def test_get_payments_details(self):
        """ Test that 200 is returned """

        payment_pk = my_account.Invoicing.get_payments_list()['data'][0]['pk']
        res_details = my_account.Invoicing.get_payment_details(payment_pk)

        self.assertEqual(res_details['status'], 200)

    def test_create_payment(self):
        """ Test that 201 is returned """

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

        res = my_account.Invoicing.get_currencies_list()
        self.assertEqual(res['status'], 200)

    def test_create_currency(self):
        """ Test that 201 is returned """

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

        # get an id
        res_get = my_account.Invoicing.get_currencies_list()
        id_currency = res_get["data"][0]['pk']

        # get details
        res_details = my_account.Invoicing.get_currency_details(id_currency)
        self.assertEqual(res_details["status"], 200)

    def test_update_currency(self):
        """ Test that 200 is returned """

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

        res_get = my_account.Invoicing.get_clients_list(team_pk)

        self.assertEqual(res_get['status'], 200)

    def test_get_client_details(self):
        """ Test that 200 is returned """

        res_get_list = my_account.Invoicing.get_clients_list(team_pk)

        client_pk = res_get_list['data'][0]['pk']
        res_get = my_account.Invoicing.get_clients_details(client_pk)

        self.assertEqual(res_get['status'], 200)

    def test_create_client(self):
        """ Test that 201 is returned """

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

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "vdebande@ooti.co",
            "email_from": "vdebande@ooti.co",
            "name_from": "Vincent de OOTI"
        }

        email_pk = my_account.Invoicing.create_email(email)['data']['id']
        return email_pk

    def test_get_emails_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_emails_list()

        self.assertEqual(res['status'], 200)

    def test_create_email(self):
        """ Test that 201 is returned """

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "vdebande@ooti.co",
            "email_from": "vdebande@ooti.co",
            "name_from": "Vincent de OOTI"
        }

        res_creation = my_account.Invoicing.create_email(email)
        my_account.Invoicing.delete_email(res_creation['data']['id'])

        self.assertEqual(res_creation['status'], 201)

    def test_get_emails_details(self):
        """ Test that 200 is returned """

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.get_email_details(email_pk)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email(self):
        """ Test that 200 is returned """

        email_pk = self._create_email_return_pk()

        data = {'name': 'UNITTEST - update'}
        res = my_account.Invoicing.update_email(email_pk, data)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_email(self):
        """ Test that 204 is returned """

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 204)

    def test_send_test_email(self):
        """ Test that 200 is returned """

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.send_test_email(email_pk)
        my_account.Invoicing.delete_email(email_pk)

        self.assertEqual(res['status'], 200)

    def test_apply_email(self):
        """ Test that 200 is returned """

        email_pk = self._create_email_return_pk()
        res = my_account.Invoicing.apply_email(email_pk)

        self.assertEqual(res['status'], 200)

    ### smtp ###
    def _create_email_smtp_return_pk(self):
        """ Create email smtp and return pk """

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

        res = my_account.Invoicing.get_emails_smtp_list()

        self.assertEqual(res['status'], 200)

    def test_create_email_smtp(self):
        """ Test that 201 is returned """

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

        smtp_pk = self._create_email_smtp_return_pk()

        res = my_account.Invoicing.get_email_smtp_details(smtp_pk)
        my_account.Invoicing.delete_email_smtp(smtp_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email_smtp(self):
        """ Test that 200 is returned """

        smtp_pk = self._create_email_smtp_return_pk()

        data = {"from_name": "UNITTEST - Update"}
        res = my_account.Invoicing.update_email_smtp(smtp_pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_email_smtp(self):
        """ Test that 204 is returned """

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

        res = my_account.Invoicing.get_folder_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_folder_details(self):
        """ Test that 200 is returned """

        folder_pk = self._create_folder_return_pk()

        res = my_account.Invoicing.get_folder_details(folder_pk)
        my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_create_folder(self):
        """ Test that 201 is returned """

        folder = {
            "name": "UNITTEST"
        }

        res = my_account.Invoicing.create_folder(project_pk, folder)
        my_account.Invoicing.delete_folder(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_update_folder(self):
        """ Test that 201 is returned """

        folder_pk = self._create_folder_return_pk()

        folder_updated = {
            "name": "UNITTEST - UPDATE"
        }

        res = my_account.Invoicing.update_folder(folder_pk, folder_updated)
        my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_folder(self):
        """ Test that 200 is returned """

        folder_pk = self._create_folder_return_pk()
        res = my_account.Invoicing.delete_folder(folder_pk)

        self.assertEqual(res['status'], 204)

    ### Files ###
    def test_get_files_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_files_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_files_details(self):
        """ Test that 200 is returned """

        file_pk = my_account.Invoicing.get_files_list(project_pk)['data'][0]['pk']
        res = my_account.Invoicing.get_file_details(file_pk)

        self.assertEqual(res['status'], 200)

    # def test_delete_file(self, pk):
    #     #! Cannot create file with sdk
    #     """ Test that 204 is returned """

    #     pk = 0

    #     res = my_account.Invoicing.delete_file(pk)

    #     self.assertEqual(res['status'], 204)

    #### Banks ####

    def test_get_banks_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_banks_list()

        self.assertEqual(res['status'], 200)

    def test_get_banks_details(self):
        """ Test that 200 is returned """

        bank_pk = my_account.Invoicing.get_banks_list()['data'][0]['id']
        res = my_account.Invoicing.get_bank_details(bank_pk)

        self.assertEqual(res['status'], 200)

    def test_create_bank(self):
        """ Test that 201 is returned """

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

        res = my_account.Invoicing.get_reports_list()

        self.assertEqual(res['status'], 200)

    def test_get_reports_project_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_reports_project_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_reports(self):
        """ Test that 201 is returned """

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

        report_pk = self._create_report_return_pk()
        res = my_account.Invoicing.get_report_details(report_pk)
        my_account.Invoicing.delete_report(report_pk)

        self.assertEqual(res['status'], 200)

    def test_update_report(self):
        """ Test that 200 is returned """

        report_pk = self._create_report_return_pk()

        report_up = {
            "name": "UPDATED UNITTEST"
        }

        res = my_account.Invoicing.update_report(report_pk, report_up)
        my_account.Invoicing.delete_report(report_pk)

        self.assertEqual(res['status'], 200)

    # def test_generate_report(self):
    #     #! 200
    #     """ Test that 201 is returned """

    #     report_pk = self._create_report_return_pk()

    #     data = {
    #         "pk": report_pk,
    #         "project": project_pk
    #     }

    #     res = my_account.Invoicing.generate_report(data)
    #     print(res)

    #     self.assertEqual(res['status'], 201)

    def test_delete_report(self):
        """ Test that 204 is returned """

        pk = self._create_report_return_pk()

        res = my_account.Invoicing.delete_report(pk)

        self.assertEqual(res['status'], 204)

    ### Templates ###
    def _create_template_return_pk(self):
        """ Create a template and return the pk """

        template = {
            "name": "UNITTEST",
            "type": "progress",
            "lang": "fr",
            "orientation": "portrait"
        }

        return my_account.Invoicing.create_template(team_pk, template)['data']['pk']

    def test_get_templates_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_templates_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_get_template_details(self):
        """ Test that 200 is returned """

        template_pk = self._create_template_return_pk()

        res = my_account.Invoicing.get_template_details(template_pk)

        self.assertEqual(res['status'], 200)

    def test_create_template(self):
        """ Test that 201 is returned """

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

        template_pk = self._create_template_return_pk()

        template_up = {
            "name": "UPDATED"
        }

        res = my_account.Invoicing.update_template(template_pk, template_up)
        my_account.Invoicing.delete_template(template_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_template(self):
        """ Test that 204 is returned """

        template_pk = self._create_template_return_pk()
        res = my_account.Invoicing.delete_template(template_pk)

        self.assertEqual(res['status'], 204)

    def test_duplicate_template(self):
        """ Test that 201 is returned """

        template_pk = self._create_template_return_pk()
        res = my_account.Invoicing.duplicate_template(template_pk)

        my_account.Invoicing.delete_template(template_pk)
        my_account.Invoicing.delete_template(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    #### Revenue ####
    def _create_revenue_return_pk(self):
        """ Create revenue and return pk"""

        data = {
            "month": 5,
            "team": team_pk,
            "title": "UNITTEST",
            "months": []
        }

        return my_account.Invoicing.create_revenue(data)['data']['id']

    #! 500
    # def _create_revenue_month_return_pk(self):
    #     """ Create revenue month and return pk"""

    #     data = {
    #         "team": team_pk,
    #     }

    #     return my_account.Invoicing.create_revenue_month(data)['data']['id']

    def test_get_revenue_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_revenue_list()

        self.assertEqual(res['status'], 200)

    def test_create_revenue(self):
        """ Test that 201 is returned """

        data = {
            "month": 5,
            "team": team_pk,
            "title": "UNITTEST",
            "months": []
        }

        res = my_account.Invoicing.create_revenue(data)

        self.assertEqual(res['status'], 201)

    def test_get_revenue_details(self):
        """ Test that 200 is returned """

        pk = self._create_revenue_return_pk()

        res = my_account.Invoicing.get_revenue_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_revenue(self):
        """ Test that 200 is returned """

        pk = self._create_revenue_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Invoicing.update_revenue(pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_revenue(self):
        """ Test that 204 is returned """

        pk = self._create_revenue_return_pk()

        res = my_account.Invoicing.delete_revenue(pk)

        self.assertEqual(res['status'], 204)

    def test_get_revenue_month_list(self):
        """ Test that 200 is returned """

        res = my_account.Invoicing.get_revenue_month_list()

        self.assertEqual(res['status'], 200)

    # def test_create_revenue_month(self):
    #     #! 500
    #     """ Test that 201 is returned """

    #     data = {
    #         "team": team_pk
    #     }

    #     res = my_account.Invoicing.create_revenue_month(data)
    #     print(res)

    #     self.assertEqual(res['status'], 201)

    #! 500 : cannot create obj

    # def test_get_revenue_month_details(self):
    #     """ Test that 200 is returned """

    #     pk = self._create_revenue_month_return_pk()

    #     res = my_account.Invoicing.get_revenue_month_details(pk)

    #     self.assertEqual(res['status'], 200)

    # def test_update_revenue_month(self):
    #     """ Test that 200 is returned """

    #     pk = self._create_revenue_month_return_pk()

    #     data = {
    #         "amont_actual": 1
    #     }

    #     res = my_account.Invoicing.update_revenue_month(pk, data)

    #     self.assertEqual(res['status'], 200)

    # def test_delete_revenue_month(self):
    #     """ Test that 204 is returned """

    #     pk = self._create_revenue_month_return_pk()

    #     res = my_account.Invoicing.delete_revenue_month(pk)

    #     self.assertEqual(res['status'], 204)

    #### Styleguides ####

    def _create_styleguide_return_pk(self):
        """ Create a styleguide and return pk """

        data = {
            "name": "UNITTEST"
        }

        return my_account.Invoicing.create_styleguide(data)['data']['id']

    def test_get_styleguides_list(self):
        """ Test that 200 is returned"""

        res = my_account.Invoicing.get_styleguides_list()

        self.assertEqual(res['status'], 200)

    def test_create_styleguide(self):
        """ Test that 201 is returned """

        data = {
            "name": "UNITTEST"
        }

        res = my_account.Invoicing.create_styleguide(data)
        my_account.Invoicing.delete_styleguide(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_styleguide_details(self):
        """ Test that 200 is returned """

        styleguide_pk = self._create_styleguide_return_pk()
        res = my_account.Invoicing.get_styleguide_details(styleguide_pk)
        my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 200)

    def test_update_styleguide(self):
        """ Test that 200 is returned """

        styleguide_pk = self._create_styleguide_return_pk()

        data_up = {
            "name": "UNITTEST - UPDATED"
        }
        res = my_account.Invoicing.update_styleguide(styleguide_pk, data_up)
        my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_styleguide(self):
        """ Test that 204 is returned """

        styleguide_pk = self._create_styleguide_return_pk()
        res = my_account.Invoicing.delete_styleguide(styleguide_pk)

        self.assertEqual(res['status'], 204)


if __name__ == '__main__':
    unittest.main()
