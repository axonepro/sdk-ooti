import requests
import json
import sys

from .costs import Costs
from .helper import Helper
from .others import Others
from .settings import Settings
from .invoicing import Invoicing
from .deliverables import Deliverables
from .collaboration import Collaboration
from .time import Time

# To read .env variables
import os
from dotenv import load_dotenv

# Loading environment variables (stored in .env file)
load_dotenv()


class Auth(Helper):
    def __init__(self, username, password, pagination=None):
        self.username = username
        self.password = password

        self.base_url()

        self.org_pk = None
        self.teams_pk = None
        self.access_token = None
        self._csrf_token = None
        self.headers = None

        self.Costs = None
        self.Others = None
        self.Settings = None
        self.Collaboration = None

        if pagination and isinstance(pagination, int) and pagination > 0:
            self.pagination = pagination
        else:
            self.pagination = 50

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_selected_org()
        self.__get_teams()

        self.Costs = Costs(self.base_url, self.org_pk, self.teams_pk,
                           self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Others = Others(self.base_url, self.org_pk, self.teams_pk,
                             self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Settings = Settings(self.base_url, self.org_pk, self.teams_pk,
                                 self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Collaboration = Collaboration(self.base_url, self.org_pk, self.teams_pk,
                                           self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Invoicing = Invoicing(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Deliverables = Deliverables(self.base_url, self.org_pk, self.teams_pk,
                                         self.access_token, self._csrf_token, self.headers, self.pagination)

        self.Time = Time(self.base_url, self.org_pk, self.teams_pk,
                         self.access_token, self._csrf_token,  self.headers, self.pagination)

    def base_url(self):
        """ Choose base_url based on ENV variable """
        ENVIRONMENT = os.getenv("ENVIRONMENT", default=None)

        if ENVIRONMENT and ENVIRONMENT == 'STAGING':
            self.base_url = 'https://ooti-staging-3.herokuapp.com/api/'
        elif ENVIRONMENT and ENVIRONMENT == 'LOCAL':
            self.base_url = 'http://127.0.0.1:8000/api/'
        else:
            self.base_url = 'https://app.ooti.co/api/'

    def update_pagination(self, pagination):
        """ Setter for pagination """
        if pagination and isinstance(pagination, int) and pagination > 0:
            self.Costs.pagination = pagination
            self.Others.pagination = pagination
            self.Settings.pagination = pagination
            self.Collaboration.pagination = pagination
            self.Invoicing.pagination = pagination
            self.Deliverables.pagination = pagination
            self.Time.pagination = pagination
            self.pagination = pagination

    ##### AUTH #####

    ##### Invitation #####

    def get_invitations_list(self):
        """ Get the list of invitations """

        route = 'v1/invitations/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_team_invitations_list(self, team_pk):
        """ Get the list of invitations of a specific team 

        Keywords arguments:
        team_pk -- pk of the team
        """

        route = 'v1/invitations/list/{0}/{1}/'.format(self.org_pk, team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_invitation_details(self, pk):
        """ Get the invitation details

        Keywords arguments:
        pk -- pk of the invitation
        """
        route = 'v1/invitations/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_invitation(self, pk, data):  # which pk ? already tested with orguser_pk and team_pk
        """ Create a new invitation """

        route = 'v1/invitations/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_invitation_details(self, pk, data):
        """ Update invitation informations

        Keywords arguments:
        pk -- pk of the invitation
        data -- content of the update:
        {
            "email": "emailchanged@mail.com
        }
        """

        route = 'v1/invitations/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_invitation(self, pk):
        """ Delete the invitation

        Keywords arguments:
        pk -- pk of the invitation
        """
        route = 'v1/invitations/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ##### Projects #####

    def get_project_details(self, id):
        """ Get the project details

        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_project_details(self, id, data):
        """ Update the project details

        Keyword arguments:
        id -- the id of the project
        data -- content of the update:
        {
            "surface_area": 238,
            "surface_unit": "m",
            "notes": "some notes",
            "project_title": "New title"
        }
        """

        route = 'v1/projects/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project(self, id):
        """ Delete a project

        Keyword arguments:
        id -- the id of the project
        """
        route = 'v1/projects/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projects_list(self, team_pk=None):
        """ Get the projects list 

        Keywords arguments:
        team_pk -- pk of a team to get the project list of a specific team
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        if team_pk is not None:
            route += '{0}/'.format(team_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def export_projects_list(self):
        """ Export the list of projects as a .xls file """

        route = 'v1/projects/export/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        xls_file = open('projects_list.xls', 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_access_projects_list(self):  # what is access on OOTI ?

        route = 'v1/projects/list/access/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_project(self, data):
        """ Create a new project

        Keyword arguments:
        data -- content of the project to be created:
        {
            "client": client_pk,
            "currency": curency_pk,
            "project_title": "New project",
            "phases": [phase_pk, phase_pk, ...],
            "project_users": [project_user_pk, ...],
            "areas": [],
            "project_tags": [],
            "start_date": "28-04-2020",
            "end_date": "28-08-2020",
            "orgusers": [orguser_pk, orguser_pk, ...],
            "city": "Paris",
            "country": "FR"
        }
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_project_fee_summary(self, id):
        """ Get the project fee summary

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/fee-summary/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_list_access(self):
        """ ? """

        route = 'v1/projects/list/access/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_project_revenue(self, id):
        """ Get the list of project revenues by years and by months

        Keywords arguments:
        id -- the id of the project
        """
        route = 'v1/projects/revenue/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_available_clients(self, id):
        """ Get the list of clients avalaible (clients that are not already participating in the project)
        Return the list of clients with their display name and pk

        Keywords arguments:
        id -- the id of the project
        """

        route = 'v1/projects/available-clients/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_projects_list_deliverables(self):
        """ Get the list of projects and their associated deliverables where the current user is a member of """

        route = 'v1/projects/deliverables/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_users_list(self, id):
        """ Get the list of users of a project 

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/users/list/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

    def get_project_user_details(self, user_pk):
        """ Get the project user details 

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def add_project_user(self, id, data):
        """ Add a new user to the project 

        Keyword arguments:
        id -- id of the project
        data -- content of the user to add to the project:
        {
            "orguser": orguser_pk,
            "permissionsset": permission_pk,
            "project": project_id,
            "is_visible": true
        }
        """

        route = 'v1/projects/users/list/{0}/'.format(id)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_project_user_details(self, user_pk, data):
        """ Update the project user details 

        Keyword arguments:
        user_pk -- pk of the user
        data -- content of the update:
        {
            "hours_actual": 10,
            "is_billable": False
        }
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project_user(self, user_pk):
        """ Delete the project user

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_tags_groups_list(self):
        """ Get the list of groups of project tags """

        route = 'v1/projects/tags/groups/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_project_tags_group(self, data):
        """ Create a new group of project tags

        Keywords arguments:
        data -- data of the new group to be created:
        {
            "name": "New group",
            "tags": [
                tag_pk,
                ...
            ]
        }
        """

        route = 'v1/projects/tags/groups/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_project_tags_group_details(self, group_pk):
        """ Get the details about the group of project tags

        Keywords arguments:
        group_pk -- pk of the group of project tags
        """

        route = 'v1/projects/tags/groups/{0}/'.format(group_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_project_tags_group_details(self, group_pk, data):
        """ Update the group

        Keywords arguments:
        group_pk -- pk of the group of project tags
        data -- content of the update:
        {
            "name": "New group name",
            "tags": [
                tag_pk,
                ...
            ]
        }
        """

        route = 'v1/projects/tags/groups/{0}/'.format(group_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project_tags_group_details(self, group_pk):
        """ Delete the group of project tags 

        Keywords arguments:
        group_pk -- pk of the group of project tags
        """

        route = 'v1/projects/tags/groups/{0}/'.format(group_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_project_tags_list(self):
        """ Get the list of tags """

        route = 'v1/projects/tags/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_project_tag(self, data):
        """ Create a new tag 

        Keywords arguments:
        data -- content of the tag to be created:
        {
            "name": "new tag", (required)
            "group": group_id, (optional)
            "projects": [project_id, project_id, ...] (optional) # list of projects to add the tag
        }
        """

        route = 'v1/projects/tags/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_project_tag_details(self, tag_pk):
        """ Get project tag details 

        Keywords arguments:
        tag_pk -- pk of the tag
        """
        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_project_tag_details(self, tag_pk, data):
        """ Update project tag details 

        Keywords arguments:
        tag_pk -- pk of the tag
        data -- content of the update:
        {
            "name": "new name",
            "projects": [project_id, project_id, ...]
        }
        """

        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_project_tag(self, tag_pk):
        """ Delete project tag 

        Keywords arguments:
        tag_pk -- pk of the tag to be deleted
        """

        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Orgusers ####

    def get_orgusers_list(self):
        """ Get the list of users in the organization """

        route = 'v1/orgusers/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_orgusers_count(self):
        """ Get only the number of orguser inside the organization """

        route = 'v1/orgusers/count/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def export_orgusers_list(self):
        """ Export the list of orgusers as a .xls file """

        route = 'v1/orgusers/export/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        xls_file = open('orgusers_list.xls', 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def invite_orguser(self, pk, team_pk):
        """ Send an invitation to the orguser

        Keywords arguments:
        pk -- pk of the orguser
        team_pk -- pk of the team
        """

        route = 'v1/orgusers/invite/'
        data = {
            'orguser': pk,
            'team': team_pk
        }
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_orguser_details(self, pk):
        """ Get the orguser details

        Keyword arguments:
        pk -- pk of the orguser
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_orguser(self, data):
        """ Create a new user in the organization 

        data -- content of the orguser to be created:
        {
            "email": "testk@email.com",
            "first_name": "Julien",
            "last_name": "DUPUIS",
            "role": role_pk
            "timeoff_validators": [],
            "time_validators": [],
            "expenses_validators": [],
            "tags": []
        }
        """

        route = 'v1/orgusers/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_orguser_details(self, pk, data):
        """ Update the orguser details 

        Keywords arguments:
        pk -- pk of the orguser to update
        data -- content of the update:
        {
            "mobile": "012345678",
            "birthday": "16-04-2021"
        }
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_orguser(self, pk):
        """ Delete the orguser 

        Keyword arguments:
        pk -- pk of the orguser to update
        """

        route = 'v1/orgusers/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Organizations ####

    def get_user_organization_details(self):
        """ Returns short user information and orgs/teams/projects he is member of """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_organization_metrics(self):
        """ Get the admin dashboard metrics """

        route = 'v1/organizations/metrics/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_organization_details(self, pk):
        """ Get organizations details 

        Keywords arguments:
        pk -- pk of the organizaton
        """

        route = 'v1/organizations/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_organization_details(self, data):
        """ Update organizations details 

        Keywords arguments:
        data - content of the update:
        {
            "name": "string",
            "company_code": "string",
            "address": "string",
            "postal_code": "string",
            "city": "string",
            "province": "string",
            "country": "string",
            "currency": 0,
            "banks": [
                "string"
            ],
            "logo": "string",
            "days_invoices_past_due": 0,
            "fees_enabled": true,
            "hours_enabled": true,
            "expenses_enabled": true,
            "blog_enabled": true,
            "contacts_enabled": true,
            "validation_enabled": true,
            "invoicing_enabled": true,
            "reports_enabled": true,
            "files_enabled": true,
            "deliverables_enabled": true,
            "ffne_enabled": true,
            "budgets_enabled": true,
            "finance_enabled": true,
            "tasks_enabled": true,
            "leads_enabled": true,
            "suppliers_enabled": true,
            "personnel_enabled": true,
            "freelancers_enabled": true,
            "task_estimates_enabled": true,
            "plan": "string",
            "interval": "string",
            "team_level_invoice_increment": true,
            "plan_code_format": "string",
            "can_customize_invoice_codes": true,
            "default_vacation_type": 0,
            "slug": "string",
            "projections_enabled": true,
            "insourcing_projections_enabled": true,
            "invoice_increment_start": 0,
            "accounting_period": "string",
            "promo_code": "string",
            "invoice_separator": "string",
            "can_manage_vat": true,
            "custom_fields_enabled": true,
            "custom_fields_limit": 0,
            "multi_client_billing_enabled": true,
            "client_groups_enabled": true,
            "trips_enabled": true,
            "billable_calculation": "string",
            "org_size": "string",
            "org_type": "string",
            "invoice_email_from": "string",
            "invoice_email_from_display": "string",
            "revenue_adjustment_enabled": true,
            "resources_use_active_users": true,
            "availability_enabled": true,
            "availability_analytics_enabled": true,
            "smtp_enabled": true,
            "contractors_enabled": true,
            "contractor_invoicing_enabled": true,
            "subcontractor_planning_enabled": true,
            "public_indices_enabled": true,
            "annex_revisions_enabled": true,
            "display_project_id": true,
            "week_structure_configs_enabled": true,
            "validate_weeks_automatically": true,
            "close_weeks_automatically": true,
            "split_recuperation": true,
            "default_week_start_day": "string",
            "timeoff_balances_enabled": true,
            "exceptional_timeoff": true,
            "partial_balance_accumulation_enabled": true,
            "continous_credit_note_code": true,
            "use_calculated_overtime": true,
            "show_project_status": true,
            "forecast_rules_enabled": true,
            "mandate_fees_enabled": true,
            "show_cost_exports": true,
            "timeoff_drafts_enabled": true,
            "managed_contracts_enabled": true,
            "treatment_enabled": true,
            "show_contractor_ibans": true,
            "accounting_exports_enabled": true,
            "deduct_direct_subcontractors": true,
            "invoice_followups_enabled": true,
            "production_revenue_enabled": true,
            "with_unallocated_payroll": true
        }
        """
        route = 'v1/organizations/{0}/'.format(self.org_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def __get_teams(self):
        """ Set the organization id of the user """

        route = 'v1/organizations/membership/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        organizations = json.loads(response.content)['organizations']
        selected_organization = next((org for org in organizations if org.get('id') == self.org_pk), None)
        teams = selected_organization['teams']
        # teams = json.loads(response.content)['organizations'][0]['teams']
        self.teams_pk = []
        for team in range(len(teams)):
            self.teams_pk.append({key: teams[team][key] for key in ('id', 'title')})
        return response.status_code

    #### Permissions ####

    def get_permissions_list(self):
        """ Get the list of permissions sets """

        route = 'v1/permissions/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_permissions(self, data):
        """ Create a new set of permissions

        Keywords arguments:
        data -- content of the permissions set to be created:
        {
            "name": "Consultant", (required)
            "name_en": "Consultant",
            "name_fr": "Consultant",
            "level": "project",
            "all_permissions": true,
            "is_default": true,
            "permissions": [
                id,
                ...
            ]
        }
        """

        route = 'v1/permissions/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_permissions_map(self):
        """ Return a dictionary with request.user permissions by level """

        route = 'v1/permissions/map/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_permissions_details(self, id):
        """ Get permissions set details

        Keywords arguments:
        id -- id of the permissions set
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_permissions_details(self, id, data):
        """ Update permissions set details

        Keywords arguments:
        id -- id of the permissions set
        data -- content of the update:
        {
            "name": "Boss",
            "name_en": "Boss",
            "name_fr": "Patron",
            "level": "organization",
            "all_permissions": true,
            "is_default": true,
            "permissions": [
                id,
                ...
            ]
        }
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_permissions(self, id):
        """ Delete permissions set

        Keywords arguments:
        id -- id of the permissions set
        """

        route = 'v1/permissions/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Profile ####

    def __get_selected_org(self):
        """ Get the organization selected on user profile
        """

        route = 'v1/profiles/profile/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        self.org_pk = json.loads(response.content)['selected_org']
        return self.process_response(response)

    def get_profile_preferences(self):
        """ Get profile preferences """

        route = 'v1/profiles/preferences/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_profile_details(self):
        """ Get current profile details """

        route = 'v1/profiles/profile/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_profile_details(self, data):
        """ Update current profile details 

        Keywords arguments:
        data -- content of the update:
        {
            "locale": "en",
            "show_sidemenu": False
        }
        """

        route = 'v1/profiles/profile/'
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    #### Team #####

    def get_teams_list(self):
        """ Get the list of teams """

        route = 'v1/teams/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)  # no 'results' key

    def get_teams_access_list(self):
        """ Get teams orguser has or has not access to """

        route = 'v1/teams/list/access/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_team(self, data):
        """ Create a new team 

        Keywords arguments:
        data -- content of the team to be created:
        {
            "name": "Beta", (required)
            "currency": currency_pk,
            "city": "Paris",
            "address": "6 Rue de la rue",
            "banks": [
                bank_id
            ]
        }
        """

        route = 'v1/teams/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_team_users_list(self, pk):
        """ Get the list of users in the team 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/users/list/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def add_team_user(self, pk, data):
        """ Add a user to a team

        Keywords arguments:
        pk -- pk of the team where to add the user
        data -- details about the user to add (pk, permissionsset, role, ...):
        {
            "orguser": orguser_pk,
            "permissionsset: permissionsset_pk,
            "role": role_pk
            "team": team_pk
        }
        """

        route = 'v1/teams/users/list/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def add_team_user_to_multiple_projects(self, data):  # Error 500
        """ Add a user to multiple teams at once

        Keywords arguments:
        data -- pk of the projects and pk of the orguser to add :
        {
            "orguser": orguser_pk,
            "teams": [

            ]
            "projects": [
                project_id,
                ...
            ]
        }
        """

        route = 'v1/teams/users/bulk/add/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def remove_team_user_to_multiple_projects(self, data):  # Error 500
        """ Remove a user from multiple teams at once

        Keywords arguments:
        data -- pks of the projects and pk of the orguser to remove :
        {
            "orguser": orguser_pk,
            "projects": [
                project_id,
                ...
            ]
        }
        """

        route = 'v1/teams/users/bulk/delete/{0}/'.format(self.org_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_team_user_details(self, user_pk):  # same thing as get_orguser_details ?
        """ Get the orguser details related to the team he is in

        Keywords arguments:
        user_pk -- pk of the team user
        """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_team_user_details(self, user_pk, data):
        """ Update the orguser details related to the team he is in

        Keywords arguments:
        user_pk -- pk of the team user
        data -- content of the update:
        {
            "permissionsset": 16464,
            "team": team_pk
        }
        """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def remove_team_user(self, user_pk):
        """ Delete a user from the team """

        route = 'v1/teams/users/{0}/'.format(user_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_team_details(self, pk):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_team_details(self, pk, data):
        """ Get the team details 

        Keywords arguments:
        pk -- pk of the team
        data -- content of the update:
        {
            "city": "Lyon",
            "address": "2 Avenue du Trône"
        }
        """

        route = 'v1/teams/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

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

        if response.content == b'{"non_field_errors":["Unable to log in with provided credentials."]}':
            print('Unable to log with provided credentials. Please modify your .ENV file.')
            sys.exit('Authentication failed.')

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
