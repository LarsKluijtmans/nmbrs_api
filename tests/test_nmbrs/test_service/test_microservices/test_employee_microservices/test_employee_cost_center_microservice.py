"""Unit tests for the EmployeeCostCenterService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.cost_center import EmployeeCostCenterService, CostCenter


class TestEmployeeCostCenterService(unittest.TestCase):
    """Unit tests for the EmployeeCostCenterService class."""

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
        self.cost_center_service = EmployeeCostCenterService(self.auth_manager, self.client)

    def test_get(self):
        """Test getting cost centers for a specific employee."""
        employee_id = 123
        period = 1
        year = 2024
        mock_cost_centers = [
            {"Id": 1, "Code": "CC1", "Description": "Cost Center 1"},
            {"Id": 2, "Code": "CC2", "Description": "Cost Center 2"},
        ]
        self.client.service.CostCenter_Get.return_value = mock_cost_centers

        result = self.cost_center_service.get(employee_id, period, year)

        expected_cost_centers = [CostCenter(employee_id=employee_id, data=cost_center) for cost_center in mock_cost_centers]
        self.assertEqual(result, expected_cost_centers)

        self.client.service.CostCenter_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test getting current cost centers for a specific employee."""
        employee_id = 123
        mock_cost_centers = [
            {"Id": 1, "Code": "CC1", "Description": "Cost Center 1"},
            {"Id": 2, "Code": "CC2", "Description": "Cost Center 2"},
        ]
        self.client.service.CostCenter_GetCurrent.return_value = mock_cost_centers

        result = self.cost_center_service.get_current(employee_id)

        expected_cost_centers = [CostCenter(employee_id=employee_id, data=cost_center) for cost_center in mock_cost_centers]
        self.assertEqual(result, expected_cost_centers)

        self.client.service.CostCenter_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all cost centers for all employees of a company."""
        company_id = 456
        period = 1
        year = 2024
        mock_cost_centers = [
            {"EmployeeId": 123, "CostCenters": {"EmployeeCostCenter": [{"Id": 1, "Code": "CC1", "Description": "Cost Center 1"}]}},
            {"EmployeeId": 456, "CostCenters": {"EmployeeCostCenter": [{"Id": 2, "Code": "CC2", "Description": "Cost Center 2"}]}},
        ]
        self.client.service.CostCenter_GetAllEmployeesByCompany.return_value = mock_cost_centers

        result = self.cost_center_service.get_all_by_company(company_id, period, year)

        expected_cost_centers = [
            CostCenter(employee_id=123, data=mock_cost_centers[0]["CostCenters"]["EmployeeCostCenter"][0]),
            CostCenter(employee_id=456, data=mock_cost_centers[1]["CostCenters"]["EmployeeCostCenter"][0]),
        ]
        self.assertEqual(result, expected_cost_centers)

        self.client.service.CostCenter_GetAllEmployeesByCompany.assert_called_once_with(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_with_no_data(self):
        """Test getting cost centers when no data is returned."""
        employee_id = 123
        period = 1
        year = 2024
        self.client.service.CostCenter_Get.return_value = []

        result = self.cost_center_service.get(employee_id, period, year)

        self.assertEqual(result, [])

    def test_get_current_with_no_data(self):
        """Test getting current cost centers when no data is returned."""
        employee_id = 123
        self.client.service.CostCenter_GetCurrent.return_value = []

        result = self.cost_center_service.get_current(employee_id)

        self.assertEqual(result, [])

    def test_get_all_by_company_with_no_data(self):
        """Test getting all cost centers for all employees of a company when no data is returned."""
        company_id = 456
        period = 1
        year = 2024
        self.client.service.CostCenter_GetAllEmployeesByCompany.return_value = []

        result = self.cost_center_service.get_all_by_company(company_id, period, year)

        self.assertEqual(result, [])
