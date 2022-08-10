from pprint import pprint

from constants import *

#### CLIENT
# client_data = {
#     "company_name": "Client test",
#     "number": "11",
#     "currency": currency_pk,
#     "billing_address": "123 rue toto",
#     "team": team_pk,
#     "tags": []
# }
# my_account.Clients.create_client(client_data)
# pprint(my_account.Clients.get_clients_list(team_pk))

#### PROJECT
# project_data = {
#             "client": client_pk,
#             "currency": currency_pk,
#             "project_title": "Project test",
#             "phases": [],
#             "project_users": [],
#             "areas": [],
#             "project_tags": [],
#             "start_date": "05-08-2022",
#             "end_date": "05-09-2022",
#             "orgusers": [org_pk],
#             "city": "Paris",
#             "country": "FR"
#         }
# my_account.Projects.create_project(project_data)
# pprint(my_account.Projects.get_projects_list(team_pk))


##### PHASES
# phase_data = {
#                 "name": "phase test",
#                 "shortname": "p t",
#                 "fee_project": fee_project_pk,
#                 "ffne_phase": False,
#                 "in_timeline": True,
#                 "pct": 5,
#                 "dependants": []
#             }
# my_account.Phases.create_phase(project_pk, phase_data)
# pprint(my_account.Phases.get_phases_list(project_pk))

# fee_data = {
#                 "title": "fee 2",
#                 "cost": 1000,
#                 "fee_pct": 10,
#                 "project": project_pk,
#             }
# my_account.Fees.create_fee_project(fee_data)
# my_account.Fees.update_fee_project(project_pk, {'is_validated':True})
# my_account.Phases.create_phase(project_pk=project_pk, data={'name': 'phase1', 'pct':10, 'fee_project': fee_project_pk, 'dependants':[]})
# my_account.Phases.create_phase(project_pk=project_pk, data={'name': 'phase2', 'pct':50, 'fee_project': fee_project_pk, 'dependants':[]})
# my_account.Phases.create_phase(project_pk=project_pk, data={'name': 'phase3', 'pct':40, 'fee_project': fee_project_pk, 'dependants':[]})
# fee_project_data = {"zone_fees_base": 50}
# my_account.Fees.update_fee_project(fee_project_pk, fee_project_data)
# pprint(my_account.Phases.get_phases_list_fee_project(project_pk, fee_project_pk))

###### PROGRESS
# FIXME not working

# my_account.Revisions.create_phase_revision(team_pk, project_pk, {'phase': phase_id, 'progress': 1.0, 'date': "08-08-2022"})
# pprint(my_account.Revisions.get_revisions_phases_team_project(team_pk,project_pk))

##### PHASES PLAN
# phaseset_data = {
#     "title": "phase set test",
#     "team": team_pk
# }
# my_account.Defaults.create_defaults_phasesets_org(phaseset_data)
# pprint(my_account.Defaults.get_defaults_phasesets_org_list())
