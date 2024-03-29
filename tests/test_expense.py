import os
import unittest

from factories.factories import ExpenseGroupFactory, TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestExpenses(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.expense_group = ExpenseGroupFactory(team_pk=cls.team_pk)

    def test_create_expenses_category(self):
        payload = {"name": "expense category test"}
        response = sdk.Expenses.create_expenses_category(payload)
        self.assertEqual(response["status"], 201)

    def test_create_expenses_group(self):
        payload = {"description": "expense group test"}
        response = sdk.Expenses.create_expenses_group(payload, team_pk=self.team_pk)
        self.assertEqual(response["status"], 201)
        delete = sdk.Expenses.delete_expenses_group(response["data"]["id"])
        self.assertEqual(delete["status"], 204)
        response = sdk.Expenses.create_expenses_group(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Expenses.delete_expenses_group(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_create_expenses_group_action(self):
        payload = {
            "team": self.team_pk,
            "is_validated": True,
        }
        response = sdk.Expenses.create_expenses_group_action(payload)
        self.assertEqual(response["status"], 200)

    def test_create_expense(self):
        payload = {
            "amount": "10",
            "date": "10-10-2021",
        }
        response = sdk.Expenses.create_expense(payload)

        self.assertEqual(response["status"], 400)

        payload["expense_group"] = self.expense_group["id"]
        response = sdk.Expenses.create_expense(payload)
        self.assertEqual(response["status"], 201)
        payload = {
            "amount": "10",
            "date": "10-10-2021",
        }
        response = sdk.Expenses.create_expense(
            payload, team_pk=self.team_pk, expense_group_id=self.expense_group["id"]
        )
        self.assertEqual(response["status"], 201)
        delete = sdk.Expenses.delete_expense(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    """
    def test_add_multiple_expenses(self):
        payload = {}
        response = sdk.Costs.add_multiple_expenses(payload, expense_group_id=self.expense_group['id'])
        self.assertEqual(response['status'], 201)
    """

    @classmethod
    def tearDown(cls):
        sdk.Expenses.delete_expenses_group(cls.expense_group)


if __name__ == "__main__":
    unittest.main()
