import ooti
import pprint


###### Connect ######
my_account = ooti.Auth('email', 'password')
my_account.connect()


###### Invoice ######
invoices = my_account.get_invoices_list()  # Get the list of invoices
for invoice in invoices:
    pprint.pp(invoice)  # Print each invoice

invoice = my_account.get_invoice_details(pk='invoice_pk')  # Get the details of one invoice
for line in invoice['items']:
    pprint.pp(line)  # Print each lines of the invoice

payload = {
    "amount": 1000,
}
invoice = my_account.create_invoice(1499, payload)  # Create an invoice
pprint.pp(invoice)

payload = {
    "amount": 3000,
}
invoice = my_account.update_invoice(pk='invoice_pk', payload)  # updatee an invoice
pprint.pp(invoice)

###### Payment ######
payments = my_account.get_payments_list()  # Get the list of payments
for payment in payments:
    pprint.pp(payment)  # Print each payment

payment = my_account.get_payment_details(pk='payment_pk')  # Get the details of one payment
pprint.pp(payment)

payload = {
    "amount": 1000,
}
payment = my_account.create_payment(1499, payload)  # Create an payment
pprint.pp(payment)

payload = {
    "amount": 3000,
}
payment = my_account.update_payment(pk='payment_pk', payload)  # updatee an payment
pprint.pp(payment)

###### Project ######
projects = my_account.get_projects_list()  # Get the list of projects
for project in projects:
    pprint.pp(project)  # Print each project

project = my_account.get_project_details(pk='invoice_pk')  # Get the details of one project
pprint.pp(project)  # Print details of the project

data = {
    'business_title': 'new_title'
}
project = my_account.update_project_details(pk='invoice_pk', data=data)  # Update the details of one project
pprint.pp(project)  # Print details of the updated project


###### Phase ######
phases = my_account.get_phases_list(project_pk='invoice_pk')  # Get the list of phases
for phase in phases:
    pprint.pp(phase)  # Print each phase

phase = my_account.get_phase_details(pk='phase_pk')  # Get the details of one phase
pprint.pp(phase)  # Print details of the phase

data = {'progress': 66}
phase = my_account.update_phase_details(pk='phase_pk', data=data)  # Update the details of one phase
pprint.pp(phase)  # Print details of the updated phase
