""" USECASE 3
STEPS :
1) create project
2) create project with fees
3) add co-contractors
4) add fees for co-contractors
5) Advance the task of co-contractors
6) Create a bill
"""

from pprint import pprint

import ooti.ooti as oo
from dotenv import dotenv_values

config = dotenv_values("../.ENV")


def connect(email, mdp):
    my_account = oo.OotiAPI(email, mdp)
    my_account.connect()
    return my_account


def create_project(myAccount, client_pk, project_name):
    data_opportunite = {
        "client": client_pk,
        "currency": "134313",
        "project_title": project_name,
    }
    return myAccount.Projects.create_project(data_opportunite)


def get_project_by_name(myAccount, name):
    for project in myAccount.Projects.get_projects_list()["data"]:
        if project["project_title"] == name:
            return project


def get_fee_id(myAccount, fee_name, project_id):
    for fee in myAccount.Fees.get_fees_project_list_projects(project_id)["data"]:
        if fee_name == fee["title"]:
            return fee["id"]


def get_contractor_id(myAccount, contractor_name):
    for contractor in myAccount.Contracts.get_contractors_list()["data"]:
        if contractor["display"] == contractor_name:
            return contractor["id"]


def get_fee_phases_dict(myAccount, project_pk, fee_pk):
    fee_phases = {}
    for fee in myAccount.Phases.get_phases_list_fee_project(project_pk, fee_pk)["data"]:
        fee_phases[fee["name_en"]] = fee["id"]
    return fee_phases


def get_item(myAccount, invoice_pk, number):
    return myAccount.Invoices.get_invoice_items(invoice_pk)["data"]["results"][number]


if __name__ == "__main__":
    my_account = oo.OotiAPI(
        config["OOTI_AUTH"], config["OOTI_PASSWORD"]
    )  # connect to ooti
    my_account.connect()

    # Create project
    client_pk = 41937
    project_name = "Project3"
    team_pk = 3583
    project = create_project(my_account, 41937, project_name)
    project_id = get_project_by_name(my_account, project_name)["id"]

    # Create a project fee
    fee_name = "Fee1"
    data = {
        "title": fee_name,
        "cost": 20000,
        "fee_pct": 10,
        "surface_area": 100,
        "is_validated": False,
        "co_contractors_enabled": True,
        "project": project_id,
    }
    my_account.Fees.create_fee_project(data)

    # Apply defaults phases
    fee_id = get_fee_id(my_account, fee_name, project_id)
    data = {"fee_project": fee_id, "library": 7559, "project": project_id}
    my_account.Defaults.apply_defaults_phasesets(data)

    # Create a contractor
    data = {
        "currency": "134313",
        "name": "Co-traitant test8",
        "email": "test@test.com",
        "address": "string",
        "telephone": "string",
        "iban": "string",
        "number": "string",
        "is_company": True,
        "is_internal": False,
    }
    my_account.Contracts.create_contractors(data)

    # Create a contract
    contractor_id = get_contractor_id(my_account, "Co-traitant test8")
    data = {
        "contractor": contractor_id,
        "project": project_id,
        "fee_project": fee_id,
        "avg_pct": 5,
        "type": "co",
    }
    my_account.Contracts.create_contract(data)

    # Validate the fee
    my_account.Fees.update_fee_project(fee_id, data={"is_validated": True})

    # Advance a task of a contractors
    fee_phase_dict = get_fee_phases_dict(my_account, project_id, fee_id)
    fee_phase_name = "Sketch studies"
    fee_phase_name2 = "Pre-Project studies"
    data = {
        "phase": fee_phase_dict[fee_phase_name],
        "progress": 40,
        "date": "19-04-2022",
    }
    data2 = {
        "phase": fee_phase_dict[fee_phase_name2],
        "progress": 25,
        "date": "19-04-2022",
    }
    my_account.Revisions.create_phase_revision(team_pk, project_id, data)
    my_account.Revisions.create_phase_revision(team_pk, project_id, data2)

    # Create the bill
    my_account.Invoices.create_invoice(
        team_pk, {"project": project_id, "invoice_date": "20-05-2022"}
    )
