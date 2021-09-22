import requests
import json

from .helper import Helper


class Posts(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_posts_albums_list(self, page=1):
        """ Get the posts albums list """

        route = 'v1/posts/album/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_posts_album(self, data):
        """ Create a new album of posts 

        Keywords arguments:
        data -- data of the new album to be created:
        {
            "post": post_pk, # REQUIRED
            "title": "new album"
        }
        """

        route = 'v1/posts/album/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_posts_album_details(self, album_pk):
        """ Get the album details

        Keywords arguments:
        album_pk -- pk of the album
        """

        route = 'v1/posts/album/{0}/'.format(album_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_posts_album_details(self, album_pk, data):
        """ Update the album details

        Keywords arguments:
        album_pk -- pk of the album
        data -- content of the update:
        {
            "post": post_pk,
            "title": "string"
        }
        """

        route = 'v1/posts/album/{0}/'.format(album_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_posts_album(self, album_pk):
        """ Delete the album

        Keywords arguments:
        album_pk -- pk of the album
        """

        route = 'v1/posts/album/{0}/'.format(album_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_posts_images_list(self, page=1):
        """ Get the list of posted images """

        route = 'v1/posts/image/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_posts_image(self, data):
        """ Add a new image to a post 

        Keywords arguments:
        data -- data of the image to be created:
        {
            "post": post_pk,
            "album": album_pk,
            "img": "string"
        }
        """

        route = 'v1/posts/image/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_posts_image_details(self, image_pk):
        """ Get the image details

        Keywords arguments:
        image_pk -- pk of the image
        """

        route = 'v1/posts/image/{0}/'.format(image_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_posts_image_details(self, image_pk, data):
        """ Update the image

        Keywords arguments:
        image_pk -- pk of the image
        data -- content of the update:
        {
            "post": post_pk,
            "album": album_pk,
            "img": "string"
        }
        """

        route = 'v1/posts/image/{0}/'.format(image_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_posts_image(self, image_pk):
        """ Delete the image

        Keywords arguments:
        image_pk -- pk of the image
        """

        route = 'v1/posts/image/{0}/'.format(image_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/posts/last-post/{org_pk}/

    def get_posts_likes_list(self, page=1):
        """ Get the list of likes """

        route = 'v1/posts/like/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_posts_like(self, data):
        """ Create a like 

        Keywords arguments:
        data -- data of the like to be created:
        {
            "post": post_pk, # REQUIRED
            "like_type": 0
        }
        """

        route = 'v1/posts/like/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_posts_like_details(self, like_pk):
        """ Get the like details

        Keywords arguments:
        like_pk -- pk of the like
        """

        route = 'v1/posts/like/{0}/'.format(like_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def delete_posts_like(self, like_pk):
        """ Remove a like from a post

        Keywords arguments:
        like_pk -- pk of the like
        """

        route = 'v1/posts/like/{0}/'.format(like_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_posts_list(self, page=1):
        """ Get the list of posts """

        route = 'v1/posts/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_post(self, data):
        """ Create a new post

        Keywors arguments:
        data -- data of the new post to be created:
        {
            "title": "string",
            "url": "string",
            "text": "string"
        }
        """

        route = 'v1/posts/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_post_comments(self, pk):
        """ Get the list of comments of the post

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/post/comments/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/posts/recent-comments/{org_pk}/

    def get_posts_tags_list(self):
        """ Get the list of posts tags """

        route = 'v1/posts/tags/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_post_details(self, pk):
        """ Get the post details

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_post_details(self, pk, data):
        """ Update the post details

        Keywords arguments:
        pk -- pk of the post
        data -- content of the update:
        {
            "project": project_id,
            "title": "string",
            "url": "string",
            "text": "string"
        }
        """

        route = 'v1/posts/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def delete_post(self, pk):
        """ Delete the post

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)