import os
import unittest

from factories.factories import TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestCustomfields(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.team_pk = TeamFactory()

    def test_get_customfields_list(self):
        response = sdk.Customfields.get_customfields_list()
        self.assertEqual(response["status"], 200)

    def test_create_customfield(self):
        payload = {
            "name": "Test custom field",
            "field_type": "t",
            "default_value": "test",
            "is_required": False,
            "admin_only": False,
            "content_type": "project",
        }
        response = sdk.Customfields.create_customfield(payload)
        self.assertEqual(response["status"], 201)
        created_id = response["data"]["pk"]
        update = sdk.Customfields.update_customfield_details(created_id, payload)
        self.assertEqual(update["status"], 200)
        get = sdk.Customfields.get_customfield_details(created_id)
        self.assertEqual(get["status"], 200)
        delete = sdk.Customfields.delete_customfield(created_id)
        self.assertEqual(delete["status"], 204)


if __name__ == "__main__":
    unittest.main()
