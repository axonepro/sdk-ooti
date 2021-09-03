import requests
import json

from .helper import Helper

"""
- Celery tasks:
    - ERROR 403 v1/celery_tasks/last/ 
    - ERROR 404 v1/celery_tasks/last/{org_pk}/

- Imports:
    - ERROR 403 : GET v1/imports/counts/
    - ERROR 400 ("Type is required"): GET & POST v1/imports/import/{org_pk}/
    - POST on v1/imports/{id}/map-columns/ ?

"""


class Settings(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Actions ####

    def get_actions_list(self, page=1):
        """ Get the list of actions """

        route = 'v1/actions/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
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

    def get_celery_tasks_list(self, page=1):
        """ Get the list of celery tasks """

        route = 'v1/celery_tasks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Customfields ####

    def get_customfields_list(self, page=1):
        """ Get the list of customfields """

        route = 'v1/customfields/field/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_customfield(self, data):  # Error 500
        """ Create a new customfield 

        Keywords arguments:
        data -- data of the new field to be created:
        {
            "content_type": "project", # REQUIRED
            "name": "string",  # REQUIRED
            "field_type": "t",  # REQUIRED
            "default_value": "string",
            "is_required": false,
            "admin_only": false,
            "permissionssets": [
                permissions_pk,
                ...
            ],
            "permissionssets_can_edit": [
                permissions_pk,
                ...
            ]
        }

        field_type:
        "t" --> Text
        "i" --> Integer
        "a" --> Large Text Field
        "f" --> Floating point decimal
        "d" --> Date

        content_type
        "contact" --> Contact
        "project" --> Project
        "orguser" --> OrgUser

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

    def get_imports_count(self):  # Error 403
        """ Get the number of imports """

        route = 'v1/imports/counts/'
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_exports_list(self, page=1):
        """ Get the list of exports """

        route = 'v1/imports/export/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
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

    def get_imports_list(self, page=1):
        """ Get the list of imports """

        route = 'v1/imports/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_import(self, data):
        """ Create a new import

        Keywords arguments:
        data -- data of the new import to be created:
        {
            "data": {

            } 
            "type":
        }
        """

        route = 'v1/imports/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_import_details(self, id):
        """ Get the import details

        Keywords arguments:
        id -- id of the import
        """

        route = 'v1/imports/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_import_details(self, id, data):
        """ Update the import details

        Keywords arguments:
        id -- id of the import
        data -- content of the update
        """

        route = 'v1/imports/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_import(self, id):
        """ Delete the import 

        Keywords arguments:
        id -- id of the import
        """

        route = 'v1/imports/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Inbound emails ####

    def get_inbound_emails_list(self, page=1):
        """ Get the list of inbound emails """

        route = 'v1/inbound_emails/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_inbound_email(self, data):
        """ Create a new inbound email

        Keywords arguments:
        data -- data of the new inbound email to be created:
        {
            "project": project_id, (required)
            "invoice": invoice_pk,,
            "received_at": "string",
            "to_address": "string",
            "from_address": "string",
            "reply_to_address": "string",
            "cc_address": "string",
            "bcc_address": "string",
            "subject": "string",
            "body": "string"
        }
        """

        route = 'v1/inbound_emails/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_inbound_email_details(self, id):
        """ Get the inbound email details

        Keywords arguments:
        id -- id of the inbound email
        """

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_inbound_email_details(self, id, data):
        """ Update the inbound email details

        Keywords arguments:
        id -- id of the inbound email
        data -- content of the update:
        {
            "project": project_id,
            "invoice": invoice_pk,
            "received_at": "string",
            "to_address": "string",
            "from_address": "string",
            "reply_to_address": "string",
            "cc_address": "string",
            "bcc_address": "string",
            "subject": "string",
            "body": "string"
        }
        """

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_inbound_email(self, id):
        """ Delete the inbound email

        Keywords arguments:
        id -- id of the inbound email
        """

        route = 'v1/inbound_emails/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Tags ####

    def get_tags_list(self, page=1):
        """ Get the list of tags """

        route = 'v1/tags/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_tag(self, data):
        """ Create a new tag 

        Keywords arguments:
        data -- data of the new tag to be created:
        {
            "name": "string",
            "contacts": [
                contact_pk,
                ...
            ],
            "contractors": [
                contractor_pk
            ],
            "clients": [
                client_pk,
                ...
            ],
            "orgusers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tags/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_tag_details(self, id):
        """ Get the tag details

        Keywords arguments:
        id -- id of the tag
        """

        route = 'v1/tags/{0}/'.format(id)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_tag_details(self, id, data):
        """ Update the tag details

        Keywords arguments:
        id -- id of the tag
        data -- content of the update:
        {
            "name": "string",
            "contacts": [
                contact_pk,
                ...
            ],
            "contractors": [
                contractor_pk
            ],
            "clients": [
                client_pk,
                ...
            ],
            "orgusers": [
                orguser_pk,
                ...
            ]
        }
        """

        route = 'v1/tags/{0}/'.format(id)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_tag(self, id):
        """ Delete the tag

        Keywords arguments:
        id -- id of the tag
        """

        route = 'v1/tags/{0}/'.format(id)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
