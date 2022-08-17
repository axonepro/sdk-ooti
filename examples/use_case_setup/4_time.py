import json
from pprint import pprint

from constants import *

###### WEEK TIMESHEET
timelog_week_data = {
                # "project": project_pk,
                "monday": 0,
                "tuesday": 1,
                "wednesday": 0,
                "thursday": 0,
                "friday": 0,
                "week": 6031,
            }
pprint(my_account.Timelogs.create_timelogs_hourslogs_my_list(team_pk, timelog_week_data))
pprint(my_account.Teams.get_teams_list())
pprint(my_account.Timelogs.get_timelogs_week_list())
pprint(my_account.Timelogs.get_timelogs_types_list())
pprint(my_account.Timelogs.get_timelogs_hourslogs_my_list(team_pk))

##### IMPORT
# FIXME code 201 but nothing appeared in the import list
import_data = {
    "type": 6,
    "team": team_pk,
}
data = {"clients": {"id":"","company_name":"Google","number":"C41","billing_address":"Adresse de facturation Exemple","currency":"EUR","group":"Google reps.","business_vat_id":"","name":"Jane Smith & CO","email":"jane@ooti.co","phone":"0987654321","address":"Adresse Exemple","notes":"","tags":["tag1"," tag2"," tag3"],"temporary_pk":1}}
pprint(my_account.Imports.get_imports_list())
pprint(my_account.Imports.create_import(import_data))
pprint(my_account.Imports.update_import_details(358, {"continue_confirm": True}))
pprint(my_account.Imports.update_import_details(358, data))
