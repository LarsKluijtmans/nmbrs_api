"""Unit tests for the CompanyWageTaxService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.company.wage_tax import (
    CompanyWageTaxService,
    WageTax,
    WageTaxXML,
)


class TestCompanyWageTaxService(unittest.TestCase):
    """Unit tests for the CompanyWageTaxService class."""

    def setUp(self):
        self.client = Mock()
        self.company_wagetax_service = CompanyWageTaxService(self.client)
        self.mock_auth_header = Mock()
        self.company_wagetax_service.set_auth_header(self.mock_auth_header)

    def test_get_all_wagetax(self):
        """Test retrieving all wage taxes for a specific company and year."""
        mock_wagetaxes = [Mock() for _ in range(3)]
        self.client.service.WageTax_GetList.return_value = mock_wagetaxes
        result = self.company_wagetax_service.get_all_wagetax(1, 2024)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(wagetax, WageTax) for wagetax in result))
        self.client.service.WageTax_GetList.assert_called_once_with(CompanyId=1, intYear=2024, _soapheaders=self.mock_auth_header)

    def test_get_wagetax_details(self):
        """Test retrieving wage tax details for a specific company and loonaangifte ID."""
        mock_wagetax_details = Mock()
        self.client.service.WageTax_GetXML.return_value = mock_wagetax_details
        result = self.company_wagetax_service.get_wagetax_details(1, "loonaangifte_id")
        self.assertIsInstance(result, WageTaxXML)
        self.client.service.WageTax_GetXML.assert_called_once_with(
            CompanyId=1,
            LoonaangifteID="loonaangifte_id",
            _soapheaders=self.mock_auth_header,
        )
