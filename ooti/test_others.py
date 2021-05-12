import ooti
import unittest

OOTI_USERNAME = 'trey@ooti.co'
OOTI_PASSWORD = 'ooti_INTEGRATION1'

sdk = ooti.Sdk(OOTI_USERNAME, OOTI_PASSWORD)
sdk.connect()


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


if __name__ == '__main__':
    unittest.main(TestIndicators())
