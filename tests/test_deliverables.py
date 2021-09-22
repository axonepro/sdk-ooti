import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import TeamFactory
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
fee_project = my_account.Fees.get_fees_project_list_projects(project_pk)['data'][0]['id']



# WAS DISABLED :::: 


# class Tests(unittest.TestCase):
#     #### Zones ####
#     def _create_zone_return_pk(self):
#         """ Create a zone and return the pk

#         :return: {"pk": zone_pk, "area_pk": area_pk}
#         """

#         area_pk = self._create_area_return_pk()

#         data = {
#             "name": "UNITTEST",
#             "area": area_pk,
#             "progress": 0,
#             "is_annex": True,
#             "internal_code": "string",
#             "client_code": "string",
#             "surface_area": 0,
#             "default_surface_price": 0,
#             "num_units": 0
#         }

#         res = my_account.Deliverables.create_zone(area_pk, data)
#         return {"pk": res['data']['id'], "area_pk": area_pk}

#     def test_export_zones(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.export_zones(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_zones_list(self):
#         """ Test that 200 is returned """
#         area_pk = self._create_area_return_pk()

#         res = my_account.Deliverables.get_zones_list(area_pk)
#         my_account.Deliverables.delete_area(area_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_zone(self):
#         """ Test that 201 is returned """

#         area_pk = self._create_area_return_pk()

#         data = {
#             "name": "string",
#             "area": area_pk,
#             "progress": 0,
#             "is_annex": True,
#             "internal_code": "string",
#             "client_code": "string",
#             "surface_area": 0,
#             "default_surface_price": 0,
#             "num_units": 0
#         }

#         res = my_account.Deliverables.create_zone(area_pk, data)

#         self.assertEqual(res['status'], 201)

#     def test_get_zone_details(self):
#         """ Test that 200 is returned """
#         res_create = self._create_zone_return_pk()

#         res = my_account.Deliverables.get_zone_details(res_create['pk'])

#         my_account.Deliverables.delete_zone(res_create['pk'])
#         my_account.Deliverables.delete_area(res_create['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_update_zone(self):
#         """ Test that 200 is returned """
#         res_create = self._create_zone_return_pk()

#         data_up = {
#             "name": "update"
#         }

#         res = my_account.Deliverables.update_zone(res_create['pk'], data_up)

#         my_account.Deliverables.delete_zone(res_create['pk'])
#         my_account.Deliverables.delete_area(res_create['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_delete_zone(self):
#         """ Test that 204 is returned """
#         area_pk = self._create_area_return_pk()

#         data = {
#             "name": "string",
#             "area": area_pk,
#             "progress": 0,
#             "is_annex": True,
#             "internal_code": "string",
#             "client_code": "string",
#             "surface_area": 0,
#             "default_surface_price": 0,
#             "num_units": 0
#         }

#         zone_pk = my_account.Deliverables.create_zone(area_pk, data)['data']['id']
#         res = my_account.Deliverables.delete_zone(zone_pk)

#         my_account.Deliverables.delete_area(area_pk)

#         self.assertEqual(res['status'], 204)

#     #### Fees ####

#     ### Fees bracket ###
#     def _create_fees_bracket_return_pk(self):
#         """ Create a fee bracket and return the pk """

#         data = {
#             "fee_project": fee_project,
#             "pct": 10,
#             "fees": 1000
#         }

#         return my_account.Deliverables.create_fees_bracket(project_pk, data)['data']['pk']

#     def test_get_fees_bracket_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fees_bracket_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_fees_bracket(self):
#         """ Test that 201 is returned """

#         data = {
#             "fee_project": fee_project,
#             "pct": 10,
#             "fees": 1000
#         }

#         res = my_account.Deliverables.create_fees_bracket(project_pk, data)
#         my_account.Deliverables.delete_fees_bracket(res['data']['pk'])

#         self.assertEqual(res['status'], 201)

#     def test_get_fees_bracket_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_fees_bracket_return_pk()
#         res = my_account.Deliverables.get_fees_bracket_details(pk)
#         my_account.Deliverables.delete_fees_bracket(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_fees_bracket(self):
#         """ Test that 200 is returned """

