import os
from pprint import pprint

from dotenv import load_dotenv

from resources import ooti, payments

load_dotenv()

my_account = ooti.OotiAPI(os.getenv('OOTI_AUTH'), os.getenv('OOTI_PASSWORD'))
my_account.connect()

project_pk = 59152
contractor = 21327
job_invoice_pk = 209

job_data = {
    'title': 'job test',
    'project': project_pk,
}

my_account.Jobs.create_job(job_data)
job_invoice_data = {
    "date": "04-08-2022",
    "contractor": contractor,
    "amount": "42"
}
my_account.Jobs.create_jobs_invoice(job_invoice_data)
pprint(my_account.Jobs.update_jobs_invoice_details(job_invoice_pk, {'is_validated': "Y", 'date_paid': '02-08-2022'}))
