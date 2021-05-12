from requests.models import Response
from ooti import ooti
import unittest

OOTI_USERNAME = 'trey@ooti.co'
OOTI_PASSWORD = 'ooti_INTEGRATION1'

sdk = ooti.Auth(OOTI_USERNAME, OOTI_PASSWORD)
sdk.connect()

team_pk = sdk.teams_pk[0]['id']
project_id = sdk.Auth.get_projects_list()['data'][0]['id']
goal_id = sdk.Others.get_goals_list()['data'][0]['id']


class TestGoals(unittest.TestCase):
    def test_get_goals_list(self):
        response = sdk.Others.get_goals_list()
        self.assertEqual(response['status'], 200)

    def test_create_goal(self):
        payload = {
            'team': team_pk,
            'name': 'goal test',
            'value': 2,
            'year': 2021
        }
        response = sdk.Others.create_goal(payload)
        self.assertEqual(response['status'], 201)

    def test_get_goal_details(self):
        response = sdk.Others.get_goal_details(goal_id)
        self.assertEqual(response['status'], 200)

    def test_update_goal_details(self):
        payload = {
            'team': team_pk,
            'name': 'goal updated',
            'value': 5,
            'year': 2020
        }
        response = sdk.Others.update_goal_details(goal_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_goal(self):
        payload = {
            'team': team_pk,
            'name': 'goal to be deleted',
            'value': 1,
            'year': 2021
        }
        goal_deleted_id = sdk.Others.create_goal(payload)['data']['id']
        response = sdk.Others.delete_goal(goal_deleted_id)
        self.assertEqual(response['status'], 204)


class TestIndicators(unittest.TestCase):
    def test_get_indicators_financial_costs(self):
        response = sdk.Others.get_indicators_financial_costs(project_id=11702)
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

        }
        response = sdk.Others.create_projections_forecast_month_rule(payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_forecast_month_rule_details(self):
        response = sdk.Others.get_projections_forecast_month_rule_details(month_rule_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_forecast_month_rule_details(self):
        payload = {

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

        }
        response = sdk.Others.create_projections_forecast_month_ruleset(payload)
        self.assertEqual(response['status'], 201)

    def test_get_projections_forecast_month_ruleset_details(self):
        response = sdk.Others.get_projections_forecast_month_ruleset_details(month_ruleset_id)
        self.assertEqual(response['status'], 200)

    def test_update_projections_forecast_month_ruleset_details(self):
        payload = {

        }
        response = sdk.Others.update_projections_forecast_month_ruleset_details(month_ruleset_id, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_projections_forecast_month_rule(self):
        response = sdk.Others.delete_projections_forecast_month_rule(month_ruleset_id)
        self.assertEqual(response['status'], 204)


if __name__ == '__main__':
    unittest.main(TestGoals())
