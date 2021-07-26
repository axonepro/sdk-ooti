import unittest
from ooti import ooti
from test_helper import TestHelper

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


class TestAreas(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.area_pk = cls.testHelper._create_area_return_pk(cls.project_pk)

    def test_get_areas_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_areas_list(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_area(self):
        """ Test that 201 is returned """

        name = self.testHelper.create_name()

        area_data = {
            "name": name,
            "project": self.project_pk,
            "surface_area": 30
        }

        res = my_account.Deliverables.create_areas(self.project_pk, area_data)
        my_account.Deliverables.delete_area(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_area_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_areas_details(self.area_pk)
        my_account.Deliverables.delete_area(self.area_pk)

        self.assertEqual(res['status'], 200)

    def test_update_area(self):
        """ Test that 200 is returned """

        name = self.testHelper.create_name()

        update = {
            "name": name,
        }

        res = my_account.Deliverables.update_areas(self.area_pk, update)
        self.assertEqual(res['status'], 200)

    def test_delete_area(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_area(self.area_pk)
        self.assertEqual(res['status'], 204)


class TestPhases(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(cls.project_pk)
        cls.phase_pk = cls.testHelper._create_phase_return_pk(cls.project_pk, cls.fee_project_pk)
        cls.plan_pk = cls.testHelper._create_plan_return_pk(cls.project_pk)

    def test_pagination(self):
        my_account.update_pagination(1)

        phase_pk1 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)
        phase_pk2 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)
        phase_pk3 = self.testHelper._create_phase_return_pk(self.project_pk, self.fee_project_pk)

        res = my_account.Deliverables.get_phases_list(self.project_pk)
        self.assertEqual(res['status'], 200)
        self.assertEqual(len(res['data']), 1)
        obj = res['data'][0]

        res = my_account.Deliverables.get_phases_list(self.project_pk, page=2)
        self.assertEqual(res['status'], 200)
        self.assertEqual(len(res['data']), 1)
        self.assertNotEqual(obj, res['data'][0])

        my_account.update_pagination(5)
        res = my_account.Deliverables.get_phases_list(self.project_pk)
        self.assertEqual(res['status'], 200)
        self.assertLessEqual(len(res['data']), 5)

    def test_get_phases_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_list(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_get_phases_list_fee_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_list_fee_project(self.project_pk, self.fee_project_pk)
        self.assertEqual(res['status'], 200)

    def test_get_phases_projections_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phases_projections_list(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_export_phase(self):
        """ Test that 200 is returned """
        currency_pk = self.testHelper._create_currency_if_none()
        client_pk = self.testHelper._create_client_return_pk(team_pk, currency_pk)
        project_pk = self.testHelper._create_project_return_pk(client_pk, currency_pk)

        fee_project_pk = self.testHelper._create_fee_project_return_pk(project_pk)
        phase_pk = self.testHelper._create_phase_return_pk(project_pk, fee_project_pk)

        res = my_account.Deliverables.export_phase(project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_phase(self):
        """ Test that 201 is returned """

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "fee_project": self.fee_project_pk,
            "pct": 10,
            "dependants": []
        }

        res = my_account.Deliverables.create_phase(self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_phase_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_phase_details(self.phase_pk)
        self.assertEqual(res['status'], 200)

    def test_update_phase(self):
        """ Test that 200 is returned """

        data = {
            "name": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_phase(self.phase_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_phase(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_phase(self.phase_pk)
        self.assertEqual(res['status'], 204)

    def test_reset_phase_order(self):
        """ Test that 200 is returned """
        res = my_account.Deliverables.reset_phases_order(self.project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_phase_planphase_details(self):
        """ Test that 200 is returned """

        planphase_pk = my_account.Deliverables.get_plan_details(self.plan_pk)['data']['plan_phases'][0]['id']
        res = my_account.Deliverables.get_phase_planphase_details(planphase_pk)

        self.assertEqual(res['status'], 200)

    def test_update_phase_planphase(self):
        """ Test that 200 is returned """

        planphase_pk = my_account.Deliverables.get_plan_details(self.plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "progress": 20
        }

        res = my_account.Deliverables.update_phase_planphase(planphase_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_phase_planphase(self):
        """ Test that 204 is returned """

        planphase_pk = my_account.Deliverables.get_plan_details(self.plan_pk)['data']['plan_phases'][0]['id']

        res = my_account.Deliverables.delete_phase_planphase(planphase_pk)

        my_account.Deliverables.delete_plan(self.plan_pk)
        self.assertEqual(res['status'], 204)

    def test_update_phases_progress(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.update_phases_progress()
        self.assertEqual(res['status'], 200)


class TestMilestones(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.milestone_pk = cls.testHelper._create_milestone_return_pk(cls.project_pk)

    def test_get_milestones_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_milestones_list()
        self.assertEqual(res['status'], 200)

    def test_get_milestone_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_milestone_details(self.milestone_pk)
        self.assertEqual(res['status'], 200)

    def test_create_milestone(self):
        """ Test that 201 is returned """

        data = {
            "title": self.testHelper.create_name(),
            "project": self.project_pk,
            "date": "30-04-2021",
            "description": "string",
            "in_timeline": True
        }

        res = my_account.Deliverables.create_milestone(data)
        self.assertEqual(res['status'], 201)

    def test_update_milestone(self):
        """ Test that 200 is returned """

        data = {
            "title": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_milestone(self.milestone_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_milestone(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_milestone(self.milestone_pk)
        self.assertEqual(res['status'], 204)


class TestDefaults(unittest.TestCase):
    """
    test_duplicate_defaults_plan not working
    """

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.client_pk = cls.testHelper._create_client_return_pk(team_pk, currency_pk)
        cls.project_pk = cls.testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        # cls.project_pk = my_account.get_projects_list()['data'][0]['id']

        cls.area_pk = cls.testHelper._create_area_return_pk(cls.project_pk)
        cls.zone_pk = cls.testHelper._create_zone_return_pk(cls.area_pk)

        cls.phaseset_pk = cls.testHelper._create_phaseset_return_pk(cls.team_pk)
        cls.default_phase_pk = cls.testHelper._create_defaults_phase_return_pk(cls.team_pk, cls.phaseset_pk)
        cls.planset_pk = cls.testHelper._create_plansets_return_pk()
        cls.default_plan_pk = cls.testHelper._create_defaults_plan_return_pk(cls.planset_pk, cls.zone_pk)

    ## Phasesets ###

    def test_apply_defaults_phasesets(self):
        """ Test that 200 is returned """

        data = {
            'library': self.phaseset_pk,
            'project': self.project_pk,
        }

        res = my_account.Deliverables.apply_defaults_phasesets(data)
        self.assertEqual(res['status'], 200)

    def test_duplicate_defaults_phasesets(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.duplicate_defaults_phasesets(self.phaseset_pk)
        self.assertEqual(res['status'], 200)

    def test_get_defaults_phasesets_org_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phasesets_org_list()
        self.assertEqual(res['status'], 200)

    def test_create_defaults_phasesets_org(self):
        """ Test that 201 is returned """
        data = {
            "is_main": False,
            "title": self.testHelper.create_name(),
            "team": self.team_pk,
        }

        res = my_account.Deliverables.create_defaults_phasesets_org(data)
        self.assertEqual(res['status'], 201)

    def test_get_defaults_phasesets_team_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phasesets_team_list(self.team_pk)
        self.assertEqual(res['status'], 200)

    def test_create_defaults_phasesets_team(self):
        """ Test that 200 is returned """

        data = {
            "is_main": False,
            "title": self.testHelper.create_name(),
        }

        res = my_account.Deliverables.create_defaults_phasesets_team(self.team_pk, data)
        self.assertEqual(res['status'], 200)

    def test_get_defaults_phasesets_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phasesets_details(self.phaseset_pk)
        my_account.Deliverables.delete_defaults_phasesets(self.phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_update_defaults_phasesets(self):
        """ Test that 200 is returned """

        data = {
            "title": self.testHelper.create_name(),
        }

        res = my_account.Deliverables.update_defaults_phasesets(self.phaseset_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_defaults_phasesets(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.delete_defaults_phasesets(self.phaseset_pk)
        self.assertEqual(res['status'], 204)

    ### Phases ###

    def test_duplicate_defaults_phase(self):
        """ Test that 201 is returned """

        res = my_account.Deliverables.duplicate_defaults_phase(self.default_phase_pk)

        my_account.Deliverables.delete_defaults_phase(self.default_phase_pk)
        my_account.Deliverables.delete_defaults_phasesets(self.phaseset_pk)

        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_org_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phase_org_list()
        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_team_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phase_team_list(self.team_pk)
        self.assertEqual(res['status'], 200)

    def test_create_defaults_phase_org(self):
        """ Test that 201 is returned """

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "pct": 10,
            "library": self.phaseset_pk,
            "team": self.team_pk
        }

        res = my_account.Deliverables.create_defaults_phase_org(data)

        self.assertEqual(res['status'], 201)

    def test_create_defaults_phase_team(self):
        """ Test that 200 is returned """

        data = {
            "name": self.testHelper.create_name(),
            "shortname": "TEST",
            "pct": 10,
            "library": self.phaseset_pk,
            "team": self.team_pk
        }

        res = my_account.Deliverables.create_defaults_phase_team(self.team_pk, data)
        self.assertEqual(res['status'], 200)

    def test_get_defaults_phase_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_phase_details(self.default_phase_pk)
        self.assertEqual(res['status'], 200)

    def test_update_defaults_phase(self):
        """ Test that 200 is returned """

        data = {
            "name": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_defaults_phase(self.default_phase_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_defaults_phase(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_defaults_phase(self.default_phase_pk)

        self.assertEqual(res['status'], 204)

    ### Plansets ###

    def test_apply_defaults_plansets(self):
        """ Test that 200 is returned """

        data = {
            'library': self.planset_pk,
            'area': self.area_pk,
            'zone_pk': self.zone_pk,
        }

        res = my_account.Deliverables.apply_defaults_plansets(data)
        self.assertEqual(res['status'], 200)

    def test_duplicate_defaults_plansets(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.duplicate_defaults_plansets(self.planset_pk)
        self.assertEqual(res['status'], 200)

    def test_get_defaults_plansets_org_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plansets_org_list()
        self.assertEqual(res['status'], 200)

    def test_create_defaults_plansets_org(self):
        """ Test that 201 is returned """

        data = {
            "title": self.testHelper.create_name()
        }

        res = my_account.Deliverables.create_defaults_plansets_org(data)
        self.assertEqual(res['status'], 201)

    def test_get_defaults_plansets_team_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plansets_team_list(self.team_pk)
        self.assertEqual(res['status'], 200)

    def test_create_defaults_plansets_team(self):
        """ Test that 201 is returned """

        data = {
            "is_main": False,
            "title": self.testHelper.create_name()
        }

        res = my_account.Deliverables.create_defaults_plansets_team(self.team_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_defaults_plansets_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plansets_details(self.planset_pk)
        self.assertEqual(res['status'], 200)

    def test_update_defaults_plansets(self):
        """ Test that 200 is returned """

        data = {
            "title": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_defaults_plansets(self.planset_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_defaults_plansets(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.delete_defaults_plansets(self.planset_pk)
        self.assertEqual(res['status'], 204)

    ### Plans ###

    def test_duplicate_defaults_plan(self):
        """ Test that 200 is returned """
        #!500

        res = my_account.Deliverables.duplicate_defaults_plan(self.default_plan_pk)
        self.assertEqual(res['status'], 200)

    def test_get_defaults_plan_org_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plans_org_list()
        self.assertEqual(res['status'], 200)

    def test_get_defaults_plan_team_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plans_team_list(self.team_pk)
        self.assertEqual(res['status'], 200)

    def test_create_defaults_plan_org(self):
        """ Test that 201 is returned """

        data = {
            "zone": self.zone_pk,
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": self.testHelper.create_name(),
            "library": self.planset_pk,
        }

        res = my_account.Deliverables.create_defaults_plan_org(data)
        self.assertEqual(res['status'], 201)

    def test_create_defaults_plan_team(self):
        """ Test that 201 is returned """

        data = {
            "zone": self.zone_pk,
            "plan_format": "string",
            "scale": "string",
            "level": "string",
            "name": self.testHelper.create_name(),
            "library": self.planset_pk
        }

        res = my_account.Deliverables.create_defaults_plan_team(self.team_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_defaults_plan_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_defaults_plan_details(self.default_plan_pk)
        self.assertEqual(res['status'], 200)

    def test_update_defaults_plan(self):
        """ Test that 200 is returned """

        data = {
            "name": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_defaults_plan(self.default_plan_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_defaults_plan(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_defaults_plan(self.default_plan_pk)
        self.assertEqual(res['status'], 204)


class TestContracts(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(cls.project_pk)

        cls.contractor_pk = cls.testHelper._create_contractor_return_pk()
        cls.contract_pk = cls.testHelper._create_contract_return_pk(
            cls.contractor_pk, cls.project_pk, cls.fee_project_pk)
        cls.contract_item_pk = cls.testHelper._create_contract_item_return_pk(cls.contract_pk)
        cls.contract_month_pk = cls.testHelper._create_contract_month_return_pk(cls.contract_pk)

    ### Contractors ###

    def test_get_contractors_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contractors_list()
        self.assertEqual(res['status'], 200)

    def test_create_contractor(self):
        """ Test that 201 is returned """

        data = {
            "name": self.testHelper.create_name(),
            "tags": []
        }

        res = my_account.Deliverables.create_contractors(data)
        self.assertEqual(res['status'], 201)

    def test_get_contractor_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contractor_details(self.contractor_pk)
        self.assertEqual(res['status'], 200)

    def test_update_contractor(self):
        """ Test that 200 is returned """

        data = {
            "name": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_contractor(self.contractor_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_contractor(self):
        """ Test that 204 is returned """

        contractor_pk_2 = self.testHelper._create_contractor_return_pk()
        res = my_account.Deliverables.delete_contractor(contractor_pk_2)
        self.assertEqual(res['status'], 204)

    ## Contract items ###

    def test_generate_contracts_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.generate_contracts_project(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_generate_contracts_org(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.generate_contracts_org(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_get_contract_items_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contracts_items_list()
        self.assertEqual(res['status'], 200)

    def test_create_contract_item(self):
        """ Test that 201 is returned """

        data = {
            "contract": self.contract_pk,
            "fee": 100
        }

        res = my_account.Deliverables.create_contracts_items(data)
        self.assertEqual(res['status'], 201)

    def test_get_contract_item_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contract_item_details(self.contract_item_pk)
        self.assertEqual(res['status'], 200)

    def test_update_contract_item(self):
        """ Test that 200 is returned """

        data = {
            "contract": self.contract_pk,
            "already_paid": 10
        }

        res = my_account.Deliverables.update_contract_item(self.contract_item_pk, data)

        self.assertEqual(res['status'], 200)

    def test_delete_contract_item_details(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_contract_item(self.contract_item_pk)
        self.assertEqual(res['status'], 204)

    ### Contracts ###

    def test_get_contracts_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contracts_list()
        self.assertEqual(res['status'], 200)

    def test_create_contract(self):
        """ Test that 201 is returned """

        contractor_pk_2 = self.testHelper._create_contractor_return_pk()

        data = {
            "contractor": contractor_pk_2,
            "fee_project": self.fee_project_pk,
            "type": "sub",
            "description": "string",
            "tax_rate": 1,
            "project": self.project_pk,
        }

        res = my_account.Deliverables.create_contract(data)
        self.assertEqual(res['status'], 201)

    def test_get_contract_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contract_details(self.contract_pk)
        self.assertEqual(res['status'], 200)

    def test_update_contract(self):
        """ Test that 200 is returned """

        data = {
            "description": "UPDATED"
        }

        res = my_account.Deliverables.update_contract(self.contract_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_contract(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_contract(self.contract_pk)
        self.assertEqual(res['status'], 204)

    ### Contracts month ###

    def test_generate_contracts_month(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.generate_contracts_month_org(self.contract_pk)
        self.assertEqual(res['status'], 200)

    def test_get_contracts_month_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contracts_month_list()
        self.assertEqual(res['status'], 200)

    def test_create_contract_month(self):
        """ Test that 201 is returned """

        data = {
            "contract": self.contract_pk,
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
        self.assertEqual(res['status'], 201)

    def test_get_contract_month_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_contract_month_details(self.contract_month_pk)
        self.assertEqual(res['status'], 200)

    def test_update_contract_month(self):
        """ Test that 200 is returned """

        data = {
            "start_date": "05-05-2021"
        }

        res = my_account.Deliverables.update_contracts_month(self.contract_month_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_contract_month(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_contract_month(self.contract_month_pk)
        self.assertEqual(res['status'], 204)


class TestRevisions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(cls.project_pk)

        cls.annex_pk = cls.testHelper._create_annex_return_pk(cls.project_pk)
        cls.document_pk = cls.testHelper._create_document_return_pk(cls.project_pk)
        cls.fee_pk = cls.testHelper._create_fee_return_pk(cls.project_pk)
        cls.phase_pk = cls.testHelper._create_phase_return_pk(cls.project_pk, cls.fee_project_pk)
        cls.plan_pk = cls.testHelper._create_plan_return_pk(cls.project_pk)

    #### Revisions ####

    ### Annexes ###

    def test_get_revisions_annexes_team_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_revisions_annexes_team_project(self.team_pk, self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_annex_revision(self):
        """ Test that 201 is returned """

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": self.annex_pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_annexe_revision(self.team_pk, self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_delete_annex_revision(self):
        """ Test that 201 is returned """

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "annex": self.annex_pk,
            "progress": 80
        }

        pk = my_account.Deliverables.create_annexe_revision(self.team_pk, self.project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_annexe_detail(pk)

        self.assertEqual(res['status'], 204)

    ### Documents ###

    def test_get_revisions_documents_team_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_revisions_documents_team_project(self.team_pk, self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_document_revision(self):
        """ Test that 201 is returned """

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": self.document_pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_document_revision(self.team_pk, self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_delete_document_revision(self):
        """ Test that 204 is returned """

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "doc": self.document_pk,
            "progress": 80
        }

        pk = my_account.Deliverables.create_document_revision(self.team_pk, self.project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_document_detail(pk)

        self.assertEqual(res['status'], 204)

    ### Fee items ###
    def test_get_revisions_fee_items_team_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_revisions_fee_items_team_project(self.team_pk, self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_fee_items_revision(self):
        """ Test that 201 is returned """

        data = {
            "fee_item": self.fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Deliverables.create_fee_items_revision(self.team_pk, self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_delete_fee_items_revision(self):
        """ Test that 204 is returned """

        data = {
            "fee_item": self.fee_pk,
            "progress": 10,
            "date": "06-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Deliverables.create_fee_items_revision(self.team_pk, self.project_pk, data)
        res = my_account.Deliverables.delete_revisions_fee_items_detail(pk['data']['id'])
        self.assertEqual(res['status'], 204)

    ### Phases ###

    def test_get_revisions_phases_team_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_revisions_phases_team_project(self.team_pk, self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_phases_revision(self):
        """ Test that 201 is returned """

        data = {
            "phase": self.phase_pk,
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        res = my_account.Deliverables.create_phase_revision(self.team_pk, self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_delete_phase_revision(self):
        """ Test that 204 is returned """

        data = {
            "phase": self.phase_pk,
            "progress": 10,
            "date": "07-05-2021",
            "is_valid": False,
            "is_mockup": False,
        }

        pk = my_account.Deliverables.create_phase_revision(self.team_pk, self.project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_phases_detail(pk)

        self.assertEqual(res['status'], 204)

    ### Plans ###

    def test_get_revisions_plans_team_project(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_revisions_plans_team_project(self.team_pk, self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_plan_revision(self):
        """ Test that 201 is returned """

        planphase_pk = my_account.Deliverables.get_plan_details(self.plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80
        }

        res = my_account.Deliverables.create_plan_revision(self.team_pk, self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_delete_plan_revision(self):
        """ Test that 204 is returned """

        planphase_pk = my_account.Deliverables.get_plan_details(self.plan_pk)['data']['plan_phases'][0]['id']

        data = {
            "is_valid": False,
            "is_mockup": False,
            "date": "05-05-2021",
            "plan_phase": planphase_pk,
            "progress": 80
        }

        pk = my_account.Deliverables.create_plan_revision(self.team_pk, self.project_pk, data)['data']['id']
        res = my_account.Deliverables.delete_revisions_plan_detail(pk)
        self.assertEqual(res['status'], 204)


class TestAnnexes(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = my_account.teams_pk[0]['id']
        cls.currency_pk = cls.testHelper._create_currency_if_none()
        cls.client_pk = cls.testHelper._create_client_return_pk(team_pk, currency_pk)
        cls.project_pk = cls.testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.annex_pk = cls.testHelper._create_annex_return_pk(cls.project_pk)

    ### Annexes ####

    def test_get_annexes_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_annexes_list(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_annexe(self):
        """ Test that 201 is returned """

        data = {
            "title": self.testHelper.create_name(),
            "annex_type": "time",
            "total_fees": 1,
            "description": "UNITTEST",
            "start_date": "06-05-2021"
        }

        res = my_account.Deliverables.create_annexe(self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_annexe_details(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_annexe_details(self.annex_pk)
        self.assertEqual(res['status'], 200)

    def test_update_annexe(self):
        """ Test that 200 is returned """

        data = {
            "title": self.testHelper.create_name()
        }

        res = my_account.Deliverables.update_annexe(self.annex_pk, data)
        self.assertEqual(res['status'], 200)

    def test_delete_annexe(self):
        """ Test that 204 is returned """

        res = my_account.Deliverables.delete_annexe(self.annex_pk)
        self.assertEqual(res['status'], 204)

    def test_get_annexes_projections_list(self):
        """ Test that 200 is returned """

        res = my_account.Deliverables.get_annexes_projections_list(self.project_pk)
        self.assertEqual(res['status'], 200)


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
        res = my_account.Deliverables.export_zones(project_pk)

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

    #### Fees ####

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

    def test_update_fee_revision(self):
        """ Test that 200 is returned """

        pk = self._create_fee_revision_return_pk()['pk']

        data = {
            "amount": 0
        }

        res = my_account.Deliverables.update_fee_revision(pk, data)
        self.assertEqual(res['status'], 200)

    ### Fees validate ###
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

    #### Documents ####

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

    # def test_set_price_documents(self):
    #     #! 500
    #     """ Test that 201 is returned """

    #     res = my_account.Deliverables.set_price_documents(project_pk)

    #     self.assertEqual(res['status'], 201)


if __name__ == '__main__':
    unittest.main()
