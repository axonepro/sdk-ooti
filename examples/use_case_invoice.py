import ooti.ooti as ooti
from dotenv import dotenv_values
import pprint
config = dotenv_values("../.env")

def create_invoice_for_project():

    my_account = ooti.OotiAPI(config['EMAIL'], config['PASSWORD'])  #connect to ooti
    my_account.connect()

    proj=my_account.Projects.get_projects_list()
    id=proj['data'][0]['id']
    phases=my_account.Phases.get_phases_list(id)
    pprint.pp(phases)

    """team_pk=my_account.Teams.get_teams_list()['data'][0]['pk']
    client_pk=my_account.Clients.get_clients_list(team_pk)['data'][0]['pk']
    currency_pk=my_account.Currencies.get_currencies_list()['data'][0]['pk']


    data={'client':client_pk,
    'currency':currency_pk,
    'project_title':'test_project',
    'start_date':'28-04-2020',
    'end_date':'28-08-2020',
    'city':'Deauville',
    'country':'FR'
    }



    my_account.Projects.create_project(data)"""

create_invoice_for_project()

