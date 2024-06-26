"""Unit tests for the EmployeeManagerService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.manager import EmployeeManagerService, Manager


class TestEmployeeManagerService(unittest.TestCase):
    """Unit tests for the EmployeeManagerService class."""

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
        self.manager_service = EmployeeManagerService(self.auth_manager, self.client)

    def test_get(self):
        """Test getting manager of an employee."""
        employee_id = 123
        period = 1
        year = 2024
        mock_manager_data = {
            "Number": 1,
            "FirstName": "John",
            "Name": "Doe",
            "Department": "Management",
            "Function": "Manager",
            "PhoneNumber": "123-456-7890",
            "Mobile": "987-654-3210",
            "Fax": "555-555-5555",
            "Email": "john.doe@example.com",
        }
        self.client.service.Manager_Get.return_value = mock_manager_data

        result = self.manager_service.get(employee_id, period, year)

        self.assertIsInstance(result, Manager)
        expected_manager = Manager(employee_id=employee_id, data=mock_manager_data)
        self.assertEqual(result.employee_id, expected_manager.employee_id)
        self.assertEqual(result.number, expected_manager.number)
        self.assertEqual(result.first_name, expected_manager.first_name)
        self.assertEqual(result.name, expected_manager.name)
        self.assertEqual(result.department, expected_manager.department)
        self.assertEqual(result.function, expected_manager.function)
        self.assertEqual(result.phone_number, expected_manager.phone_number)
        self.assertEqual(result.mobile, expected_manager.mobile)
        self.assertEqual(result.fax, expected_manager.fax)
        self.assertEqual(result.email, expected_manager.email)
        # Assert other fields as needed

        self.client.service.Manager_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test getting the current manager of an employee."""
        employee_id = 123
        mock_manager_data = {
            "Number": 1,
            "FirstName": "John",
            "Name": "Doe",
            "Department": "Management",
            "Function": "Manager",
            "PhoneNumber": "123-456-7890",
            "Mobile": "987-654-3210",
            "Fax": "555-555-5555",
            "Email": "john.doe@example.com",
        }
        self.client.service.Manager_GetCurrent.return_value = mock_manager_data

        result = self.manager_service.get_current(employee_id)

        self.assertIsInstance(result, Manager)
        expected_manager = Manager(employee_id=employee_id, data=mock_manager_data)
        self.assertEqual(result.employee_id, expected_manager.employee_id)
        self.assertEqual(result.number, expected_manager.number)
        self.assertEqual(result.first_name, expected_manager.first_name)
        self.assertEqual(result.name, expected_manager.name)
        self.assertEqual(result.department, expected_manager.department)
        self.assertEqual(result.function, expected_manager.function)
        self.assertEqual(result.phone_number, expected_manager.phone_number)
        self.assertEqual(result.mobile, expected_manager.mobile)
        self.assertEqual(result.fax, expected_manager.fax)
        self.assertEqual(result.email, expected_manager.email)
        # Assert other fields as needed

        self.client.service.Manager_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)
