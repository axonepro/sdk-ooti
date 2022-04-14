import os
import random
import string
import sys
import time
import unittest

from dotenv import load_dotenv
from factories.factories import TeamFactory
from requests.models import Response
from test_helper import HelperTest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti  # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

my_account = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
my_account.connect()

team_pk = TeamFactory()
currency_pk = my_account.Currencies.get_currencies_list()['data'][0]['pk']
project_pk = my_account.Projects.get_projects_list()['data'][0]['id']

class TestFiles(unittest.TestCase):

    @classmethod
    def setUp(cls):
        testHelper = HelperTest(my_account)
        cls.team_pk = TeamFactory()
        # cls.project_pk = testHelper._create_project_return_pk(cls.client_pk, cls.currency_pk)
        cls.project_pk = my_account.Projects.get_projects_list()['data'][0]['id']
        cls.folder_pk = testHelper._create_folder_return_pk(cls.project_pk)
        cls.file_pk = testHelper._create_file_return_pk(cls.project_pk, cls.folder_pk)

        #### Files ####

    ### Folders ###

    def test_get_folders_list(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_folder_list(self.project_pk)

        self.assertEqual(res['status'], 200)

    def test_get_folder_details(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_folder_details(self.folder_pk)
        my_account.Files.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 200)

    def test_create_folder(self):
        """ Test that 201 is returned """

        folder = {
            "name": "UNITTEST"
        }

        res = my_account.Files.create_folder(self.project_pk, folder)
        my_account.Files.delete_folder(res['data']['pk'])

        self.assertEqual(res['status'], 201)

    def test_update_folder(self):
        """ Test that 201 is returned """

        folder_updated = {
            "name": "UNITTEST - UPDATE"
        }

        res = my_account.Files.update_folder(self.folder_pk, folder_updated)
        my_account.Files.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_folder(self):
        """ Test that 200 is returned """

        res = my_account.Files.delete_folder(self.folder_pk)

        self.assertEqual(res['status'], 204)

    ### Files ###
    def test_get_files_list(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_files_list(self.project_pk)

        self.assertEqual(res['status'], 200)

    def test_create_file(self):
        """ Test that 201 is returned """
        data = {
            "name": "file_UNITTEST",
            "file": "README.md",
            "folder": self.folder_pk,
        }

        res = my_account.Files.create_file(self.project_pk, data)
        self.assertEqual(res['status'], 201)

    def test_get_files_details(self):
        """ Test that 200 is returned """

        res = my_account.Files.get_file_details(self.file_pk)

        self.assertEqual(res['status'], 200)

    def test_delete_file(self):
        """ Test that 204 is returned """

        res = my_account.Files.delete_file(self.file_pk)
        self.assertEqual(res['status'], 204)

    @classmethod
    def tearDown(cls):
        my_account.Files.delete_folder(cls.folder_pk)
        my_account.Files.delete_file(cls.file_pk)

if __name__ == '__main__':
    unittest.main()