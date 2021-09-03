import requests
import json

from .helper import Helper

"""

- Contacts
    - ERROR 500 : POST on v1/contacts/list-action/{org_pk}/

"""


class Collaboration(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Contacts ####

    def get_contact_categories_list(self, project_id=None):
        """ Get the list of categories of contact

        Keywords arguments:
        project_id -- id of the project if the category is specific to a project
        """

        route = 'v1/contacts/categories/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contact_category(self, data, project_id=None):
        """ Create a new category for contacts

        Keywords arguments:
        project_id -- id of the project if the category is specific to a project
        data -- data of the new category to be created:
        {
            "name": "new category",
            "count": 2,
            "permissionssets": [
                permissionset_pk,
                ...
            ]
        }
        """
        route = 'v1/contacts/categories/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def get_contact_category_details(self, category_pk):
        """ Get the contact category details

        Keywords arguments:
        category_pk -- the pk of the contact
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contact_category_details(self, category_pk, data):
        """ Update the contact category details

        Keywords arguments:
        category_pk -- the pk of the contact category
        data -- content of the update:
        {
            "name": "new name",
            "count": 1,
            "permissionssets": [
                permissionsset_pk,
                ...
            ]
        }
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contact_category(self, category_pk):
        """ Delete the contact

        Keywords arguments:
        category_pk -- the pk of the contact category
        """

        route = 'v1/contacts/category/{0}/'.format(category_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_contact_list_action(self):

        route = 'v1/contacts/list-action/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_contacts_list(self, project_id=None, page=1):
        """ Get the contacts list

        project_id -- id of the contacts' project (optional)
        """

        route = 'v1/contacts/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contact(self, data, project_id=None):
        """ Create a new contact

        Keywords arguments:
        project_id -- id of the contact's project (optional)
        data -- data to create:
            {   
                "name": "string" (required),
                "first_name": "string" (optional),
                "last_name": "string" (optional),
                "email": "string" (optional),
                "mobile_phone": "string" (optional),
                "job_title": "string" (optional)
            }
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_id is not None:
            route += '{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_number_uncategorized_contacts(self, team_pk=None, project_id=None):
        """ Return the number of uncategorized contacts """

        route = 'v1/contacts/uncategorized/count/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_id is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_id is not None:
                    parameters += '&'
            if project_id is not None:
                parameters += 'project={0}'.format(team_pk)
        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response)

    def get_contact_details(self, pk):
        """ Get the contact details

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contact_details(self, pk, data):
        """ Update the contact details

        Keywords arguments:
        pk -- the pk of the contact
        data -- content of the update:
        {
            "name": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "mobile_phone": "string",
            "office_phone": "string",
            "home_phone": "string",
            "fax": "string",
            "website": "string",
            "street1": "string",
            "postal_code1": "string",
            "city1": "string",
            "province1": "string",
            "country1": "string",
            "job_title": "string",
            "client": [ (ids of the clients associated with this contact)
                "string" 
            ]
        }
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contact(self, pk):
        """ Delete the contact

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Newsletters ####

    def get_newsletters_list(self, page=1):
        """ Get the list of newsletters """

        route = 'v1/newsletters/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_newsletters(self, data):
        """ Create a new newsletter

        Keywords arguments:
        data -- data of the new newsletter to be created:
        {
            "template": 0,
            "receivers": [
                orguser_pk,
                ...
            ],
            "name": "string",
            "start_date": "string",
            "end_date": "string",
            "time": "string",
            "type": "string",
            "frequency": 0,
            "all_users_are_receivers": true
        }
        """

        route = 'v1/newsletters/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_newsletter_details(self, pk):
        """ Get newsletter details

        Keywords arguments:
        pk -- pk of the newsletter
        """

        route = 'v1/newsletters/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_newsletter_details(self, pk, data):
        """ Update newsletter details

        Keywords arguments:
        pk -- pk of the newsletter
        data -- content of the update:
        {
            "template": 0,
            "receivers": [
                orguser_pk,
                ...
            ],
            "name": "string",
            "start_date": "string",
            "end_date": "string",
            "time": "string",
            "type": "string",
            "frequency": 0,
            "all_users_are_receivers": true
        }
        """

        route = 'v1/newsletters/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_newsletter(self, pk):
        """ Delete the newsletter 

        Keywords arguments:
        pk -- pk of the newsletter
        """

        route = 'v1/newsletters/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Note ####

    def get_notes_list(self, page=1):
        """ Get the list of notes """

        route = 'v1/notes/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_note(self, data):
        """ Create a new note

        Keywords arguments:
        data -- data of the new note to be created:
        {
            "text": "string",
            "title": "string",
            "is_pinned": true,
            "project": project_pk,
            "orguser": orguser_pk,
            "is_public": true,
            "entire_project": true,
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/notes/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_note_details(self, pk):
        """ Get note details

        Keywords arguments:
        pk -- pk of the note
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_note_details(self, pk, data):
        """ Update note details

        Keywords arguments:
        pk -- pk of the note
        data -- content of the update:
        {
            "text": "string",
            "title": "string",
            "is_pinned": true,
            "project": project_pk,
            "orguser": orguser_pk,
            "is_public": true,
            "entire_project": true,
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_note(self, pk):
        """ Delete the note

        Keywords arguments:
        pk -- pk of the note
        """

        route = 'v1/notes/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Notifications ####

    def get_notifications_config(self):
        """ Get the notifications config of the organization """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_notifications_config(self, data):  # "off"/? - "on" and "active" rejected
        """ Update the notifications config of the organization 

        Keywords arguments:
        data -- content of the update
        {
            daily_time": "18:00:00",
            "weekly_time": null,
            "weekday": 5,
            "expense_reports_submissions": "off",
            "expense_reports_submissions_email": false,
            "expense_reports_validations": "off",
            "expense_reports_validations_email": false,
            "expense_reports_reimbursal": "off",
            "expense_reports_reimbursal_email": false,
            "time_off_submissions": "off",
            "time_off_submissions_email": false,
            "time_off_validations": "off",
            "time_off_validations_email": false,
            "time_entry_refusals": "off",
            "time_entry_refusals_email": false,
            "invoices_sent": "off",
            "invoices_sent_email": false,
            "invoices_paid": "off",
            "invoices_paid_email": false,
            "post_posted": "off",
            "post_posted_email": false,
            "project_fees_changed": "off",
            "project_fees_changed_email": false,
            "project_dates_changed": "off",
            "project_dates_changed_email": false,
            "invitations_accepted": "off",
            "invitations_accepted_email": false,
            "permissions_changed": "off",
            "permissions_changed_email": false
        }
        """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    #### Posts ###

    def get_posts_albums_list(self, page=1):
        """ Get the posts albums list """

        route = 'v1/posts/album/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_posts_album_details(self, album_pk):
        """ Get the album details

        Keywords arguments:
        album_pk -- pk of the album
        """

        route = 'v1/posts/album/{0}/'.format(album_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_posts_album(self, album_pk):
        """ Delete the album

        Keywords arguments:
        album_pk -- pk of the album
        """

        route = 'v1/posts/album/{0}/'.format(album_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_posts_images_list(self, page=1):
        """ Get the list of posted images """

        route = 'v1/posts/image/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_posts_image_details(self, image_pk):
        """ Get the image details

        Keywords arguments:
        image_pk -- pk of the image
        """

        route = 'v1/posts/image/{0}/'.format(image_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_posts_image(self, image_pk):
        """ Delete the image

        Keywords arguments:
        image_pk -- pk of the image
        """

        route = 'v1/posts/image/{0}/'.format(image_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_posts_likes_list(self, page=1):
        """ Get the list of likes """

        route = 'v1/posts/like/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_posts_like_details(self, like_pk):
        """ Get the like details

        Keywords arguments:
        like_pk -- pk of the like
        """

        route = 'v1/posts/like/{0}/'.format(like_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_posts_like(self, like_pk):
        """ Remove a like from a post

        Keywords arguments:
        like_pk -- pk of the like
        """

        route = 'v1/posts/like/{0}/'.format(like_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_posts_list(self, page=1):
        """ Get the list of posts """

        route = 'v1/posts/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_post_comments(self, pk):
        """ Get the list of comments of the post

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/post/comments/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_posts_tags_list(self):
        """ Get the list of posts tags """

        route = 'v1/posts/tags/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_post_details(self, pk):
        """ Get the post details

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_post(self, pk):
        """ Delete the post

        Keywords arguments:
        pk -- pk of the post
        """

        route = 'v1/posts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Tasks ####

    def empty_tasks_trash(self, project_id):
        """ Set delete all not-completed archived tasks in project """

        route = 'v1/tasks/empty-trash/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_task_labels_list(self, page=1):
        """ Get the list of tasks labels """

        route = 'v1/tasks/label/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_task_label(self, data):
        """ Create a new task label 

        Keywords arguments:
        data -- data of the new label to be created:
        {
            "creator": orguser_pk,
            "team": team_pk,
            "title": "label title",
            "description": "new task label"
        }
        """

        route = 'v1/tasks/label/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_task_label_details(self, label_pk):
        """ Get the task label details

        Keywords arguments:
        label_pk -- pk of the task label
        """

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_task_label_details(self, label_pk, data):
        """ Update the task label details

        Keywords arguments:
        label_pk -- pk of the task label
        data -- content of the update:
        {
            "creator": orguser_pk,
            "team": team_pk,
            "title": "new title",
            "description": "description updated"
        }
        """

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_task_label(self, label_pk):
        """ Delete the task label details

        Keywords arguments:
        label_pk -- pk of the task label
        """

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_tasks_list(self, page=1):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_task(self, data):
        """ Create a new task 

        Keywords arguments:
        data -- data of the new task to be created:
        {
            "creator": orguser_pk,
            "created_at": "string",
            "labels": [
                label_pk,
                ...
            ],
            "title": "string",
            "due_date": "string",
            "description": "string"
        }
        """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_tasks_lists_list(self, page=1):
        """ Get the list of tasks list """

        route = 'v1/tasks/lists/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_tasks_list(self, data):
        """ Create a new list of tasks 

        Keywords arguments:
        data -- data of the new list of tasks to be created:
        {
            "author": orguser_pk,
            "title": "new list",
            "tasks": [
                task_pk,
                ...
            ],
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tasks/lists/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_tasks_list_details(self, list_pk):
        """ Get the list of tasks details 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(list_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_tasks_list_details(self, list_pk, data):
        """ Update the list of tasks details 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        data -- content of the update:
        {
            "author": orguser_pk,
            "title": "new list",
            "tasks": [
                task_pk,
                ...
            ],
            "followers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tasks/lists/{0}/'.format(list_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_tasks_list(self, list_pk):
        """ Delete the list of tasks 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(list_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def log_tasks(self):
        """ Set all tasks to is_logged True """

        route = 'v1/tasks/log-tasks/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_tasks_timeline(self):

        route = 'v1/tasks/timeline/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_task_details(self, pk):
        """ Get task details 

        Keywords arguments:
        pk -- the pk of the task
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_task_details(self, pk, data):
        """ Update task details 

        Keywords arguments:
        pk -- the pk of the task
        data -- content of the update:
        {
            "creator": orguser_pk,
            "created_at": "string",
            "estimate": 0,
            "is_logged": true,
            "labels": [
                "string"
            ],
            "title": "string",
            "due_date": "string",
            "completed_at": "string",
            "description": "string",
            "is_completed": true
        }
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_task(self, pk):
        """ Delete task 

        Keywords arguments:
        pk -- the pk of the task
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
