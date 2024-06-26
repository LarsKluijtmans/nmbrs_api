"""Unit tests for the CompanyCostCenterService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.cost_center import CompanyCostCenterService, CostCenter


class TestCompanyCostCenterService(unittest.TestCase):
    """Unit tests for the CompanyCostCenterService class."""

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
        self.cost_center_service = CompanyCostCenterService(self.auth_manager, self.client)

    def test_get_cost_centers(self):
        """Test retrieving cost centers associated with a company."""
        mock_cost_centers = [{"Id": 1, "Code": "CC1", "Description": "Cost Center 1"}]
        self.client.service.CostCenter_GetList.return_value = mock_cost_centers
        result = self.cost_center_service.get_current(1)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], CostCenter)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "CC1")
        self.assertEqual(result[0].description, "Cost Center 1")
        self.client.service.CostCenter_GetList.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_insert_cost_center(self):
        """Test inserting a new cost center for a company."""
        self.client.service.CostCenter_Insert.return_value = 123
        result = self.cost_center_service.post(company_id=1, cost_center_id=456, code="CC2", description="Cost Center 2")
        self.assertEqual(result, 123)
        self.client.service.CostCenter_Insert.assert_called_once_with(
            CompanyId=1,
            kostenplaats={"Id": 456, "Code": "CC2", "Description": "Cost Center 2"},
            _soapheaders=self.mock_auth_header,
        )
