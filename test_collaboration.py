from factories import AlbumFactory, OrguserFactory, PostFactory, ProjectFactory, TaskFactory, TeamFactory
from ooti import ooti
import unittest

OOTI_USERNAME = 'root@root.com'
OOTI_PASSWORD = 'root'

sdk = ooti.Auth(OOTI_USERNAME, OOTI_PASSWORD)
sdk.connect()


class TestContacts(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()

    def test_get_number_uncategorized_contacts(self):
        response = sdk.Collaboration.get_number_uncategorized_contacts()
        self.assertEqual(response['status'], 200)


class TestNewsletters(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.orguser_pk = OrguserFactory()['id']
        cls.team_pk = TeamFactory()

    def test_create_newsletter(self):
        payload = {
            "receivers": [
                self.orguser_pk
            ],
            "name": "newsletter tested",
            "start_date": "04-05-2021",
            "end_date": "07-05-2021",
            "frequency": 1,
            "all_users_are_receivers": True
        }
        response = sdk.Collaboration.create_newsletters(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_newsletter(response['data']['id'])
        self.assertEqual(delete['status'], 204)


class TestNotes(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.project_pk = ProjectFactory()['id']
        cls.orguser_pk = OrguserFactory()['id']
        cls.team_pk = TeamFactory()

    def test_create_note(self):
        payload = {
            "text": "A note to see if the function works correctly",
            "title": "note tested",
            "is_pinned": True,
            "project": self.project_pk,
            "orguser": self.orguser_pk,
            "is_public": True,
            "entire_project": True,
            "followers": [
                self.orguser_pk,
            ]
        }
        response = sdk.Collaboration.create_note(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_note(response['data']['id'])
        self.assertEqual(delete['status'], 204)


class TestNotifications(unittest.TestCase):
    def test_get_notifications_config(self):
        response = sdk.Collaboration.get_notifications_config()
        self.assertEqual(response['status'], 200)

    def test_update_notifications_details(self):
        payload = {
            "weekday": 5,
            "daily_time": "19:00:00"
        }
        response = sdk.Collaboration.update_notifications_config(payload)
        self.assertEqual(response['status'], 200)


class TestTasks(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.orguser_pk = OrguserFactory()['id']
        cls.task_pk = TaskFactory()['pk']

    def test_create_task_label(self):
        payload = {
            "creator": self.orguser_pk,
            "team": self.team_pk,
            "title": "task label tested",
            "description": "test if the function works correctly"
        }
        response = sdk.Collaboration.create_task_label(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_task_label(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_task(self):
        payload = {
            "creator": self.orguser_pk,
            "title": "task tested",
            "due_date": "07-08-2021",
            "description": "test if the tasks creation works"
        }
        response = sdk.Collaboration.create_task(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_task(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_tasks_list(self):
        payload = {
            "title": 'task list test',
        }
        response = sdk.Collaboration.create_tasks_list(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_tasks_list(response['data']['id'])
        self.assertEqual(delete['status'], 204)


class TestPosts(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.post_pk = PostFactory()['pk']
        cls.album_pk = AlbumFactory()['pk']

    def test_create_post(self):
        payload = {
            "title": "post tested",
            "text": "test if the function create_post() works"
        }
        response = sdk.Collaboration.create_post(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_post(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_get_post_details(self):
        response = sdk.Collaboration.get_post_details(self.post_pk)
        self.assertEqual(response['status'], 200)

    def test_create_post_like(self):
        payload = {}
        response = sdk.Collaboration.create_posts_like(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
        }
        response = sdk.Collaboration.create_posts_like(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Collaboration.get_posts_like_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Collaboration.delete_posts_like(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_post_album(self):
        payload = {}
        response = sdk.Collaboration.create_posts_album(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
            'title': 'album test'
        }
        response = sdk.Collaboration.create_posts_album(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Collaboration.get_posts_album_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Collaboration.delete_posts_album(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_post_image(self):
        payload = {}
        response = sdk.Collaboration.create_posts_image(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
            'album': self.album_pk,
            'title': 'album test'
        }
        response = sdk.Collaboration.create_posts_image(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Collaboration.get_posts_image_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Collaboration.delete_posts_image(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_get_post_comments(self):
        response = sdk.Collaboration.get_post_comments(self.post_pk)
        self.assertEqual(response['status'], 200)

    def test_get_posts_likes_list(self):
        response = sdk.Collaboration.get_posts_likes_list()
        self.assertEqual(response['status'], 200)


class TestContacts(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.post_pk = PostFactory()['pk']
        cls.album_pk = AlbumFactory()['pk']

    def test_create_contact(self):
        payload = {
            'name': 'contact test'
        }
        response = sdk.Collaboration.create_contact(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_contact(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_contact_category(self):
        payload = {
            'name': 'contact category test'
        }
        response = sdk.Collaboration.create_contact_category(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Collaboration.delete_contact_category(response['data']['id'])
        self.assertEqual(delete['status'], 204)


if __name__ == '__main__':
    unittest.main(TestPosts())