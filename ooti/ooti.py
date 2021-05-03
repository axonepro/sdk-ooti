import requests
import json

from .invoicing import Invoicing
from .helper import Helper


class Auth(Helper):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://ooti-staging-3.herokuapp.com/api/'  # "https://app.ooti.co/api/"
        self.org_pk = None
        self.teams_pk = None
        self.access_token = None
        self._csrf_token = None
        self.headers = None
        self.Invoicing = None

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_org()
        self.Invoicing = Invoicing(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers)


##### AUTH #####

    ##### Projects #####

    def get_project_details(self, pk):
        """Get the project details
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def update_project_details(self, pk, data):
        """Update the project details
        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def get_projects_list(self):
        """Get the project list"""

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    #### Organizations ####

    def get_organization_details(self):
        """ Get organization details """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def __get_org(self):
        """ Set the organization id of the user """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        self.org_pk = json.loads(response.content)['organizations'][0]['id']
        teams = json.loads(response.content)['organizations'][0]['teams']
        self.teams_pk = []
        for team in range(len(teams)):
            self.teams_pk.append({key: teams[team][key] for key in ('id', 'title')})
        return response.status_code

    #### Token ####

    def __get_token(self):
        route = 'v1/token-auth/'
        headers = {
            'Accept': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=headers, data=data)
        self.access_token = json.loads(response.content)['token']
        self.headers = {
            'Authorization': 'JWT {0}'.format(self.access_token),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRF-Token': self._csrf_token
        }
        return response.status_code

    def __get_csrf_token(self):
        client = requests.session()
        # Retrieve the CSRF token first
        client.get("https://app.ooti.co/accounts/login/")  # sets cookie
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']

        self._csrf_token = csrftoken

    def __refresh_token(self):
        """ Refresh the access token """

        route = 'v1/token-refresh/'
        data = {
            'token': self.access_token
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        if response == 201:
            self.headers['Authorization'] = 'JWT {0}'.format(self.access_token)
        return response.status_code

    def __verify_token(self):
        """ Verify if the access token is still valid """

        route = 'v1/token-verify/'
        data = {
            'token': self.access_token
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return response.status_code


##### DELIVERABLES #####

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

        route = 'v1/zones/list/{0}/'.format(area_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_zone(self, area_pk, data):
        """ Create zone

        Keyword arguments:

        area_pk -- the pk of the project
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
                "name": "string",
                "project": 0,
                "internal_code": "string",
                "client_code": "string"
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

        route = 'v1/fees/bracket/list/{0}/'.format(project_pk)
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

        route = 'v1/fees/fee-project-version/list/{0}/'.format(self.org_pk)
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
        #! Cannot test, type is unknown
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

        route = 'v1/fees/projections/list/{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_fees_project_list(self):
        """ Get fees project list """

        route = 'v1/fees/projects/list/{0}/'.format(self.org_pk)
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

        route = 'v1/fees/zones/list/{0}/'.format(self.org_pk)
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

        route = 'v1/plans/list/{0}/'.format(project_pk)
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

        Keyword arguments:

        plan_pk -- the pk of the plan
        """

        route = 'v1/plans/{0}/'.format(plan_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_plan(self, project_pk, data):
        """ Update plan

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

        route = 'v1/plans/{0}/'.format(project_pk)
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


##### COSTS #####

    #### Expenses ####

    def get_expenses_list(self):
        """ Get the expenses list """

        route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_expenses_details(self, pk):
        """Get the expense details

        Keyword arguments:

        pk - - the pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}


##### COLLABORATION #####

    #### Contact ####

    def get_contacts_list(self, project_pk=None):
        """ Get the contacts list

        project_pk - - the pk of the contacts' project(optional)
        """

        route = 'v1/contacts/list/{0}/'.format(self.org_pk)
        if project_pk is not None:
            route += '{0}/'.format(project_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_contact_details(self, pk):
        """ Get the contact details

        Keywords arguments:
        pk - - the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}

    def update_contact_details(self, pk, data):
        """ Update the contact details

        Keywords arguments:
        pk - - the pk of the contact
        data - - data to update, example value:
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
            "client": [(ids of the clients associated with this contact)
                "string"
            ]
        }
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return {"status": response.status_code, "data": json.loads(response.content)}

    def create_contact(self, data, project_pk=None):
        """ Create contact

        Keywords arguments:
        project_pk - - the pk of the contact's project(optional)
        data - - data to create:
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
        if(response.status_code != 500):
            return {'status': response.status_code, 'data': json.loads(response.content)['results']}
        else:
            return {'status': response.status_code}

    def delete_contact(self, pk):
        """ Delete the contact

        Keywords arguments:
        pk - - the pk of the contact
        """

        route = 'v1/contacts/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        if(response.status_code == 204):
            return {'status': response.status_code, 'data': 'Contact deleted'}
        else:
            return {'status': response.status_code, 'data': json.loads(response.content)}

    #### Task ####

    def get_tasks_list(self):
        """ Get the tasks list """

        route = 'v1/tasks/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)}


##### TIME #####


##### SETTINGS #####


##### RANDOM #####
