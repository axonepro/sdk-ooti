import requests
import json

from .helper import Helper


class Phases(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_phases_list(self, project_pk, page=1):
        """Get the phases list

        Keyword arguments:

        project_pk -- the pk of the project

        """
        route = 'v1/phases/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_phases_list_fee_project(self, project_pk, fee_project, page=1):
        """Get the phase list fee project

        Keyword arguments:

        project_pk -- the pk of the project
        fee_project -- pk of the fee project
        """

        route = 'v1/phases/list/{0}/?page_size={1}&page={2}&fee_project={3}'.format(
            project_pk, self.pagination, page, fee_project)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_phase_details(self, pk):
        """Get the phase details

        Keyword arguments:

        pk -- the pk of the phase
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_phase(self, project_pk, data):
        """ Create a phase

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "name": "string",
                "shortname": "string",
                "fee_project": "string",
                "ffne_phase": False,
                "in_timeline": True,
                "pct": 0,
                "dependants": ["string"]
            }
        """
        route = 'v1/phases/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_phase(self, pk):
        """ Delete a phase """

        route = 'v1/phases/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_phase(self, pk, data):
        """Update the phase

        Keyword arguments:

        pk -- the pk of the phase
        data -- data update:
            {
                "name": "string",
                "shortname": "string",
                "pct": "string" (number in string)
            }
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_phases_projections_list(self, project_pk, page=1):
        """Get the phases projections list

        Keyword arguments:

        project_pk -- the pk of the project

        """

        route = 'v1/phases/projections/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def reset_phases_order(self, project_pk):
        """ Reset phase order

        Keyword arguments:

        pk -- pk of the project
        """
        route = 'v1/phases/reset-orders/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_phases_progress(self):
        """ Update progress of phase """

        route = 'v1/phases/update_progress/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def export_phase(self, project_pk):
        """ Export phase

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/phases/export/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_phase_planphase_details(self, pk):
        """ Get the planphase details

        Keyword arguments:

        pk -- the pk of the phase
        """

        route = 'v1/phases/planphases/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def delete_phase_planphase(self, pk):
        """ Delete planphase

        Keyword arguments:

        pk -- the pk of the phase
        """

        route = 'v1/phases/planphases/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_phase_planphase(self, pk, data):
        """ Update planphase

        Keyword arguments:

        pk -- the pk of the phase
        data -- data update : 
            {
                "is_active": true,
                "is_immediate": true,
                "zone_phase": 0,
                "progress": 0
            }
        """

        route = 'v1/phases/planphases/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)