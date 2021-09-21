import requests
import json

from .helper import Helper

"""
- ERROR 403 v1/celery_tasks/last/ 
- ERROR 404 v1/celery_tasks/last/{org_pk}/

"""

class Celery_tasks(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO GET on /api/v1/celery_tasks/last/

    def get_last_celery_task(self):
        """ """

        route = 'v1/celery_tasks/last/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_celery_tasks_list(self, page=1):
        """ Get the list of celery tasks """

        route = 'v1/celery_tasks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)