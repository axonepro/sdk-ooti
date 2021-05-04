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

        route = 'v1/phase/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_custom_phase(self, project_pk):
        """ Delete custom phase and use default

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
        #TODO : add tests, type is not required
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
        #! Cannot test, code is required and unknown
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
                "code": "string",
                "custom_field_1": "string",
                "custom_field_2": "string",
                "custom_field_3": "string"
            }
        """

        route = 'v1/plans/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_plan_details(self, plan_pk):
        """ Get plans details 
        #! Cannot test, cannot create plan

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = 'v1/plans/{0}/'.format(plan_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_plan(self, plan_pk, data):
        """ Update plan
        #! Cannot test, cannot create plan

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
        #! Cannot test, cannot create plan
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
