from factories.factories import AlbumFactory, OrguserFactory, PostFactory, ProjectFactory
from factories.factories import TaskFactory, TeamFactory
import unittest

# To read .env variables
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

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

class TestPosts(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        cls.team_pk = TeamFactory()
        cls.post_pk = PostFactory()['pk']
        cls.album_pk = AlbumFactory()['pk']

    def test_get_number_uncategorized_contacts(self):
        response = sdk.Contacts.get_number_uncategorized_contacts()
        self.assertEqual(response['status'], 200)

    def test_create_post(self):
        payload = {
            "title": "post tested",
            "text": "test if the function create_post() works"
        }
        response = sdk.Posts.create_post(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Posts.delete_post(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_get_post_details(self):
        response = sdk.Posts.get_post_details(self.post_pk)
        self.assertEqual(response['status'], 200)

    def test_create_post_like(self):
        payload = {}
        response = sdk.Posts.create_posts_like(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
        }
        response = sdk.Posts.create_posts_like(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Posts.get_posts_like_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Posts.delete_posts_like(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_post_album(self):
        payload = {}
        response = sdk.Posts.create_posts_album(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
            'title': 'album test'
        }
        response = sdk.Posts.create_posts_album(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Posts.get_posts_album_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Posts.delete_posts_album(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_create_post_image(self):
        payload = {}
        response = sdk.Posts.create_posts_image(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'post': self.post_pk,
            'album': self.album_pk,
            'title': 'album test'
        }
        response = sdk.Posts.create_posts_image(payload)
        self.assertEqual(response['status'], 201)
        response = sdk.Posts.get_posts_image_details(response['data']['pk'])
        self.assertEqual(response['status'], 200)
        delete = sdk.Posts.delete_posts_image(response['data']['pk'])
        self.assertEqual(delete['status'], 204)

    def test_get_post_comments(self):
        response = sdk.Posts.get_post_comments(self.post_pk)
        self.assertEqual(response['status'], 200)

    def test_get_posts_likes_list(self):
        response = sdk.Posts.get_posts_likes_list()
        self.assertEqual(response['status'], 200)

    @classmethod
    def tearDown(cls):
        sdk.Posts.delete_post(cls.post_pk)
        sdk.Posts.delete_posts_album(cls.album_pk)

if __name__ == '__main__':
    unittest.main()