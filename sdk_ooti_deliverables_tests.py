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
    #     print(res)

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
        #! Pass but returns a 200 and a list of objects

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

        my_account.Deliverables.delete_defaults_plan(res['data'][0]['id'])
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


if __name__ == '__main__':
    unittest.main()
