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
currency_pk = my_account.Invoicing.get_currencies_list()['data'][0]['pk']
project_pk = my_account.get_projects_list()['data'][0]['id']


# invoice_payment_pk = my_account.Invoicing.get_payment_details(584321)
# print(invoice_payment_pk)
# quit()
class TestPayements(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        cls.currency_pk = testHelper._create_currency_if_none()
        cls.client_pk = testHelper._create_client_return_pk(cls.team_pk, cls.currency_pk)
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.invoice_pk = testHelper._create_invoice_return_pk(cls.team_pk, cls.project_pk)
        cls.payment_pk = testHelper._create_payment_return_pk(cls.team_pk, cls.invoice_pk, cls.currency_pk)

    def test_get_payments_list(self):
        """ Test that 200 is returned """

        res_payments = my_account.Payements.get_payments_list()

        self.assertEqual(res_payments['status'], 200)

    def test_get_payments_details(self):
        """ Test that 200 is returned """

        res_details = my_account.Payements.get_payment_details(self.payment_pk)

        self.assertEqual(res_details['status'], 200)

    def test_create_payment(self):
        """ Test that 201 is returned """

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = my_account.Payements.create_invoice_item(self.invoice_pk, invoice_item)
        my_account.Payements.validate_invoice(self.invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "team": self.team_pk,
            "project": self.project_pk,
            "invoice": self.invoice_pk,
        }

        res_creation_payment = my_account.Payements.create_payment(self.team_pk, payment)
        self.assertEqual(res_creation_payment['status'], 201)

    def test_update_payment(self):
        """ Test that 200 is returned """

        update = {
            'date': '20-04-2021',
        }

        res_update_payment = my_account.Payements.update_payment(self.payment_pk, update)
        self.assertEqual(res_update_payment['status'], 200)

    def test_update_amount_payment_invoice(self):
        """ Test that 200 is returned """

        update = {
            "amount": 10
        }

        my_account.Payements.update_payment(self.payment_pk, update)
        invoice_payment_pk = my_account.Payements.get_payment_details(self.payment_pk)['data']['invoice_payments'][0]['pk']
        res_update_amount_invoice = my_account.Payements.update_payment_invoice(invoice_payment_pk, update)
        self.assertEqual(res_update_amount_invoice['status'], 200)


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

        res_get = my_account.Payements.get_invoices_list()

        self.assertEqual(res_get['status'], 200)

    def test_get_invoice_details(self):
        """ Test that 200 is returned """

        res_details = my_account.Payements.get_invoice_details(self.invoice_pk)

        self.assertEqual(res_details['status'], 200)

    def test_get_invoices_sent_valid_list(self):
        """ Test that 200 is returned """

        res_sent_valid = my_account.Payements.get_invoices_sent_valid_list(self.team_pk)

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

        res_creation = my_account.Payements.create_invoice(self.team_pk, invoice_project)
        self.assertEqual(res_creation['status'], 201)

        # Test with client in paylaod
        invoice_client = {
            "client": self.client_pk,
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": 'UNITTEST',
            "type": 4
        }

        res_creation = my_account.Payements.create_invoice(self.team_pk, invoice_client)
        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice(self):
        """ Test that 200 is returned """

        invoice_updated = {
            "invoice_date": "20-04-2021",
            "references": "This is my new reference!!!",
            "purchase_order": "Hey this is the purchase order"
        }

        res_update = my_account.Payements.update_invoice(self.invoice_pk_not_validated, invoice_updated)
        self.assertEqual(res_update['status'], 200)

    def test_validate_invoice(self):
        """ Test that 200 is returned """

        res_validate = my_account.Payements.validate_invoice(self.invoice_pk_not_validated)
        self.assertEqual(res_validate['status'], 200)

    def test_send_invoice(self):
        """ Test that 200 is returned """

        res_send = my_account.Payements.send_invoice(self.invoice_pk)
        self.assertEqual(res_send['status'], 200)

    def test_close_invoice(self):
        """ Test that 200 is returned """

        res_close = my_account.Payements.cancel_invoice(self.invoice_pk)
        self.assertEqual(res_close['status'], 200)

    def test_get_invoice_items(self):
        """ Test that 200 is returned """

        res_items = my_account.Payements.get_invoice_items(self.invoice_pk)
        self.assertEqual(res_items['status'], 200)

    def test_create_invoice_item(self):
        """ Test that 201 is returned """

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation = my_account.Payements.create_invoice_item(self.invoice_pk, invoice_item)
        self.assertEqual(res_creation['status'], 201)

    def test_update_invoice_item(self):
        """ Test that 200 is returned """

        update = {
            "amount": 1200
        }

        res_update = my_account.Payements.update_invoice_item(self.invoice_item_pk_not_validated, update)
        self.assertEqual(res_update['status'], 200)

    def test_delete_invoice_item(self):
        """ Test that 204 is returned """

        res_delete = my_account.Payements.delete_invoice_item(self.invoice_item_pk)
        self.assertEqual(res_delete['status'], 204)

    def test_get_credit_notes(self):
        """ Test that 200 is returned """

        res = my_account.Payements.get_credit_notes_list()
        self.assertEqual(res['status'], 200)

    def test_get_credit_notes_sent_valid(self):
        """ Test that 200 is returned """
        res = my_account.Payements.get_credit_notes_sent_valid_list(self.team_pk)

        self.assertEqual(res['status'], 200)


class TestCurrencies(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
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


class TestClients(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
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


class TestEmails(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
        cls.email_pk = testHelper._create_email_return_pk()
        cls.smtp_pk = testHelper._create_email_smtp_return_pk()

    ### Classic ###

    def test_get_emails_list(self):
        """ Test that 200 is returned """

        res = my_account.Emails.get_emails_list()
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

        res_creation = my_account.Emails.create_email(email)
        my_account.Emails.delete_email(res_creation['data']['id'])

        self.assertEqual(res_creation['status'], 201)

    def test_get_emails_details(self):
        """ Test that 200 is returned """

        res = my_account.Emails.get_email_details(self.email_pk)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email(self):
        """ Test that 200 is returned """

        data = {'name': 'UNITTEST - update'}
        res = my_account.Emails.update_email(self.email_pk, data)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_email(self):
        """ Test that 204 is returned """

        res = my_account.Emails.delete_email(self.email_pk)
        self.assertEqual(res['status'], 204)

    def test_send_test_email(self):
        """ Test that 200 is returned """

        res = my_account.Emails.send_test_email(self.email_pk)
        my_account.Emails.delete_email(self.email_pk)

        self.assertEqual(res['status'], 200)

    def test_apply_email(self):
        """ Test that 200 is returned """

        res = my_account.Emails.apply_email(self.email_pk)
        self.assertEqual(res['status'], 200)

    ### smtp ###
    def test_get_emails_smtp(self):
        """ Test that 200 is returned """

        res = my_account.Emails.get_emails_smtp_list()
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

        res = my_account.Emails.create_email_smtp(data)
        my_account.Emails.delete_email_smtp(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_email_smtp_details(self):
        """ Test that 200 is returned """

        res = my_account.Emails.get_email_smtp_details(self.smtp_pk)
        my_account.Emails.delete_email_smtp(self.smtp_pk)

        self.assertEqual(res['status'], 200)

    def test_update_email_smtp(self):
        """ Test that 200 is returned """

        data = {"from_name": "UNITTEST - Update"}
        res = my_account.Emails.update_email_smtp(self.smtp_pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_email_smtp(self):
        """ Test that 204 is returned """

        res = my_account.Emails.delete_email_smtp(self.smtp_pk)
        self.assertEqual(res['status'], 204)

    def test_send_test_email_smtp(self):
        """ Test that 200 is returned """

        res = my_account.Emails.send_test_email_smtp(self.smtp_pk)
        self.assertEqual(res['status'], 200)


class TestFiles(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.folder_pk = testHelper._create_folder_return_pk(cls.project_pk)
        cls.file_pk = testHelper._create_file_return_pk(cls.project_pk, cls.folder_pk)

        #### Files ####

    ### Folders ###

    def test_get_folders_list(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_folder_list(self.project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_folder_details(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_folder_details(self.folder_pk)
        my_account.Invoicing.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 200)

    def test_create_folder(self):
        """ Test that 201 is returned """

        folder = {
            "name": "UNITTEST"
        }

        res = my_account.Files.create_folder(self.project_pk, folder)
        my_account.Files.delete_folder(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_update_folder(self):
        """ Test that 201 is returned """

        folder_updated = {
            "name": "UNITTEST - UPDATE"
        }

        res = my_account.Files.update_folder(self.folder_pk, folder_updated)
        my_account.Files.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_folder(self):
        """ Test that 200 is returned """

        res = my_account.Files.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 204)

    ### Files ###
    def test_get_files_list(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_files_list(self.project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_file(self):
        """ Test that 201 is returned """
        data = {
            "name": "file_UNITTEST",
            "file": "README.md",
            "folder": self.folder_pk,
        }

        res = my_account.Files.create_file(self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_files_details(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_file_details(self.file_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_file(self):
        """ Test that 204 is returned """

        res = my_account.Files.delete_file(self.file_pk)
        self.assertEqual(res['status'], 204)


class TestBanks(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.bank_pk = cls.testHelper._create_bank_return_pk(cls.team_pk, cls.project_pk, cls.currency_pk)

    def test_get_banks_list(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_banks_list()

        self.assertEqual(res['status'], 200)

    def test_get_banks_details(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_bank_details(self.bank_pk)
        self.assertEqual(res['status'], 200)

    def test_create_bank(self):
        """ Test that 201 is returned """

        name = self.testHelper.create_name()

        data = {
            "name": name,
            "currency": self.currency_pk,
            "country": "FR",
            "iban": "XXX-{0}".format(name),
            "bic": "XXX-{0}".format(name),
            "rib": "XXX-{0}".format(name),
            "teams": [str(self.team_pk)],
            "projects": [str(self.project_pk)]
        }

        res = my_account.Files.create_bank(data)
        my_account.Files.delete_bank(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_update_bank(self):
        """ Test that 200 is returned """

        name = self.testHelper.create_name()

        update = {
            "name": name
        }

        res = my_account.Files.update_bank(self.bank_pk, update)
        my_account.Files.delete_bank(self.bank_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_bank(self):
        """ Test that 204 is returned """

        res = my_account.Files.delete_bank(self.bank_pk)
        self.assertEqual(res['status'], 204)


# class Tests(unittest.TestCase):
#     def _create_invoice_return_pk(self):
#         """ Create and return the pk of an invoice """

#         try:
#             client_pk = my_account.Invoicing.get_clients_list(team_pk)['data'][0]['pk']
#         except IndexError as error:
#             data_client = {
#                 "company_name": "test-unittest",
#                 "number": "123",
#                 "currency": currency_pk,
#                 "team": team_pk,
#             }

#             res = my_account.Invoicing.create_client(data_client)
#             self.assertEqual(res['status'], 201)

#             client_pk = res['data']['pk']

#         invoice = {
#             # "client": client_pk,
#             "project": project_pk,
#             "invoice_date": '19-04-2021',
#             "due_date": '19-05-2021',
#             "references": "UNITTEST ref",
#             "type": 4
#         }

#         invoice_pk = my_account.Invoicing.create_invoice(team_pk, invoice)['data']['pk']
#         return invoice_pk

#     ##### Reports ####

#     ### Reports ###

#     def _create_report_return_pk(self):
#         """ Create a report and return the pk """

#         report = {
#             "name": "UNITTEST",
#             "project": project_pk,
#             "type": "billed_progress_report",
#             "lang": "fr"
#         }

#         res = my_account.Invoicing.create_report(report)['data']['pk']
#         return res

#     def test_get_reports_list(self):
#         """ Test that 200 is returned """

#         res = my_account.Invoicing.get_reports_list()

#         self.assertEqual(res['status'], 200)

#     def test_get_reports_project_list(self):
#         """ Test that 200 is returned """

#         res = my_account.Invoicing.get_reports_project_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_reports(self):
#         """ Test that 201 is returned """

#         report = {
#             "name": "UNITTEST_billed_progress",
#             "project": project_pk,
#             "type": "billed_progress_report",
#             "lang": "fr"
#         }

#         res = my_account.Invoicing.create_report(report)

#         self.assertEqual(res['status'], 201)

#     def test_get_report_details(self):
#         """ Test that 200 is returned """

#         report_pk = self._create_report_return_pk()
#         res = my_account.Invoicing.get_report_details(report_pk)
#         my_account.Invoicing.delete_report(report_pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_report(self):
#         """ Test that 200 is returned """

#         report_pk = self._create_report_return_pk()

#         report_up = {
#             "name": "UPDATED UNITTEST"
#         }

#         res = my_account.Invoicing.update_report(report_pk, report_up)
#         my_account.Invoicing.delete_report(report_pk)

#         self.assertEqual(res['status'], 200)

#     # def test_generate_report(self):
#     #     #! 200
#     #     """ Test that 201 is returned """

#     #     report_pk = self._create_report_return_pk()

#     #     data = {
#     #         "pk": report_pk,
#     #         "project": project_pk
#     #     }

#     #     res = my_account.Invoicing.generate_report(data)
#     #     print(res)

#     #     self.assertEqual(res['status'], 201)

#     def test_delete_report(self):
#         """ Test that 204 is returned """

#         pk = self._create_report_return_pk()

#         res = my_account.Invoicing.delete_report(pk)

#         self.assertEqual(res['status'], 204)

#     ### Reports Templates ###
#     def _create_template_return_pk(self):
#         """ Create a template and return the pk """

#         template = {
#             "name": "UNITTEST",
#             "type": "progress",
#             "lang": "fr",
#             "orientation": "portrait"
#         }

#         return my_account.Invoicing.create_template(team_pk, template)['data']['pk']

#     def test_get_templates_list(self):
#         """ Test that 200 is returned """

#         res = my_account.Invoicing.get_templates_list(team_pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_template_details(self):
#         """ Test that 200 is returned """

#         template_pk = self._create_template_return_pk()

#         res = my_account.Invoicing.get_template_details(template_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_template(self):
#         """ Test that 201 is returned """

#         template = {
#             "name": "UNITTEST",
#             "type": "progress",
#             "lang": "fr",
#             "orientation": "portrait"
#         }

#         res = my_account.Invoicing.create_template(team_pk, template)

#         self.assertEqual(res['status'], 201)

#     def test_update_template(self):
#         """ Test that 200 is returned """

#         template_pk = self._create_template_return_pk()

#         template_up = {
#             "name": "UPDATED"
#         }

#         res = my_account.Invoicing.update_template(template_pk, template_up)
#         my_account.Invoicing.delete_template(template_pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_template(self):
#         """ Test that 204 is returned """

#         template_pk = self._create_template_return_pk()
#         res = my_account.Invoicing.delete_template(template_pk)

#         self.assertEqual(res['status'], 204)

#     def test_duplicate_template(self):
#         """ Test that 201 is returned """

#         template_pk = self._create_template_return_pk()
#         res = my_account.Invoicing.duplicate_template(template_pk)

#         my_account.Invoicing.delete_template(template_pk)
#         my_account.Invoicing.delete_template(res['data']['pk'])

#         self.assertEqual(res['status'], 201)

#     #### Revenue ####
#     def _create_revenue_return_pk(self):
#         """ Create revenue and return pk"""

#         data = {
#             "month": 5,
#             "team": team_pk,
#             "title": "UNITTEST",
#             "months": []
#         }

#         return my_account.Invoicing.create_revenue(data)['data']['id']

#     #! 500
#     # def _create_revenue_month_return_pk(self):
#     #     """ Create revenue month and return pk"""

#     #     data = {
#     #         "team": team_pk,
#     #     }

#     #     return my_account.Invoicing.create_revenue_month(data)['data']['id']

#     def test_get_revenue_list(self):
#         """ Test that 200 is returned """

#         res = my_account.Invoicing.get_revenue_list()

#         self.assertEqual(res['status'], 200)

#     def test_create_revenue(self):
#         """ Test that 201 is returned """

#         data = {
#             "month": 5,
#             "team": team_pk,
#             "title": "UNITTEST",
#             "months": []
#         }

#         res = my_account.Invoicing.create_revenue(data)

#         self.assertEqual(res['status'], 201)

#     def test_get_revenue_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_revenue_return_pk()

#         res = my_account.Invoicing.get_revenue_details(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_revenue(self):
#         """ Test that 200 is returned """

#         pk = self._create_revenue_return_pk()

#         data = {
#             "title": "UPDATED"
#         }

#         res = my_account.Invoicing.update_revenue(pk, data)

#         self.assertEqual(res['status'], 200)

#     def test_delete_revenue(self):
#         """ Test that 204 is returned """

#         pk = self._create_revenue_return_pk()

#         res = my_account.Invoicing.delete_revenue(pk)

#         self.assertEqual(res['status'], 204)

#     def test_get_revenue_month_list(self):
#         """ Test that 200 is returned """

#         res = my_account.Invoicing.get_revenue_month_list()

#         self.assertEqual(res['status'], 200)

#     # TODO Work in progress
#     # def test_create_revenue_month(self):
#     #     """ Test that 201 is returned """

#     #     data = {
#     #         "team": team_pk
#     #     }

#     #     res = my_account.Invoicing.create_revenue_month(data)
#     #     print(res)

#     #     self.assertEqual(res['status'], 201)

#     # def test_get_revenue_month_details(self):
#     #     """ Test that 200 is returned """

#     #     pk = self._create_revenue_month_return_pk()

#     #     res = my_account.Invoicing.get_revenue_month_details(pk)

#     #     self.assertEqual(res['status'], 200)

#     # def test_update_revenue_month(self):
#     #     """ Test that 200 is returned """

#     #     pk = self._create_revenue_month_return_pk()

#     #     data = {
#     #         "amont_actual": 1
#     #     }

#     #     res = my_account.Invoicing.update_revenue_month(pk, data)

#     #     self.assertEqual(res['status'], 200)

#     # def test_delete_revenue_month(self):
#     #     """ Test that 204 is returned """

#     #     pk = self._create_revenue_month_return_pk()

#     #     res = my_account.Invoicing.delete_revenue_month(pk)

#     #     self.assertEqual(res['status'], 204)

#     #### Styleguides ####

#     def _create_styleguide_return_pk(self):
#         """ Create a styleguide and return pk """

#         data = {
#             "name": "UNITTEST"
#         }

#         return my_account.Invoicing.create_styleguide(data)['data']['id']

#     def test_get_styleguides_list(self):
#         """ Test that 200 is returned"""

#         res = my_account.Invoicing.get_styleguides_list()

#         self.assertEqual(res['status'], 200)

#     def test_create_styleguide(self):
#         """ Test that 201 is returned """

#         data = {
#             "name": "UNITTEST"
#         }

#         res = my_account.Invoicing.create_styleguide(data)
#         my_account.Invoicing.delete_styleguide(res['data']['id'])

#         self.assertEqual(res['status'], 201)

#     def test_get_styleguide_details(self):
#         """ Test that 200 is returned """

#         styleguide_pk = self._create_styleguide_return_pk()
#         res = my_account.Invoicing.get_styleguide_details(styleguide_pk)
#         my_account.Invoicing.delete_styleguide(styleguide_pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_styleguide(self):
#         """ Test that 200 is returned """

#         styleguide_pk = self._create_styleguide_return_pk()

#         data_up = {
#             "name": "UNITTEST - UPDATED"
#         }
#         res = my_account.Invoicing.update_styleguide(styleguide_pk, data_up)
#         my_account.Invoicing.delete_styleguide(styleguide_pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_styleguide(self):
#         """ Test that 204 is returned """

#         styleguide_pk = self._create_styleguide_return_pk()
#         res = my_account.Invoicing.delete_styleguide(styleguide_pk)

#         self.assertEqual(res['status'], 204)


if __name__ == '__main__':
    unittest.main()
