import unittest

from factories.factories import ContractorFactory
from factories.factories import EmployeeContractFactory
from factories.factories import EmployeePeriodFactory
from factories.factories import ExpenseGroupFactory
from factories.factories import JobFactory
from factories.factories import JobInvoiceFactory
from factories.factories import OrguserFactory
from factories.factories import ProjectFactory
from factories.factories import TeamFactory
from factories.factories import CostFactory
from factories.factories import CostMonthFactory

import os
import sys
from dotenv import load_dotenv


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from resources import ooti # noqa E402

# Loading environment variables (stored in .env file)
load_dotenv()

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()

class TestJobs(unittest.TestCase):
    @ classmethod
    def setUp(cls):
        cls.team_pk = TeamFactory()
        cls.project = ProjectFactory()
        cls.job = JobFactory()
        cls.job_invoice = JobInvoiceFactory()
        cls.contractor_id = ContractorFactory()['id']

    def test_create_job(self):
        payload = {
            'title': 'job test',
        }
        response = sdk.Jobs.create_job(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'title': 'job test',
            'project': self.project['id'],
        }
        response = sdk.Jobs.create_job(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Jobs.delete_job(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_job_invoice(self):
        payload = {
            'contractor': self.contractor_id,
            'team': self.team_pk,
            'date': '19-03-2020',
            'amount': '10',
        }
        response = sdk.Jobs.create_jobs_invoice(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Jobs.delete_jobs_invoice(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_jobs_invoices_item(self):
        payload = {
            'project': self.project['id'],
        }
        response = sdk.Jobs.create_jobs_invoices_item(payload)
        self.assertEqual(response['status'], 400)
        payload = {
            'invoice': self.job_invoice['id'],
            'project': self.project['id'],
        }
        response = sdk.Jobs.create_jobs_invoices_item(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Jobs.delete_jobs_invoices_item(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_create_job_month(self):
        payload = {
            'job': self.job['id'],
            'year': '2021',
        }
        response = sdk.Jobs.create_jobs_month(payload)
        self.assertEqual(response['status'], 201)
        delete = sdk.Jobs.delete_jobs_month(response['data']['id'])
        self.assertEqual(delete['status'], 204)

    def test_generate_jobs_invoices_items(self):
        payload = {}
        response = sdk.Jobs.generate_jobs_invoices_items(payload)
        self.assertEqual(response['status'], 404)
        payload = {
            'invoice': self.job_invoice['id']
        }
        response = sdk.Jobs.generate_jobs_invoices_items(payload)
        self.assertEqual(response['status'], 200)

    @classmethod
    def tearDown(cls):
        sdk.Projects.delete_project(cls.project)
        sdk.Jobs.delete_job(cls.job)
        sdk.Jobs.delete_jobs_invoice(cls.job_invoice)
        sdk.Contracts.delete_contractor(cls.contractor_id)

if __name__ == '__main__':
    unittest.main()