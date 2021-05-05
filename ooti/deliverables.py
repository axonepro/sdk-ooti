import requests
import json

from .helper import Helper


class Deliverables(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Zones ####

    def export_zones(self):
        """ Export zone

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/zones/export/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_zones_list(self, area_pk):
        """ Get zones list

        Keyword arguments:

        area_pk -- the pk of the area
        """

        route = 'v1/zones/list/{0}/?page_size=999999'.format(area_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_zone(self, area_pk, data):
        """ Create zone

        Keyword arguments:

        area_pk -- the pk of the project
        data -- data create :
        {
            "name": "string" (in UI),
            "area": 0 (required),
            "progress": 0,
            "is_annex": true,
            "internal_code": "string" (in UI),
            "client_code": "string" (in UI),
            "surface_area": 0 (in UI),
            "default_surface_price": 0 (in UI),
            "num_units": 0 (in UI)
        }
        """

        route = 'v1/zones/list/{0}/'.format(area_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_zone_details(self, pk):
        """ Get the zone details

        Keyword arguments:

        pk -- pk of the zone
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_zone(self, pk, data):
        """ Update zone

        Keyword arguments:

        pk -- the pk of the zone
        data -- data create :
        {
            "name": "string",
            "area": 0,
            "progress": 0,
            "is_annex": true,
            "internal_code": "string",
            "client_code": "string",
            "surface_area": 0,
            "default_surface_price": 0,
            "num_units": 0
        }
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_zone(self, pk):
        """ Get the zone details

        Keyword arguments:

        pk -- pk of the zone
        """

        route = 'v1/zones/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Areas ####

    def get_areas_list(self, project_pk):
        """ Get the areas list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/areas/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_areas_details(self, pk):
        """ Get the area details

        Keyword arguments:

        pk -- pk of the area
        """

        route = 'v1/areas/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_areas(self, project_pk, data):
        """ Create an area

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "name": "string" (in UI),
                "project": 0,
                "internal_code": "string" (in UI),
                "client_code": "string" (in UI)
            }
        """
        route = 'v1/areas/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_areas(self, pk, data):
        """ Update an area

        Keyword arguments:

        pk -- pk of the project
        data -- data update:
            {
                "name": "string",
                "project": 0,
                "internal_code": "string",
                "client_code": "string"
            }
        """
        route = 'v1/areas/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_area(self, pk):
        """ Delete an area

        Keyword arguments:

        pk -- pk of the project
        """
        route = 'v1/areas/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Phases ####

    def get_phases_list(self, project_pk):
        """Get the phases list

        Keyword arguments:

        project_pk -- the pk of the project

        """

        route = 'v1/phases/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_phase_details(self, pk):
        """Get the phase details
        Keyword arguments:
        pk -- the pk of the phase
        data -- data to update
        """

        route = 'v1/phases/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_phase(self, project_pk, data):
        """ Create an area
        #! Cannot test because fee_project is missing
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_phase(self, pk):
        """ Delete a phase """
        #! Cannot test because cannot create obj (fee_project)

        route = 'v1/phase/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_phase(self, pk, data):
        """Update the phase
        #! Cannot test because cannot create obj (fee_project)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_custom_phase(self, project_pk):
        """ Delete custom phase and use default
        #! Cannot test because cannot create obj (fee_project)
        Keyword arguments:

        pk -- pk of the project
        """
        route = 'v1/phases/delete/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_phases_projections_list(self, project_pk):
        """Get the phases projections list

        Keyword arguments:

        project_pk -- the pk of the project

        """

        route = 'v1/phases/projections/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def reset_phases_order(self, project_pk):
        """ Reset phase order

        Keyword arguments:

        pk -- pk of the project
        """
        route = 'v1/phases/reset-orders/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_phases_progress(self):
        """ Update progress of phases
        #! Not working
        """

        route = 'v1/phases/update_progress/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def export_phase(self, project_pk):
        """ Export phases

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/phases/export/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Milestones ####

    def get_milestones_list(self):
        """ Get milestones list """
        route = 'v1/milestones/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_milestone_details(self, pk):
        """ Get melistone details

        Keyword arguments:

        pk -- pk of the milestone
        """
        route = 'v1/milestones/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_milestone(self, data):
        """ Create a milestone

        Keyword arguments:

        project_pk -- pk of the project
        data -- data create:
            {
                "title": "string",
                "project": 0,
                "date": "string",
                "phases": [
                    "string"
                ],
                "annexes": [
                    "string"
                ],
                "description": "string",
                "in_timeline": true
            }
        """
        route = 'v1/milestones/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_milestone(self, pk, data):
        """ Update a milestone

        Keyword arguments:

        pk -- pk of the milestone
        data -- data update:
            {
                "title": "string",
                "project": 0,
                "date": "string",
                "phases": [
                    "string"
                ],
                "annexes": [
                    "string"
                ],
                "description": "string",
                "in_timeline": true
            }
        """
        route = 'v1/milestones/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_milestone(self, pk):
        """ Delete milestone

        Keyword arguments:

        pk -- pk of the milestone
        """
        route = 'v1/milestones/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Fees ####
    def get_fees_bracket_list(self, project_pk):
        """ Get fees brackets

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/bracket/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_fees_bracket(self, project_pk, data):
        """ Create a fee bracket
        #! Cannot test, fee_project missing
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fees_bracket_details(self, fee_bracket_pk):
        """ Get fee bracket details
        #! Cannot test, fee_project missing to create obj

        Keyword arguments:

        fee_bracket_pk -- pk of the fee bracket
        """
        route = 'v1/fees/bracket/{0}/'.format(fee_bracket_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fees_bracket(self, fee_bracket_pk, data):
        """ Update a fee bracket
        #! Cannot test, fee_project missing to create obj
        Keyword arguments:

        fee_bracket_pk -- pk of the fee bracket
        data -- data update:
            {
                "fee_project": 0,
                "lower": 0,
                "upper": 0,
                "pct": 0,
                "fees": 0
            }
        """
        route = 'v1/fees/bracket/{0}/'.format(fee_bracket_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_fees_bracket(self, data):
        """ Delete a fee bracket
        #! Cannot test, fee_project missing to create obj
        Keyword arguments:

        fee_bracket_pk -- pk of the fee bracket
        """
        route = 'v1/fees/bracket/{0}/'.format(fee_bracket_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def export_project_fees(self, project_pk):
        """ Export all project's fees into .xls file

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/export/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fee_project_version_list(self):
        """ Get fee project version list """

        route = 'v1/fees/fee-project-version/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_fee_project_version(self, data):
        """ Create a fee project version
        #! Cannot test, fee_project missing
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fee_project_version_details(self, fee_project_version_pk):
        """ Get fee project version details
        #! Cannot test, fee_project missing to create obj
        Keyword arguments:

        fee_project_version_pk -- pk of the fee project version
        """

        route = 'v1/fees/fee-project-version/{0}/'.format(fee_project_version_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fee_project_version(self, fee_project_version_pk, data):
        """ Update a fee project version
        #! Cannot test, fee_project missing to create obj
        Keyword arguments:

        fee_project_version_pk -- pk of the fee project version
        data -- data update:
            {
                "title": "string",
                "fee_project": 0,
                "show_on_table": true,
                "data": {}
            }
        """
        route = 'v1/fees/fee-project-version/{0}/'.format(fee_project_version_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_fee_project_version(self, fee_project_version_pk):
        """ Get fee project version details
        #! Cannot test, fee_project missing to create obj

        Keyword arguments:

        fee_project_version_pk -- pk of the fee project version
        """

        route = 'v1/fees/fee-project-version/{0}/'.format(fee_project_version_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_list(self, project_pk):
        """ Get fees list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fees_projection_list(self, project_pk):
        """ Get fees projection list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/projections/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_project_list(self):
        """ Get fees project list """

        route = 'v1/fees/projects/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_fee_project(self, data):
        """ Create a fee project
        #! Cannot test: {'status': 403, 'data': {'detail': 'You do not have permission to perform this action.'}}
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
                "mandate_fees_enabled": true
            }
        """
        route = 'v1/fees/projects/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fees_projects_update(self, fee_project_pk):
        """ Get fees projects update
        #! Cannot test, cannot create obj
        Keyword arguments:

        fee_project_pk -- pk of the fee project
        """

        route = 'v1/fees/projects/update/{0}/'.format(fee_project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_project_details(self, feep_project_pk):
        """ Get fees projects
        #! Cannot test, cannot create obj
        Keyword arguments:

        feep_project_pk -- pk of the fee project
        """

        route = 'v1/fees/projects/{0}/'.format(feep_project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fee_project(self, fee_project_pk, data):
        """ Update a fee project
        #! Cannot test, cannot create obj
        Keyword arguments:

        fee_project_pk -- pk of the fee project
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
        route = 'v1/fees/projects/{0}/'.format(fee_project_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_fee_project(self, feep_project_pk):
        """ Get fees projects
        #! Cannot test, cannot create obj
        Keyword arguments:

        feep_project_pk -- pk of the fee project
        """

        route = 'v1/fees/projects/list/{0}/'.format(feep_project_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_revision(self, fee_pk):
        """ Get fees revision
        #! Canno test, cannot create fee

        Keyword arguments:

        fee_pk -- pk of the fee
        """

        route = 'v1/fees/revision/{0}/'.format(fee_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fee_revision(self, fee_revision_pk):
        """ Update a fee revision
        #! Canno test, cannot create fee revision

        Keyword arguments:

        fee_revision_pk -- pk of the fee revision
        data -- data create:
            {
                "amount": 0,
                "date": "string"
            }
        """
        route = 'v1/fees/revision/{0}/'.format(fee_revision_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_fee_revision(self, fee_revision_pk):
        """ Get fees revision
        #! Canno test, cannot create fee revision

        Keyword arguments:

        fee_revision_pk -- pk of the fee revision
        """

        route = 'v1/fees/revision/{0}/'.format(fee_revision_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_revisions_item_details(self, fee_item_pk):
        """ Get fees revisions for fee item
        #! Canno test, cannot create fee item

        Keyword arguments:

        fee_pk -- pk of the fee item
        """

        route = 'v1/fees/revisions/{0}/'.format(fee_item_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_fee_revisions_item(self, fee_item_pk, data):
        """ Create a fee revision fee item
        #! Canno test, cannot create fee item

        Keyword arguments:

        data -- data create:
            {
                "amount": 0,
                "date": "string"
            }
        """
        route = 'v1/fees/revisions/{0}/'.format(fee_item_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def validation_fees_costs(self, project_pk):
        """ Validate fees costs

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_costs/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def validation_fees_ffne(self, project_pk):
        """ Validate fees ffne

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_ffne/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def validation_fees_production(self, project_pk):
        """ Create a fees revision fee item

        Keyword arguments:

        project_pk -- pk of the project
        """
        route = 'v1/fees/validate_production/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_zones_list(self):
        """ Get fees list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/fees/zones/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_fee_zones(self, fee_item_pk, data):
        """ Create a fee zone
        #! Cannot test, fee_project is missing
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
        route = 'v1/fees/revisions/{0}/'.format(fee_item_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fees_zone_details(self, fee_zone_pk):
        """ Get fee zone details
        #! Cannot test, no fee_project to create obj

        Keyword arguments:

        fee_zone_pk -- pk of the fee zone
        """

        route = 'v1/fees/zones/{0}/'.format(fee_zone_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fee_zone(self, fee_zone_pk):
        """ Update a fee zone
        #! Cannot test, no fee_project to create obj

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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_fees_zone(self, fee_zone_pk):
        """ Delete fee zone
        #! Cannot test, no fee_project to create obj

        Keyword arguments:

        fee_zone_pk -- pk of the fee zone
        """

        route = 'v1/fees/zones/{0}/'.format(fee_zone_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fee_details(self, fee_pk):
        """ Get fee zone details
        #! Cannot test, fee_pk is missing

        Keyword arguments:

        fee_pk -- pk of the fee
        """

        route = 'v1/fees/{0}/'.format(fee_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_fee(self, fee_pk):
        """ Update a fee
        #! Cannot test, fee_pk is missing

        Keyword arguments:

        fee_pk -- pk of the fee
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
        route = 'v1/fees/zones/{0}/'.format(fee_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_fee_details(self, fee_pk):
        """ Delete fee
        #! Cannot test, fee_pk is missing

        Keyword arguments:

        fee_pk -- pk of the fee
        """

        route = 'v1/fees/{0}/'.format(fee_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Plans ####

    def get_plans_list_action(self, project_pk):
        """ Get data needed to perfom actions

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/plans/list-action/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_plans_list_action(self, project_pk):
        """ Create plans list action

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/plans/list-action/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_plans_list(self, project_pk):
        """ Get plans list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/plans/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_plan(self, project_pk, data):
        """ Create plan

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "is_default": true,
                "progress": 0,
                "sub_zone_code": "string",
                "plan_code": "string",
                "project": 0,
                "area": 0,
                "code": "string", ("pln", "det", "elv", "sec")
                "custom_field_1": "string",
                "custom_field_2": "string",
                "custom_field_3": "string",
                "org": 0
            }
        """

        route = 'v1/plans/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_plan_details(self, plan_pk):
        """ Get plans details

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = 'v1/plans/{0}/'.format(plan_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_plan(self, plan_pk, data):
        """ Update plan

        Keyword arguments:

        plan_pk -- the pk of the plan
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "is_default": true,
                "progress": 0,
                "sub_zone_code": "string",
                "plan_code": "string",
                "project": 0,
                "area": 0,
                "code": "string",
                "custom_field_1": "string",
                "custom_field_2": "string",
                "custom_field_3": "string"
            }
        """

        route = 'v1/plans/{0}/'.format(plan_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_plan(self, plan_pk):
        """ Delete plan

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = 'v1/plans/{0}/'.format(plan_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Prescription ####

    def get_prescriptions_list(self, project_pk):
        """ Get prescription list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/prescriptions/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_prescription(self, project_pk, data):
        """ Create prescription

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create :
            {
                "fee_pct": "string",
                "fee": 0,
                "date": "string",
                "description": "string",
                "supplier": "string",
                "supplier_contact": "string",
                "supplier_phone": "string",
                "supplier_email": "string",
                "notes": "string",
                "is_valid": true,
                "is_ordered": true,
                "is_invoiced": true,
                "file": "string",
                "area": 0,
                "type": "string"
            }
        """

        route = 'v1/prescriptions/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_prescriptions_details(self, pk):
        """ Get plans details

        Keyword arguments:

        pk -- the pk of the prescription
        """

        route = 'v1/prescriptions/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_prescriptions(self, pk, data):
        """ Update prescriptions

        Keyword arguments:

        pk -- the pk of the prescription
        data -- data create :
            {
                "fee_pct": "string",
                "fee": 0,
                "date": "string",
                "description": "string",
                "supplier": "string",
                "supplier_contact": "string",
                "supplier_phone": "string",
                "supplier_email": "string",
                "notes": "string",
                "is_valid": true,
                "is_ordered": true,
                "is_invoiced": true,
                "file": "string",
                "area": 0,
                "type": "string"
            }
        """

        route = 'v1/prescriptions/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_prescription(self, pk):
        """ Delete prescription

        Keyword arguments:

        pk -- the pk of the prescription
        """

        route = 'v1/prescriptions/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Defaults ####

    ### Phases ###
    def duplicate_defaults_phase(self, pk):
        """ Duplicate defaults phase  

        Keyword arguements:

        pk -- pk of the phase
        """

        data = {
            "phase": pk
        }

        route = 'v1/defaults/defaults/phase/duplicate/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phase_org_list(self):
        """ Get defaults phase list for organization """

        route = 'v1/defaults/defaults/phases/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_phase_org(self, data):
        """ Create default phase for organization

        Keyword arguments:

        data -- data create :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true,
                "team": 0 (R)
            }
        """

        route = 'v1/defaults/defaults/phases/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phase_team_list(self, team_pk):
        """ Get defaults phase list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/defaults/defaults/phases/list/{0}/{1}/?page_size=999999'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_phase_team(self, team_pk, data):
        """ Create default phase for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true
            }
        """

        route = 'v1/defaults/defaults/phases/list/{0}/{1}'.format(self.org_pk, team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phase_details(self, pk):
        """ Get default phase details

        Keyword arguments:

        pk -- the pk of the default phase
        """

        route = 'v1/defaults/defaults/phases/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_defaults_phase(self, pk, data):
        """ Update default phase details

        Keyword arguments:

        pk -- the pk of the default phase
        data -- data update :
            {
                "name": "string",
                "name_en": "string",
                "shortname_en": "string",
                "name_fr": "string",
                "shortname_fr": "string",
                "shortname": "string",
                "pct": 0,
                "library": 0 (Model in wich are the phases),
                "in_timeline": true,
                "ffne_phase": true
            }
        """

        route = 'v1/defaults/defaults/phases/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_defaults_phase(self, pk):
        """ Delete default phase

        Keyword arguments :

        pk -- pk of the phase
        """
        route = 'v1/defaults/defaults/phases/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Phasesets ###
    def apply_defaults_phasesets(self):
        """ Apply default phase sets """

        route = 'v1/defaults/defaults/phasesets/apply/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def duplicate_defaults_phasesets(self, pk):
        """ Duplicate default phase sets 

        Keyword arguements:

        pk -- pk of the phasesets
        """

        data = {
            "library": pk
        }

        route = 'v1/defaults/defaults/phasesets/duplicate/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phasesets_org_list(self):
        """ Get defaults phase sets list for organization """

        route = 'v1/defaults/defaults/phasesets/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_phasesets_org(self, data):
        """ Create default phase sets for organization

        Keyword arguments:

        data -- data create :
            {
                "is_main": true,
                "title": "string",
                "team": 0 (R)
            }
        """

        route = 'v1/defaults/defaults/phasesets/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phasesets_team_list(self, team_pk):
        """ Get defaults phase sests list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/defaults/defaults/phasesets/list/{0}/{1}/?page_size=999999'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_phasesets_team(self, team_pk, data):
        """ Create default phase for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "is_main": true,
                "title": "string",
                "team": 0 (R)
            }
        """

        route = 'v1/defaults/defaults/phasesets/list/{0}/{1}'.format(self.org_pk, team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_phasesets_details(self, pk):
        """ Get default phase sets details

        Keyword arguments:

        pk -- the pk of the default phase set
        """

        route = 'v1/defaults/defaults/phasesets/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_defaults_phasesets(self, pk, data):
        """ Update default phase sets

        Keyword arguments:

        pk -- the pk of the default phase sets
        data -- data update :
            {
                "is_main": true,
                "title": "string"
            }
        """

        route = 'v1/defaults/defaults/phasesets/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_defaults_phasesets(self, pk):
        """ Delete default phase sets

        Keyword arguments :

        pk -- pk of the phase sets
        """
        route = 'v1/defaults/defaults/phasesets/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Plans ###
    def duplicate_defaults_plan(self, pk):
        """ Duplicate defaults plan 

        Keyword arguments : 

        pk -- pk of the plan 
        """

        data = {
            "plan": pk
        }

        route = 'v1/defaults/defaults/plan/duplicate/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plans_org_list(self):
        """ Get defaults plans list for organization """

        route = 'v1/defaults/defaults/plans/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_plan_org(self, data):
        """ Create default plan for organization

        Keyword arguments:

        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0
            }
        """

        route = 'v1/defaults/defaults/plans/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plans_team_list(self, team_pk):
        """ Get defaults plans list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/defaults/defaults/plans/list/{0}/{1}/?page_size=999999'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_plan_team(self, team_pk, data):
        """ Create default plan for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0
            }
        """

        route = 'v1/defaults/defaults/plans/list/{0}/{1}'.format(self.org_pk, team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plan_details(self, pk):
        """ Get default plan details

        Keyword arguments:

        pk -- the pk of the default plan
        """

        route = 'v1/defaults/defaults/plans/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_defaults_plan(self, pk, data):
        """ Update default plan details

        Keyword arguments:

        pk -- the pk of the default plan
        data -- data update :
            {
                "zone": 0,
                "name_fr": "string",
                "name_en": "string",
                "plan_format": "string",
                "scale": "string",
                "level": "string",
                "lot": 0,
                "name": "string",
                "code": "string",
                "library": 0,
                "team": 0
            }
        """

        route = 'v1/defaults/defaults/plans/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_defaults_plan(self, pk):
        """ Delete default plan

        Keyword arguments :

        pk -- pk of the plan
        """
        route = 'v1/defaults/defaults/plans/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Plansets ###
    def apply_defaults_plansets(self):
        """ Apply default plan sets """

        route = 'v1/defaults/defaults/plansets/apply/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def duplicate_defaults_plansets(self, pk):
        """ Duplicate default plan sets 

        Keyword arguements:

        pk -- pk of the phasesets
        """

        data = {
            "library": pk
        }

        route = 'v1/defaults/defaults/plansets/duplicate/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plansets_org_list(self):
        """ Get defaults plan sets list for organization """

        route = 'v1/defaults/defaults/plansets/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_plansets_org(self, data):
        """ Create default plan sets for organization

        Keyword arguments:

        data -- data create :
            {
                "title": "string"
            }
        """

        route = 'v1/defaults/defaults/plansets/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plansets_team_list(self, team_pk):
        """ Get defaults plan sests list for team

        Keyword arguments :

        team_pk -- pk of the team
        """

        route = 'v1/defaults/defaults/plansets/list/{0}/{1}/?page_size=999999'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_defaults_plansets_team(self, team_pk, data):
        """ Create default plan et for team

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create :
            {
                "title": "string"
            }
        """

        route = 'v1/defaults/defaults/plansets/list/{0}/{1}'.format(self.org_pk, team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_defaults_plansets_details(self, pk):
        """ Get default plan sets details

        Keyword arguments:

        pk -- the pk of the default plan set
        """

        route = 'v1/defaults/defaults/plansets/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_defaults_plansets(self, pk, data):
        """ Update default plan sets

        Keyword arguments:

        pk -- the pk of the default plan sets
        data -- data update :
            {
                "title": "string"
            }
        """

        route = 'v1/defaults/defaults/plansets/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_defaults_plansets(self, pk):
        """ Delete default plan sets

        Keyword arguments :

        pk -- pk of the plan sets
        """
        route = 'v1/defaults/defaults/plansets/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Documents ####
    def get_documents_list(self, project_pk):
        """ Get docuemnts list

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/documents/list/{0}/?page_size=999999'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_document(self, project_pk, data):
        """ Create a docuemnt

        Keyword arguments:

        project_pk -- the pk of the project
        data -- data create : 
            {
                "progress": 0,
                "name": "string", (R)
                "doc_category": "string",
                "price_weight": 0,
                "price": 0, (R)
                "weight": 0,
                "progress_weighted": 0,
                "phase": 0,
                "is_mockup": true,
                "is_additional": true,
                "in_contract": true,
                "annexes": [
                    "string"
                ],
                "zone": 0
            }
        """

        route = 'v1/documents/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def set_price_documents(self, project_pk):
        """ Set price document

        Keyword arguments:

        project_pk -- the pk of the project
        """

        route = 'v1/documents/set-price/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_document_details(self, pk):
        """ Get document details

        Keyword arguments:

        pk -- the pk of the document
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_document(self, pk, data):
        """ Create a docuemnt

        Keyword arguments:

        pk -- the pk of the document
        data -- data update : 
            {
                "progress": 0,
                "name": "string",
                "doc_category": "string",
                "price_weight": 0,
                "price": 0,
                "weight": 0,
                "progress_weighted": 0,
                "phase": 0,
                "is_mockup": true,
                "is_additional": true,
                "in_contract": true,
                "annexes": [
                    "string"
                ],
                "zone": 0
            }
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_document(self, pk):
        """ Delete document

        Keyword arguments:

        pk -- the pk of the document
        """

        route = 'v1/documents/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Contracts ####

    ### Contractors ###
    def get_contractors_list(self):
        """ Get contractors list """

        route = 'v1/contracts/contractor/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contractors(self, data):
        """ Create a contractor

        Keyword arguments:

        data -- data create : 
            {
                "identity_team": 0,
                "currency": 0,
                "name": "string",
                "photo": "string",
                "email": "string",
                "address": "string",
                "telephone": "string",
                "iban": "string",
                "number": "string",
                "is_company": true,
                "is_internal": true,
                "tags": [
                "string"
                ]
            }
        """

        route = 'v1/contracts/contractor/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_contractor_details(self, pk):
        """ Get contractor details

        Keyword arguments:

        pk -- the pk of the contractor
        """

        route = 'v1/contracts/contractor/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contractor(self, pk, data):
        """ Update a contractor

        Keyword arguments:

        pk -- the pk of the contractor
        data -- data create : 
            {
                "identity_team": 0,
                "currency": 0,
                "name": "string",
                "photo": "string",
                "email": "string",
                "address": "string",
                "telephone": "string",
                "iban": "string",
                "number": "string",
                "is_company": true,
                "is_internal": true,
                "tags": [
                "string"
                ]
            }
        """

        route = 'v1/contracts/contractor/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contractor(self, pk):
        """ Delete contractor

        Keyword arguments:

        pk -- the pk of the contractor
        """

        route = 'v1/contracts/contractor/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Contract items ###
    def generate_contracts_project(self, project_pk):
        """ Copy contracts from fee projects to annexes

        Keyword arguments:

        project_pk -- pk of the project :
        """

        route = 'v1/contracts/generate/contracts/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def generate_contracts_org(self):
        """ Generate contracts """

        route = 'v1/contracts/generate/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_contracts_items_list(self):
        """ Get contracts item list """

        route = 'v1/contracts/item/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contracts_items(self, data):
        """ Create a contract item
        #! Cannot test because cannot create contract
        Keyword arguments:

        data -- data create : 
            {
                "contract": 0,
                "phase": 0,
                "annex": 0,
                "type": "string",
                "fee": 0,
                "amount_current": 0,
                "already_billed": 0,
                "amount_billed": 0,
                "already_paid": 0
            }
        """

        route = 'v1/contracts/item/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_contract_item_details(self, pk):
        """ Get contract item details
        #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the item
        """

        route = 'v1/contracts/item/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contract_item(self, pk, data):
        """ Update a contract item
        #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- pk of the item
        data -- data update : 
            {
                "contract": 0,
                "phase": 0,
                "annex": 0,
                "type": "string",
                "fee": 0,
                "amount_current": 0,
                "already_billed": 0,
                "amount_billed": 0,
                "already_paid": 0
            }
        """

        route = 'v1/contracts/item/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contract_item(self, pk):
        """ Delete a contract item
        #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- pk of the item
        """

        route = 'v1/contracts/item/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Contracts ###
    def get_contracts_list(self):
        """ Get contracts list """

        route = 'v1/contracts/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contract(self, data):
        """ Create a contract
        #! A contract can be added to a fee_project under review only. 
        #! Cannot test because cannot get fee_project based on a project 

        Keyword arguments:

        data -- data create : 
            {
                "contractor": 0, (R)
                "manager": 0,
                "fee_project": 0,
                "is_valid": true,
                "is_archived": true,
                "type": "string", (R) ("sub")
                "forecast_type": "string",
                "invoicing_method": "string",
                "description": "string",
                "is_mandate": true,
                "tax_rate": 0,
                "project": 0,
                "fee_project": 0
            }
        """

        route = 'v1/contracts/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_contract_details(self, pk):
        """ Get contract details
        #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the contract
        """

        route = 'v1/contracts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contract(self, pk, data):
        """ Update a contract
        #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the contract
        data -- data create : 
            {
                "contractor": 0,
                "manager": 0,
                "fee_project": 0,
                "is_valid": true,
                "is_archived": true,
                "type": "string",
                "forecast_type": "string",
                "invoicing_method": "string",
                "description": "string",
                "is_mandate": true,
                "tax_rate": 0
            }
        """

        route = 'v1/contracts/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contract(self, pk):
        """ Delete contract 
        #! Cannot test because cannot create contract
        Keyword arguments:

        pk -- the pk of the contract
        """

        route = 'v1/contracts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Contract month ###
    def generate_contracts_month_org(self, contract_pk):
        """ Generate contract month 
        #! Cannot test because cannot create contract

        Keyword arguments:

        contract_pk -- pk of the contract
        """

        data = {
            "contract": contract_pk
        }

        route = 'v1/contracts/month/generate/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_contracts_month_list(self):
        """ Get contracts list """

        route = 'v1/contracts/month/list/{0}/?page_size=999999'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_contracts_month(self, data):
        """ Create a contract month
         #! Cannot test because cannot create contract

        Keyword arguments:

        data -- data create : 
            {
                "contract": 0,
                "year": 0,
                "month": 0,
                "start_date": "string",
                "end_date": "string",
                "is_past": true,
                "is_present": true,
                "is_future": true,
                "budget": 0,
                "budget_projected": 0,
                "actual": 0,
                "pct": 0
            }
        """

        route = 'v1/contracts/month/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_contract_month_details(self, pk):
        """ Get contract details
         #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the contract month
        """

        route = 'v1/contracts/month/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_contracts_month(self, pk, data):
        """ Create a contract month
         #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the contract month
        data -- data create : 
            {
                "contract": 0,
                "year": 0,
                "month": 0,
                "start_date": "string",
                "end_date": "string",
                "is_past": true,
                "is_present": true,
                "is_future": true,
                "budget": 0,
                "budget_projected": 0,
                "actual": 0,
                "pct": 0
            }
        """

        route = 'v1/contracts/month/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_contract_month(self, pk):
        """ Delete contract month
         #! Cannot test because cannot create contract

        Keyword arguments:

        pk -- the pk of the contract month
        """

        route = 'v1/contracts/month/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Annexes ####

    def get_annexes_list(self, project_pk):
        """Get the annexes list

        Keyword arguments:
        project_pk - - the pk of the project
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_annexe_details(self, pk):
        """Get the annexe details

        Keyword arguments:
        pk - - the pk of the annexe
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def create_annexe(self, project_pk, data):
        """Create an payment

        Keyword arguments:
        project_pk - - the pk of the project
        data - - data to create
        """

        route = 'v1/annexes/list/{0}/'.format(project_pk)
        parameters = '?phase='
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))

    def update_annexe(self, pk, data):
        """Update the annexe details

        Keyword arguments:
        pk - - the pk of the project
        """

        route = 'v1/annexes/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}
