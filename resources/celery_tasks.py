import requests

from .resource import Resource

"""
- ERROR 403 v1/celery_tasks/last/
- ERROR 404 v1/celery_tasks/last/{org_pk}/

"""


class CeleryTask(Resource):
    # TODO GET on /api/v1/celery_tasks/last/

    def get_last_celery_task(self):
        """ """

        route = f"v1/celery_tasks/last/{self.org_pk}/"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_celery_tasks_list(self, page=1):
        """Get the list of celery tasks"""

        route = f"v1/celery_tasks/list/{self.org_pk}/?page_size={self.pagination}&page={page}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
