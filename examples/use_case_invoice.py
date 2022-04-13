import ooti.ooti as ooti
from dotenv import dotenv_values
import pprint
config = dotenv_values("../.env")

def create_invoice_for_project():

    my_account = ooti.OotiAPI(config['EMAIL'], config['PASSWORD'])  #connect to ooti
    my_account.connect()

    team_pk=my_account.Teams.get_teams_list()['data'][0]['pk']
    client_pk=my_account.Clients.get_clients_list(team_pk)['data'][0]['pk']
    currency_pk=my_account.Currencies.get_currencies_list()['data'][0]['pk']


    data={'client':client_pk,
    'currency':currency_pk,
    'project_title':'test_project',
    'start_date':'28-04-2020',
    'end_date':'28-08-2020',
    'city':'Deauville',
    'country':'FR',
    'total_fees':100
    }



    my_account.Projects.create_project(data)

    projects=my_account.Projects.get_projects_list()
    for i in projects['data']:
        if(i['project_title']=='test_project'):
            id=i['id']
    
    my_account.Phases.create_phase(id,{'name':'phase1','pct':10.0})
    my_account.Phases.create_phase(id,{'name':'phase2','pct':60.0})
    my_account.Phases.create_phase(id,{'name':'phase3','pct':30.0})

create_invoice_for_project()

