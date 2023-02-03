import os
import unittest

from factories.factories import ProjectFactory, TeamFactory

from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestInboundEmails(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()["id"]

    def test_get_inbound_emails_list(self):
        response = sdk.Inbound_emails.get_inbound_emails_list()
        self.assertEqual(response["status"], 200)

    def test_create_inbound_email(self):
        payload = {
            "project": self.project_id,
            "subject": "test subject",
            "body": "test body",
        }
        response = sdk.Inbound_emails.create_inbound_email(payload)
        self.assertEqual(response["status"], 201)
        created_id = response["data"]["id"]
        payload = {"subject": "updated", "body": "body update"}
        update = sdk.Inbound_emails.update_inbound_email_details(created_id, payload)
        self.assertEqual(update["status"], 200)
        get = sdk.Inbound_emails.get_inbound_email_details(created_id)
        self.assertEqual(get["status"], 200)
        delete = sdk.Inbound_emails.delete_inbound_email(created_id)
        self.assertEqual(delete["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project_id)


if __name__ == "__main__":
    unittest.main()
