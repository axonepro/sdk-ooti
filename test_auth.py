from requests.api import delete
from factories import OrguserFactory, ProjectFactory, TeamFactory
from ooti import ooti
import unittest

# To read .env variables
import os
from dotenv import load_dotenv

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.Auth(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestProject(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()['id']
        cls.orguser_pk = OrguserFactory()['pk']

    def test_get_project_details(self):
        response = sdk.get_project_details(self.project_id)
        self.assertEqual(response['status'], 200)

    def test_get_projects_list(self):
        response = sdk.get_projects_list()
        self.assertEqual(response['status'], 200)

    def test_export_projects_list(self):
        response = sdk.export_projects_list()
        self.assertEqual(response['status'], 200)

    def test_create_project(self):
        payload = {
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [self.orguser_pk],
            "city": "Paris",
            "country": "FR"
        }
        response = sdk.create_project(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            "project_title": "New project",
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [self.orguser_pk],
            "city": "Paris",
            "country": "FR"
        }
        response = sdk.create_project(payload)
        self.assertEqual(response['status'], 201)

    def test_update_project_details(self):

        payload = {
            "surface_area": 730
        }
        response = sdk.update_project_details(self.project_id, payload)
        self.assertEqual(response['status'], 200)

    def test_get_project_fee_summary(self):

        response = sdk.get_project_fee_summary(self.project_id)
        self.assertEqual(response['status'], 200)

    def test_get_projects_list_deliverables(self):

        response = sdk.get_projects_list_deliverables()
        self.assertEqual(response['status'], 200)

    def test_get_project_available_clients(self):

        response = sdk.get_project_available_clients(self.project_id)
        self.assertEqual(response['status'], 200)

    def test_get_project_users_list(self):

        response = sdk.get_project_users_list(self.project_id)
        self.assertEqual(response['status'], 200)

    def test_add_project_user(self):
        payload = {
            "orguser": self.orguser_pk,
            "project": self.project_id,
            "is_visible": True
        }
        response = sdk.add_project_user(self.project_id, payload)
        project_user_pk = response['data']['pk']
        self.assertEqual(response['status'], 201)
        payload = {
            "is_billable": True
        }
        update = sdk.update_project_user_details(project_user_pk, payload)
        self.assertEqual(update['status'], 200)
        delete = sdk.delete_project_user(project_user_pk)
        self.assertEqual(delete['status'], 204)


class TestOrguser(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.project_id = ProjectFactory()['id']
        cls.orguser_pk = OrguserFactory()['pk']

    def test_get_orguser_details(self):
        response = sdk.get_orguser_details(self.orguser_pk)
        self.assertEqual(response['status'], 200)

    def test_get_orgusers_list(self):
        response = sdk.get_orgusers_list()
        self.assertEqual(response['status'], 200)

    def test_export_orgusers_list(self):
        response = sdk.export_orgusers_list()
        self.assertEqual(response['status'], 200)

    def test_create_orguser(self):  # Error 500
        payload = {
            "email": "test13@test.fr",
            "first_name": "Julie",
            "last_name": "TEST",
        }
        response = sdk.create_orguser(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.delete_orguser(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_update_orguser_details(self):
        payload = {
            "mobile": "0777777777",
            "birthday": "28-06-1989"
        }

        response = sdk.update_orguser_details(self.orguser_pk, payload)
        self.assertEqual(response['status'], 200)

    def test_invite_orguser(self):

        response = sdk.invite_orguser(self.orguser_pk, self.team_pk)
        self.assertEqual(response['status'], 200)


class TestProfile(unittest.TestCase):
    def test_get_profile_preferences(self):
        response = sdk.get_profile_preferences()
        self.assertEqual(response['status'], 200)

    def test_get_profile_details(self):
        response = sdk.get_profile_details()
        self.assertEqual(response['status'], 200)

    def test_update_profile_details(self):
        payload = {
            "locale": "en"
        }
        response = sdk.update_profile_details(payload)
        self.assertEqual(response['status'], 200)


""" Not cleanup yet
class TestTeam(unittest.TestCase):
    def test_get_teams_list(self):
        response = sdk.get_teams_list()
        self.assertEqual(response['status'], 200)

    def test_get_team_users_list(self):
        response = sdk.get_team_users_list(1689)
        self.assertEqual(response['status'], 200)

    def test_get_team_user_details(self):
        response = sdk.get_team_user_details(5042)
        self.assertEqual(response['status'], 200)

    def test_update_team_user_details(self):
        payload = {
            "permissionsset": 16464,
            "team": 1689
        }
        response = sdk.update_team_user_details(5042, payload)
        self.assertEqual(response['status'], 200)

    def test_get_team_details(self):
        response = sdk.get_team_details(1689)
        self.assertEqual(response['status'], 200)

    def test_update_team_details(self):
        payload = {
            "city": "Lyon",
            "address": "14 Avenue de France"
        }
        response = sdk.update_team_details(1689, payload)
        self.assertEqual(response['status'], 200)

    def test_create_team(self):
        payload = {
            "name": "Beta"
        }
        response = sdk.create_team(payload)
        self.assertEqual(response['status'], 201)

    def test_add_team_user(self):

        payload = {
            "orguser": 5042,
            "role": 6487,
            "permissionsset": 16462
        }
        response = sdk.add_team_user(3237, payload)
        self.assertEqual(response['status'], 201)

    def test_add_team_user_to_multiple_projects(self):

        payload = {
            "orguser": 11585,
            "teams": [
                1689
            ],
            "projects": [
                11702,
                11678,
                11707
            ]
        }
        response = sdk.add_team_user_to_multiple_projects(payload)
        self.assertEqual(response['status'], 201)

    def test_delete_team_user_to_multiple_projects(self):

        payload = {
            "orguser": 11585,
            "projects": [
                11702,
                11678,
                11707
            ]
        }
        response = sdk.remove_team_user_to_multiple_projects(payload)
        self.assertEqual(response['status'], 204)



class TestPermissions(unittest.TestCase):
    def test_get_permissions_list(self):
        response = sdk.get_permissions_list()
        self.assertEqual(response['status'], 200)

    def test_get_permissions_details(self):
        response = sdk.get_permissions_details(16466)
        self.assertEqual(response['status'], 200)

    def test_get_permissions_map(self):
        response = sdk.get_permissions_map()
        self.assertEqual(response['status'], 200)

    def test_create_permissions(self):
        payload = {
            "name": "Lead Architect",
            "name_en": "Lead Architect",
            "name_fr": "Architecte en chef",
            "level": "project",
            "all_permissions": True
        }
        response = sdk.create_permissions(payload)
        self.assertEqual(response['status'], 201)

    def test_update_permissions_details(self):
        payload = {
            "name_fr": "Membre d'équipe",
            "all_permissions": True
        }
        response = sdk.update_permissions_details(16459, payload)
        return self.assertEqual(response['status'], 200)

    def test_delete_permissions(self):
        response = sdk.delete_permissions(35750)
        self.assertEqual(response['status'], 204)

class TestInvitation(unittest.TestCase):
    def test_get_invitations_list(self):
        response = sdk.get_invitations_list()
        self.assertEqual(response['status'], 200)

    def test_get_team_invitations_list(self):
        response = sdk.get_team_invitations_list(1689)
        self.assertEqual(response['status'], 200)

    def test_get_invitation_details(self):
        response = sdk.get_invitation_details(71)
        self.assertEqual(response['status'], 200)

    def test_create_invitation(self):
        payload = {
            "team": 1689,
            "invitor": 5042,
            "invitee": 9868,
            "email": "test@mail.com",
        }
        response = sdk.create_invitation(0, payload)
        self.assertEqual(response['status'], 201)

    def test_update_invitation(self):
        payload = {
            "email": "mailchanged@mail.com"
        }
        response = sdk.update_invitation_details(71, payload)
        self.assertEqual(response['status'], 200)

    def test_delete_invitation(self):
        response = sdk.delete_invitation(71)
        self.assertEqual(response['status'], 204)
"""

if __name__ == '__main__':
    unittest.main()
