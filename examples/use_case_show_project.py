import pprint

from dotenv import dotenv_values

import resources.ooti as ooti

config = dotenv_values("../.ENV")


def show_tasks_for_projects():
    my_account = ooti.OotiAPI(
        config["OOTI_AUTH"], config["OOTI_PASSWORD"]
    )  # connect to ooti
    my_account.connect()

    id_project = my_account.Projects.get_projects_list()["data"][0]["id"]

    pk_employee = my_account.Orgusers.get_orgusers_list()["data"][0]["pk"]

    res = my_account.Tasks.create_task(
        {
            "priority": str(2),
            "title": "Test Task",
            "project": str(id_project),
            "due_date": "30-04-2022",
            "assigned_to": str(pk_employee),
            "labels": [],
            "description": "",
            "list": "",
            "phase": "",
        }
    )  # add a task to a random project

    pprint.pprint(res)

    tasks = []
    for i in my_account.Tasks.get_tasks_list()["data"]:
        if not i["is_completed"] and i["project"] == id_project:
            tasks.append(
                (
                    i["due_date"],
                    i["priority_display"],
                    i["title"],
                    i["assigned_to_display"],
                    i["project_display"],
                )
            )

    print(
        "Tasks for the project {0}:".format(tasks[0][4])
    )  # list the tasks of the previous project
    for i in tasks:
        print("{0},{1},{2},{3}".format(i[0], i[1], i[2], i[3]))


show_tasks_for_projects()
