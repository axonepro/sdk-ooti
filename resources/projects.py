import requests
import json

from .helper import Helper


class Projects(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO POST on /api/v1/projects/actions/{org_pk}/

    def get_project_available_clients(self, id):
        """ Get the list of clients avalaible (clients that are not already participating in the project)
        Return the list of clients with their display name and pk

        Keywords arguments:
        id -- the id of the project
        """

        route = 'v1/projects/available-clients/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_projects_list_deliverables(self):
        """ Get the list of projects and their associated deliverables where the current user is a member of """

        route = 'v1/projects/deliverables/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def export_projects_list(self):
        """ Export the list of projects as a .xls file """

        route = 'v1/projects/export/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        xls_file = open('projects_list.xls', 'wb')
        xls_file.write(response.content)
        xls_file.close()
        return self.process_response(response)

    def get_project_fee_summary(self, id):
        """ Get the project fee summary

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/fee-summary/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/projects/leads2/{org_pk}/

    # TODO GET on /api/v1/projects/leads2/{org_pk}/{team_pk}/

    def get_project_list_access(self):
        """ ? """

        route = 'v1/projects/list/access/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_access_projects_list(self):  # WARNING same function as above

        route = 'v1/projects/list/access/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_projects_list(self, team_pk=None):
        """ Get the projects list 

        Keywords arguments:
        team_pk -- pk of a team to get the project list of a specific team
        """

        route = 'v1/projects/list/{0}/'.format(self.org_pk)
        if team_pk is not None:
            route += '{0}/'.format(team_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    # TODO GET on /api/v1/projects/list/{org_pk}/{team_pk}/

    # TODO POST on /api/v1/projects/list/{org_pk}/{team_pk}/

    # TODO GET on /api/v1/projects/project_timeline/{org_pk}/

    # TODO GET on /api/v1/projects/projects-dashboard/{org_pk}/

    # TODO GET on /api/v1/projects/projects-dashboard/{org_pk}/{team_pk}/

    def get_project_revenue(self, id):
        """ Get the list of project revenues by years and by months

        Keywords arguments:
        id -- the id of the project
        """
        route = 'v1/projects/revenue/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_project_tags_groups_list(self):
        """ Get the list of groups of project tags """

        route = 'v1/projects/tags/groups/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_project_tags_group_details(self, group_pk):
        """ Get the details about the group of project tags

        Keywords arguments:
        group_pk -- pk of the group of project tags
        """

        route = 'v1/projects/tags/groups/{0}/'.format(group_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_project_tags_group_details(self, group_pk):
        """ Delete the group of project tags 

        Keywords arguments:
        group_pk -- pk of the group of project tags
        """

        route = 'v1/projects/tags/groups/{0}/'.format(group_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_project_tags_list(self):
        """ Get the list of tags """

        route = 'v1/projects/tags/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_project_tag_details(self, tag_pk):
        """ Get project tag details 

        Keywords arguments:
        tag_pk -- pk of the tag
        """
        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_project_tag(self, tag_pk):
        """ Delete project tag 

        Keywords arguments:
        tag_pk -- pk of the tag to be deleted
        """

        route = 'v1/projects/tags/{0}/'.format(tag_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO POST on /api/v1/projects/users/bulk/add/{org_pk}/

    # TODO DELETE on /api/v1/projects/users/bulk/delete/{org_pk}/

    # TODO GET on /api/v1/projects/users/list/

    # TODO POST on /api/v1/projects/users/list/

    # TODO POST on /api/v1/projects/users/list/action/

    def get_project_users_list(self, id):
        """ Get the list of users of a project 

        Keyword arguments:
        id -- the id of the project
        """

        route = 'v1/projects/users/list/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return {'status': response.status_code, 'data': json.loads(response.content)['results']}

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
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_project_user_details(self, user_pk):
        """ Get the project user details 

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_project_user(self, user_pk):
        """ Delete the project user

        Keyword arguments:
        user_pk -- pk of the user
        """

        route = 'v1/projects/users/{0}/'.format(user_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_project_details(self, id):
        """ Get the project details

        Keyword arguments:
        pk -- the pk of the project
        """

        route = 'v1/projects/{0}/'.format(id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
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
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_project(self, id):
        """ Delete a project

        Keyword arguments:
        id -- the id of the project
        """
        route = 'v1/projects/{0}/'.format(id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/projects/{id}/clients/split-matrix/

    # TODO GET on /api/v1/projects/{id}/setup_checklist/