import pprint

import ooti.ooti as ooti
from dotenv import dotenv_values

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

    pprint.pprint(my_account.Fees.get_fees_project_list())

    """my_account.Phases.create_phase(project_pk=id,data={'name':'phase1','pct':10,'bas_production_fees':0.1*100,'mockup_pct':10,'dependants':[]})
    my_account.Phases.create_phase(project_pk=id,data={'name':'phase2','pct':50,'base_production_fees':0.5*100,'mockup_pct':50,'dependants':[]})
    pprint.pprint(my_account.Phases.create_phase(project_pk=id,data={'name':'phase3','pct':40,'production_fees':0.4*100,'mockup_pct':40,'dependants':[]}))"""

    #pprint.pprint(my_account.Phases.get_phases_list(48013)['data'][6])


    #my_account.Invoices.create_invoice(team_pk,{'project':id,'invoice_date':"14-05-2022"}) #Create an invoice
    #pprint.pprint(my_account.Invoices.get_invoices_list())

create_invoice_for_project()

