import ooti.ooti as oo
from dotenv import dotenv_values
from pandas import read_csv

config = dotenv_values("../.ENV")


def get_project_id(myAccount, project_name):
    for project in myAccount.Projects.get_projects_list()["data"]:
        if project_name in project["display"]:
            return project["id"]


def connect(email, mdp):
    my_account = oo.OotiAPI(email, mdp)
    my_account.connect()
    return my_account


def create_note(myAccount, title, project_name, commentaire):
    project_id = get_project_id(myAccount, project_name)
    data = {
        "text": commentaire,
        "title": title,
        "is_pinned": False,
        "project": project_id,
        "is_public": False,
        "entire_project": False,
    }
    myAccount.Notes.create_note(data)


def extract_columns(csv_file, columns_list):
    df = read_csv(csv_file)
    return df[columns_list]


def import_csv_file_to_notes(myAccount, csv_file, columns_list):
    df = extract_columns(csv_file, columns_list)
    for i in range(len(df)):
        create_note(
            myAccount,
            title=df.iloc[i, 0],
            project_name=df.iloc[i, 1],
            commentaire=df.iloc[i, 2],
        )


if __name__ == "__main__":
    my_account = oo.OotiAPI(
        config["OOTI_AUTH"], config["OOTI_PASSWORD"]
    )  # connect to ooti
    my_account.connect()
    csv_file = "notes.csv"
    columns_list = ["Titre", "Projet", "Commentaire"]
    import_csv_file_to_notes(my_account, csv_file, columns_list)
