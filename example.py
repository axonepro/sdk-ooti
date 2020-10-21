import main
import pprint


###### Connect ######
my_account = main.Auth('username', 'password')
my_account.connect()


###### Invoice ######
invoices = my_account.get_invoices_list() # Get the list of invoices
for invoice in invoices:
    pprint.pp(invoice) # Print each invoice

invoice = my_account.get_invoice_details(pk='invoice_pk') # Get the details of one invoice
for line in invoice['items']:
    pprint.pp(line) # Print each lines of the invoice


###### Project ######
projects = my_account.get_projects_list() # Get the list of projects
for project in projects:
    pprint.pp(project) # Print each project

project = my_account.get_project_details(pk='invoice_pk') # Get the details of one project
pprint.pp(project) # Print details of the project

data = {
    'business_title': 'new_title'
    }
project = my_account.update_project_details(pk='invoice_pk', data=data) # Update the details of one project
pprint.pp(project) # Print details of the updated project


###### Phase ######
phases = my_account.get_phases_list(project_pk='invoice_pk') # Get the list of phases
for phase in phases:
    pprint.pp(phase) # Print each phase

phase = my_account.get_phase_details(pk='phase_pk') # Get the details of one phase
pprint.pp(phase) # Print details of the phase

data = {'progress': 66}
phase = my_account.update_phase_details(pk='phase_pk', data=data) # Update the details of one phase
pprint.pp(phase) # Print details of the updated phase
