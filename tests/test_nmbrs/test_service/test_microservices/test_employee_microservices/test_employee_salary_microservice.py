"""Unit tests for the EmployeeSalaryService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.salary import EmployeeSalaryService, Salary


class TestEmployeeSalaryService(unittest.TestCase):
    """Unit tests for the EmployeeSalaryService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.mock_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": "test_username",
                "Token": "test_token",
                "Domain": "test_domain",
            }
        }
        self.client = Mock()
        self.salary_service = EmployeeSalaryService(self.auth_manager, self.client)

    def test_get_all_by_company(self):
        """Test getting all salaries of all employees in a company."""
        company_id = 123
        self.client.service.Salary_GetAll_AllEmployeesByCompany.return_value = [
            {
                "EmployeeId": 1,
                "EmployeeSalaries": {
                    "Salary_V2": [
                        {
                            "ID": 1,
                            "Value": 5000,
                            "Type": 1,
                            "StartDate": "2023-01-01",
                            "CreationDate": "2023-12-31",
                            "SalaryTable": {
                                "Code": 1,
                                "Description": "Table 1",
                                "Schaal": {
                                    "Scale": "A",
                                    "SchaalDescription": "Description A",
                                    "ScaleValue": 5000,
                                    "ScalePercentageMax": 100,
                                    "ScalePercentageMin": 0,
                                },
                                "Trede": {"Step": "I", "StepDescription": "Description I", "StepValue": 5000},
                            },
                        },
                        {
                            "ID": 2,
                            "Value": 6000,
                            "Type": 1,
                            "StartDate": "2023-01-01",
                            "CreationDate": "2023-12-31",
                            "SalaryTable": {
                                "Code": 2,
                                "Description": "Table 2",
                                "Schaal": {
                                    "Scale": "B",
                                    "SchaalDescription": "Description B",
                                    "ScaleValue": 6000,
                                    "ScalePercentageMax": 100,
                                    "ScalePercentageMin": 0,
                                },
                                "Trede": {"Step": "II", "StepDescription": "Description II", "StepValue": 6000},
                            },
                        },
                    ]
                },
            }
        ]

        result = self.salary_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)

        for item in result:
            self.assertIsInstance(item, Salary)

        salary_1 = result[0]
        self.assertEqual(salary_1.employee_id, 1)
        self.assertEqual(salary_1.id, 1)
        self.assertEqual(salary_1.value, 5000)
        self.assertEqual(salary_1.type, 1)
        self.assertEqual(salary_1.start_date, "2023-01-01")
        self.assertEqual(salary_1.creation_date, "2023-12-31")
        self.assertEqual(salary_1.table_code, 1)
        self.assertEqual(salary_1.table_description, "Table 1")
        self.assertEqual(salary_1.scale, "A")
        self.assertEqual(salary_1.scale_description, "Description A")
        self.assertEqual(salary_1.scale_value, 5000)
        self.assertEqual(salary_1.scale_percentage_max, 100)
        self.assertEqual(salary_1.scale_percentage_min, 0)
        self.assertEqual(salary_1.step, "I")
        self.assertEqual(salary_1.step_description, "Description I")
        self.assertEqual(salary_1.step_value, 5000)

        salary_2 = result[1]
        self.assertEqual(salary_2.employee_id, 1)
        self.assertEqual(salary_2.id, 2)
        self.assertEqual(salary_2.value, 6000)
        self.assertEqual(salary_2.type, 1)
        self.assertEqual(salary_2.start_date, "2023-01-01")
        self.assertEqual(salary_2.creation_date, "2023-12-31")
        self.assertEqual(salary_2.table_code, 2)
        self.assertEqual(salary_2.table_description, "Table 2")
        self.assertEqual(salary_2.scale, "B")
        self.assertEqual(salary_2.scale_description, "Description B")
        self.assertEqual(salary_2.scale_value, 6000)
        self.assertEqual(salary_2.scale_percentage_max, 100)
        self.assertEqual(salary_2.scale_percentage_min, 0)
        self.assertEqual(salary_2.step, "II")
        self.assertEqual(salary_2.step_description, "Description II")
        self.assertEqual(salary_2.step_value, 6000)

        self.client.service.Salary_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )
