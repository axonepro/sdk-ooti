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
fee_project = my_account.Deliverables.get_fees_project_list_projects(project_pk)['data'][0]['id']

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

"""


class Tests(unittest.TestCase):
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

        res = my_account.Deliverables.get_areas_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_area(self):
        """ Test that 201 is returned """

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

        area_pk = self._create_area_return_pk()
        res = my_account.Deliverables.delete_area(area_pk)

        self.assertEqual(res['status'], 204)

    #### Phases ####
    def _create_phase_return_pk(self):
        """ Create phase and return pk 

        :return:{"pk": pk, "fee_project": fee_project}
        """

        fee_project = self._create_fee_project_return_pk()

        data = {
            "name": "UNITTEST",
            "shortname": "TEST",
            "fee_project": fee_project,
            "pct": 10,
            "dependants": []
        }

        pk = my_account.Deliverables.create_phase(project_pk, data)['data']['id']

        return {"pk": pk, "fee_project": fee_project}

    def test_get_phases_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_phases_list_fee_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_list_fee_project(project_pk, fee_project)

        self.assertEqual(res['status'], 200)

    def test_get_phases_projections_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_projections_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_export_phase(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.export_phase(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_phase(self):
        """ Test that 201 is returned 

        :return: {"pk": pk, "fee_project": fee_project}
        """

        fee_project = self._create_fee_project_return_pk()

        data = {
            "name": "UNITTEST",
            "shortname": "TEST",
            "fee_project": fee_project,
            "pct": 10,
            "dependants": []
        }

        res = my_account.Deliverables.create_phase(project_pk, data)

        my_account.Deliverables.delete_phase(res['data']['id'])
        my_account.Deliverables.delete_fee_project(fee_project)

        self.assertEqual(res['status'], 201)

    def test_get_phase_details(self):
        """ Test that 200 is returned """

        res_pk = self._create_phase_return_pk()

        res = my_account.Deliverables.get_phase_details(res_pk['pk'])

        my_account.Deliverables.delete_phase(res_pk['pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_update_phase(self):
        """ Test that 200 is returned """

        res_pk = self._create_phase_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Deliverables.update_phase(res_pk['pk'], data)

        my_account.Deliverables.delete_phase(res_pk['pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_delete_phase(self):
        """ Test that 204 is returned """

        res_pk = self._create_phase_return_pk()

        res = my_account.Deliverables.delete_phase(res_pk['pk'])

        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 204)

    def test_reset_phase_order(self):
        """ Test that 201 is returned """
        #! Passe but 200 is returned
        res = my_account.Deliverables.reset_phases_order(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_phase_planphase_details(self):
        """ Test that 200 is returned """
        plan_pk = self._create_plan_return_pk()

        planphase_pk = my_account.Deliverables.get_plan_details(plan_pk)['data']['plan_phases'][0]['id']
        res = my_account.Deliverables.get_phase_planphase_details(planphase_pk)

        my_account.Deliverables.delete_plan(plan_pk)

        self.assertEqual(res['status'], 200)

    def test_update_phase_planphase(self):
        """ Test that 200 is returned """
        plan_pk = self._create_plan_return_pk()

        planphase_pk = my_account.Deliverables.get_plan_details(plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "progress": 20
        }

        res = my_account.Deliverables.update_phase_planphase(planphase_pk, data)

        my_account.Deliverables.delete_plan(plan_pk)
        self.assertEqual(res['status'], 200)

    def test_delete_phase_planphase(self):
        """ Test that 204 is returned """
        plan_pk = self._create_plan_return_pk()

        planphase_pk = my_account.Deliverables.get_plan_details(plan_pk)['data']['plan_phases'][0]['id']

        res = my_account.Deliverables.delete_phase_planphase(planphase_pk)

        my_account.Deliverables.delete_plan(plan_pk)
        self.assertEqual(res['status'], 204)

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

    ### Fees bracket ###
    def _create_fees_bracket_return_pk(self):
        """ Create a fee bracket and return the pk """

        data = {
            "fee_project": fee_project,
            "pct": 10,
            "fees": 1000
        }

        return my_account.Deliverables.create_fees_bracket(project_pk, data)['data']['pk']

    def test_get_fees_bracket_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_bracket_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_fees_bracket(self):
        """ Test that 201 is returned """

        data = {
            "fee_project": fee_project,
            "pct": 10,
            "fees": 1000
        }

        res = my_account.Deliverables.create_fees_bracket(project_pk, data)
        my_account.Deliverables.delete_fees_bracket(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_get_fees_bracket_details(self):
        """ Test that 200 is returned """

        pk = self._create_fees_bracket_return_pk()
        res = my_account.Deliverables.get_fees_bracket_details(pk)
        my_account.Deliverables.delete_fees_bracket(pk)

        self.assertEqual(res['status'], 200)

    def test_update_fees_bracket(self):
        """ Test that 200 is returned """

        pk = self._create_fees_bracket_return_pk()

        data = {
            "fees": 1500
        }

        res = my_account.Deliverables.update_fees_bracket(pk, data)
        my_account.Deliverables.delete_fees_bracket(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_fees_bracket(self):
        """ Test that 204 is returned """

        pk = self._create_fees_bracket_return_pk()
        res = my_account.Deliverables.delete_fees_bracket(pk)

        self.assertEqual(res['status'], 204)

    ### Fee project version ###
    def _create_fee_project_version_return_pk(self):
        """ Create a fee project version and return pk """

        data = {
            "title": "UNITTEST",
            "fee_project": fee_project,
            "show_on_table": True,
            "data": {}
        }

        return my_account.Deliverables.create_fee_project_version(data)['data']['id']

    def test_export_project_fees(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.export_project_fees(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_fee_project_version_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fee_project_version_list()

        self.assertEqual(res['status'], 200)

    def test_create_fee_project_version(self):
        """ Test that 201 is returned """

        data = {
            "title": "UNITTEST",
            "fee_project": fee_project,
            "show_on_table": True,
            "data": {}
        }

        res = my_account.Deliverables.create_fee_project_version(data)
        my_account.Deliverables.delete_fee_project_version(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_fee_project_version_details(self):
        """ Test that 200 is returned """

        pk = self._create_fee_project_version_return_pk()
        res = my_account.Deliverables.get_fee_project_version_details(pk)
        my_account.Deliverables.delete_fee_project_version(pk)

        self.assertEqual(res['status'], 200)

    def test_update_fee_project_version(self):
        """ Test that 200 is returned """

        pk = self._create_fee_project_version_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Deliverables.update_fee_project_version(pk, data)
        my_account.Deliverables.delete_fee_project_version(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_fee_project_version(self):
        """ Test that 204 is returned """

        pk = self._create_fee_project_version_return_pk()
        res = my_account.Deliverables.delete_fee_project_version(pk)

        self.assertEqual(res['status'], 204)

    ### Fees ###
    def _create_fee_return_pk(self):
        """ Create a fee and return the pk """
        data = {
            "title": "UNITTEST",
            "amount_base": 0,
            "amount_current": 0,
            "progress": 0,
            "in_timeline": True
        }

        return my_account.Deliverables.create_fee(project_pk, data)['data']['pk']

    def test_get_fees_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_fee(self):
        """ Test that 201 is returned """

        data = {
            "title": "UNITTEST",
            "amount_base": 0,
            "amount_current": 0,
            "progress": 0,
            "in_timeline": True
        }

        res = my_account.Deliverables.create_fee(project_pk, data)
        my_account.Deliverables.delete_fee(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_get_fee_details(self):
        """ Test that 200 is returned """

        pk = self._create_fee_return_pk()
        res = my_account.Deliverables.get_fee_details(pk)
        my_account.Deliverables.delete_fee(pk)

        self.assertEqual(res['status'], 200)

    def test_update_fee(self):
        """ Test that 200 is returned """

        pk = self._create_fee_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Deliverables.update_fee(pk, data)
        my_account.Deliverables.delete_fee(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_fee(self):
        """ Test that 201 is returned """

        pk = self._create_fee_return_pk()
        res = my_account.Deliverables.delete_fee(pk)

        self.assertEqual(res['status'], 204)

    ### Fee projections ###
    def test_get_fees_projection_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_projection_list(project_pk)

        self.assertEqual(res['status'], 200)

    ### Fees project ###
    def _create_fee_project_return_pk(self):
        """ Create a fee project and return pk """
        data = {
            "title": "UNITTEST",
            "project": project_pk
        }

        return my_account.Deliverables.create_fee_project(data)['data']['id']

    def test_get_fees_project_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_project_list()

        self.assertEqual(res['status'], 200)

    def test_get_fees_project_list_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_fees_project_list_projects(project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_fees_projects_update(self):
        """ Test that 200 is returned """

        pk = self._create_fee_project_return_pk()

        res = my_account.Deliverables.get_fees_projects_update(pk)

        self.assertEqual(res['status'], 200)

    def test_create_fees_project(self):
        """ Test that 201 is returned """

        data = {
            "title": "UNITTEST",
            "project": project_pk
        }

        res = my_account.Deliverables.create_fee_project(data)
        my_account.Deliverables.delete_fee_project(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_fees_project_details(self):
        """ Test that 200 is returned """

        pk = self._create_fee_project_return_pk()

        res = my_account.Deliverables.get_fees_project_details(pk)
        my_account.Deliverables.delete_fee_project(pk)

        self.assertEqual(res['status'], 200)

    def test_update_fee_project(self):
        """ Test that 200 is returned """

        pk = self._create_fee_project_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Deliverables.update_fee_project(pk, data)
        my_account.Deliverables.delete_fee_project(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_fee_project(self):
        """ Test that 204 is returned """

        pk = self._create_fee_project_return_pk()
        res = my_account.Deliverables.delete_fee_project(pk)

        self.assertEqual(res['status'], 204)

    ### Fees revision ###
    def _create_fee_revision_return_pk(self):
        """ Test that 201 is returned 

        :return: {"pk": pk, "fee_pk": fee_pk}
        """
        fee_pk = self._create_fee_return_pk()

        data = {
            "amount": 10,
            "date": "06-05-2021"
        }

        pk = my_account.Deliverables.create_fee_revisions_item(fee_pk, data)['data']['pk']

        return {"pk": pk, "fee_pk": fee_pk}

    def test_get_fees_revision_details(self):
        """ Test that 200 is returned """

        res_creation = self._create_fee_revision_return_pk()

        res = my_account.Deliverables.get_fees_revision_details(res_creation['pk'])
        my_account.Deliverables.delete_fee(res_creation['fee_pk'])

        self.assertEqual(res['status'], 200)

    def test_delete_fees_revision(self):
        """ Test that 204 is returned """

        res_creation = self._create_fee_revision_return_pk()

        data = {
            "amount": 11
        }

        res = my_account.Deliverables.delete_fee_revision(res_creation['pk'])
        my_account.Deliverables.delete_fee(res_creation['fee_pk'])

        self.assertEqual(res['status'], 204)

    def test_get_fees_revision_details(self):
        """ Test that 200 is returned """

        res_creation = self._create_fee_revision_return_pk()

        res = my_account.Deliverables.get_fees_revision_details(res_creation['pk'])

        self.assertEqual(res['status'], 200)

    def test_get_fees_revision_fees(self):
        """ Test that 200 is returned """

        pk = self._create_fee_return_pk()
        res = my_account.Deliverables.get_fees_revisions_item_details(pk)

        my_account.Deliverables.delete_fee(pk)

        self.assertEqual(res['status'], 200)

    def test_create_fee_revisions_item(self):
        """ Test that 201 is returned """

        pk = self._create_fee_return_pk()

        data = {
            "amount": 10,
            "date": "06-05-2021"
        }

        res = my_account.Deliverables.create_fee_revisions_item(pk, data)
        my_account.Deliverables.delete_fee(pk)
        my_account.Deliverables.delete_fee_revision(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    ### other ###

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

    # Fee zones
    def _create_fee_zones_return_pk(self):
        """ Create fee zones return pk 

        :return: {"pk": pk, "zone_pk": zone_pk['pk'], "area_pk": zone_pk['area_pk']}
        """
        zone_pk = self._create_zone_return_pk()

        data = {
            "zone": zone_pk['pk'],
            "project": project_pk,
            "fee_project": fee_project,
            "board": 0,
            "rendering": 0
        }

        pk = my_account.Deliverables.create_fee_zones(data)['data']['id']

        return {"pk": pk, "zone_pk": zone_pk['pk'], "area_pk": zone_pk['area_pk']}

    def test_get_fees_zones_list(self):
        """ Test that 200 is returend """
        res = my_account.Deliverables.get_fees_zones_list()

        self.assertEqual(res['status'], 200)

    def test_create_fees_zones(self):
        """ Test that 201 is returned """

        zone_pk = self._create_zone_return_pk()

        data = {
            "zone": zone_pk['pk'],
            "project": project_pk,
            "fee_project": fee_project,
            "board": 0,
            "rendering": 0
        }

        res = my_account.Deliverables.create_fee_zones(data)

        my_account.Deliverables.delete_fees_zone(res['data']['id'])
        my_account.Deliverables.delete_zone(zone_pk['pk'])
        my_account.Deliverables.delete_area(zone_pk['area_pk'])

        self.assertEqual(res['status'], 201)

    def test_get_fees_zone_details(self):
        """ Test that 200 is returned """

        res_pk = self._create_fee_zones_return_pk()
        res = my_account.Deliverables.get_fees_zone_details(res_pk['pk'])

        my_account.Deliverables.delete_fees_zone(res_pk['pk'])
        my_account.Deliverables.delete_zone(res_pk['zone_pk'])
        my_account.Deliverables.delete_area(res_pk['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_update_fee_zones(self):
        """ Test that 200 is returned """

        res_pk = self._create_fee_zones_return_pk()

        data = {
            "date": "05-05-2021"
        }

        res = my_account.Deliverables.update_fee_zone(res_pk['pk'], data)

        my_account.Deliverables.delete_fees_zone(res_pk['pk'])
        my_account.Deliverables.delete_zone(res_pk['zone_pk'])
        my_account.Deliverables.delete_area(res_pk['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_delete_fee_zone(self):
        """ Test that 204 is returned """

        res_pk = self._create_fee_zones_return_pk()

        res = my_account.Deliverables.delete_fees_zone(res_pk['pk'])
        my_account.Deliverables.delete_zone(res_pk['zone_pk'])
        my_account.Deliverables.delete_area(res_pk['area_pk'])

        self.assertEqual(res['status'], 204)

    #### Plans ####

    def _create_plan_return_pk(self):
        """ Create plan and return pk """

        data = {
            "name_fr": "UNITTEST",
            "name_en": "UNITTEST",
            "plan_format": "A1",
            "scale": "1/50e",
            "level": "000",
            "lot": 10,
            "code": "pln",
            "custom_field_1": "",
            "custom_field_2": "",
            "custom_field_3": "",
            "org": my_account.org_pk
        }

        return my_account.Deliverables.create_plan(project_pk, data)['data']['id']

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

    def test_create_plan(self):
        """ Test that 201 is returned """

        data = {
            "name_fr": "UNITTEST",
            "name_en": "UNITTEST",
            "plan_format": "A1",
            "scale": "1/50e",
            "level": "000",
            "lot": 10,
            "code": "pln",
            "custom_field_1": "",
            "custom_field_2": "",
            "custom_field_3": "",
            "org": my_account.org_pk
        }

        res = my_account.Deliverables.create_plan(project_pk, data)

        my_account.Deliverables.delete_plan(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_update_plan(self):
        """ Test that 200 is returned """

        pk = self._create_plan_return_pk()

        data = {
            "name_fr": "UPDATED",
        }

        res = my_account.Deliverables.update_plan(pk, data)

        my_account.Deliverables.delete_plan(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_plan(self):
        """ Test that 204 is returned """

        pk = self._create_plan_return_pk()

        res = my_account.Deliverables.delete_plan(pk)

        self.assertEqual(res['status'], 204)

    def test_get_plan_details(self):
        """ Test that 200 is returned """
        pk = self._create_plan_return_pk()

        res = my_account.Deliverables.get_plan_details(pk)

        my_account.Deliverables.delete_plan(pk)

        self.assertEqual(res['status'], 200)

    def test_get_plans_planphases_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_plans_planphases_list(project_pk)

        self.assertEqual(res['status'], 200)

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

    #### Defaults ####

    ### Phasesets ###
    def _create_phaseset_return_pk(self):
        """ Create a phaseset and return pk """
        data = {
            "is_main": False,
            "title": "UNITTEST",
            "team": team_pk
        }

        return my_account.Deliverables.create_defaults_phasesets_org(data)['data']['id']

    # def test_apply_defaults_phasesets(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass : 404
    #     res = my_account.Deliverables.apply_defaults_phasesets()

    #     self.assertEqual(res['status'], 201)

    def test_duplicate_defaults_phasesets(self):
        """ Test that 201 is returned """
        #! Pass, but returns 200 instead of 201
        pk = self._create_phaseset_return_pk()

        res = my_account.Deliverables.duplicate_defaults_phasesets(pk)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phasesets_org_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_phasesets_org_list()

        self.assertEqual(res['status'], 200)

    def test_create_defaults_phasesets_org(self):
        """ Test that 201 is returned """
        data = {
            "is_main": False,
            "title": "UNITTEST",
            "team": team_pk
        }

        res = my_account.Deliverables.create_defaults_phasesets_org(data)

        self.assertEqual(res['status'], 201)

    def test_get_defaults_phasesets_team_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_phasesets_team_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_defaults_phasesets_team(self):
        """ Test that 201 is returned """
        #! Pass, but returns 200 instead of 201

        data = {
            "is_main": False,
            "title": "UNITTEST"
        }

        res = my_account.Deliverables.create_defaults_phasesets_team(team_pk, data)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phasesets_details(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_phaseset_return_pk()
        res = my_account.Deliverables.get_defaults_phasesets_details(phaseset_pk)
        my_account.Deliverables.delete_defaults_phasesets(phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_update_defaults_phasesets(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_phaseset_return_pk()

        data = {
            "title": "UNITTEST"
        }

        res = my_account.Deliverables.update_defaults_phasesets(phaseset_pk, data)
        my_account.Deliverables.delete_defaults_phasesets(phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_defaults_phasesets(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_phaseset_return_pk()
        res = my_account.Deliverables.delete_defaults_phasesets(phaseset_pk)

        self.assertEqual(res['status'], 204)

    ### Phases ###
    def _create_defaults_phase_return_pk(self):
        """ Create a default phase and return it 

        :return: {'pk': pk, "phaseset_pk": phaseset_pk}
        """
        phaseset_pk = self._create_phaseset_return_pk()

        data = {
            "name": "UNITTEST",
            "shortname": "TEST",
            "pct": 10,
            "library": phaseset_pk,
            "team": team_pk
        }

        pk = my_account.Deliverables.create_defaults_phase_org(data)['data']['id']

        return {'pk': pk, "phaseset_pk": phaseset_pk}

    def test_duplicate_defaults_phase(self):
        """ Test that 201 is returned """
        res_creation = self._create_defaults_phase_return_pk()

        res = my_account.Deliverables.duplicate_defaults_phase(res_creation['pk'])

        my_account.Deliverables.delete_defaults_phase(res_creation['pk'])
        my_account.Deliverables.delete_defaults_phasesets(res_creation['phaseset_pk'])

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_org_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_phase_org_list()

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_team_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_phase_team_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_defaults_phase_org(self):
        """ Test that 201 is returned """
        phaseset_pk = self._create_phaseset_return_pk()

        data = {
            "name": "UNITTEST",
            "shortname": "TEST",
            "pct": 10,
            "library": phaseset_pk,
            "team": team_pk
        }

        res = my_account.Deliverables.create_defaults_phase_org(data)
        my_account.Deliverables.delete_defaults_phasesets(phaseset_pk)

        self.assertEqual(res['status'], 201)

    def test_create_defaults_phase_team(self):
        """ Test that 201 is returned """
        #! Pass, but 200 is returned instead of 201
        phaseset_pk = self._create_phaseset_return_pk()

        data = {
            "name": "UNITTEST",
            "shortname": "TEST",
            "pct": 10,
            "library": phaseset_pk,
            "team": team_pk
        }

        res = my_account.Deliverables.create_defaults_phase_team(team_pk, data)
        my_account.Deliverables.delete_defaults_phasesets(phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_details(self):
        """ Test that 200 is returned """
        res_creation = self._create_defaults_phase_return_pk()

        res = my_account.Deliverables.get_defaults_phase_details(res_creation['pk'])

        my_account.Deliverables.delete_defaults_phase(res_creation['pk'])
        my_account.Deliverables.delete_defaults_phasesets(res_creation['phaseset_pk'])

        self.assertEqual(res['status'], 200)

    def test_update_defaults_phase(self):
        """ Test that 200 is returned """
        res_creation = self._create_defaults_phase_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Deliverables.update_defaults_phase(res_creation['pk'], data)

        my_account.Deliverables.delete_defaults_phase(res_creation['pk'])
        my_account.Deliverables.delete_defaults_phasesets(res_creation['phaseset_pk'])

        self.assertEqual(res['status'], 200)

    def test_delete_defaults_phase(self):
        """ Test that 204 is returned """

        res_creation = self._create_defaults_phase_return_pk()

        res = my_account.Deliverables.delete_defaults_phase(res_creation['pk'])
        my_account.Deliverables.delete_defaults_phasesets(res_creation['phaseset_pk'])

        self.assertEqual(res['status'], 204)

    ### Plansets ###
    def _create_plansets_return_pk(self):
        """ Create a plansets and return pk """
        data = {
            "title": "UNITTEST"
        }

        return my_account.Deliverables.create_defaults_plansets_org(data)['data']['id']

    # def test_apply_defaults_plansets(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass : 404
    #     pk = self._create_plansets_return_pk()
    #     res = my_account.Deliverables.apply_defaults_plansets()

    #     self.assertEqual(res['status'], 201)

    def test_duplicate_defaults_plansets(self):
        """ Test that 201 is returned """
        #! Pass, but returns 200 instead of 201
        pk = self._create_plansets_return_pk()

        res = my_account.Deliverables.duplicate_defaults_plansets(pk)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_plansets_org_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_plansets_org_list()

        self.assertEqual(res['status'], 200)

    def test_create_defaults_plansets_org(self):
        """ Test that 201 is returned """
        data = {
            "title": "UNITTEST"
        }

        res = my_account.Deliverables.create_defaults_plansets_org(data)

        self.assertEqual(res['status'], 201)

    def test_get_defaults_plansets_team_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_plansets_team_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_defaults_plansets_team(self):
        """ Test that 201 is returned """
        #! Pass, but returns 200 instead of 201

        data = {
            "is_main": False,
            "title": "UNITTEST"
        }

        res = my_account.Deliverables.create_defaults_plansets_team(team_pk, data)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_plansets_details(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_plansets_return_pk()
        res = my_account.Deliverables.get_defaults_plansets_details(phaseset_pk)
        my_account.Deliverables.delete_defaults_plansets(phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_update_defaults_plansets(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_plansets_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Deliverables.update_defaults_plansets(phaseset_pk, data)
        my_account.Deliverables.delete_defaults_plansets(phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_defaults_plansets(self):
        """ Test that 200 is returned """

        phaseset_pk = self._create_plansets_return_pk()
        res = my_account.Deliverables.delete_defaults_plansets(phaseset_pk)

        self.assertEqual(res['status'], 204)

    ### Phases ###
    def _create_defaults_plan_return_pk(self):
        """ Create a default plan and return it 

        :return: {'pk': pk, "plansets_pk": plansets_pk, "zone_pk": res_zone_pk['pk'], "area_pk": res_zone_pk['area_pk']}
        """
        plansets_pk = self._create_plansets_return_pk()
        res_zone_pk = self._create_zone_return_pk()

        data = {
            "zone": res_zone_pk['pk'],
            "name_fr": "string",
            "name_en": "string",
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": "string",
            "library": plansets_pk
        }

        pk = my_account.Deliverables.create_defaults_plan_org(data)['data']['id']

        return {'pk': pk, "plansets_pk": plansets_pk, "zone_pk": res_zone_pk['pk'], "area_pk": res_zone_pk['area_pk']}

    # def test_duplicate_defaults_plan(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass : 500
    #     res_creation = self._create_defaults_plan_return_pk()

    #     res = my_account.Deliverables.duplicate_defaults_plan(res_creation['pk'])

        # my_account.Deliverables.delete_defaults_plan(res_creation['pk'])
        # my_account.Deliverables.delete_defaults_plansets(res_creation['plansets_pk'])
        # my_account.Deliverables.delete_zone(res_creation['zone_pk'])
        # my_account.Deliverables.delete_area(res_creation['area_pk'])

    #     self.assertEqual(res['status'], 200)

    def test_get_defaults_plan_org_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_plans_org_list()

        self.assertEqual(res['status'], 200)

    def test_get_defaults_plan_team_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_defaults_plans_team_list(team_pk)

        self.assertEqual(res['status'], 200)

    def test_create_defaults_plan_org(self):
        """ Test that 201 is returned """

        plansets_pk = self._create_plansets_return_pk()
        res_zone_pk = self._create_zone_return_pk()

        data = {
            "zone": res_zone_pk['pk'],
            "name_fr": "string",
            "name_en": "string",
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": "string",
            "library": plansets_pk
        }

        res = my_account.Deliverables.create_defaults_plan_org(data)

        my_account.Deliverables.delete_defaults_plan(res['data']['id'])
        my_account.Deliverables.delete_defaults_plansets(plansets_pk)
        my_account.Deliverables.delete_zone(res_zone_pk['pk'])
        my_account.Deliverables.delete_area(res_zone_pk['area_pk'])

        self.assertEqual(res['status'], 201)

    def test_create_defaults_plan_team(self):
        """ Test that 201 is returned """
        #! Pass but returns a 200 and a list of objects / Do not return anything in the list

        plansets_pk = self._create_plansets_return_pk()
        res_zone_pk = self._create_zone_return_pk()

        data = {
            "zone": res_zone_pk['pk'],
            "name_fr": "string",
            "name_en": "string",
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": "string",
            "library": plansets_pk
        }

        res = my_account.Deliverables.create_defaults_plan_team(team_pk, data)

        # my_account.Deliverables.delete_defaults_plan(res['data'][0]['id'])
        my_account.Deliverables.delete_defaults_plansets(plansets_pk)
        my_account.Deliverables.delete_zone(res_zone_pk['pk'])
        my_account.Deliverables.delete_area(res_zone_pk['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_get_defaults_plan_details(self):
        """ Test that 200 is returned """
        res_creation = self._create_defaults_plan_return_pk()

        res = my_account.Deliverables.get_defaults_plan_details(res_creation['pk'])

        my_account.Deliverables.delete_defaults_plan(res_creation['pk'])
        my_account.Deliverables.delete_defaults_plansets(res_creation['plansets_pk'])
        my_account.Deliverables.delete_zone(res_creation['zone_pk'])
        my_account.Deliverables.delete_area(res_creation['area_pk'])

        self.assertEqual(res['status'], 200)

    def test_update_defaults_plan(self):
        """ Test that 200 is returned """
        res_creation = self._create_defaults_plan_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Deliverables.update_defaults_plan(res_creation['pk'], data)

        my_account.Deliverables.delete_defaults_plan(res_creation['pk'])
        my_account.Deliverables.delete_defaults_plansets(res_creation['plansets_pk'])
        my_account.Deliverables.delete_zone(res_creation['zone_pk'])
        my_account.Deliverables.delete_area(res_creation['area_pk'])

        self.assertEqual(res['status'], 200)

    # def test_delete_defaults_plan(self):
    #     """ Test that 204 is returned """
    #     #! Do not pass : 500

    #     res_creation = self._create_defaults_plan_return_pk()

    #     res = my_account.Deliverables.delete_defaults_phase(res_creation['pk'])

    #     my_account.Deliverables.delete_defaults_plansets(res_creation['plansets_pk'])
    #     my_account.Deliverables.delete_zone(res_creation['zone_pk'])
    #     my_account.Deliverables.delete_area(res_creation['area_pk'])

    #     self.assertEqual(res['status'], 204)

    #### Documents ####
    def _create_document_return_pk(self):
        """ Create a document a return pk """

        data = {
            "name": "UNITTEST",
            "price": 10,
            "annexes": []
        }

        return my_account.Deliverables.create_document(project_pk, data)['data']['id']

    def test_get_documents_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_documents_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_document(self):
        """ Test that 201 is returned """

        data = {
            "name": "UNITTEST",
            "price": 10,
            "annexes": []
        }

        res = my_account.Deliverables.create_document(project_pk, data)
        my_account.Deliverables.delete_document(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_documents_details(self):
        """ Test that 200 is returned """

        pk = self._create_document_return_pk()

        res = my_account.Deliverables.get_document_details(pk)

        self.assertEqual(res['status'], 200)

    def test_update_document(self):
        """ Test that 200 is returned """

        pk = self._create_document_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Deliverables.update_document(pk, data)
        my_account.Deliverables.delete_document(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_document(self):
        """ Test that 204 is returned """

        pk = self._create_document_return_pk()
        res = my_account.Deliverables.delete_document(pk)

        self.assertEqual(res['status'], 204)

    #### Contracts ####

    ### Contractors ###
    def _create_contractor_return_pk(self):
        """ Create contractor and return pk """
        data = {
            "name": "UNITTEST",
            "tags": []
        }

        return my_account.Deliverables.create_contractors(data)['data']['id']

    def test_get_contractors_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_contractors_list()

        self.assertEqual(res['status'], 200)

    def test_create_contractor(self):
        """ Test that 201 is returned """

        data = {
            "name": "UNITTEST",
            "tags": []
        }

        res = my_account.Deliverables.create_contractors(data)
        my_account.Deliverables.delete_contractor(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_contractor_details(self):
        """ Test that 200 is returned """
        pk = self._create_contractor_return_pk()

        res = my_account.Deliverables.get_contractor_details(pk)
        my_account.Deliverables.delete_contractor(pk)

        self.assertEqual(res['status'], 200)

    def test_update_contractor(self):
        """ Test that 200 is returned """
        pk = self._create_contractor_return_pk()

        data = {
            "name": "UPDATED"
        }

        res = my_account.Deliverables.update_contractor(pk, data)
        my_account.Deliverables.delete_contractor(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_contractor(self):
        """ Test that 204 is returned """
        pk = self._create_contractor_return_pk()

        res = my_account.Deliverables.delete_contractor(pk)

        self.assertEqual(res['status'], 204)

    ### Contract items ###
    def _create_contract_item_return_pk(self):
        """ Create a contract item and return pk 

        :return: {"pk": pk, "contract_pk": contract_pk['pk'], "contractor_pk": contract_pk['contractor_pk'],
                "fee_project": contract_pk['fee_project']}
        """
        contract_pk = self._create_contract_return_pk()

        data = {
            "contract": contract_pk['pk'],
            "fee": 100
        }

        pk = my_account.Deliverables.create_contracts_items(data)['data']['id']

        return {"pk": pk, "contract_pk": contract_pk['pk'], "contractor_pk": contract_pk['contractor_pk'],
                "fee_project": contract_pk['fee_project']}

    def test_generate_contracts_project(self):
        """ Test that 201 is returned """
        #! Pass but returns 200 instead of 201
        res = my_account.Deliverables.generate_contracts_project(project_pk)

        self.assertEqual(res['status'], 200)

    # def test_generate_contracts_org(self):
    #     """ Test that 201 is returned """
    #     #! Do not pass : 403 : no permission to perfom this action
    #     res = my_account.Deliverables.generate_contracts_org()

    #     self.assertEqual(res['status'], 201)

    def test_get_contract_items_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_contracts_items_list()

        self.assertEqual(res['status'], 200)

    def test_create_contract_item(self):
        """ Test that 201 is returned """

        res_pk = self._create_contract_return_pk()

        data = {
            "contract": res_pk['pk'],
            "fee": 100
        }

        res = my_account.Deliverables.create_contracts_items(data)

        my_account.Deliverables.delete_contract_item(res['data']['id'])
        my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 201)

    def test_get_contract_item_details(self):
        """ Test that 200 is returned """

        res_pk = self._create_contract_item_return_pk()

        res = my_account.Deliverables.get_contract_item_details(res_pk['pk'])

        my_account.Deliverables.delete_contract_item(res_pk['pk'])
        my_account.Deliverables.delete_contract(res_pk['contract_pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    # def test_update_contract_item(self):
    #     """ Test that 200 is returned """
    #     #! Do not pass : 500 withtout message

    #     res_pk = self._create_contract_item_return_pk()

    #     data = {
    #         "contract": res_pk['contract_pk'],
    #         "already_paid": 10
    #     }

    #     res = my_account.Deliverables.update_contract_item(res_pk['pk'], data)
    #     print(res)

    #     my_account.Deliverables.delete_contract_item(res_pk['pk'])
    #     my_account.Deliverables.delete_contract(res_pk['contract_pk'])
    #     my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
    #     my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

    #     self.assertEqual(res['status'], 200)

    def test_delete_contract_item_details(self):
        """ Test that 204 is returned """

        res_pk = self._create_contract_item_return_pk()

        res = my_account.Deliverables.delete_contract_item(res_pk['pk'])
        my_account.Deliverables.delete_contract(res_pk['contract_pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 204)

    ### Contracts ###

    def _create_contract_return_pk(self):
        """ Create contract and return pk 

        {"pk": pk, "contractor_pk": pk_contractor, "fee_project", fee_project}
        """

        pk_contractor = self._create_contractor_return_pk()
        fee_project = self._create_fee_project_return_pk()

        data = {
            "contractor": pk_contractor,
            "fee_project": fee_project,
            "type": "sub",
            "description": "string",
            "tax_rate": 1,
            "project": project_pk,
        }

        pk = my_account.Deliverables.create_contract(data)['data']['id']

        return {"pk": pk, "contractor_pk": pk_contractor, "fee_project": fee_project}

    def test_get_contracts_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_contracts_list()

        self.assertEqual(res['status'], 200)

    def test_create_contract(self):
        """ Test that 201 is returned """

        pk_contractor = self._create_contractor_return_pk()
        fee_project = self._create_fee_project_return_pk()

        data = {
            "contractor": pk_contractor,
            "fee_project": fee_project,
            "type": "sub",
            "description": "string",
            "tax_rate": 1,
            "project": project_pk,
        }

        res = my_account.Deliverables.create_contract(data)

        my_account.Deliverables.delete_contract(res['data']['id'])
        my_account.Deliverables.delete_contractor(pk_contractor)
        my_account.Deliverables.delete_fee_project(fee_project)

        self.assertEqual(res['status'], 201)

    def test_get_contract_details(self):
        """ Test that 200 is returned """

        res_pk = self._create_contract_return_pk()

        res = my_account.Deliverables.get_contract_details(res_pk['pk'])

        my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_update_contract(self):
        """ Test that 200 is returned """

        res_pk = self._create_contract_return_pk()

        data = {
            "description": "UPDATED"
        }

        res = my_account.Deliverables.update_contract(res_pk['pk'], data)

        my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_delete_contract(self):
        """ Test that 204 is returned """

        res_pk = self._create_contract_return_pk()

        res = my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 204)

    ### Contracts month ###
    def _create_contract_month_return_pk(self):
        """ Create contract month return pk 

        :return: {"pk": pk, "contract_pk": res_pk['pk'], "contractor_pk": res_pk['contractor_pk'],
                "fee_project": res_pk['fee_project']}

        """
        res_pk = self._create_contract_return_pk()

        data = {
            "contract": res_pk['pk'],
            "year": 2021,
            "month": 5,
            "start_date": "06-05-2021",
            "end_date": "06-05-2021",
            "budget": 0,
            "budget_projected": 0,
            "actual": 0,
            "pct": 0
        }

        pk = my_account.Deliverables.create_contracts_month(data)['data']['id']

        return {"pk": pk, "contract_pk": res_pk['pk'], "contractor_pk": res_pk['contractor_pk'],
                "fee_project": res_pk['fee_project']}

    def test_generate_contracts_month(self):
        """ Test that 201 is returned """

        #! Pass but 200 is returned

        res_pk = self._create_contract_return_pk()

        res = my_account.Deliverables.generate_contracts_month_org(res_pk['pk'])

        my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_get_contracts_month_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_contracts_month_list()

        self.assertEqual(res['status'], 200)

    def test_create_contract_month(self):
        """ Test that 201 is returned """

        res_pk = self._create_contract_return_pk()

        data = {
            "contract": res_pk['pk'],
            "year": 2021,
            "month": 5,
            "start_date": "06-05-2021",
            "end_date": "06-05-2021",
            "budget": 0,
            "budget_projected": 0,
            "actual": 0,
            "pct": 0
        }

        res = my_account.Deliverables.create_contracts_month(data)

        my_account.Deliverables.delete_contract_month(res['data']['id'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_contract(res_pk['pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 201)

    def test_get_contract_month_details(self):
        """ Test that 200 is returned """

        res_pk = self._create_contract_month_return_pk()

        res = my_account.Deliverables.get_contract_month_details(res_pk['pk'])

        my_account.Deliverables.delete_contract_month(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_contract(res_pk['contract_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_update_contract_month(self):
        """ Test that 200 is returned """

        res_pk = self._create_contract_month_return_pk()

        data = {
            "start_date": "05-05-2021"
        }

        res = my_account.Deliverables.update_contracts_month(res_pk['pk'], data)

        my_account.Deliverables.delete_contract_month(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_contract(res_pk['contract_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 200)

    def test_delete_contract_month(self):
        """ Test that 204 is returned """

        res_pk = self._create_contract_month_return_pk()

        res = my_account.Deliverables.delete_contract_month(res_pk['pk'])
        my_account.Deliverables.delete_contractor(res_pk['contractor_pk'])
        my_account.Deliverables.delete_contract(res_pk['contract_pk'])
        my_account.Deliverables.delete_fee_project(res_pk['fee_project'])

        self.assertEqual(res['status'], 204)

    #### Revisions ####

    ### Annexes ###

    def test_get_revisions_annexes_team_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_revisions_annexes_team_project(team_pk, project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_annex_revision(self):
        """ Test that 201 is returned """

        pk = self._create_annexe_return_pk()

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_annexe_revision(team_pk, project_pk, data)
        my_account.Deliverables.delete_revisions_annexe_detail(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_delete_annex_revision(self):
        """ Test that 201 is returned """

        pk_annex = self._create_annexe_return_pk()

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": pk_annex,
            "progress": 80
        }

        pk = my_account.Deliverables.create_annexe_revision(team_pk, project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_annexe_detail(pk)

        self.assertEqual(res['status'], 204)

    ### Documents ###

    def test_get_revisions_documents_team_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_revisions_documents_team_project(team_pk, project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_document_revision(self):
        """ Test that 201 is returned """
        pk = self._create_document_return_pk()

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_document_revision(team_pk, project_pk, data)

        self.assertEqual(res['status'], 201)

    def test_delete_document_revision(self):
        """ Test that 204 is returned """

        pk_doc = self._create_document_return_pk()

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": pk_doc,
            "progress": 80
        }

        pk = my_account.Deliverables.create_document_revision(team_pk, project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_document_detail(pk)

        self.assertEqual(res['status'], 204)

    ### Fee items ###
    def test_get_revisions_fee_items_team_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_revisions_fee_items_team_project(team_pk, project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_fee_items_revision(self):
        """ Test that 201 is returned """

        fee_pk = self._create_fee_return_pk()

        data = {
            "fee_item": fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Deliverables.create_fee_items_revision(team_pk, project_pk, data)
        my_account.Deliverables.delete_fee(fee_pk)
        my_account.Deliverables.delete_revisions_fee_items_detail(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_delete_fee_items_revision(self):
        """ Test that 204 is returned """

        fee_pk = self._create_fee_return_pk()

        data = {
            "fee_item": fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Deliverables.create_fee_items_revision(team_pk, project_pk, data)
        res = my_account.Deliverables.delete_revisions_fee_items_detail(pk['data']['id'])
        my_account.Deliverables.delete_fee(fee_pk)

        self.assertEqual(res['status'], 204)

    ### Phases ###

    def test_get_revisions_phases_team_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_revisions_phases_team_project(team_pk, project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_phases_revision(self):
        """ Test that 201 is returned """

        phase_pk = self._create_phase_return_pk()

        data = {
            "phase": phase_pk['pk'],
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Deliverables.create_phase_revision(team_pk, project_pk, data)

        my_account.Deliverables.delete_phase(phase_pk['pk'])
        my_account.Deliverables.delete_fee_project(phase_pk['fee_project'])

        self.assertEqual(res['status'], 201)

    def test_delete_phase_revision(self):
        """ Test that 204 is returned """

        phase_pk = self._create_phase_return_pk()

        data = {
            "phase": phase_pk['pk'],
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Deliverables.create_phase_revision(team_pk, project_pk, data)['data']['id']

        res = my_account.Deliverables.delete_revisions_phases_detail(pk)

        my_account.Deliverables.delete_phase(phase_pk['pk'])
        my_account.Deliverables.delete_fee_project(phase_pk['fee_project'])

        self.assertEqual(res['status'], 204)
    ### Plans ###

    def test_get_revisions_plans_team_project(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_revisions_plans_team_project(team_pk, project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_plan_revision(self):
        """ Test that 201 is returned """

        plan_pk = self._create_plan_return_pk()

        planphase_pk = my_account.Deliverables.get_plan_details(plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_plan_revision(team_pk, project_pk, data)

        my_account.Deliverables.delete_revisions_plan_detail(res['data']['id'])
        my_account.Deliverables.delete_plan(plan_pk)

        self.assertEqual(res['status'], 201)

    def test_delete_plan_revision(self):
        """ Test that 204 is returned """

        plan_pk = self._create_plan_return_pk()

        planphase_pk = my_account.Deliverables.get_plan_details(plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80
        }

        pk = my_account.Deliverables.create_plan_revision(team_pk, project_pk, data)['data']['id']

        res = my_account.Deliverables.delete_revisions_plan_detail(pk)

        my_account.Deliverables.delete_phase_planphase(plan_pk)

        self.assertEqual(res['status'], 204)

    #### Annexes ####
    def _create_annexe_return_pk(self):
        """ Create annexe and return pk """

        data = {
            "title": "UNITTEST",
            "annex_type": "time",
            "total_fees": 1,
            "description": "UNITTEST",
            "date": "06-05-2021"
        }

        return my_account.Deliverables.create_annexe(project_pk, data)['data']['id']

    def test_get_annexes_list(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.get_annexes_list(project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_annexe(self):
        """ Test that 201 is returned """

        data = {
            "title": "UNITTEST",
            "annex_type": "time",
            "total_fees": 1,
            "description": "UNITTEST",
            "date": "06-05-2021"
        }

        res = my_account.Deliverables.create_annexe(project_pk, data)
        my_account.Deliverables.delete_annexe(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_annexe_details(self):
        """ Test that 200 is returned """

        pk = self._create_annexe_return_pk()
        res = my_account.Deliverables.get_annexe_details(pk)
        my_account.Deliverables.delete_annexe(pk)

        self.assertEqual(res['status'], 200)

    def test_update_annexe(self):
        """ Test that 200 is returned """

        pk = self._create_annexe_return_pk()

        data = {
            "title": "UPDATED"
        }

        res = my_account.Deliverables.update_annexe(pk, data)
        my_account.Deliverables.delete_annexe(pk)

        self.assertEqual(res['status'], 200)

    def test_delete_annexe(self):
        """ Test that 204 is returned """

        pk = self._create_annexe_return_pk()

        res = my_account.Deliverables.delete_annexe(pk)

        self.assertEqual(res['status'], 204)


if __name__ == '__main__':
    unittest.main()
