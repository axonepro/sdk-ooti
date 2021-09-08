import unittest
from test_helper import TestHelper
from factories.factories import TeamFactory

import os
import sys
from dotenv import load_dotenv


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.get_projects_list()['data'][0]['id']
fee_project = my_account.Fees.get_fees_project_list_projects(project_pk)['data'][0]['id']

class TestAreas(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.testHelper = TestHelper(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.get_projects_list()['data'][0]['id']
        cls.area_pk = cls.testHelper._create_area_return_pk(cls.project_pk)

    def test_get_areas_list(self):
        """ Test that 200 is returned """

        res = my_account.Areas.get_areas_list(self.project_pk)
        self.assertEqual(res['status'], 200)

    def test_create_area(self):
        """ Test that 201 is returned """

        name = self.testHelper.create_name()

        area_data = {
            "name": name,
            "project": self.project_pk,
            "surface_area": 30
        }

        res = my_account.Areas.create_areas(self.project_pk, area_data)
        my_account.Areas.delete_area(res['data']['id'])

        self.assertEqual(res['status'], 201)

    def test_get_area_details(self):
        """ Test that 200 is returned """

        res = my_account.Areas.get_areas_details(self.area_pk)
        my_account.Areas.delete_area(self.area_pk)

        self.assertEqual(res['status'], 200)

    def test_update_area(self):
        """ Test that 200 is returned """

        name = self.testHelper.create_name()

        update = {
            "name": name,
        }

        res = my_account.Areas.update_areas(self.area_pk, update)
        self.assertEqual(res['status'], 200)

    def test_delete_area(self):
        """ Test that 204 is returned """

        res = my_account.Areas.delete_area(self.area_pk)
        self.assertEqual(res['status'], 204)

    @classmethod
    def tearDown(cls):
        del cls.testHelper
        del cls.team_pk
        del cls.project_pk
        del cls.area_pk

if __name__ == '__main__':
    unittest.main()