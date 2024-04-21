"""Unit tests for the EmployeeFunctionService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from src.nmbrs.service.microservices.employee.function import EmployeeFunctionService, Function


class TestEmployeeFunctionService(unittest.TestCase):
    """Unit tests for the EmployeeFunctionService class."""

    def setUp(self):
        self.client = Mock()
        self.function_service = EmployeeFunctionService(self.client)
        self.mock_auth_header = Mock()
        self.function_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all function history of all employees in a company."""
        company_id = 123
        self.client.service.Function_GetAll_AllEmployeesByCompany_V2.return_value = [
            {
                "EmployeeId": 1,
                "EmployeeFunctions": {
                    "EmployeeFunction": [
                        {
                            "RecordId": 1,
                            "Function": {"Id": 1},
                            "CreationDate": datetime.now(),
                            "StartPeriod": datetime.now(),
                            "StartYear": datetime.now(),
                        }
                    ]
                },
            },
            {
                "EmployeeId": 2,
                "EmployeeFunctions": {
                    "EmployeeFunction": [
                        {
                            "RecordId": 2,
                            "Function": {"Id": 2},
                            "CreationDate": datetime.now(),
                            "StartPeriod": datetime.now(),
                            "StartYear": datetime.now(),
                        }
                    ]
                },
            },
        ]

        result = self.function_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)

        for item in result:
            self.assertIsInstance(item, Function)

        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].record_id, 1)
        self.assertEqual(result[0].function_id, 1)
        self.assertIsInstance(result[0].creation_date, datetime)
        self.assertIsInstance(result[0].start_period, datetime)
        self.assertIsInstance(result[0].start_year, datetime)

        self.assertEqual(result[1].employee_id, 2)
        self.assertEqual(result[1].record_id, 2)
        self.assertEqual(result[1].function_id, 2)
        self.assertIsInstance(result[1].creation_date, datetime)
        self.assertIsInstance(result[1].start_period, datetime)
        self.assertIsInstance(result[1].start_year, datetime)

        self.client.service.Function_GetAll_AllEmployeesByCompany_V2.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )