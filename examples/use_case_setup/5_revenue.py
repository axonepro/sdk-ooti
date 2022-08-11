from pprint import pprint

from constants import *

#### BANK
# bank_data = {
#             "name": "bank test",
#             "currency": currency_pk,
#             "country": "FR",
#             "iban": f"XXX-test",
#             "bic": f"XXX-test",
#             "rib": f"XXX-test",
#             "teams": [str(team_pk)],
#             "projects": [str(project_pk)]
#         }
# my_account.Banks.create_bank(bank_data)
# pprint(my_account.Banks.get_banks_list())

### INVOICE TEST
# invoice_data = {
#                 "project": project_pk,
#                 "invoice_date": '05-08-2022',
#                 "due_date": '05-09-2022',
#                 "references": "test ref",
#                 "type": 4,
#                 "is_sent": False
#             }
# my_account.Invoices.create_invoice(team_pk, invoice_data)
# pprint(my_account.Invoices.get_invoices_list())

##### GRAPHIC CHARTER
# styleguide_data = {
#                 "logo": "test"
#             }
# my_account.Styleguides.create_styleguide({"name": "test style"})
# my_account.Styleguides.update_styleguide(styleguide_pk, styleguide_data)
# my_account.Styleguides.delete_styleguide(177) # delete the default one
# pprint(my_account.Styleguides.get_styleguides_list())

##### INVOICE IMPORT
# FIXME status 201 but not appeared in import list -> not working maybe Settings
import_data = {
    "team": team_pk,
    "project": project_pk,
    "type": 12,
}
# pprint(my_account.Imports.create_import(import_data))

##### VALIDATE INVOICE
# FIXME {'data': ['You cannot edit a valid invoice.'], 'status': 400} -> probably wrong method
# pprint(my_account.Invoices.validate_invoice(invoice_pk))
# pprint(my_account.Invoices.get_invoices_list())

##### INVOICE EXPORT
# export_data = {
#             "orguser": orguser_pk,
#             "team": team_pk,
#             "project": project_pk,
#             "type": 9,
#         }
# my_account.Imports.create_export(export_data)