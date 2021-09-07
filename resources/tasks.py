import requests
import json

from .helper import Helper


class Tasks(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def empty_tasks_trash(self, project_id):
        """ Set delete all not-completed archived tasks in project """

        route = 'v1/tasks/empty-trash/{0}/'.format(project_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_task_labels_list(self, page=1):
        """ Get the list of tasks labels """

        route = 'v1/tasks/label/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_task_label_details(self, label_pk):
        """ Get the task label details

        Keywords arguments:
        label_pk -- pk of the task label
        """

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_task_label(self, label_pk):
        """ Delete the task label details

        Keywords arguments:
        label_pk -- pk of the task label
        """

        route = 'v1/tasks/label/{0}/'.format(label_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_tasks_list(self, page=1):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_tasks_lists_list(self, page=1):
        """ Get the list of tasks list """

        route = 'v1/tasks/lists/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_tasks_list_details(self, list_pk):
        """ Get the list of tasks details 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(list_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_tasks_list(self, list_pk):
        """ Delete the list of tasks 

        Keywords arguments:
        list_pk -- the pk of list of tasks
        """

        route = 'v1/tasks/lists/{0}/'.format(list_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def log_tasks(self):
        """ Set all tasks to is_logged True """

        route = 'v1/tasks/log-tasks/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_tasks_timeline(self):

        route = 'v1/tasks/timeline/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_task_details(self, pk):
        """ Get task details 

        Keywords arguments:
        pk -- the pk of the task
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_task(self, pk):
        """ Delete task 

        Keywords arguments:
        pk -- the pk of the task
        """

        route = 'v1/tasks/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)