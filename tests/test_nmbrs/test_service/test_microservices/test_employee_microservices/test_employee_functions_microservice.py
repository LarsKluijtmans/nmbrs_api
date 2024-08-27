"""Unit tests for the EmployeeFunctionService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.employee import FunctionAll, Function
from src.nmbrs.service.microservices.employee.function import EmployeeFunctionService


class TestEmployeeFunctionService(unittest.TestCase):
    """Unit tests for the EmployeeFunctionService class."""

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
        self.function_service = EmployeeFunctionService(self.auth_manager, self.client)

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
            self.assertIsInstance(item, FunctionAll)

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

    def test_get_current(self):
        """Test getting the currently active function for an employee."""
        employee_id = 123
        mock_function = {
            "Id": 1,
            "Code": 123,
            "Description": "Description of Test Function",
        }
        self.client.service.Function_GetCurrent.return_value = mock_function

        result = self.function_service.get_current(employee_id)

        self.assertEqual(result.employee_id, employee_id)
        self.assertIsInstance(result, Function)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.code, 123)
        self.assertEqual(result.description, "Description of Test Function")
        # Assert other fields as needed

        self.client.service.Function_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_update_current(self):
        """Test updating the current function of an employee."""
        employee_id = 123
        function_id = 456

        # Call the update_current method
        self.function_service.update_current(employee_id, function_id)

        # Assert that the SOAP service method was called with the correct parameters
        self.client.service.Function_UpdateCurrent.assert_called_once_with(
            EmployeeId=employee_id,
            FunctionId=function_id,
            _soapheaders=self.mock_auth_header,
        )
