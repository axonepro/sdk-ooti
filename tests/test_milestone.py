import os
import sys
import unittest

from dotenv import load_dotenv
from factories.factories import TeamFactory
from test_helper import HelperTest

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

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


class TestMilestones(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()["data"][0]["id"]
        cls.milestone_pk = cls.testHelper._create_milestone_return_pk(cls.project_pk)

    def test_get_milestones_list(self):
        """Test that 200 is returned"""

        res = my_account.Milestones.get_milestones_list()
        self.assertEqual(res["status"], 200)

    def test_get_milestone_details(self):
        """Test that 200 is returned"""

        res = my_account.Milestones.get_milestone_details(self.milestone_pk)
        self.assertEqual(res["status"], 200)

    def test_create_milestone(self):
        """Test that 201 is returned"""

        data = {
            "title": self.testHelper.create_name(),
            "project": self.project_pk,
            "date": "30-04-2021",
            "description": "string",
            "in_timeline": True,
        }

        res = my_account.Milestones.create_milestone(data)
        self.assertEqual(res["status"], 201)

    def test_update_milestone(self):
        """Test that 200 is returned"""

        data = {"title": self.testHelper.create_name()}

        res = my_account.Milestones.update_milestone(self.milestone_pk, data)
        self.assertEqual(res["status"], 200)

    def test_delete_milestone(self):
        """Test that 204 is returned"""

        res = my_account.Milestones.delete_milestone(self.milestone_pk)
        self.assertEqual(res["status"], 204)

    @classmethod
    def tearDown(cls):
        my_account.Milestones.delete_milestone(cls.milestone_pk)


if __name__ == "__main__":
    unittest.main()
