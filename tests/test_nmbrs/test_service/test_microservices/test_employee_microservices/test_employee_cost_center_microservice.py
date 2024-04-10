"""Unit tests for the EmployeeCostCenterService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.employee.cost_center import EmployeeCostCenterService, CostCenter


class TestEmployeeCostCenterService(unittest.TestCase):
    """Unit tests for the EmployeeCostCenterService class."""

    def setUp(self):
        self.client = Mock()
        self.cost_center_service = EmployeeCostCenterService(self.client)
        self.mock_auth_header = Mock()
        self.cost_center_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all cost centers for all employees in a company."""
        company_id = 123
        period = 1
        year = 2024
        self.client.service.CostCenter_GetAllEmployeesByCompany.return_value = [
            {"EmployeeId": 1, "CostCenters": {"EmployeeCostCenter": [{"Id": 1, "Code": "CC1", "Description": "Cost Center 1"}]}},
            {"EmployeeId": 2, "CostCenters": {"EmployeeCostCenter": [{"Id": 2, "Code": "CC2", "Description": "Cost Center 2"}]}},
        ]

        result = self.cost_center_service.get_all_by_company(company_id, period, year)

        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, CostCenter)
        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "CC1")
        self.assertEqual(result[0].description, "Cost Center 1")

        self.assertEqual(result[1].employee_id, 2)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].code, "CC2")
        self.assertEqual(result[1].description, "Cost Center 2")

        self.client.service.CostCenter_GetAllEmployeesByCompany.assert_called_once_with(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )
