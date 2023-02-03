import os
import unittest

from dotenv import load_dotenv
from factories.factories import (
    ContractorFactory,
    CostFactory,
    CostMonthFactory,
    JobFactory,
    JobInvoiceFactory,
    ProjectFactory,
)
from resources import ooti
from test_helper import HelperTest

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestCosts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testHelper = HelperTest(sdk)
        cls.team_pk = testHelper._get_selected_team()
        cls.cost = CostFactory(cls.team_pk)
        cls.cost_month = CostMonthFactory(team_pk=cls.team_pk, cost_id=cls.cost["id"])

    def test_create_cost(self):
        payload = {
            "amount_actual": 10,
            "amount_budgeted": 0,
            "description": "string",
            "type": "monthly",
            "title": "string",
            "year": 0,
            "team": self.team_pk,
            "months": [],
        }
        response = sdk.Costs.create_cost(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Costs.delete_cost(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_get_costs_list(self):
        response = sdk.Costs.get_costs_list()
        self.assertEqual(response["status"], 200)

    def test_create_costs_month(self):
        payload = {
            "fixed_cost": self.cost["id"],
            "team": self.team_pk,
            "amount_budgeted": 120,
            "amount_actual": 100,
            "year": 2020,
            "month": 3,
        }
        response = sdk.Costs.create_costs_month(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Costs.delete_costs_month(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_delete_cost(self):
        cost = CostFactory(self.team_pk)
        response = sdk.Costs.delete_cost(cost["id"])
        self.assertEqual(response["status"], 204)

    def test_delete_costs_month(self):
        cost_month = CostMonthFactory(self.team_pk, self.cost["id"])
        response = sdk.Costs.delete_costs_month(cost_month["id"])
        self.assertEqual(response["status"], 204)

    def test_update_costs_month_details(self):
        payload = {
            "fixed_cost": self.cost["id"],
            "team": self.team_pk,
            "amount_budgeted": 150,
            "amount_actual": 130,
            "year": 2019,
            "month": 6,
        }
        response = sdk.Costs.update_costs_month_details(self.cost_month["id"], payload)
        self.assertEqual(response["status"], 200)

    def test_update_cost_details(self):
        payload = {
            "amount_actual": 12,
            "amount_budgeted": 10,
            "description": "new description",
            "type": "monthly",
            "month": 10,
            "title": "updated cost",
            "year": 2020,
            "team": self.team_pk,
            "months": [],
        }
        response = sdk.Costs.update_cost_details(self.cost["id"], payload)
        self.assertEqual(response["status"], 200)

    def test_get_costs_months_list(self):
        response = sdk.Costs.get_costs_months_list()
        self.assertEqual(response["status"], 200)


if __name__ == "__main__":
    unittest.main()
