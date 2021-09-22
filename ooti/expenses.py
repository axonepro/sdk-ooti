import requests
import json

from .helper import Helper


class Expenses(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_expenses_categories_list(self, page=1):
        """ Get the list of expenses categories """

        route = 'v1/expenses/category/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_expenses_category(self, data):
        """ Create a new expenses category 

        Keywords arguments:
        data -- data of the new expenses category to be created:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "accounting_code": "string",
            "vat": "string"
        }
        """

        route = 'v1/expenses/category/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_category_details(self, category_pk):
        """ Get the expenses category details

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_expenses_category_details(self, category_pk, data):
        """ Update the expense details

        Keyword arguments:
        category_pk -- pk of the expense category
        data -- content of the update:
        {
            "name": "string",
            "name_en": "string",
            "name_fr": "string",
            "accounting_code": "string",
            "vat": "string"
        }
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expenses_category(self, category_pk):
        """ Delete the expenses category

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = 'v1/expenses/category/{0}'.format(category_pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def add_multiple_expenses(self, expense_group_id, files):

        route = 'v1/expenses/groups/create-multiple-expenses/{0}/'.format(expense_group_id)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, files)
        return self.process_response(response)

    def create_expenses_group_action(self, data):
        """ Create an action

        Keyword arguments:
        {
            'team': team_pk # REQUIRED
            'is_treated': bool
            'is_validated': bool
        }
        """

        route = 'v1/expenses/groups/list/action/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_groups_list(self, team_pk=None, page=1):
        """ Get the list of expenses groups

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        if team_pk is None:
            route = 'v1/expenses/groups/v2/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        else:
            route = 'v1/expenses/groups/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_expenses_group(self, data, team_pk=None):
        """ Create a new group of expenses

        Keyword arguments:
        data -- data of the new group of expenses to be created
        """

        if team_pk is None:
            route = 'v1/expenses/groups/v2/list/{0}/'.format(self.org_pk)
        else:
            route = 'v1/expenses/groups/list/{0}/'.format(team_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_group_details(self, expense_group_id):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_expenses_group_details(self, expense_group_id, data):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expenses_group(self, expense_group_id):

        route = 'v1/expenses/groups/{0}/'.format(expense_group_id)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_expenses_list(self, team_pk=None, expense_group_id=None, page=1):
        """ Get the expenses list """

        if team_pk is not None and expense_group_id is not None:
            route = 'v1/expenses/list/{0}/{1}/?page_size={2}&page={3}'.format(
                team_pk, expense_group_id, self.pagination, page)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/?page_size={1}&page={2}'.format(team_pk, self.pagination, page)
        else:
            route = 'v1/expenses/list/{0}/?page_size={1}&page={2}'.format(self.org_pk, self.pagination, page)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_expense(self, data, team_pk=None, expense_group_id=None):
        """ Create a new expense

        Keywords arguments:
        data -- data of the new expense to be created:
        {
            "expense_group": 0,
            "description": "string",
            "amount": 0,
            "vat": 0,
            "file": "string",
            "date": "string",
            "is_paid": true,
            "is_billed": true,
            "comments": "string",
            "local_amount": 0,
            "currency": 0,
            "currency_rate": 0,
            "has_duplicate_receipt": true,
            "distance": 0,
            "rate_per_km": 0,
            "phase": 0
        }
        """

        if team_pk is not None and expense_group_id is not None:
            route = 'v1/expenses/list/{0}/{1}/'.format(team_pk, expense_group_id)
        elif team_pk is not None:
            route = 'v1/expenses/my-groups/list/{0}/'.format(team_pk)
        else:
            route = 'v1/expenses/list/{0}/'.format(self.org_pk)
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_pdf_count(self, expense_group_id):

        route = 'v1/expenses/pdf_count/{0}/'.format(expense_group_id)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # Missing DELETE on v1/expenses/{expense_group_pk}/versions/{version_pk}/delete/

    def get_expenses_details(self, pk):
        """Get the expense details

        Keyword arguments:
        pk -- pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_expense_details(self, pk, data):
        """Update the expense details

        Keyword arguments:
        pk -- pk of the expense
        data -- content of the update:
        {
            "expense_group": group_id,
            "description": "string",
            "amount": 0,
            "vat": 0,
            "file": "string",
            "date": "string",
            "is_paid": true,
            "is_billed": true,
            "comments": "string",
            "local_amount": 0,
            "currency": 0,
            "currency_rate": 0,
            "has_duplicate_receipt": true,
            "distance": 0,
            "rate_per_km": 0,
            "phase": phase_id
        }
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expense(self, pk):
        """Delete the expense

        Keyword arguments:
        pk -- pk of the expense
        """

        route = 'v1/expenses/{0}'.format(pk)
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)