import requests
import json

from helper import Helper


class Collaboration(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Contacts ####

    # POST on v1/contacts/list-action/{org_pk}/ ? Error 500

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
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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

    def get_contacts_list(self, project_id=None):
        """ Get the contacts list

        project_id -- id of the contacts' project (optional)
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
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

    def get_newsletters_list(self):
        """ Get the list of newsletters """

        route = 'v1/newsletters/list/{0}/'.format(self.org_pk)
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

    def get_notes_list(self):
        """ Get the list of notes """

        route = 'v1/notes/list/{0}/'.format(self.org_pk)
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

    # PATCH on v1/notifications/digest-config/{org_pk}/ ?

    def get_notifications_config(self):
        """ Get the notifications config of the organization """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_notifications_config(self, data):  # not tested
        """ Update the notifications config of the organization 

        Keywords arguments:
        data -- content of the update
        {

        }
        """

        route = 'v1/notifications/digest-config/{0}/'.format(self.org_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    #### Posts ###

    #### Tasks ####

    def empty_tasks_trash(self, project_id):
        """ Set delete all not-completed archived tasks in project """

        route = 'v1/tasks/empty-trash/{0}/'.format(project_id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_task_labels_list(self):
        """ Get the list of tasks labels """

        route = 'v1/tasks/label/list/{0}/'.format(self.org_pk)
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

    def get_tasks_list(self):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
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

    def get_tasks_lists_list(self):
        """ Get the list of tasks list """

        route = 'v1/tasks/lists/list/{0}/'.format(self.org_pk)
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

    def get_tasks_list_detail(self, list_pk):
        """ Get the list of tasks details 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(pk)
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

        route = 'v1/tasks/lists/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_tasks_list_details(self, list_pk):
        """ Delete the list of tasks 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(pk)
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

    def delete_task_details(self, pk):
        """ Delete task 

        Keywords arguments:
        pk -- the pk of the task
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
