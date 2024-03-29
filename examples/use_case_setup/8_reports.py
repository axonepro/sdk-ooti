from pprint import pprint

from constants import *

report_data = {
            "name": "report test",
            "project": project_pk,
            "type": 1,
        }
my_account.Reports.create_report(report_data)
pprint(my_account.Reports.get_reports_list())

#### PROJECT REPORT
report_data = {
            "name": "my project report",
            "project": project_pk,
            "type": "one_pager",
        }
pprint(my_account.Reports.create_report(report_data))
pprint(my_account.Reports.generate_report({"pk": 197,"project": project_pk}))

#### TEAM REPORT
pprint(my_account.Reports.get_reports_list())
report_data = {
            "name": "my team report",
            "project": project_pk,
            "type": "org_hours_by_collaborator",
            "filter_team": team_pk
        }
generate_data = {
    "pk": 196,
    "project": project_pk,
}
pprint(my_account.Reports.generate_report(generate_data))
pprint(my_account.Reports.create_report(report_data))
