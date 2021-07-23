import random
import string
import time


class TestHelper:
    """ TestHelper class 

    Create all needed object to do tests
    """

    def __init__(self, my_account):
        self.my_account = my_account

    def _create_currency_if_none(self):
        currency_pk = -1
        currencies = self.my_account.Invoicing.get_currencies_list()['data']

        if len(currencies) == 0:
            data_currency = {
                "name": "usd",
                "longname": "United States Dollar",
                "symbol": "$",
            }

            res = self.my_account.Invoicing.create_currency(data_currency)
            currency_pk = res['data']['pk']
        else:
            currency_pk = currencies[0]['pk']

        return currency_pk

    def _create_currency_return_pk(self):
        """
        Generate a currency with random name
        """
        name = ''
        for i in range(6):
            name += random.choice(string.ascii_letters)
            time.sleep(0.1)

        data_currency = {
            "name": name,
            "longname": "longname",
            "symbol": "$",
        }

        res = self.my_account.Invoicing.create_currency(data_currency)
        if res['status'] == 201:
            currency_pk = res['data']['pk']
            return currency_pk
        else:
            self._create_currency_return_pk()

    def _create_client_return_pk(self, team_pk, currency_pk):
        """ Create client and return pk

        :return: client_pk
        """

        data_client = {
            "name": "UNITTEST",
            "number": "0001",
            "currency": currency_pk,
            "team": team_pk,
            "tags": [],
        }

        client = self.my_account.Invoicing.create_client(data_client)
        return client['data']['pk']

    def _create_project_return_pk(self, client_pk, currency_pk):
        """ Create project and return pk
        TODO: 500

        :return: project_pk
        """

        data_project = {
            "client": client_pk,
            "currency": currency_pk,
            "project_title": "UNITTEST-test",
            "start_date": "01-07-2021",
            "end_date": "23-07-2021",
        }

        res = self.my_account.create_project(data_project)
        print(res)
        return res['data']['pk']

    def _create_invoice_return_pk(self, team_pk, project_pk):
        """ Create and return the pk of an invoice 

        It creates 
        """

        invoice = {
            "project": project_pk,
            "invoice_date": '19-04-2021',
            "due_date": '19-05-2021',
            "references": "UNITTEST ref",
            "type": 4
        }

        invoice_pk = self.my_account.Invoicing.create_invoice(team_pk, invoice)['data']['pk']
        return invoice_pk

    def _create_invoice_item_return_pk(self, invoice_pk):
        data_invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res = self.my_account.Invoicing.create_invoice_item(invoice_pk, data_invoice_item)
        return res['data']['pk']

    def _create_payment_return_pk(self, team_pk, invoice_pk, currency_pk):
        """ Create payment
        Create an invoice, an item invoice, validate the invoice and then a payment. 

        :return: pk of payment
        """

        invoice_item = {
            "description": "UNITTEST ITEM",
            "subtitle": "My subtitle",
            "amount": 1000
        }

        res_creation_item = self.my_account.Invoicing.create_invoice_item(invoice_pk, invoice_item)
        self.my_account.Invoicing.validate_invoice(invoice_pk)

        payment = {
            "date": "21-04-2021",
            "amount": 100,
            "currency": currency_pk,
            "invoice": invoice_pk,
            "team": team_pk
        }

        res_creation_payment = self.my_account.Invoicing.create_payment(team_pk, payment)
        payment_pk = res_creation_payment['data']['pk']

        return payment_pk

    def _create_email_return_pk(self):
        """ Create an email template and return the pk """

        email = {
            "name": "UNITTEST",
            "email_subject": "UNITTEST",
            "email_body": "UNITTEST",
            "email_to": "test@ooti.co",
            "email_from": "test@ooti.co",
            "name_from": "Test de OOTI"
        }

        email_pk = self.my_account.Invoicing.create_email(email)['data']['id']
        return email_pk

    def _create_email_smtp_return_pk(self):
        """ Create email smtp and return pk """

        data = {
            "from_name": "UNITTEST",
            "from_email": "UNITTEST",
            "username": "UNITTEST",
            "password": "UNITTEST",
            "protocol": "TLS",
            "host": "UNITTEST",
            "port": 0
        }

        smtp_pk = self.my_account.Invoicing.create_email_smtp(data)['data']['id']
        return smtp_pk

    def _create_folder_return_pk(self, project_pk):
        """ Create a folder and return the pk """

        name = self.create_name()

        folder = {
            "name": name
        }

        folder_pk = self.my_account.Invoicing.create_folder(project_pk, folder)['data']['pk']
        return folder_pk

    def _create_file_return_pk(self, project_pk, folder_pk):
        """ Test that 200 is returned """

        name = self.create_name()

        data = {
            "name": name,
            "file": "README.md",
            "folder": folder_pk,
        }

        res = self.my_account.Invoicing.create_file(project_pk, data)
        if res['status'] == 201:
            return res['data']['pk']
        elif 'non_field_errors' in res['data'] and res['data']['non_field_errors'] == ['The fields folder, name must make a unique set.']:
            self._create_file_return_pk(project_pk, folder_pk)

    def _create_bank_return_pk(self, team_pk, project_pk, currency_pk):

        name = self.create_name()

        data = {
            "name": name,
            "currency": currency_pk,
            "country": "FR",
            "iban": "XXX-{0}".format(name),
            "bic": "XXX-{0}".format(name),
            "rib": "XXX-{0}".format(name),
            "teams": [str(team_pk)],
            "projects": [str(project_pk)]
        }

        res = self.my_account.Invoicing.create_bank(data)
        return res['data']['id']

    def create_name(self):
        name = ''
        for i in range(6):
            name += random.choice(string.ascii_letters)
            time.sleep(0.1)
        name += '_UNITTEST'
        return name
