import random
import unittest

import pytest
from factories.factories import TeamFactory
from test_helper import HelperTest

from resources import ooti  # noqa E402


@pytest.mark.usefixtures("my_account")
class TestClients(unittest.TestCase):
    def setUp(self):
        test_helper = HelperTest(self.my_account)
        self.team_pk = TeamFactory()
        self.currency_pk = test_helper._create_currency_if_none()
        self.client_pk = test_helper._create_client_return_pk(
            self.team_pk, self.currency_pk
        )

    def test_get_clients_list(self):
        """Test that 200 is returned"""

        res_get = self.my_account.Clients.get_clients_list(self.team_pk)
        self.assertEqual(res_get["status"], 200)

    def test_get_client_details(self):
        """Test that 200 is returned"""

        res_get = self.my_account.Clients.get_clients_details(self.client_pk)
        self.assertEqual(res_get["status"], 200)

    def test_create_client(self):
        """Test that 201 is returned"""

        client = {
            "name": "UNITTEST",
            "number": f"{random.randint(0, 99999):05d}",
            "currency": self.currency_pk,
            "billing_address": "Unittest address",
            "team": self.team_pk,
            "tags": [],
        }

        res_creation = self.my_account.Clients.create_client(client)
        self.assertEqual(res_creation["status"], 201)

    def test_update_client(self):
        """Test that 200 is returned"""

        update = {
            "billing_address": "Update unittest address",
        }

        res_update = self.my_account.Clients.update_client(self.client_pk, update)
        self.assertEqual(res_update["status"], 200)

    def test_delete_client(self):
        """Test that 204 is returned"""

        res_delete = self.my_account.Clients.delete_client(self.client_pk)
        self.assertEqual(res_delete["status"], 204)

    def tearDown(self):
        self.my_account.Currencies.delete_currency(self.currency_pk)
        self.my_account.Clients.delete_client(self.client_pk)


if __name__ == "__main__":
    unittest.main()
