from pprint import pprint

from constants import *

###### WEEK TIMESHEET
# FIXME not working
timelog_week_data = {
                "project": project_pk,
                # "monday": 0,
                # "tuesday": 1,
                # "wednesday": 0,
                # "thursday": 0,
                # "friday": 0,
            }
# pprint(my_account.Projects.get_projects_list())
# pprint(my_account.Timelogs.create_timelogs_hourslogs_my_list(team_pk, timelog_week_data))
# pprint(my_account.Timelogs.get_timelogs_hourslogs_my_list(team_pk))

##### IMPORT
# FIXME not working
import_data = {
    "type": 6,
}
pprint(my_account.Imports.create_import(import_data))