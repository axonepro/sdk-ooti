import requests
import json
import sys

# TODO Trouver comment refacto tous ces imports
from .accounting import Accounting
from .actions import Actions
from .annexes import Annexes
from .areas import Areas
from .auth import Auth
from .banks import Banks
from .billing import Billing
from .celery_tasks import Celery_tasks
from .clients import Clients
from .contacts import Contacts
from .contracts import Contracts
from .costs import Costs
from .countries import Countries
from .currencies import Currencies
from .customfields import Customfields
from .defaults import Defaults
from .documents import Documents
from .emails import Emails
from .employees import Employees
from .expenses import Expenses
from .fees import Fees
from .files import Files
from .goals import Goals
from .help import Help
from .helper import Helper
from .imports import Imports
from .inbound_emails import Inbound_emails
from .indicators import Indicators
from .invitations import Invitations
from .invoices import Invoices
from .jobs import Jobs
from .languages import Languages
from .lots import Lots
from .milestones import Milestones
from .newsletters import Newsletters
from .notes import Notes
from .notifications import Notifications
from .organizations import Organizations
from .orgusers import Orgusers
from .payments import Payments
from .permissions import Permissions
from .phases import Phases
from .pipelines import Pipelines
from .plans import Plans
from .posts import Posts
from .prescriptions import Prescriptions
from .profiles import Profiles
from .projections import Projections
from .projects import Projects
from .quickbooks import Quickbooks
from .reports import Reports
from .revenue import Revenue
from .revisions import Revisions
from .roles import Roles
from .stats import Stats
from .styleguides import Styleguides
from .tags import Tags
from .tasks import Tasks
from .teams import Teams
from .timelogs import Timelogs
from .timeperiods import Timeperiods
from .token_auth import Token_auth
from .token_refresh import Token_refresh
from .token_verify import Token_verify
from .trips import Trips
from .zones import Zones

# To read .env variables
import os
from dotenv import load_dotenv

# Loading environment variables (stored in .env file)
load_dotenv()


class OotiAPI(Helper):
    def __init__(self, username, password, pagination=None):
        self.username = username
        self.password = password

        self.base_url()

        self.org_pk = None
        self.teams_pk = None
        self.access_token = None
        self._csrf_token = None
        self.headers = None

        self.Accounting = None
        self.Actions = None
        self.Annexes = None
        self.Areas = None
        self.Auth = None
        self.Banks = None
        self.Billing = None
        self.Celery_tasks = None
        self.Clients = None
        self.Contacts = None
        self.Contracts = None
        self.Costs = None
        self.Countries = None
        self.Currencies = None
        self.Customfields = None
        self.Defaults = None
        self.Documents = None
        self.Emails = None
        self.Employees = None
        self.Expenses = None
        self.Fees = None
        self.Files = None
        self.Goals = None
        self.Help = None
        self.Helper = None
        self.Imports = None
        self.Inbound_emails = None
        self.Indicators = None
        self.Invitations = None
        self.Invoices = None
        self.Jobs = None
        self.Languages = None
        self.Lots = None
        self.Milestones = None
        self.Newsletters = None
        self.Notes = None
        self.Notifications = None
        self.Organizations = None
        self.Orgusers = None
        self.Payments = None
        self.Permissions = None
        self.Phases = None
        self.Pipelines = None
        self.Plans = None
        self.Posts = None
        self.Prescriptions = None
        self.Profiles = None
        self.Projections = None
        self.Projects = None
        self.Quickbooks = None
        self.Reports = None
        self.Revenue = None
        self.Revisions = None
        self.Roles = None
        self.Stats = None
        self.Styleguides = None
        self.Tags = None
        self.Tasks = None
        self.Teams = None
        self.Timelogs = None
        self.Timeperiods = None
        self.Token_auth = None
        self.Token_refresh = None
        self.Token_verify = None
        self.Trips = None
        self.Zones = None

        if pagination and isinstance(pagination, int) and pagination > 0:
            self.pagination = pagination
        else:
            self.pagination = 50

    def connect(self):
        self.__get_csrf_token()
        self.__get_token()
        self.__get_selected_org()
        self.__get_teams()

        self.Accounting = Accounting(self.base_url, self.org_pk, self.teams_pk,
                           self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Actions = Actions(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Annexes = Annexes(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Areas = Areas(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Auth = Auth(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Banks = Banks(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Billing = Billing(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Celery_tasks = Celery_tasks(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Clients = Clients(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Contacts = Contacts(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Contracts = Contracts(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Costs = Costs(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Countries = Countries(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Currencies = Currencies(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Customfields = Customfields(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Defaults = Defaults(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Documents = Documents(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Emails = Emails(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Employees = Employees(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Expenses = Expenses(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Fees = Fees(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Files = Files(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Goals = Goals(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Help = Help(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Helper = Helper(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Imports = Imports(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Inbound_emails = Inbound_emails(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Indicators = Indicators(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Invitations = Invitations(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Invoices = Invoices(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Jobs = Jobs(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Languages = Languages(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Lots = Lots(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Milestones = Milestones(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Newsletters = Newsletters(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Notes = Notes(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Notifications = Notifications(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Organizations = Organizations(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Orgusers = Orgusers(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Payments = Payments(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Permissions = Permissions(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Phases = Phases(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Pipelines = Pipelines(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Plans = Plans(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Posts = Posts(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Prescriptions = Prescriptions(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Profiles = Profiles(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Projections = Projections(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Projects = Projects(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Quickbooks = Quickbooks(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Reports = Reports(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Revenue = Revenue(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Revisions = Revisions(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Roles = Roles(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Stats = Stats(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Styleguides = Styleguides(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Tags = Tags(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Tasks = Tasks(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Teams = Teams(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Timelogs = Timelogs(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Timeperiods = Timeperiods(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Token_auth = Token_auth(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Token_refresh = Token_refresh(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Token_verify = Token_verify(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Trips = Trips(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)
        self.Zones = Zones(self.base_url, self.org_pk, self.teams_pk,
                                   self.access_token, self._csrf_token, self.headers, self.pagination)

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
            self.Accounting.pagination = pagination
            self.Actions.pagination = pagination
            self.Annexes.pagination = pagination
            self.Areas.pagination = pagination
            self.Auth.pagination = pagination
            self.Banks.pagination = pagination
            self.Billing.pagination = pagination
            self.Celery_tasks.pagination = pagination
            self.Clients.pagination = pagination
            self.Contacts.pagination = pagination
            self.Contracts.pagination = pagination
            self.Costs.pagination = pagination
            self.Countries.pagination = pagination
            self.Currencies.pagination = pagination
            self.Customfields.pagination = pagination
            self.Defaults.pagination = pagination
            self.Documents.pagination = pagination
            self.Emails.pagination = pagination
            self.Employees.pagination = pagination
            self.Expenses.pagination = pagination
            self.Fees.pagination = pagination
            self.Files.pagination = pagination
            self.Goals.pagination = pagination
            self.Help.pagination = pagination
            self.Helper.pagination = pagination
            self.Imports.pagination = pagination
            self.Inbound_emails.pagination = pagination
            self.Indicators.pagination = pagination
            self.Invitations.pagination = pagination
            self.Invoices.pagination = pagination
            self.Jobs.pagination = pagination
            self.Languages.pagination = pagination
            self.Lots.pagination = pagination
            self.Milestones.pagination = pagination
            self.Newsletters.pagination = pagination
            self.Notes.pagination = pagination
            self.Notifications.pagination = pagination
            self.Organizations.pagination = pagination
            self.Orgusers.pagination = pagination
            self.Payments.pagination = pagination
            self.Permissions.pagination = pagination
            self.Phases.pagination = pagination
            self.Pipelines.pagination = pagination
            self.Plans.pagination = pagination
            self.Posts.pagination = pagination
            self.Prescriptions.pagination = pagination
            self.Profiles.pagination = pagination
            self.Projections.pagination = pagination
            self.Projects.pagination = pagination
            self.Quickbooks.pagination = pagination
            self.Reports.pagination = pagination
            self.Revenue.pagination = pagination
            self.Revisions.pagination = pagination
            self.Roles.pagination = pagination
            self.Stats.pagination = pagination
            self.Styleguides.pagination = pagination
            self.Tags.pagination = pagination
            self.Tasks.pagination = pagination
            self.Teams.pagination = pagination
            self.Timelogs.pagination = pagination
            self.Timeperiods.pagination = pagination
            self.Token_auth.pagination = pagination
            self.Token_refresh.pagination = pagination
            self.Token_verify.pagination = pagination
            self.Trips.pagination = pagination
            self.Zones.pagination = pagination

    #### Token ####

    def __get_csrf_token(self):
        client = requests.session()
        # Retrieve the CSRF token first
        client.get("https://app.ooti.co/accounts/login/")  # sets cookie
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']

        self._csrf_token = csrftoken

    def __get_token(self):
        route = 'v1/token-auth/'
        headers = {
            'Accept': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.process_request(requests, 'POST', self.base_url, route, headers, None, data)

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

    def __get_selected_org(self):
        """ Get the organization selected on user profile
        """

        route = 'v1/profiles/profile/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        self.org_pk = json.loads(response.content)['selected_org']
        return self.process_response(response)

    def __get_teams(self):
        """ Set the organization id of the user """

        route = 'v1/organizations/membership/'
        response = self.process_request(requests, 'GET', self.base_url, route, self.headers, None, None)
        organizations = json.loads(response.content)['organizations']
        selected_organization = next((org for org in organizations if org.get('id') == self.org_pk), None)
        teams = selected_organization['teams']
        # teams = json.loads(response.content)['organizations'][0]['teams']
        self.teams_pk = []
        for team in range(len(teams)):
            self.teams_pk.append({key: teams[team][key] for key in ('id', 'title')})
        return response.status_code