import requests
import json

from .helper import Helper


class Clients(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_clients_list(self, team_pk, page=1):
        """Get the clients list

        Keyword arguments:

        pk -- the pk of the team
        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}&page_size={1}&page={2}'.format(team_pk, self.pagination, page)

        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, parameters, None)
        return self.process_response(response, True)

    # TODO POST on /api/v1/clients/list/{org_pk}/

    def get_clients_details(self, pk):
        """Get the client details

        Keyword arguments:

        pk -- the pk of the client
        """

        route = 'v1/clients/{0}/'.format(pk)

        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_client(self, data):
        """ Create client

        Keyword arguments:

        data -- data create, required fields:
            {
                "company_name": "string",
                "number": "string",
                "currency": "string" (currency_pk)
                "billing_address": "string",
                "team": "string",
                "tags": []
            }
        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)

        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_client(self, pk, data):
        """ Update client

        Keyword arguments:

        pk -- pk of the client
        data -- data create, required fields:
            {
                "company_name": "string",
                "currency": "string" (currency_pk),
                "number": "string",
                "business_vat_id: "string",
                "billing_address": "string",
                "group": "?"
                "address: "string"
            }
        """
        route = 'v1/clients/{0}/'.format(pk)

        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_client(self, pk):
        """ Delete client

        Keyword arguments:

        pk -- pk of the client
        """
        route = 'v1/clients/{0}/'.format(pk)

        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/clients/export/{org_pk}/

    # TODO GET on /api/v1/clients/group/list/{org_pk}/

    # TODO POST on /api/v1/clients/group/list/{org_pk}/

    # TODO GET on /api/v1/clients/group/{id}/

    # TODO PATCH on /api/v1/clients/group/{id}/

    # TODO DELETE on /api/v1/clients/group/{id}/

    # TODO GET on /api/v1/clients/project/list/{org_pk}/

    # TODO POST on /api/v1/clients/project/list/{org_pk}/

    # TODO GET on /api/v1/clients/project/{id}/

    # TODO PATCH on /api/v1/clients/project/{id}/

    # TODO DELETE on /api/v1/clients/project/{id}/

    # TODO GET on /api/v1/clients/split/list/{org_pk}/

    # TODO POST on /api/v1/clients/split/list/{org_pk}/

    # TODO GET on /api/v1/clients/split/{id}/

    # TODO PATCH on /api/v1/clients/split/{id}/

    # TODO DELETE on /api/v1/clients/split/{id}/

    # TODO POST on /api/v1/clients/{id}/apply_default_contact/