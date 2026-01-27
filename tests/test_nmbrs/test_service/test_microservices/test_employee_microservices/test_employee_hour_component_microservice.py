"""Test cases for the EmployeeHourComponentFixedService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime

from src.nmbrs.data_classes.employee import HourComponent
from src.nmbrs.service.microservices.employee import EmployeeHourComponentFixedService
from src.nmbrs.auth.token_manager import AuthManager


class TestEmployeeHourComponentFixedService(unittest.TestCase):
    """Test cases for the EmployeeHourComponentFixedService class."""

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
        self.hour_component_service = EmployeeHourComponentFixedService(self.auth_manager, self.client)

    def test_get_fixed(self):
        """Test the get_fixed method of EmployeeHourComponentFixedService."""
        employee_id = 123
        period = 1
        year = 2023
        expected_hour_components = [
            {"Id": 1, "Name": "Overtime", "Amount": 10, "Date": datetime(2023, 1, 1)},
            {"Id": 2, "Name": "Bonus", "Amount": 20, "Date": datetime(2023, 1, 5)},
        ]
        self.client.service.HourComponentFixed_Get.return_value = expected_hour_components

        result = self.hour_component_service.get_fixed(employee_id, period, year)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_hour_components))
        for item in result:
            self.assertIsInstance(item, HourComponent)
        self.client.service.HourComponentFixed_Get.assert_called_once_with(
            EmployeeId=employee_id, Year=year, Period=period, _soapheaders=self.mock_auth_header
        )

    def test_get_current_fixed(self):
        """Test the get_current_fixed method of EmployeeHourComponentFixedService."""
        employee_id = 123
        expected_hour_components = [
            {"Id": 1, "HourCode": 3756, "Hours": -32.00},
            {"Id": 2, "HourCode": 3757, "Hours": 32.00},    
        ]
        self.client.service.HourComponentFixed_GetCurrent.return_value = expected_hour_components

        result = self.hour_component_service.get_current_fixed(employee_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_hour_components))
        for item in result:
            self.assertIsInstance(item, HourComponent)
        self.client.service.HourComponentFixed_GetCurrent.assert_called_once_with(
            EmployeeId=employee_id, _soapheaders=self.mock_auth_header
        )

    def test_get_variable(self):
        """Test the get_variable method of EmployeeHourComponentFixedService."""
        employee_id = 123
        period = 1
        year = 2023
        expected_hour_components = [
            {"Id": 1, "Name": "Overtime", "Amount": 10, "Date": datetime(2023, 1, 1)},
            {"Id": 2, "Name": "Bonus", "Amount": 20, "Date": datetime(2023, 1, 5)},
        ]
        self.client.service.HourComponentVar_Get.return_value = expected_hour_components

        result = self.hour_component_service.get_variable(employee_id, period, year)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_hour_components))
        for item in result:
            self.assertIsInstance(item, HourComponent)
        self.client.service.HourComponentVar_Get.assert_called_once_with(
            EmployeeId=employee_id, Year=year, Period=period, _soapheaders=self.mock_auth_header
        )

    def test_get_current_variable(self):
        """Test the get_current_variable method of EmployeeHourComponentFixedService."""
        employee_id = 123
        expected_hour_components = [
            {"Id": 1, "HourCode": 3756, "Hours": -32.00},
            {"Id": 2, "HourCode": 3757, "Hours": 32.00},    
        ]
        self.client.service.HourComponentVar_GetCurrent.return_value = expected_hour_components

        result = self.hour_component_service.get_current_variable(employee_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_hour_components))
        for item in result:
            self.assertIsInstance(item, HourComponent)
        self.client.service.HourComponentVar_GetCurrent.assert_called_once_with(
            EmployeeId=employee_id, _soapheaders=self.mock_auth_header
        )
