import requests
import json

from helper import Helper

"""
- Celery tasks:
    - ERROR 403 v1/celery_tasks/last/ 
    - ERROR 404 v1/celery_tasks/last/{org_pk}/

- Custom fields : needs a Pro subscription to create one
- Imports:
    - ERROR 403 v1/imports/counts/
    -

"""


class Settings(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers):
        self.base_url = base_url
        self.org_pk = org_pk
        self.teams_pk = teams_pk
        self.access_token = access_token
        self._csrf_token = _csrf_token
        self.headers = headers

    #### Actions ####

    def get_actions_list(self):
        """ Get the list of actions """

        route = 'v1/actions/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_actions_details(self, id):
        """ Get the action details

        Keywords arguments:
        id -- id of the action
        """

        route = 'v1/actions/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Billing ####

    def cancel_subscription(self):  # return 200
        """ Cancel subscription """

        route = 'v1/billing/cancel-subscription/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_billing_card(self):
        """ Update payment method """

        route = 'v1/billing/card/{0}/'.format(self.org_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_billing_card(self):
        """ Delete payment method """

        route = 'v1/billing/card/{0}/'.format(self.org_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def reactivate_subscription(self):  # return 200
        """ Reactivate subscription """

        route = 'v1/billing/reactivate-subscription/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_subscription(self):
        """ Change subscription """

        route = 'v1/billing/update-subscription/{0}/'.format(self.org_pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Celery tasks ####

    def get_last_celery_task(self):
        """ """

        route = 'v1/celery_tasks/last/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_celery_tasks_list(self):
        """ Get the list of celery tasks """

        route = 'v1/celery_tasks/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Customfields ####

    def get_customfields_list(self):
        """ Get the list of customfields """

        route = 'v1/customfields/field/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_customfield(self, data):
        """ Create a new customfield 

        Keywords arguments:
        data -- data of the new field to be created:
        {
            "name": "string",
            "field_type": "t",
            "default_value": "string",
            "is_required": false,
            "admin_only": false,
            "permissionssets: [
                permissionsset_pk,
                ...
            ],
            "permissionssets_can_edit: [
                permissionsset_pk,
                ...
            ]
        }

        field_type:
        "t" --> Text
        "i" --> Integer
        "a" --> Large Text Field
        "f" --> Floating point decimal
        "d" --> Date
        """

        route = 'v1/customfields/field/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_customfield_details(self, pk):
        """ Get the customfield details 

        Keywords arguments:
        pk -- pk of the customfield
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_customfield_details(self, pk, data):
        """ Update the customfield details 

        Keywords arguments:
        pk -- pk of the customfield
        data -- data of the new field to be created:
        {
            "name": "string",
            "field_type": "t",
            "default_value": "string",
            "is_required": false,
            "admin_only": false,
            "permissionssets: [
                permissionsset_pk,
                ...
            ],
            "permissionssets_can_edit: [
                permissionsset_pk,
                ...
            ]
        }
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_customfield(self, pk):
        """ Delete the customfield 

        Keywords arguments:
        pk -- pk of the customfield
        """

        route = 'v1/customfields/field/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Imports ####

    def get_imports_count(self):
        """ Get the number of imports """

        route = 'v1/imports/counts/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_exports_list(self):
        """ Get the list of exports """

        route = 'v1/imports/export/list/{0}/'.format(self.org_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_export(self, data):
        """ Get imports list

        Keywords arguments
        data -- data of the new import to be created:
        {
            "orguser": orguser_pk,
            "team": team_pk,
            "project": project_id,
            "type": "string",
            "items": 0,
            "started_processing_at": "string",
            "ended_processing_at": "string",
            "include_documents": true
        }
        """

        route = 'v1/imports/export/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_export_details(self, export_pk):
        """ Get the export details 

        Keywords arguments:
        export_pk -- pk of the export
        """

        route = 'v1/imports/export/{0}/'.format(export_pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_export(self, export_pk):
        """ Delete the export

        Keywords arguments:
        export_pk -- pk of the export
        """

        route = 'v1/imports/export/{0}/'.format(export_pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Inbound emails ####

    #### Tags ####