#         pk = self._create_fees_bracket_return_pk()

#         data = {
#             "fees": 1500
#         }

#         res = my_account.Deliverables.update_fees_bracket(pk, data)
#         my_account.Deliverables.delete_fees_bracket(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_fees_bracket(self):
#         """ Test that 204 is returned """

#         pk = self._create_fees_bracket_return_pk()
#         res = my_account.Deliverables.delete_fees_bracket(pk)

#         self.assertEqual(res['status'], 204)

#     ### Fee project version ###
#     def _create_fee_project_version_return_pk(self):
#         """ Create a fee project version and return pk """

#         data = {
#             "title": "UNITTEST",
#             "fee_project": fee_project,
#             "show_on_table": True,
#             "data": {}
#         }

#         return my_account.Deliverables.create_fee_project_version(data)['data']['id']

#     def test_export_project_fees(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.export_project_fees(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_fee_project_version_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fee_project_version_list()

#         self.assertEqual(res['status'], 200)

#     def test_create_fee_project_version(self):
#         """ Test that 201 is returned """

#         data = {
#             "title": "UNITTEST",
#             "fee_project": fee_project,
#             "show_on_table": True,
#             "data": {}
#         }

#         res = my_account.Deliverables.create_fee_project_version(data)
#         my_account.Deliverables.delete_fee_project_version(res['data']['id'])

#         self.assertEqual(res['status'], 201)

#     def test_get_fee_project_version_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_project_version_return_pk()
#         res = my_account.Deliverables.get_fee_project_version_details(pk)
#         my_account.Deliverables.delete_fee_project_version(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_fee_project_version(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_project_version_return_pk()

#         data = {
#             "title": "UPDATED"
#         }

#         res = my_account.Deliverables.update_fee_project_version(pk, data)
#         my_account.Deliverables.delete_fee_project_version(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_fee_project_version(self):
#         """ Test that 204 is returned """

#         pk = self._create_fee_project_version_return_pk()
#         res = my_account.Deliverables.delete_fee_project_version(pk)

#         self.assertEqual(res['status'], 204)

#     ### Fees ###
#     def _create_fee_return_pk(self):
#         """ Create a fee and return the pk """
#         data = {
#             "title": "UNITTEST",
#             "amount_base": 0,
#             "amount_current": 0,
#             "progress": 0,
#             "in_timeline": True
#         }

#         return my_account.Deliverables.create_fee(project_pk, data)['data']['pk']

#     def test_get_fees_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fees_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_fee(self):
#         """ Test that 201 is returned """

#         data = {
#             "title": "UNITTEST",
#             "amount_base": 0,
#             "amount_current": 0,
#             "progress": 0,
#             "in_timeline": True
#         }

#         res = my_account.Deliverables.create_fee(project_pk, data)
#         my_account.Deliverables.delete_fee(res['data']['pk'])

#         self.assertEqual(res['status'], 201)

#     def test_get_fee_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_return_pk()
#         res = my_account.Deliverables.get_fee_details(pk)
#         my_account.Deliverables.delete_fee(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_fee(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_return_pk()

#         data = {
#             "title": "UPDATED"
#         }

#         res = my_account.Deliverables.update_fee(pk, data)
#         my_account.Deliverables.delete_fee(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_fee(self):
#         """ Test that 201 is returned """

#         pk = self._create_fee_return_pk()
#         res = my_account.Deliverables.delete_fee(pk)

#         self.assertEqual(res['status'], 204)

#     ### Fee projections ###
#     def test_get_fees_projection_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fees_projection_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     ### Fees project ###
#     def _create_fee_project_return_pk(self):
#         """ Create a fee project and return pk """
#         data = {
#             "title": "UNITTEST",
#             "project": project_pk
#         }

#         return my_account.Deliverables.create_fee_project(data)['data']['id']

#     def test_get_fees_project_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fees_project_list()

#         self.assertEqual(res['status'], 200)

#     def test_get_fees_project_list_project(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_fees_project_list_projects(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_fees_projects_update(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_project_return_pk()

#         res = my_account.Deliverables.get_fees_projects_update(pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_fees_project(self):
#         """ Test that 201 is returned """

#         data = {
#             "title": "UNITTEST",
#             "project": project_pk
#         }

#         res = my_account.Deliverables.create_fee_project(data)
#         my_account.Deliverables.delete_fee_project(res['data']['id'])

#         self.assertEqual(res['status'], 201)

#     def test_get_fees_project_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_project_return_pk()

#         res = my_account.Deliverables.get_fees_project_details(pk)
#         my_account.Deliverables.delete_fee_project(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_fee_project(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_project_return_pk()

#         data = {
#             "title": "UPDATED"
#         }

#         res = my_account.Deliverables.update_fee_project(pk, data)
#         my_account.Deliverables.delete_fee_project(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_fee_project(self):
#         """ Test that 204 is returned """

#         pk = self._create_fee_project_return_pk()
#         res = my_account.Deliverables.delete_fee_project(pk)

#         self.assertEqual(res['status'], 204)

#     ### Fees revision ###
#     def _create_fee_revision_return_pk(self):
#         """ Test that 201 is returned

#         :return: {"pk": pk, "fee_pk": fee_pk}
#         """
#         fee_pk = self._create_fee_return_pk()

#         data = {
#             "amount": 10,
#             "date": "06-05-2021"
#         }

#         pk = my_account.Deliverables.create_fee_revisions_item(fee_pk, data)['data']['pk']

#         return {"pk": pk, "fee_pk": fee_pk}

#     def test_get_fees_revision_details(self):
#         """ Test that 200 is returned """

#         res_creation = self._create_fee_revision_return_pk()

#         res = my_account.Deliverables.get_fees_revision_details(res_creation['pk'])
#         my_account.Deliverables.delete_fee(res_creation['fee_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_delete_fees_revision(self):
#         """ Test that 204 is returned """

#         res_creation = self._create_fee_revision_return_pk()

#         data = {
#             "amount": 11
#         }

#         res = my_account.Deliverables.delete_fee_revision(res_creation['pk'])
#         my_account.Deliverables.delete_fee(res_creation['fee_pk'])

#         self.assertEqual(res['status'], 204)

#     def test_get_fees_revision_fees(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_return_pk()
#         res = my_account.Deliverables.get_fees_revisions_item_details(pk)

#         my_account.Deliverables.delete_fee(pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_fee_revisions_item(self):
#         """ Test that 201 is returned """

#         pk = self._create_fee_return_pk()

#         data = {
#             "amount": 10,
#             "date": "06-05-2021"
#         }

#         res = my_account.Deliverables.create_fee_revisions_item(pk, data)
#         my_account.Deliverables.delete_fee(pk)
#         my_account.Deliverables.delete_fee_revision(res['data']['pk'])

#         self.assertEqual(res['status'], 201)

#     def test_update_fee_revision(self):
#         """ Test that 200 is returned """

#         pk = self._create_fee_revision_return_pk()['pk']

#         data = {
#             "amount": 0
#         }

#         res = my_account.Deliverables.update_fee_revision(pk, data)
#         self.assertEqual(res['status'], 200)

#     ### Fees validate ###
#     def test_validate_fees_costs(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.validation_fees_costs(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_validate_fees_ffne(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.validation_fees_ffne(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_validate_fees_production(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.validation_fees_production(project_pk)

#         self.assertEqual(res['status'], 200)

#     # Fee zones
#     def _create_fee_zones_return_pk(self):
#         """ Create fee zones return pk

#         :return: {"pk": pk, "zone_pk": zone_pk['pk'], "area_pk": zone_pk['area_pk']}
#         """
#         zone_pk = self._create_zone_return_pk()

#         data = {
#             "zone": zone_pk['pk'],
#             "project": project_pk,
#             "fee_project": fee_project,
#             "board": 0,
#             "rendering": 0
#         }

#         pk = my_account.Deliverables.create_fee_zones(data)['data']['id']

#         return {"pk": pk, "zone_pk": zone_pk['pk'], "area_pk": zone_pk['area_pk']}

#     def test_get_fees_zones_list(self):
#         """ Test that 200 is returend """
#         res = my_account.Deliverables.get_fees_zones_list()

#         self.assertEqual(res['status'], 200)

