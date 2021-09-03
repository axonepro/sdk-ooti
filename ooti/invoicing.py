import requests
import json

from .helper import Helper


class Invoicing(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    #### Invoices ####

    def get_invoice_details(self, pk):
        """ Get the invoice details

        Keyword arguments:

        pk -- the pk of the invoice
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_invoices_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_invoices_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_invoice(self, pk, data):
        """Create an invoice

        Keyword arguments:

        pk -- the pk of the invoice
        data -- data create:
            {
                "invoice_date": "DD-MM-YYYY",
                "billing_option": 0,
                "bank": 0,
                "purchase_order": "string",
                "references": "string",
                "is_valid": Boolean,
                "is_sent": Boolean,
                "multi_tax_enabled": Boolean(if invoice items have multi tax rates)
            }
        """

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def create_invoice(self, team_pk, data):
        """Create an invoice
        Keyword arguments:
        team_pk -- the pk of the team
        data -- data create:
            {
                "project": 0,
                "type": 0,
                "invoice_date": "DD-MM-YYYY",
                "due_date": "DD-MM-YYYY"
                "client_name": "string",
                "client_address": "string",
                "references": "string"
                "team": 0
            }

            Note that for type 4 (other), project is not mandatory
        """

        route = 'v1/invoices/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def validate_invoice(self, pk):
        """Validate an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_valid": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def send_invoice(self, pk):
        """Send an invoice
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_sent": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def cancel_invoice(self, pk):
        """Cancel an invoice and create a credit note
        Keyword arguments:
        pk -- the pk of the invoice
        """
        data = {"is_closed": True}

        route = 'v1/invoices/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))

        if(response.status_code == 200):
            response_data = json.loads(response.content)
            credit_note_pk = response_data['credit_note_url'].split('/')[4]
            return {'status': response.status_code, 'data': credit_note_pk}

        return self.process_response(response)

    def get_invoice_items(self, pk, page=1):
        """ Get invoice's items

        Keyword arguments:

        pk -- invoice pk
        """

        route = 'v1/invoices/items/{0}/?page_size={1}&page={2}'.format(pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_invoice_item(self, pk, data):
        """ Create invoice's item

        Keyword Arguments:

        pk -- pk of the invoice
        data -- data create:
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0,
                "tax_rate": 0.0 (if invoice.multi_tax_rate=True)
                "tax": 0.0 (tax amount, if invoice.multi_tax_rate=True)
            }
        """

        route = 'v1/invoices/items/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_invoice_item(self, pk, data):
        """ Update invoice's item

        Keyword Arguments:

        pk -- pk of the item
        data -- data update:
            {
                "descritpion": "string" (title of the item),
                "subtitle": "string" (description of the item),
                "amount": 0
            }
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_invoice_item(self, pk):
        """ Update invoice's item

        Keyword Arguments:

        pk -- pk of the item
        """

        route = 'v1/invoices/item/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Credit notes ####

    def get_credit_notes_list(self, page=1):
        """ Get the invoice list """

        route = 'v1/invoices/list/{0}/?page_size={1}&page={2}&type=9'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_credit_notes_sent_valid_list(self, team_pk, page=1):
        """ Get the sent and valid invoice list

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/invoices/list/{0}/?team={1}&page_size={2}&page={3}&q=&is_sent=true&is_valid=true&type=9'.format(
            self.org_pk, team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    #### Payments ####

    def get_payment_details(self, pk):
        """ Get the payment details

        Keyword arguments:

        pk -- the pk of the payment
        """

        route = 'v1/payments/{0}'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def get_payments_list(self, page=1):
        """Get the payment list"""

        route = 'v1/payments/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def update_payment(self, pk, data):
        """Create an payment

        Keyword arguments:

        pk -- the pk of the payment
        data -- data create:
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "currency_rate": 0,
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk)
            }
        """

        route = 'v1/payments/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_payment_invoice(self, pk, data):
        """ Update payment's amount on invoice

        Please do not call this function before update_payment.
        To make an update on a payment, first use the "update_payment" method.
        Then, update the amount on the invoice with this method.

        Keyword arguments:

        pk -- pk of payment
        data -- data update:
            {
                "amount": 0
            }
        """
        route = 'v1/payments/invoice/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def create_payment(self, team_pk, data):
        """Create an payment

        Keyword arguments:

        team_pk -- the pk of the team
        data -- data create:
            {
                "date": "DD-MM-YYYY",
                "amount": 0,
                "currency": "string" (currency_pk),
                "type": "string",
                "invoice": "string" (invoice_pk)
                "team": "string" (team_pk),
                "project": "string" (project_pk)(no need of project for invoices of type 4)
            }
        """

        route = 'v1/payments/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}'.format(team_pk)
        response = requests.post('{0}{1}{2}'.format(self.base_url, route, parameters),
                                 headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    ##### Clients #####

    def get_clients_list(self, team_pk, page=1):
        """Get the clients list

        Keyword arguments:

        pk -- the pk of the team
        """

        route = 'v1/clients/list/{0}/'.format(self.org_pk)
        parameters = '?team={0}&page_size={1}&page={2}'.format(team_pk, self.pagination, page)

        response = requests.get('{0}{1}{2}'.format(self.base_url, route, parameters), headers=self.headers)
        return self.process_response(response, True)

    def get_clients_details(self, pk):
        """Get the client details

        Keyword arguments:

        pk -- the pk of the client
        """

        route = 'v1/clients/{0}/'.format(pk)

        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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

        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
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

        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_client(self, pk):
        """ Delete client

        Keyword arguments:

        pk -- pk of the client
        """
        route = 'v1/clients/{0}/'.format(pk)

        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ##### Currencies #####

    def get_currencies_list(self, page=1):
        """Get the currencies list """

        route = 'v1/currencies/list/?page_size={0}&page={1}'.format(self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_currency_details(self, pk):
        """ Get the currency details

        Keyword arguments:

        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_currency(self, pk):
        """ Delete a currency
        Keyword arguments:
        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_currency(self, data):
        """ Create a currency

        Keyword arguments:

        data -- data create, required fields:
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }
        """

        route = 'v1/currencies/list/'
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_currency(self, pk, data):
        """ Update a currency

        Keyword arguments:

        data -- data create, required fields:
            {
                "name": "string",
                "longname": "string",
                "decimal_points": 0,
                "symbol": "string"
            }

        pk -- the pk of the currency
        """

        route = 'v1/currencies/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers,
                                  data=json.dumps(data))

        return self.process_response(response)

    #### Emails ####

    ### Classic ###

    def get_emails_list(self, page=1):
        """ Get the emails list """

        route = 'v1/emails/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_email_details(self, pk):
        """ Get the email details

        Keyword arguments:

        pk -- the pk of the email
        """
        route = 'v1/emails/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_email(self, data):
        """ Create an email

        Keyword arguments:

        data -- data create, fields:
            {
                "team": 0,
                "name": "string", (name of the template)
                "type": "", ('invoice', 'followup' or 'contractor_notification')
                "email_to": "string",
                "email_from": "string",
                "name_from": "string",
                "email_cc": "string",
                "email_bcc": "string",
                "email_subject": "string",
                "email_body": "string",
                "smtp_setting": 0,
                "projects": [],
                "invoices": []
            }

        Note that there is no required fields to create the email template.
        """

        route = 'v1/emails/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_email(self, pk, data):
        """ Update an email

        Keyword arguments:

        pk -- the pk of the email template
        data -- data create, fields:
            {
                "team": 0,
                "name": "string", (name of the template)
                "type": "", ('invoice', 'followup' or 'contractor_notification')
                "email_to": "string",
                "email_from": "string",
                "name_from": "string",
                "email_cc": "string",
                "email_bcc": "string",
                "email_subject": "string",
                "email_body": "string",
                "smtp_setting": 0,
                "projects": [],
                "invoices": []
            }

        Note that there is no required fields to create the email template.
        """

        route = 'v1/emails/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_email(self, pk):
        """Delete an email

        Keyword arguments:

        pk -- pk of the email
        """
        route = 'v1/emails/{0}'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def send_test_email(self, pk):
        """ Send test email to the email of the account

        Keyword arguments:

        pk -- the pk of the email template
        """

        route = 'v1/emails/{0}/send-test/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def apply_email(self, pk):
        """ Apply the template to related projects and unsent invoices

        Keyword arguments:

        pk -- pk of the email template
        """
        route = 'v1/emails/{0}/apply/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### smtp ###

    def get_emails_smtp_list(self, page=1):
        """ Get the emails smtp list """

        route = 'v1/emails/smtp/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_email_smtp_details(self, pk):
        """ Get the email smtp details

        Keyword arguments:

        pk -- the pk of the email smtp
        """

        route = 'v1/emails/smtp/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_email_smtp(self, data):
        """ Create an email smtp

        Keyword Arguments:

        data -- data create: fields:
           {
               "from_name": "string",
               "from_email": "string",
               "username": "string",
               "password": "string",
               "protocol": "TLS" or "SSL",
               "host": "string",
               "port": 0
           }
        """
        route = 'v1/emails/smtp/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_email_smtp(self, pk, data):
        """ Update an email smtp

        Keyword arguments:

        pk -- the pk of the email smtp
        data -- data create: fields:
           {
               "from_name": "string",
               "from_email": "string",
               "username": "string",
               "password": "string",
               "protocol": "TLS" or "SSL",
               "host": "string",
               "port": 0
           }
        """

        route = 'v1/emails/smtp/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_email_smtp(self, pk):
        """ Delete an email smtp

        Keyword arguments:

        pk -- pk of the email smtp
        """
        route = 'v1/emails/smtp/{0}'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def send_test_email_smtp(self, pk):
        """ Verify the status of the smtp

        Keyword arguments:

        pk -- the pk of the email template
        """

        route = 'v1/emails/smtp/{0}/send-test/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Files ####

    ### Folders ###

    def get_folder_list(self, project_pk, page=1):
        """ Get the folder list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/files/folder/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_folder_details(self, pk):
        """ Get the folder details

        Keyword arguments:

        pk -- pk of the folder
        """

        route = 'v1/files/folder/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_folder(self, project_pk, data):
        """ Create a folder

        Keyword arguments:

        project_pk -- pk of the project
        data -- data to be created:
            {
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "parent": 0
            }
        """
        route = 'v1/files/folder/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_folder(self, pk, data):
        """ Update a folder

        Keyword arguments:

        pk -- pk of the folder
        data -- data to be updated:
            {
                "name": "string",
                "name_en": "string",
                "name_fr": "string",
                "parent": 0
            }
        """
        route = 'v1/files/folder/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_folder(self, pk):
        """ Delete a folder

        Keyword arguments:

        pk -- pk of the folder
        """
        route = 'v1/files/folder/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    ### Files ###

    def get_files_list(self, project_pk, page=1):
        """ Get the files list

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/files/list/{0}/?page_size={1}&page={2}'.format(project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_file(self, project_pk, data):
        """ Create a file 

        Keyword arguments:

        project_pk -- pk of the project
        """

        route = 'v1/files/list/{0}/'.format(project_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response, True)

    def get_file_details(self, pk):
        """ Get the file details

        Keyword arguments:

        pk -- pk of the file
        """

        route = 'v1/files/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def delete_file(self, pk):
        """ Delete a file

        Keyword arguments:

        pk -- pk of the file
        """

        route = 'v1/files/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Banks ####

    def get_banks_list(self, page=1):
        """ Get the banks list """

        route = 'v1/banks/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_bank_details(self, pk):
        """ Get the bank details

        Keyword arguments:

        pk -- pk of the bank
        """

        route = 'v1/banks/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_bank(self, data):
        """ Create a bank

        Keyword arguments:

        data -- data to be created:
            {
                "name": "string",
                "currency": 0,
                "country": "string",
                "iban": "string",
                "bic": "string",
                "rib": "string",
                "teams": ["string"]
                "projects": ["string"]
            }
        """
        route = 'v1/banks/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_bank(self, pk, data):
        """ Update a bank

        Keyword arguments:

        data -- data to be created:
            {
                "name": "string",
                "currency": 0,
                "country": "string",
                "iban": "string",
                "bic": "string",
                "rib": "string",
                "teams": ["string"]
                "projects": ["string"]
            }
        """
        route = 'v1/banks/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_bank(self, pk):
        """ Create a bank

        Keyword arguments:

        pk -- pk of the bank
        """
        route = 'v1/banks/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Reports ####

    ### Reports ###

    def get_reports_list(self, page=1):
        """ Get the reports list """

        route = 'v1/reports/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_reports_project_list(self, project_pk, page=1):
        """ Get the reports list for a project """

        route = 'v1/reports/list/{0}/?project={1}&page_size={2}&page={3}'.format(
            self.org_pk, project_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_report_details(self, pk):
        """ Get the report details

        Keyword arguments:

        pk -- pk of the report
        """

        route = 'v1/reports/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        route = 'v1/reports/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
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
        route = 'v1/reports/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_report(self, pk):
        """ Delete a report

        Keyword arguments:

        pk -- pk of the report
        """
        route = 'v1/reports/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
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
        route = 'v1/reports/generate/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    ### Reports Templates ###

    def get_templates_list(self, team_pk, page=1):
        """ Get list of templates

        Keyword arguments:

        team_pk -- pk of the team
        """

        route = 'v1/reports/templates/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_template_details(self, pk):
        """Get the template details

        Keyword arguments:

        pk -- pk of the template
        """

        route = 'v1/reports/templates/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
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

        route = 'v1/reports/templates/list/{0}/'.format(team_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
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

        route = 'v1/reports/templates/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_template(self, pk):
        """ Delete a template

        Keyword arguments:

        pk -- pk of the template
         """

        route = 'v1/reports/templates/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def duplicate_template(self, pk):
        """ Duplicate a template

        Keyword arguments:

        pk -- pk of the template
         """

        route = 'v1/reports/templates/duplicate/{0}/'.format(pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Revenue ####
    def get_revenue_list(self, page=1):
        """ Get the revenue list """

        route = 'v1/revenue/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_revenue_details(self, pk):
        """ Get the revenue details

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_revenue(self, data):
        """ Create a revenue

        Keyword arguments:

        data -- data create:
            {
                "amount_actual": 0,
                "amount_budgeted": 0,
                "description": "string",
                "type": "string",
                "month": 0,
                "title": "string",
                "year": 0,
                "team": 0,
                "project": 0,
                "months": [
                    "string"
                ]
            }
        """

        route = 'v1/revenue/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_revenue_month_list(self, page=1):
        """ Get the revenue month list """

        route = 'v1/revenue/month/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def create_revenue_month(self, data):
        """ Create a revenue month

        Keyword arguments:

        data -- data create:
        {
            "revenue_adjustment": 0,
            "team": 0,
            "project": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/revenue/month/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def get_revenue_month_details(self, pk):
        """Get the revenue month details

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_revenue_month(self, pk, data):
        """ Update a revenue month

        Keyword arguments:

        pk -- pk of the revenue month
        data -- data create:
        {
            "revenue_adjustment": 0,
            "team": 0,
            "project": 0,
            "amount_budgeted": 0,
            "amount_actual": 0,
            "year": 0,
            "month": 0
        }
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_revenue_month(self, pk):
        """ Delete the revenue month

        Keyword arguments:

        pk -- pk of the revenue month
        """

        route = 'v1/revenue/month/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def update_revenue(self, pk, data):
        """ Update a revenue

        Keyword arguments:

        pk -- pk of the revenue
        data -- data update:
            {
                "amount_actual": 0,
                "amount_budgeted": 0,
                "description": "string",
                "type": "string",
                "month": 0,
                "title": "string",
                "year": 0,
                "team": 0,
                "project": 0,
                "months": [
                    "string"
                ]
            }
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_revenue(self, pk):
        """ Delete the revenue

        Keyword arguments:

        pk -- pk of the revenue
        """

        route = 'v1/revenue/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    #### Styleguides ####

    def get_styleguides_list(self, page=1):
        """ Get the styleguide list """

        route = 'v1/styleguides/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response, True)

    def get_styleguide_details(self, pk):
        """ Get the styleguide details

        Keyword arguments:

        pk -- pk of the styleguide
        """

        route = 'v1/styleguides/{0}/'.format(pk)
        response = requests.get('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)

    def create_styleguide(self, data):
        """ Create a styleguide

        Keyword arguments:

        data -- data create:
            {
                "name": "string"
            }
        """

        route = 'v1/styleguides/list/{0}/'.format(self.org_pk)
        response = requests.post('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def update_styleguide(self, pk, data):
        """ Update a styleguide

        Keyword arguments:

        pk -- pk of the styleguide
        data -- data create:
            {
                "name": "string",
                "type": "string" ("all", "report", "invoice", "proposal"),
                "font_color": "string",
                "font": "string",
                "font_size": "string",
                "margin_left": 0,
                "margin_right": 0
            }
        """

        route = 'v1/styleguides/{0}/'.format(pk)
        response = requests.patch('{0}{1}'.format(self.base_url, route), headers=self.headers, data=json.dumps(data))
        return self.process_response(response)

    def delete_styleguide(self, pk):
        """ Delete a styleguide

        Keyword arguments:

        pk -- pk of the styleguide
        """

        route = 'v1/styleguides/{0}/'.format(pk)
        response = requests.delete('{0}{1}'.format(self.base_url, route), headers=self.headers)
        return self.process_response(response)
