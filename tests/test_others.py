from factories.factories import ProjectFactory
import unittest

# To read .env variables
import os
import sys
from dotenv import load_dotenv
from test_helper import TestHelper

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ooti import ooti # noqa E402


# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.Auth(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestGoals(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        testHelper = TestHelper(sdk)
        cls.team_pk = testHelper._get_selected_team()

    def test_get_goals_list(self):
        response = sdk.Others.get_goals_list()
        self.assertEqual(response['status'], 200)

    def test_create_goal(self):
        payload = {
            'team': self.team_pk,
            'name': 'goal test',
            'value': 2,
            'year': 2021
        }
        response = sdk.Others.create_goal(payload)
        self.assertEqual(response['status'], 201)
        payload = {
            'team': self.team_pk,
            'name': 'goal updated',
            'value': 5,
            'year': 2020
        }
        update = sdk.Others.update_goal_details(response['data']['id'], payload)
        self.assertEqual(update['status'], 200)
        get = sdk.Others.get_goal_details(response['data']['id'])
        self.assertEqual(get['status'], 200)
        delete = sdk.Others.delete_goal(response['data']['id'])
        self.assertEqual(delete['status'], 204)


class TestIndicators(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        testHelper = TestHelper(sdk)
        cls.team_pk = testHelper._get_selected_team()
        cls.project_id = ProjectFactory()['id']

    def test_get_indicators_financial_costs(self):
        response = sdk.Others.get_indicators_financial_costs(project_id=self.project_id)
        self.assertEqual(response['status'], 200)

    def test_get_indicators_financial_incomes(self):
        response = sdk.Others.get_indicators_financial_incomes()
        self.assertEqual(response['status'], 200)

    def test_get_indicators_financial_revenues(self):
        response = sdk.Others.get_indicators_financial_revenues()
        self.assertEqual(response['status'], 200)

    def test_get_indicators_financial_summary(self):
        response = sdk.Others.get_indicators_financial_summary()
        self.assertEqual(response['status'], 200)

    def test_get_indicators_revenue(self):
        response = sdk.Others.get_indicators_revenue()
        self.assertEqual(response['status'], 200)


'''
class TestProjections(unittest.TestCase):

    def test_get_component_metrics_widget(self):
        response = sdk.Others.get_component_metrics_widget()
        self.assertEqual(response['status'], 200)

    def test_export_projections_project_timeline(self):
        response = sdk.Others.export_projections_project_timeline(project_id)
        self.assertEqual(response['status'], 200)

    def test_get_projections_forecast_month_rule_list(self):
        response = sdk.Others.get_projections_forecast_month_rule_list()
        self.assertEqual(response['status'], 200)

    def test_create_projections_forecast_month_rule(self):
        payload = {
            "ruleset": 6,
            "index": 1,
            "pct": 1
        }
        response = sdk.Others.create_projections_forecast_month_rule(payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_forecast_month_rule_details(self):
        response = sdk.Others.get_projections_forecast_month_rule_details(month_rule_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_forecast_month_rule_details(self):
        payload = {
            "ruleset": 6,
            "index": 2,
            "pct": 4
        }
        response = sdk.Others.update_projections_forecast_month_rule_details(month_rule_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_forecast_month_rule(self):
        response = sdk.Others.delete_projections_forecast_month_rule(month_rule_id)
        self.assertEqual(response['status'], 204)

    def test_get_projections_forecast_month_ruleset_list(self):
        response = sdk.Others.get_projections_forecast_month_ruleset_list()
        self.assertEqual(response['status'], 200)

    def test_create_projections_forecast_month_ruleset(self):
        payload = {
            "name": "new ruleset",
            "rules": []
        }
        response = sdk.Others.create_projections_forecast_month_ruleset(payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_forecast_month_ruleset_details(self):
        response = sdk.Others.get_projections_forecast_month_ruleset_details(month_ruleset_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_forecast_month_ruleset_details(self):
        payload = {
            "name": "updated ruleset",
            "rules": [
                7
            ]
        }
        response = sdk.Others.update_projections_forecast_month_ruleset_details(month_ruleset_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_forecast_month_rule(self):
        response = sdk.Others.delete_projections_forecast_month_ruleset(month_ruleset_id)
        self.assertEqual(response['status'], 204)

    def test_get_projections_month_annexes_list(self):
        response = sdk.Others.get_projections_month_annexes_list(project_id)
        self.assertEqual(response['status'], 200)

    def test_create_projections_month_annex(self):
        payload = {
            "annex": 17,
            "year": 2020,
            "month": 1,
            "start_date": "03-03-2020",
            "end_date": "03-06-2020",
            "is_past": True,
            "pct": 10,
            "billing_pct": 10,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "planned_invoicing": 0,
            "actual_invoiced": 0,
            "projected_invoiced": 0,
            "cost_payroll_projected": 0
        }
        response = sdk.Others.create_projections_month_annex(project_id, payload)
        self.assertEqual(response['status'], 201)

    def get_projections_month_annex_details(self):
        response = sdk.Others.get_projections_month_annex_details(month_annex_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_month_annex_details(self):
        payload = {
            "annex": 17,
            "year": 2020,
            "month": 3,
            "start_date": "03-03-2020",
            "end_date": "03-06-2020",
            "is_past": True,
            "pct": 10,
            "billing_pct": 10,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "planned_invoicing": 0,
            "actual_invoiced": 0,
            "projected_invoiced": 0,
            "cost_payroll_projected": 0
        }
        response = sdk.Others.update_projections_month_annex_details(month_annex_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_month_annex(self):
        payload = {
            "annex": 17,
            "year": 2020,
            "month": 7,
            "start_date": "03-03-2020",
            "end_date": "03-06-2020",
            "is_past": True,
            "pct": 10,
            "billing_pct": 10,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "planned_invoicing": 0,
            "actual_invoiced": 0,
            "projected_invoiced": 0,
            "cost_payroll_projected": 0
        }
        month_annex_id_deleted = sdk.Others.create_projections_month_annex(project_id, payload)['data']['id']
        response = sdk.Others.delete_projections_month_annex(month_annex_id_deleted)
        self.assertEqual(response['status'], 204)

    def test_get_projections_month_fees_list(self):
        response = sdk.Others.get_projections_month_fees_list(project_id)
        self.assertEqual(response['status'], 200)

    def test_create_projections_month_fee(self):
        payload = {
            "year": 2020,
            "month": 10,
            "start_date": "01-01-2020",
            "end_date": "01-10-2020",
            "is_past": True,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "pct": 10,
            "billing_pct": 10,
            "mockup_billing_pct": 5
        }
        response = sdk.Others.create_projections_month_fee(project_id, payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_month_fee_details(self):
        response = sdk.Others.get_projections_month_fee_details(month_fee_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_month_fee_details(self):
        payload = {
            "fee": 1,
            "year": 2020,
            "month": 9,
            "start_date": "01-01-2020",
            "end_date": "01-09-2020",
            "is_past": True,
            "pct": 10,
            "mockup_pct": 10,
            "billing_pct": 10,
            "mockup_billing_pct": 10,
            "is_locked": True,
            "mockup_is_locked": True
        }
        response = sdk.Others.update_projections_month_fee_details(month_fee_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_month_fee(self):
        response = sdk.Others.delete_projections_month_fee(653977)
        self.assertEqual(response['status'], 204)

    def test_get_projections_month_phases_list(self):
        response = sdk.Others.get_projections_month_phases_list(project_id)
        self.assertEqual(response['status'], 200)

    def test_create_projections_month_phase(self):
        payload = {
            "phase": 0,
            "year": 0,
            "month": 0,
            "start_date": "string",
            "end_date": "string",
            "is_past": True,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "pct": 0,
            "billing_pct": 0,
            "mockup_billing_pct": 0
        }
        response = sdk.Others.create_projections_month_phase(project_id, payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_month_phase_details(self):
        response = sdk.Others.get_projections_month_phase_details(month_phase_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_month_phase_details(self):
        payload = {
            "phase": 184893,
            "year": 2020,
            "month": 10,
            "start_date": "01-01-2020",
            "end_date": "01-10-2020",
            "is_past": True,
            "is_locked": True,
            "mockup_pct": 0,
            "mockup_is_locked": True,
            "pct": 10,
            "billing_pct": 10,
            "mockup_billing_pct": 5
        }
        response = sdk.Others.update_projections_month_phase_details(month_phase_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_month_phase(self):
        response = sdk.Others.delete_projections_month_phase(653978)
        self.assertEqual(response['status'], 204)

    # def test_create_projections_planning_deliverables_months_bulk_update(self):
    #     #! 404
    #     """ Test that 201 is returned """
    #     res = sdk.Others.create_projections_planning_deliverables_months_bulk_update()
    #     self.assertEqual(res['status'], 200)

    def test_get_projections_reset_budget(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_reset_budget(project_id)
        self.assertEqual(res['status'], 200)

    def test_get_projections_roles_annex_list(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_roles_annex_list(project_id)
        self.assertEqual(res['status'], 200)

    # def test_get_projections_roles_annex_details(self):
    #     """ Test that 200 is returned """
    #     #! What pk
    #     pk = 0
    #     res = sdk.Others.get_projections_roles_annex_details(pk)
    #     self.assertEqual(res['status'], 200)

    # def test_update_projections_roles_annex(self):
    #     """ Test that 200 is returned """
    #     #! What pk
    #     pk = 0
    #     data = {
    #     }
    #     res = sdk.Others.update_projections_roles_annex(pk, data)
    #     self.assertEqual(res['status'], 200)

    # def test_delete_projections_roles_annex(self):
    #     """ Test that 204 is returned """
    #     #! What pk
    #     pk = 0
    #     res = sdk.Others.delete_projections_roles_annex(pk)
    #     self.assertEqual(res['status'], 204)

    def test_get_projections_roles_phase_list(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_roles_phase_list(project_id)
        self.assertEqual(res['status'], 200)

    # def test_get_projections_roles_phase_details(self):
    #     """ Test that 200 is returned """
    #     #! What pk
    #     pk = 0
    #     res = sdk.Others.get_projections_roles_phase_details(pk)
    #     self.assertEqual(res['status'], 200)

    # def test_update_projections_roles_phase(self):
    #     """ Test that 200 is returned """
    #     #! What pk
    #     pk = 0
    #     data = {
    #     }
    #     res = sdk.Others.update_projections_roles_phase(pk, data)
    #     self.assertEqual(res['status'], 200)

    # def test_delete_projections_roles_phase(self):
    #     """ Test that 204 is returned """
    #     #! What pk
    #     pk = 0
    #     res = sdk.Others.delete_projections_roles_phase(pk)
    #     self.assertEqual(res['status'], 204)

    def test_update_all_teamuser_months(self):
        """ Test that 200 is returned """
        res = sdk.Others.update_all_teamuser_months()
        self.assertEqual(res['status'], 200)

    def test_get_projections_update_project_budget(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_update_project_budget(project_id)
        self.assertEqual(res['status'], 200)

    def test_get_projections_update_project_projections(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_update_project_projections(project_id)
        self.assertEqual(res['status'], 200)

    def test_get_projections_update_projections(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_update_projections()
        self.assertEqual(res['status'], 200)

    def test_get_projections_users_annex_list(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_users_annex_list(project_id)
        self.assertEqual(res['status'], 200)
    # def test_get_projections_users_annex_details(self):
    #     """ Test that 200 is returned """
    #     #! what pk ?
    #     pk = 0
    #     res = sdk.Others.get_projections_users_annex_details(pk)
    #     self.assertEqual(res['status'], 200)

    # def test_update_projections_users_annex(self):
    #     """ Test that 200 is returned """
    #     #! what pk ?
    #     pk = 0
    #     data = {
    #     }
    #     res = sdk.Others.update_projections_users_annex(pk, data)
    #     self.assertEqual(res['status'], 200)

    def test_get_projections_users_phase_list(self):
        """ Test that 200 is returned """
        res = sdk.Others.get_projections_users_phase_list(project_id)
        self.assertEqual(res['status'], 200)
    # def test_get_projections_users_phase_details(self):
    #     """ Test that 200 is returned """
    #     #! what pk ?
    #     pk = 0
    #     res = sdk.Others.get_projections_users_phase_details(pk)
    #     self.assertEqual(res['status'], 200)

    # def test_update_projections_users_phase(self):
    #     """ Test that 200 is returned """
    #     #! what pk ?
    #     pk = 0
    #     data = {
    #     }
    #     res = sdk.Others.update_projections_users_phase(pk, data)
    #     self.assertEqual(res['status'], 200)
'''

if __name__ == '__main__':
    unittest.main()
