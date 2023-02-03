import os
import unittest

from factories.factories import (
    EmployeeContractFactory,
    EmployeePeriodFactory,
    OrguserFactory,
    TeamFactory,
)
from resources import ooti

OOTI_AUTH = os.getenv("OOTI_AUTH")
OOTI_PASSWORD = os.getenv("OOTI_PASSWORD")

sdk = ooti.OotiAPI(OOTI_AUTH, OOTI_PASSWORD)
sdk.connect()


class TestEmployees(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.orguser = OrguserFactory()
        cls.team_pk = TeamFactory()
        cls.employee_contract = EmployeeContractFactory()

    def test_create_employee_contract(self):
        payload = {
            "orguser": self.orguser["pk"],
            "team": self.team_pk,
            "status": "active",
            "end_date": "20-10-2022",
        }
        response = sdk.Employees.create_employees_contract(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Employees.delete_employees_contract(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_delete_employee_contract(self):
        employee_contract = EmployeeContractFactory()
        response = sdk.Employees.delete_employees_contract(employee_contract["id"])
        self.assertEqual(response["status"], 204)

    def test_create_employees_period(self):
        payload = {
            "contract": self.employee_contract["id"],
            "notes": "some notes",
            "start_date": "09-05-2021",
            "end_date": "20-05-2021",
            "status": "active",
            "salary_daily_gross": 100,
            "salary_hourly_gross": 10,
            "salary_gross_coefficent": 1,
            "salary_monthly_net": 1200,
            "salary_monthly_gross": 1500,
            "salary_loaded_coefficent": 0,
            "weekly_hours_limit": 30,
            "daily_hours_limit": 5,
            "overtime_enabled": True,
            "overtime_hours_limit": 5,
            "days_per_week": 6,
        }
        response = sdk.Employees.create_employees_period(payload)
        self.assertEqual(response["status"], 201)
        delete = sdk.Employees.delete_employees_period(response["data"]["id"])
        self.assertEqual(delete["status"], 204)

    def test_delete_employees_period(self):
        employee_period = EmployeePeriodFactory()
        response = sdk.Employees.delete_employees_period(employee_period["id"])
        self.assertEqual(response["status"], 204)

    @classmethod
    def tearDown(cls):
        sdk.Orgusers.delete_orguser(cls.orguser)
        sdk.Employees.delete_employees_contract(cls.employee_contract)


if __name__ == "__main__":
    unittest.main()
