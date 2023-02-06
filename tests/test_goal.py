import os
import unittest

from factories.factories import TeamFactory
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestGoals(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()

    def test_get_goals_list(self):
        response = sdk.Goals.get_goals_list()
        self.assertEqual(response["status"], 200)

    def test_create_goal(self):
        payload = {"team": self.team_pk, "name": "goal test", "value": 2, "year": 2021}
        response = sdk.Goals.create_goal(payload)
        self.assertEqual(response["status"], 201)
        payload = {
            "team": self.team_pk,
            "name": "goal updated",
            "value": 5,
            "year": 2020,
        }
        update = sdk.Goals.update_goal_details(response["data"]["id"], payload)
        self.assertEqual(update["status"], 200)
        get = sdk.Goals.get_goal_details(response["data"]["id"])
        self.assertEqual(get["status"], 200)
        delete = sdk.Goals.delete_goal(response["data"]["id"])
        self.assertEqual(delete["status"], 204)


if __name__ == "__main__":
    unittest.main()
