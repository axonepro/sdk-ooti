import ooti.ooti as oo
from time import sleep
from dotenv import dotenv_values

config = dotenv_values("../.ENV")

def connect(email,mdp):
    my_account = oo.OotiAPI(email,mdp)
    my_account.connect()
    return my_account

def create_client(myAccount,name,adress):
    data_client = {"company_name": name,
                    "currency": "134313",
                    "billing_address": adress,
                    "group": None,
                    "address": adress}
    return myAccount.Clients.create_client(data_client)

def get_client_id(client):
    return client["data"]["id"]

def create_opportunite(myAccount,client_pk,project_name,number):
    data_opportunite = {"client": client_pk,
                        "currency": "134313",
                        "case_number":number,
                        "project_title": project_name}
    return myAccount.Projects.create_project(data_opportunite)

def get_opportunite_id(opportunite):
    return opportunite["data"]["id"]

def get_project_by_name(myAccount,name):
    for project in myAccount.Projects.get_projects_list()["data"]:
        if project["project_title"] == name:
            return project

def get_project_by_id(myAccount,project_id):
    for project in myAccount.Projects.get_projects_list()["data"]:
        if project["id"] == project_id:
            return project

def get_dict_stages(myAccount):
    out = {}
    for stage in myAccount.Pipelines.get_pipelines_stage_list()["data"]["results"]:
        out[stage["title"]] = stage["pk"] 
    return out

def change_stage_project(myAccount,project_id,name_stage):
    dict_stages = get_dict_stages(myAccount)
    data = {"stage":dict_stages[name_stage],"signed":False}
    myAccount.Projects.update_project_details(project_id,data)

def signed_project(myAccount,project_id):
    data = {"signed":True}
    myAccount.Projects.update_project_details(project_id,data)

if __name__ == '__main__':
    my_account = oo.OotiAPI(config['OOTI_AUTH'], config['OOTI_PASSWORD'])  #connect to ooti
    my_account.connect()
    
    client = create_client(my_account,"Aminata Company","Paris 2e")
    client_pk = get_client_id(client)
    opportunite = create_opportunite(my_account,client_pk,"My Project")
    opportunite_pk = get_opportunite_id(opportunite)

    change_stage_project(my_account,opportunite_pk,"Prospect")
    print("Proposition dans prospect")
    sleep(10) 
    change_stage_project(my_account,opportunite_pk,"Proposition Envoyé")
    print("Proposition dans Proposition Envoyé")
    sleep(10)
    signed_project(my_account,opportunite_pk) 
    print("Proposition devenue un projet")