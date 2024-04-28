"""Unit tests for the CompanyCostUnitService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.company.cost_unit import CompanyCostUnitService, CostUnit


class TestCompanyCostUnitService(unittest.TestCase):
    """Unit tests for the CompanyCostUnitService class."""

    def setUp(self):
        self.client = Mock()
        self.cost_unit_service = CompanyCostUnitService(self.client)
        self.mock_auth_header = Mock()
        self.cost_unit_service.set_auth_header(self.mock_auth_header)

    def test_get_cost_units(self):
        """Test retrieving cost units associated with a company."""
        mock_cost_units = [{"Id": 1, "Code": "CU1", "Description": "Cost Unit 1"}]
        self.client.service.CostUnit_GetList.return_value = mock_cost_units
        result = self.cost_unit_service.get_current(1)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], CostUnit)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "CU1")
        self.assertEqual(result[0].description, "Cost Unit 1")
        self.client.service.CostUnit_GetList.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_insert_cost_unit(self):
        """Test inserting a new cost unit for a company."""
        self.client.service.CostUnit_Insert.return_value = 123
        result = self.cost_unit_service.post(company_id=1, cost_unit_id=456, code="CU2", description="Cost Unit 2")
        self.assertEqual(result, 123)
        self.client.service.CostUnit_Insert.assert_called_once_with(
            CompanyId=1,
            costunit={"Id": 456, "Code": "CU2", "Description": "Cost Unit 2"},
            _soapheaders=self.mock_auth_header,
        )
