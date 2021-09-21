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
