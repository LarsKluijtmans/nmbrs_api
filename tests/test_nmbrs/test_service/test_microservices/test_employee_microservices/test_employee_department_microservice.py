"""Unit tests for the EmployeeDepartmentsService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime

from src.nmbrs.data_classes.employee import DepartmentAll, Department
from src.nmbrs.service.microservices.employee.department import EmployeeDepartmentsService


class TestEmployeeDepartmentsService(unittest.TestCase):
    """Unit tests for the EmployeeDepartmentsService class."""

    def setUp(self):
        self.client = Mock()
        self.departments_service = EmployeeDepartmentsService(self.client)
        self.mock_auth_header = Mock()
        self.departments_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all departments for all employees in a company."""
        company_id = 123
        self.client.service.Department_GetAll_AllEmployeesByCompany.return_value = [
            {
                "EmployeeId": 1,
                "EmployeeDepartments": {
                    "Department_V2": [
                        {
                            "Id": 1,
                            "Code": "Dept1",
                            "Description": "Department 1",
                            "CreationDate": datetime.now(),
                            "StartPeriod": 1,
                            "StartYear": 2024,
                        }
                    ]
                },
            },
            {
                "EmployeeId": 2,
                "EmployeeDepartments": {
                    "Department_V2": [
                        {
                            "Id": 2,
                            "Code": "Dept2",
                            "Description": "Department 2",
                            "CreationDate": datetime.now(),
                            "StartPeriod": 2,
                            "StartYear": 2024,
                        }
                    ]
                },
            },
        ]

        result = self.departments_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, DepartmentAll)
        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "Dept1")
        self.assertEqual(result[0].description, "Department 1")

        self.assertEqual(result[1].employee_id, 2)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].code, "Dept2")
        self.assertEqual(result[1].description, "Department 2")

        self.client.service.Department_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test getting the current department of an employee."""
        employee_id = 123
        mock_department_data = {
            "Id": 1,
            "Code": 333,
            "Description": "Human Resources",
        }
        self.client.service.Department_GetCurrent.return_value = mock_department_data

        result = self.departments_service.get_current(employee_id)

        self.assertIsInstance(result, Department)
        self.assertEqual(result.employee_id, 123)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.code, 333)
        self.assertEqual(result.description, "Human Resources")

        self.client.service.Department_GetCurrent.assert_called_once_with(
            EmployeeId=employee_id, _soapheaders=self.mock_auth_header
        )
