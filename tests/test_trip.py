import os
import unittest

from factories.factories import OrguserPkFactory, TeamFactory
from test_helper import HelperTest
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()["data"][0]["pk"]
project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]

orguser = OrguserPkFactory(my_account.org_pk)
week_pk = my_account.Timelogs.get_timelogs_week_list()["data"][0]["id"]
res = my_account.Orgusers.update_orguser_details(orguser, {"trips_enabled": True})
print(res.get("status"))


class TestTrips(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.orguser_pk = OrguserPkFactory(my_account.org_pk)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
        cls.trip_pk = cls.testHelper._create_trip_return_pk(
            cls.team_pk, cls.project_pk, cls.orguser_pk
        )

    def test_get_trips_list(self):
        """Test that 200 is returned"""

        res = my_account.Trips.get_trips_list()
        self.assertEqual(res["status"], 200)

    def test_create_trip(self):
        """Test that 201 is returned"""

        data = {
            "team": self.team_pk,
            "project": self.project_pk,
            "orguser": self.orguser_pk,
            "start_date": "11-05-2021",
            "end_date": "11-06-2021",
            "notes": "UNITTEST",
        }

        res = my_account.Trips.create_trip(data)
        self.assertEqual(res["status"], 201)

    def test_get_trips_details(self):
        """Test that 200 is returned"""

        res = my_account.Trips.get_trips_details(self.trip_pk)
        self.assertEqual(res["status"], 200)

    def test_update_trip(self):
        """Test that 200 is returned"""

        data = {"notes": "UPDATED"}

        res = my_account.Trips.update_trip(self.trip_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_trip(self):
        """Test that 204 is returned"""

        res = my_account.Trips.delete_trip(self.trip_pk)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Trips.delete_trip(cls.trip_pk)


if __name__ == "__main__":
    unittest.main()
