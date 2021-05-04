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

    #### Contact ####

    def get_contacts_list(self, project_pk=None):
        """ Get the contacts list

        project_pk -- the pk of the contacts' project (optional)
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def create_contact(self, data, project_pk=None):
        """ Create a new contact

        Keywords arguments:
        project_pk -- the pk of the contact's project (optional)
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
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_number_uncategorized_contacts(self, team_pk=None, project_pk=None):
        """ Return the number of uncategorized contacts """

        route = 'v1/contacts/uncategorized/count/{0}/'.format(self.org_pk)
        parameters = ''
        if team_pk is not None or project_pk is not None:
            parameters = '?'
            if team_pk is not None:
                parameters += 'team={0}'.format(team_pk)
                if project_pk is not None:
                    parameters += '&'
            if project_pk is not None:
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
        data -- data to update, example value:
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
        return {"status": response.status_code, "data": json.loads(response.content)}

    def delete_contact(self, pk):
        """ Delete the contact

        Keywords arguments:
        pk -- the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {'status': response.status_code, 'data': 'Contact deleted'}
        else:
            return self.process_response(response)

    #### Task ####

    def empty_tasks_trash(self, project_pk):
        """ Set delete all not-completed archived tasks in project """

        route = 'v1/tasks/empty-trash/{0}/'.format(project_pk)
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

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_task_label_details(self, label_pk, data):

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_task_label(self, label_pk):

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
