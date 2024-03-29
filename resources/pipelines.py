import requests

from .resource import Resource


class Pipelines(Resource):

    def get_pipelines_stage_list(self):
        """Get the list of stages"""
        route = "v1/pipelines/stage/list/{0}".format(self.org_pk)
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)

    def get_pipeline_stage_details(self, stage_pk):
        """Get details of a stage

        Keywords arguments:
        stage_pk --  pk of the stage

        """
        route = f"v1/pipelines/stage/{stage_pk}"
        response = self.process_request(
            requests, "GET", self.base_url, route, self.headers, None, None
        )
        return self.process_response(response)
