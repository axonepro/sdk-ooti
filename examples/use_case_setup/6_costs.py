from pprint import pprint

from constants import *

##### EMPLOYEE SALARY
employee_data = {
            'orguser': orguser_pk,
            'team': team_pk,
            'status': 'active',
            'start_date': '01-08-2022',
            'end_date': '31-12-2022',
        }
my_account.Employees.create_employees_contract(employee_data)

####### JOB INVOICE
pprint(my_account.Contracts.get_contractors_list())
job_data = {
    'title': 'job test',
    'project': project_pk,
}
pprint(my_account.Jobs.create_job(job_data))
job_invoice_data = {
    "date": "08-08-2022",
    "contractor": contractor_pk,
    "team": team_pk
    # 'amount': '42'
}
pprint(my_account.Jobs.create_jobs_invoice(job_invoice_data))
pprint(my_account.Jobs.get_jobs_invoices_list())
my_account.Teams.create_team
my_account.Contracts.create_contractors({"name": "contractor test"})
pprint(my_account.Contracts.get_contractors_list())
pprint(my_account.Invoices.get_invoice_items(invoice_pk))
