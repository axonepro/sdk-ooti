from pprint import pprint

from constants import *

#### COLLABORATOR
orguser_data = {
            "email": "czheng+4@ooti.co",
            "first_name": "Julien",
            "last_name": "DUPUIS",
            "role": role_pk,
        }
my_account.Orgusers.create_orguser(orguser_data)
pprint(my_account.Orgusers.get_orgusers_list())

#### ROLE
role_data = {
    "title": "role test",
    "billable_per_hour": 10,
    "payable_per_hour": 10
}
my_account.Roles.create_roles(role_data)

team_user_data = {
    "orguser": orguser_pk,
    "permissionsset": permission_pk,
    "role": role_pk,
    "team": team_pk
}
my_account.Teams.add_team_user(pk=team_pk, data=team_user_data)
