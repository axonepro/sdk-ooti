import pprint

from dotenv import dotenv_values

import resources.ooti as ooti

config = dotenv_values("../.ENV")


def create_invoice_for_project():

    my_account = ooti.OotiAPI(
        config["OOTI_AUTH"], config["OOTI_PASSWORD"]
    )  # connect to ooti
    my_account.connect()

    team_pk = my_account.Teams.get_teams_list()["data"][0]["pk"]
    client_pk = my_account.Clients.get_clients_list(team_pk)["data"][0]["pk"]
    for i in my_account.Currencies.get_currencies_list()["data"]:
        if i["name"] == "EUR":
            currency_pk = i["pk"]

    data = {
        "client": client_pk,
        "currency": currency_pk,
        "project_title": "test_project",
        "start_date": "28-04-2020",
        "end_date": "28-08-2020",
        "city": "Deauville",
        "country": "FR",
    }

    my_account.Projects.create_project(data)  # create a project

    projects = my_account.Projects.get_projects_list()
    for i in projects["data"]:
        if i["project_title"] == "test_project":
            id_project = i["id"]

    id_fee_project = my_account.Fees.get_fees_project_list_projects(id_project)["data"][
        0
    ][
        "id"
    ]  # get the id of the fee project to update it

    my_account.Phases.create_phase(
        project_pk=id_project,
        data={
            "name": "phase1",
            "pct": 10,
            "fee_project": id_fee_project,
            "dependants": [],
        },
    )  # add 3 phases
    my_account.Phases.create_phase(
        project_pk=id_project,
        data={
            "name": "phase2",
            "pct": 50,
            "fee_project": id_fee_project,
            "dependants": [],
        },
    )
    my_account.Phases.create_phase(
        project_pk=id_project,
        data={
            "name": "phase3",
            "pct": 40,
            "fee_project": id_fee_project,
            "dependants": [],
        },
    )

    my_account.Fees.update_fee_project(
        id_fee_project, {"cost": 700000, "is_validated": True}
    )  # validate fee project

    id_phase = my_account.Phases.get_phases_list_fee_project(
        id_project, id_fee_project
    )["data"][0]["id"]

    my_account.Revisions.create_phase_revision(
        team_pk, id_project, {"phase": id_phase, "progress": 10.0, "date": "19-04-2022"}
    )  # update the progress of the phase

    my_account.Invoices.create_invoice(
        team_pk,
        {
            "project": id_project,
            "invoice_date": "14-05-2022",
            "type": 1,
            "client": client_pk,
        },
    )  # create an invoice
    for i in my_account.Invoices.get_invoices_list()["data"]:
        if i["project"] == id_project:
            pk_invoice = i["pk"]

    my_account.Invoices.validate_invoice(pk_invoice)  # validate invoice
    my_account.Invoices.send_invoice(pk_invoice)  # send invoice

    amount = my_account.Invoices.get_invoice_details(pk_invoice)["data"]["total"]

    my_account.Payments.create_payment(
        team_pk,
        {
            "currency": currency_pk,
            "date": "19-04-2022",
            "invoice": pk_invoice,
            "project": id_project,
            "type": "C",
            "amount": amount,
        },
    )  # pay the invoice


create_invoice_for_project()
