import requests
import json

from .helper import Helper


class Fees(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO GET on /api/v1/fees/apply-project-defaults/{fee_project_pk}/{is_price}/

    def get_fees_bracket_list(self, project_pk, page=1):
        """ Get fees brackets list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/bracket/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fees_bracket(self, project_pk, data):
        """ Create a fee bracket
        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "fee_project": 0,
                "lower": 0,
                "upper": 0,
                "pct": 0,
                "fees": 0
            }
        """
        route = 'v1/fees/bracket/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_fees_bracket_details(self, pk):
        """ Get fee bracket details

        Keyword arguments:

        pk -- pk of the fee bracket
        """
        route = 'v1/fees/bracket/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fees_bracket(self, pk, data):
        """ Update a fee bracket

        Keyword arguments:

        pk -- pk of the fee bracket
        data -- data update:
            {
                "fee_project": 0,
                "lower": 0,
                "upper": 0,
                "pct": 0,
                "fees": 0
            }
        """
        route = 'v1/fees/bracket/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fees_bracket(self, pk):
        """ Delete a fee bracket

        Keyword arguments:

        pk -- pk of the fee bracket
        """
        route = 'v1/fees/bracket/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def export_project_fees(self, project_pk):
        """ Export all project's fees into .xls file

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/export/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fee_project_version_list(self, page=1):
        """ Get fee project version list """

        route = 'v1/fees/fee-project-version/list/{0}/?page_size={1}&page={2}'.format(
            self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fee_project_version(self, data):
        """ Create a fee project version

        Keyword arguments:

        data -- data create:
            {
                "title": "string",
                "fee_project": 0,
                "show_on_table": true,
                "data": {}
            }
        """
        route = 'v1/fees/fee-project-version/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_fee_project_version_details(self, pk):
        """ Get fee project version details

        Keyword arguments:

        pk -- pk of the fee project version
        """

        route = 'v1/fees/fee-project-version/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fee_project_version(self, pk, data):
        """ Update a fee project version

        Keyword arguments:

        pk -- pk of the fee project version
        data -- data update:
            {
                "title": "string",
                "fee_project": 0,
                "show_on_table": true,
                "data": {}
            }
        """
        route = 'v1/fees/fee-project-version/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fee_project_version(self, pk):
        """ Get fee project version details

        Keyword arguments:

        pk -- pk of the fee project version
        """

        route = 'v1/fees/fee-project-version/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/fees/index/populate_ffne/{project_pk}/{is_price}/

    # TODO GET on /api/v1/fees/index/populate_prod/{project_pk}/{is_price}/

    def get_fees_list(self, project_pk):
        """ Get fees list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fee(self, project_pk, data):
        """ Create a fee

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "title": "string",
                "amount_base": 0,
                "amount_current": 0,
                "type": "string",
                "is_mockup": true,
                "progress": 0,
                "in_timeline": true
            }
        """
        route = 'v1/fees/list/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_fees_projection_list(self, project_pk, page=1):
        """ Get fees projection list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/projections/list/{0}/?page_size={1}n&page={2}'.format(project_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fees_project_list_projects(self, project_pk, page=1):
        """ Get fees project list for a given project 

        Keyword arguments :

        project_pk -- pk of the project 
        """

        route = 'v1/fees/projects/list/{0}/?page_size={1}&page={2}&project={3}'.format(
            self.org_pk, self.pagination, page, project_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_fees_project_list(self, page=1):
        """ Get fees project list """

        route = 'v1/fees/projects/list/{0}/?page_size={1}n&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fee_project(self, data):
        """ Create a fee project

        Keyword arguments:

        data -- data create:
            {
                "title": "string",
                "title_en": "string",
                "title_fr": "string",
                "calculation_method": "string",
                "cost": 0,
                "fee_pct": 0,
                "fees_base": 0,
                "fees_contract": 0,
                "advance_payment_pct": 0,
                "advance_payment": 0,
                "insurance_pct": 0,
                "insurance": 0,
                "discount_pct": 0,
                "discount": 0,
                "zone_fees_base": 0,
                "zone_fees_contract": 0,
                "surface_area": 0,
                "fees_per_surface_unit": 0,
                "cost_per_surface_unit": 0,
                "default_surface_price": 0,
                "board_price": 0,
                "rendering_price": 0,
                "is_validated": true,
                "has_mockup": true,
                "master": 0,
                "co_contractors_enabled": true,
                "subcontractors_enabled": true,
                "total_advance_payment": 0,
                "mandate_fees_enabled": true,
                "project": 0
            }
        """
        route = 'v1/fees/projects/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_fees_projects_update(self, pk):
        """ Get fees projects update

        Keyword arguments:

        pk -- pk of the fee project
        """

        route = 'v1/fees/projects/update/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fees_project_details(self, pk):
        """ Get fees project details

        Keyword arguments:

        pk -- pk of the fee project
        """

        route = 'v1/fees/projects/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fee_project(self, pk, data):
        """ Update a fee project

        Keyword arguments:

        pk -- pk of the fee project
        data -- data create:
            {
                "title": "string",
                "title_en": "string",
                "title_fr": "string",
                "calculation_method": "string",
                "cost": 0,
                "fee_pct": 0,
                "fees_base": 0,
                "fees_contract": 0,
                "advance_payment_pct": 0,
                "advance_payment": 0,
                "insurance_pct": 0,
                "insurance": 0,
                "discount_pct": 0,
                "discount": 0,
                "zone_fees_base": 0,
                "zone_fees_contract": 0,
                "surface_area": 0,
                "fees_per_surface_unit": 0,
                "cost_per_surface_unit": 0,
                "default_surface_price": 0,
                "board_price": 0,
                "rendering_price": 0,
                "is_validated": true,
                "has_mockup": true,
                "master": 0,
                "co_contractors_enabled": true,
                "subcontractors_enabled": true,
                "total_advance_payment": 0,
                "mandate_fees_enabled": true
            }
        """
        route = 'v1/fees/projects/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fee_project(self, pk):
        """ Delete fee project

        Keyword arguments:

        pk -- pk of the fee project
        """

        route = 'v1/fees/projects/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fees_revision_details(self, fee_pk):
        """ Get fees revision details

        Keyword arguments:

        fee_pk -- pk of the fee
        """

        route = 'v1/fees/revision/{0}/'.format(fee_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fee_revision(self, fee_revision_pk, data):
        """ Update a fee revision

        Keyword arguments:

        fee_revision_pk -- pk of the fee revision
        data -- data create:
            {
                "amount": 0,
                "date": "string"
            }
        """
        route = 'v1/fees/revision/{0}/'.format(fee_revision_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fee_revision(self, fee_revision_pk):
        """ Delete fees revision

        Keyword arguments:

        fee_revision_pk -- pk of the fee revision
        """

        route = 'v1/fees/revision/{0}/'.format(fee_revision_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fees_revisions_item_details(self, fee_item_pk):
        """ Get fees revisions item details

        Note that "fee_item" is a fee 

        Keyword arguments:

        fee_pk -- pk of the fee item
        """

        route = 'v1/fees/revisions/{0}/'.format(fee_item_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_fee_revisions_item(self, fee_item_pk, data):
        """ Create a fee revision item

        Note that "fee_item" is a fee 

        Keyword arguments:

        data -- data create:
            {
                "amount": 0,
                "date": "string"
            }
        """
        route = 'v1/fees/revisions/{0}/'.format(fee_item_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def validation_fees_costs(self, project_pk):
        """ Validate fees costs

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_costs/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def validation_fees_ffne(self, project_pk):
        """ Validate fees ffne

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_ffne/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def validation_fees_production(self, project_pk):
        """ Create a fees revision fee item

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_production/{0}/'.format(project_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fees_zones_list(self, page=1):
        """ Get fees zones list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/zones/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_fee_zones(self, data):
        """ Create a fee zone

        Keyword arguments:

        data -- data create:
            {
                "zone": 0,
                "project": 0,
                "fee_project": 0,
                "board": 0,
                "rendering": 0
            }
        """
        route = 'v1/fees/zones/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_fees_zone_details(self, fee_zone_pk):
        """ Get fee zone details

        Keyword arguments:

        fee_zone_pk -- pk of the fee zone
        """

        route = 'v1/fees/zones/{0}/'.format(fee_zone_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fee_zone(self, fee_zone_pk, data):
        """ Update a fee zone

        Keyword arguments:

        fee_zone_pk -- pk of the fee zone
        data -- data create:
            {
                "zone": 0,
                "project": 0,
                "fee_project": 0,
                "board": 0,
                "rendering": 0
            }
        """
        route = 'v1/fees/zones/{0}/'.format(fee_zone_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fees_zone(self, fee_zone_pk):
        """ Delete fee zone

        Keyword arguments:

        fee_zone_pk -- pk of the fee zone
        """

        route = 'v1/fees/zones/{0}/'.format(fee_zone_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_fee_details(self, pk):
        """ Get fee details

        Keyword arguments:

        pk -- pk of the fee
        """

        route = 'v1/fees/{0}/'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_fee(self, pk, data):
        """ Update a fee

        Keyword arguments:

        pk -- pk of the fee
        data -- data update:
            {
                "title": "string",
                "amount_base": 0,
                "amount_current": 0,
                "type": "string",
                "is_mockup": true,
                "progress": 0,
                "in_timeline": true
            }
        """
        route = 'v1/fees/{0}/'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_fee(self, pk):
        """ Delete fee

        Keyword arguments:

        pk -- pk of the fee
        """

        route = 'v1/fees/{0}/'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)