from pprint import pprint

from constants import *

##### CONTACT
# contact_data = {
#             'name': 'contact test',
#             'tags':[]
#         }
# my_account.Contacts.create_contact(data=contact_data)
# pprint(my_account.Contacts.get_contacts_list())

#### OPPORTUNITY ###
# opportunity_data = {
#     "project_title": "hello",
#     "stage": 551,
#     "country": "FR",
#     "language": "fr",
#     "tax_rate": 10.0
# }
# my_account.Projects.create_project(opportunity_data)
# pprint(my_account.Pipelines.get_pipelines_stage_list())

### PROPOSITION
# FIXME not working
proposition_data = {
    "stage": 553
}
pprint(my_account.Projects.update_project_details(1336, proposition_data))
# pprint(my_account.Pipelines.get_pipelines_stage_list())
# pprint(my_account.Projects.get_projects_list())
