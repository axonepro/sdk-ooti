import pprint

from dotenv import dotenv_values

import resources.ooti as ooti

config = dotenv_values("../.ENV")


def add_tag_to_project(id, tag):

    my_account = ooti.OotiAPI(
        config["OOTI_AUTH"], config["OOTI_PASSWORD"]
    )  # connect to ooti
    my_account.connect()

    project = my_account.Projects.get_project_details(id)
    if project["status"] == 200:  # check if the project exists
        tags = my_account.Projects.get_project_tags_list()
        test = False
        for i in tags["data"]:  # check if the tag exists
            if i["name"] == tag:
                test = True
                break
        if not test:
            my_account.Projects.create_project_tag({"name": tag})  # create tag if not
        tag_id = 0
        tags = my_account.Projects.get_project_tags_list()
        for i in tags["data"]:
            if i["name"] == tag:
                tag_id = i["pk"]
                break
        data = {
            "project_tags": list(set(project["data"]["project_tags"] + [tag_id]))
        }  # update the tags of the project
        my_account.Projects.update_project_details(id, data)
        print(
            "The projects with the tag " + tag + " are:"
        )  # show the projects with the tag
        for i in tags["data"]:
            if i["pk"] == tag_id:
                pprint.pp(i["projects"])
    else:
        print("The id of the project is not assigned")


add_tag_to_project(48013, "test3")
