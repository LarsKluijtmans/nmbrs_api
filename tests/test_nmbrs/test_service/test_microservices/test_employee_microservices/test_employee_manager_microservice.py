"""Unit tests for the EmployeeManagerService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.employee.manager import EmployeeManagerService, Manager


class TestEmployeeManagerService(unittest.TestCase):
    """Unit tests for the EmployeeManagerService class."""

    def setUp(self):
        self.client = Mock()
        self.manager_service = EmployeeManagerService(self.client)
        self.mock_auth_header = Mock()
        self.manager_service.set_auth_header(self.mock_auth_header)


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
            # Add more fields if needed
        }
        self.client.service.Manager_GetCurrent.return_value = mock_manager_data

        result = self.manager_service.get_current(employee_id)

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

        self.client.service.Manager_GetCurrent.assert_called_once_with(
            EmployeeId=employee_id, _soapheaders=self.mock_auth_header
        )
