import json

import requests

from .helper import Helper


class Reports(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    # TODO POST on /api/v1/reports/copy-as-custom/{project_pk}/

    def get_reports_list(self, page=1):
        """ Get the reports list """

        route = f'v1/reports/list/{self.org_pk}/?page_size={self.pagination}&page={page}'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_reports_project_list(self, project_pk, page=1):
        """ Get the reports list for a project """

        route = f'v1/reports/list/{self.org_pk}/?project={project_pk}&page_size={self.pagination}&page={page}'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_report_details(self, pk):
        """ Get the report details

        Keyword arguments:

        pk -- pk of the report
        """

        route = f'v1/reports/{pk}/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_report(self, data):
        """ Create a report

        Keyword arguments:

        data -- data to be created:
        {
            "name": "string", (required)
            "project": 0, (required)
            "type": "string", (required)
            "status": "string",
            "styleguide": 0,
            "lang": "string",
            "orientation": "string",
            "filter_team": 0,
            "footer_team": 0,
            "font_size": 0,
            "margin_left": 0,
            "margin_right": 0,
            "cover_body_template": "string",
            "report_body_template": "string",
            "use_cover_page": true,
            "year": 0,
            "date_range": "string",
            "is_custom_date_range": true,
            "start_date": "string",
            "end_date": "string",
            "phase": 0,
            "annex": 0,
            "orguser": 0,
            "scheduled_recipients": [
                "string"
            ],
            "scheduled_guests": "string",
            "scheduled_sent_at": "string",
            "scheduled_start_date": "string",
            "scheduled_next_date": "string",
            "scheduled_last_sent": "string",
            "scheduled_count": 0,
            "scheduled_frequency": 0,
            "hide_currency": true,
            "notes": "string"
        }

        Note: You can create a report without "type", but this will create a blank page.
        """
        route = f'v1/reports/list/{self.org_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_report(self, pk, data):
        """ Update a report

        Keyword arguments:

        pk -- pk of the report
        data -- data update:
        {
            "name": "string", (required)
            "styleguide": 0,
            "lang": "string",
            "orientation": "string",
            "footer_team": 0,
            "font_size": 0,
            "margin_left": 0,
            "margin_right": 0,
            "use_cover_page": true,
            "scheduled_recipients": [
                "string"
            ],
            "scheduled_start_date": "string",
            "scheduled_frequency": 0,
        }

        Note: You can create a report without "type", but this will create a blank page.
        """
        route = f'v1/reports/{pk}/'
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_report(self, pk):
        """ Delete a report

        Keyword arguments:

        pk -- pk of the report
        """
        route = f'v1/reports/{pk}/'
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def generate_report(self, data):
        """ Generate a report (report that is already created)

        Keyword arguments:

        data -- data to be created:
            {
                "pk": 0 (pk of the report),
                "project": 0 (project linked to the report)
            }
        """
        route = f'v1/reports/generate/{self.org_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_templates_list(self, team_pk, page=1):
        """ Get list of templates

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = f'v1/reports/templates/list/{team_pk}/?page_size={self.pagination}&page={page}'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def get_template_details(self, pk):
        """Get the template details

        Keyword arguments:

        pk -- pk of the template
        """

        route = f'v1/reports/templates/{pk}/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def create_template(self, team_pk, data):
        """ Create a template

        Keyword arguments:

        team_pk -- pk of the team
        data -- data create:
            {
                "name": "string", (required)
                "type": "string", (required: "proprosal" or "progress")
                "styleguide": 0,
                "lang": "string", (required: "fr", "en", "it")
                "orientation": "string", (portrait, landscape)
                "font_size": 0,
                "margin_top": 0,
                "margin_bottom": 0,
                "margin_left": 0,
                "margin_right": 0
            }
            """

        route = f'v1/reports/templates/list/{team_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def update_template(self, pk, data):
        """ Update a template

        Keyword arguments:

        pk -- pk of the template
        data -- data update:
            {
                "name": "string", (required)
                "type": "string", (required: "proprosal" or "progress")
                "styleguide": 0,
                "lang": "string", (required: "fr", "en", "it")
                "orientation": "string", (portrait, landscape)
                "font_size": 0,
                "margin_top": 0,
                "margin_bottom": 0,
                "margin_left": 0,
                "margin_right": 0
            }
            """

        route = f'v1/reports/templates/{pk}/'
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_template(self, pk):
        """ Delete a template

        Keyword arguments:

        pk -- pk of the template
         """

        route = f'v1/reports/templates/{pk}/'
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def duplicate_template(self, pk):
        """ Duplicate a template

        Keyword arguments:

        pk -- pk of the template
         """

        route = f'v1/reports/templates/duplicate/{pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # TODO GET on /api/v1/reports/variables/{id}/

    # TODO DELETE on /api/v1/reports/version/delete/{id}/