#     def test_create_fees_zones(self):
#         """ Test that 201 is returned """

#         zone_pk = self._create_zone_return_pk()

#         data = {
#             "zone": zone_pk['pk'],
#             "project": project_pk,
#             "fee_project": fee_project,
#             "board": 0,
#             "rendering": 0
#         }

#         res = my_account.Deliverables.create_fee_zones(data)

#         my_account.Deliverables.delete_fees_zone(res['data']['id'])
#         my_account.Deliverables.delete_zone(zone_pk['pk'])
#         my_account.Deliverables.delete_area(zone_pk['area_pk'])

#         self.assertEqual(res['status'], 201)

#     def test_get_fees_zone_details(self):
#         """ Test that 200 is returned """

#         res_pk = self._create_fee_zones_return_pk()
#         res = my_account.Deliverables.get_fees_zone_details(res_pk['pk'])

#         my_account.Deliverables.delete_fees_zone(res_pk['pk'])
#         my_account.Deliverables.delete_zone(res_pk['zone_pk'])
#         my_account.Deliverables.delete_area(res_pk['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_update_fee_zones(self):
#         """ Test that 200 is returned """

#         res_pk = self._create_fee_zones_return_pk()

#         data = {
#             "date": "05-05-2021"
#         }

#         res = my_account.Deliverables.update_fee_zone(res_pk['pk'], data)

#         my_account.Deliverables.delete_fees_zone(res_pk['pk'])
#         my_account.Deliverables.delete_zone(res_pk['zone_pk'])
#         my_account.Deliverables.delete_area(res_pk['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_delete_fee_zone(self):
#         """ Test that 204 is returned """

#         res_pk = self._create_fee_zones_return_pk()

#         res = my_account.Deliverables.delete_fees_zone(res_pk['pk'])
#         my_account.Deliverables.delete_zone(res_pk['zone_pk'])
#         my_account.Deliverables.delete_area(res_pk['area_pk'])

#         self.assertEqual(res['status'], 204)

#     #### Plans ####

#     def _create_plan_return_pk(self):
#         """ Create plan and return pk """

#         data = {
#             "name_fr": "UNITTEST",
#             "name_en": "UNITTEST",
#             "plan_format": "A1",
#             "scale": "1/50e",
#             "level": "000",
#             "lot": 10,
#             "code": "pln",
#             "custom_field_1": "",
#             "custom_field_2": "",
#             "custom_field_3": "",
#             "org": my_account.org_pk
#         }

#         return my_account.Deliverables.create_plan(project_pk, data)['data']['id']

#     def test_get_plans_list_action(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_plans_list_action(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_plans_list_action(self):
#         """ Test that 201 is returned """
#         res = my_account.Deliverables.create_plans_list_action(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_plans_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_plans_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_plan(self):
#         """ Test that 201 is returned """

#         data = {
#             "name_fr": "UNITTEST",
#             "name_en": "UNITTEST",
#             "plan_format": "A1",
#             "scale": "1/50e",
#             "level": "000",
#             "lot": 10,
#             "code": "pln",
#             "custom_field_1": "",
#             "custom_field_2": "",
#             "custom_field_3": "",
#             "org": my_account.org_pk
#         }

#         res = my_account.Deliverables.create_plan(project_pk, data)

#         my_account.Deliverables.delete_plan(res['data']['id'])

#         self.assertEqual(res['status'], 201)

#     def test_update_plan(self):
#         """ Test that 200 is returned """

#         pk = self._create_plan_return_pk()

#         data = {
#             "name_fr": "UPDATED",
#         }

#         res = my_account.Deliverables.update_plan(pk, data)

#         my_account.Deliverables.delete_plan(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_plan(self):
#         """ Test that 204 is returned """

#         pk = self._create_plan_return_pk()

#         res = my_account.Deliverables.delete_plan(pk)

#         self.assertEqual(res['status'], 204)

#     def test_get_plan_details(self):
#         """ Test that 200 is returned """
#         pk = self._create_plan_return_pk()

#         res = my_account.Deliverables.get_plan_details(pk)

#         my_account.Deliverables.delete_plan(pk)

#         self.assertEqual(res['status'], 200)

