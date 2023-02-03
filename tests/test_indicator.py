import os
import unittest

from factories.factories import ProjectFactory, TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestIndicators(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()["id"]

    def test_get_indicators_financial_costs(self):
        response = sdk.Indicators.get_indicators_financial_costs(
            project_id=self.project_id
        )
        self.assertEqual(response["status"], 200)

    def test_get_indicators_financial_incomes(self):
        response = sdk.Indicators.get_indicators_financial_incomes()
        self.assertEqual(response["status"], 200)

    def test_get_indicators_financial_revenues(self):
        response = sdk.Indicators.get_indicators_financial_revenues()
        self.assertEqual(response["status"], 200)

    def test_get_indicators_financial_summary(self):
        response = sdk.Indicators.get_indicators_financial_summary()
        self.assertEqual(response["status"], 200)

    def test_get_indicators_revenue(self):
        response = sdk.Indicators.get_indicators_revenue()
        self.assertEqual(response["status"], 200)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)


if __name__ == "__main__":
    unittest.main()
