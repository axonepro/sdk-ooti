import requests
import json

from .helper import Helper


class Expenses(Helper):
    def __init__(self, base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination):
        super().__init__(base_url, org_pk, teams_pk, access_token, _csrf_token, headers, pagination)

    def get_expenses_categories_list(self, page=1):
        """ Get the list of expenses categories """

        route = f'v1/expenses/category/list/{self.org_pk}/?page_size={self.pagination}&page={page}'
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

        route = f'v1/expenses/category/list/{self.org_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_category_details(self, category_pk):
        """ Get the expenses category details

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = f'v1/expenses/category/{category_pk}'
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

        route = f'v1/expenses/category/{category_pk}'
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expenses_category(self, category_pk):
        """ Delete the expenses category

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        route = f'v1/expenses/category/{category_pk}'
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def add_multiple_expenses(self, expense_group_id, files):

        route = f'v1/expenses/groups/create-multiple-expenses/{expense_group_id}/'
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

        route = f'v1/expenses/groups/list/action/{self.org_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_groups_list(self, team_pk=None, page=1):
        """ Get the list of expenses groups

        Keyword arguments:
        category_pk -- pk of the expenses category
        """

        if team_pk is None:
            route = f'v1/expenses/groups/v2/list/{self.org_pk}/?page_size={self.pagination}&page={page}'
        else:
            route = f'v1/expenses/groups/list/{team_pk}/?page_size={self.pagination}&page={page}'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response, True)

    def create_expenses_group(self, data, team_pk=None):
        """ Create a new group of expenses

        Keyword arguments:
        data -- data of the new group of expenses to be created
        """

        if team_pk is None:
            route = f'v1/expenses/groups/v2/list/{self.org_pk}/'
        else:
            route = f'v1/expenses/groups/list/{team_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_group_details(self, expense_group_id):

        route = f'v1/expenses/groups/{expense_group_id}/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def update_expenses_group_details(self, expense_group_id, data):

        route = f'v1/expenses/groups/{expense_group_id}/'
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expenses_group(self, expense_group_id):

        route = f'v1/expenses/groups/{expense_group_id}/'
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    def get_expenses_list(self, team_pk=None, expense_group_id=None, page=1):
        """ Get the expenses list """

        if team_pk is not None and expense_group_id is not None:
            route = f'v1/expenses/list/{team_pk}/{expense_group_id}/?page_size={self.pagination}&page={page}'
        elif team_pk is not None:
            route = f'v1/expenses/my-groups/list/{team_pk}/?page_size={self.pagination}&page={page}'
        else:
            route = f'v1/expenses/list/{self.org_pk}/?page_size={self.pagination}&page={page}'
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
            route = f'v1/expenses/list/{team_pk}/{expense_group_id}/'
        elif team_pk is not None:
            route = f'v1/expenses/my-groups/list/{team_pk}/'
        else:
            route = f'v1/expenses/list/{self.org_pk}/'
        response = self.process_request(requests, 'POST', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def get_expenses_pdf_count(self, expense_group_id):

        route = f'v1/expenses/pdf_count/{expense_group_id}/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        return self.process_response(response)

    # Missing DELETE on v1/expenses/{expense_group_pk}/versions/{version_pk}/delete/

    def get_expenses_details(self, pk):
        """Get the expense details

        Keyword arguments:
        pk -- pk of the expense
        """

        route = f'v1/expenses/{pk}'
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

        route = f'v1/expenses/{pk}'
        response = self.process_request(requests, 'PATCH', self.base_url, route, self.headers, None, json.dumps(data))
        return self.process_response(response)

    def delete_expense(self, pk):
        """Delete the expense

        Keyword arguments:
        pk -- pk of the expense
        """

        route = f'v1/expenses/{pk}'
        response = self.process_request(requests, 'DELETE', self.base_url, route, self.headers, None, None)
        return self.process_response(response)