#     def test_get_plans_planphases_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_plans_planphases_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     #### Prescription ####

#     def _create_prescription_return_pk(self):
#         """ Create a prescription and return pk

#         :return: {"pk": pk, "area_pk": area_pk, "fee_pk": fee_pk}

#         """

#         fee_pk = self._create_fee_return_pk()
#         area_pk = self._create_area_return_pk()

#         data = {
#             "fee_pct": "10",
#             "fee": fee_pk,
#             "date": "04-05-2021",
#             "description": "UNITTEST",
#             "area": area_pk,
#         }

#         pk = my_account.Deliverables.create_prescription(project_pk, data)['data']['id']
#         return {"pk": pk, "area_pk": area_pk, "fee_pk": fee_pk}

#     def test_get_prescription_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_prescriptions_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_prescription(self):
#         """ Test that 201 is returned """

#         fee_pk = self._create_fee_return_pk()
#         area_pk = self._create_area_return_pk()

#         data = {
#             "fee_pct": "10",
#             "fee": fee_pk,
#             "date": "04-05-2021",
#             "description": "UNITTEST",
#             "area": area_pk,
#         }

#         res = my_account.Deliverables.create_prescription(project_pk, data)
#         my_account.Deliverables.delete_prescription(res['data']['id'])
#         my_account.Deliverables.delete_area(area_pk)

#         self.assertEqual(res['status'], 201)

#     def test_get_prescription_details(self):
#         """ Test that 200 is returned """

#         res_creation = self._create_prescription_return_pk()

#         res = my_account.Deliverables.get_prescriptions_details(res_creation['pk'])
#         my_account.Deliverables.delete_prescription(res_creation['pk'])
#         my_account.Deliverables.delete_area(res_creation['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_update_prescription(self):
#         """ Test that 200 is returned """

#         res_creation = self._create_prescription_return_pk()

#         data = {
#             "description": "UPDATED"
#         }

#         res = my_account.Deliverables.update_prescriptions(res_creation['pk'], data)
#         my_account.Deliverables.delete_prescription(res_creation['pk'])
#         my_account.Deliverables.delete_area(res_creation['area_pk'])

#         self.assertEqual(res['status'], 200)

#     def test_delete_prescription(self):
#         """ Test that 204 is returned """

#         res_creation = self._create_prescription_return_pk()

#         res = my_account.Deliverables.delete_prescription(res_creation['pk'])

#         my_account.Deliverables.delete_area(res_creation['area_pk'])

#         self.assertEqual(res['status'], 204)

#     #### Documents ####

#     def test_get_documents_list(self):
#         """ Test that 200 is returned """
#         res = my_account.Deliverables.get_documents_list(project_pk)

#         self.assertEqual(res['status'], 200)

#     def test_create_document(self):
#         """ Test that 201 is returned """

#         data = {
#             "name": "UNITTEST",
#             "price": 10,
#             "annexes": []
#         }

#         res = my_account.Deliverables.create_document(project_pk, data)
#         my_account.Deliverables.delete_document(res['data']['id'])

#         self.assertEqual(res['status'], 201)

#     def test_get_documents_details(self):
#         """ Test that 200 is returned """

#         pk = self._create_document_return_pk()

#         res = my_account.Deliverables.get_document_details(pk)

#         self.assertEqual(res['status'], 200)

#     def test_update_document(self):
#         """ Test that 200 is returned """

#         pk = self._create_document_return_pk()

#         data = {
#             "name": "UPDATED"
#         }

#         res = my_account.Deliverables.update_document(pk, data)
#         my_account.Deliverables.delete_document(pk)

#         self.assertEqual(res['status'], 200)

#     def test_delete_document(self):
#         """ Test that 204 is returned """

#         pk = self._create_document_return_pk()
#         res = my_account.Deliverables.delete_document(pk)

#         self.assertEqual(res['status'], 204)

#     # def test_set_price_documents(self):
#     #     #! 500
#     #     """ Test that 201 is returned """

#     #     res = my_account.Deliverables.set_price_documents(project_pk)

#     #     self.assertEqual(res['status'], 201)


if __name__ == '__main__':
    unittest.main()
