import os
import unittest

from factories.factories import TeamFactory
from test_helper import HelperTest
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()["data"][0]["pk"]
project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
fee_project = my_account.Fees.get_fees_project_list_projects(project_pk)["data"][0][
    "id"
]


class TestContracts(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
        cls.fee_project_pk = cls.testHelper._create_fee_project_return_pk(
            cls.project_pk
        )

        cls.contractor_pk = cls.testHelper._create_contractor_return_pk()
        cls.contract_pk = cls.testHelper._create_contract_return_pk(
            cls.contractor_pk, cls.project_pk, cls.fee_project_pk
        )
        cls.contract_item_pk = cls.testHelper._create_contract_item_return_pk(
            cls.contract_pk
        )
        cls.contract_month_pk = cls.testHelper._create_contract_month_return_pk(
            cls.contract_pk
        )

    ### Contractors #### noqa: E266

    def test_get_contractors_list(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contractors_list()
        self.assertEqual(res["status"], 200)

    def test_create_contractor(self):
        """Test that 201 is returned"""

        data = {"name": self.testHelper.create_name(), "tags": []}

        res = my_account.Contracts.create_contractors(data)
        self.assertEqual(res["status"], 201)

    def test_get_contractor_details(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contractor_details(self.contractor_pk)
        self.assertEqual(res["status"], 200)

    def test_update_contractor(self):
        """Test that 200 is returned"""

        data = {"name": self.testHelper.create_name()}

        res = my_account.Contracts.update_contractor(self.contractor_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_contractor(self):
        """Test that 204 is returned"""

        contractor_pk_2 = self.testHelper._create_contractor_return_pk()
        res = my_account.Contracts.delete_contractor(contractor_pk_2)
        self.assertEqual(res["status"], 204)

    ## Contract items ### noqa: E266

    def test_generate_contracts_project(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.generate_contracts_project(self.project_pk)
        self.assertEqual(res["status"], 200)

    def test_generate_contracts_org(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.generate_contracts_org(self.project_pk)
        self.assertEqual(res["status"], 200)

    def test_get_contract_items_list(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contracts_items_list()
        self.assertEqual(res["status"], 200)

    def test_create_contract_item(self):
        """Test that 201 is returned"""

        data = {"contract": self.contract_pk, "fee": 100}

        res = my_account.Contracts.create_contracts_items(data)
        self.assertEqual(res["status"], 201)

    def test_get_contract_item_details(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contract_item_details(self.contract_item_pk)
        self.assertEqual(res["status"], 200)

    def test_update_contract_item(self):
        """Test that 200 is returned"""

        data = {"contract": self.contract_pk, "already_paid": 10}

        res = my_account.Contracts.update_contract_item(self.contract_item_pk, data)

        self.assertEqual(res["status"], 200)

    def test_delete_contract_item_details(self):
        """Test that 204 is returned"""

        res = my_account.Contracts.delete_contract_item(self.contract_item_pk)
        self.assertEqual(res["status"], 204)

    ### Contracts ### noqa: E266

    def test_get_contracts_list(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contracts_list()
        self.assertEqual(res["status"], 200)

    def test_create_contract(self):
        """Test that 201 is returned"""

        contractor_pk_2 = self.testHelper._create_contractor_return_pk()

        data = {
            "contractor": contractor_pk_2,
            "fee_project": self.fee_project_pk,
            "type": "sub",
            "description": "string",
            "tax_rate": 1,
            "project": self.project_pk,
        }
        res = my_account.Contracts.create_contract(data)
        self.assertEqual(res["status"], 201)

    def test_get_contract_details(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contract_details(self.contract_pk)
        self.assertEqual(res["status"], 200)

    def test_update_contract(self):
        """Test that 200 is returned"""

        data = {"description": "UPDATED"}

        res = my_account.Contracts.update_contract(self.contract_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_contract(self):
        """Test that 204 is returned"""

        my_account.Contracts.get_contracts_list()
        res = my_account.Contracts.delete_contract(self.contract_pk)
        self.assertEqual(
            res["status"], 400
        )  # This contract has fees and cannot be deleted
        # my_account.Contracts.get_contracts_items_list(contract_pk=self.contract_pk)
        # for i in my_account.Contracts.get_contracts_items_list(contract_pk=self.contract_pk)['data']:
        #     my_account.Contracts.update_contract_item(int(i['id']), {'fee': 0.0})
        # res = my_account.Contracts.delete_contract(int(self.contract_pk))
        # self.assertEqual(res['status'], 204)

    ### Contracts month ### noqa: E266

    def test_generate_contracts_month(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.generate_contracts_month_org(self.contract_pk)
        self.assertEqual(res["status"], 200)

    def test_get_contracts_month_list(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contracts_month_list()
        self.assertEqual(res["status"], 200)

    def test_create_contract_month(self):
        """Test that 201 is returned"""

        data = {
            "contract": self.contract_pk,
            "year": 2021,
            "month": 5,
            "start_date": "06-05-2021",
            "end_date": "06-05-2021",
            "budget": 0,
            "budget_projected": 0,
            "actual": 0,
            "pct": 0,
        }

        res = my_account.Contracts.create_contracts_month(data)
        self.assertEqual(res["status"], 201)

    def test_get_contract_month_details(self):
        """Test that 200 is returned"""

        res = my_account.Contracts.get_contract_month_details(self.contract_month_pk)
        self.assertEqual(res["status"], 200)

    def test_update_contract_month(self):
        """Test that 200 is returned"""

        data = {"start_date": "05-05-2021"}

        res = my_account.Contracts.update_contracts_month(self.contract_month_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_contract_month(self):
        """Test that 204 is returned"""

        res = my_account.Contracts.delete_contract_month(self.contract_month_pk)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Fees.delete_fee_project(cls.fee_project_pk)
        my_account.Contracts.delete_contractor(cls.contractor_pk)
        my_account.Contracts.delete_contract(cls.contract_pk)
        my_account.Contracts.delete_contract_item(cls.contract_item_pk)
        my_account.Contracts.delete_contract_month(cls.contract_month_pk)


if __name__ == "__main__":
    unittest.main()
