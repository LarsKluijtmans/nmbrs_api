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
        mock_wage_taxes = [Mock() for _ in range(3)]
        self.client.service.WageTax_GetList.return_value = mock_wage_taxes
        result = self.company_wagetax_service.get_all_wagetax(1, 2024)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(wagetax, WageTax) for wagetax in result))
        self.client.service.WageTax_GetList.assert_called_once_with(CompanyId=1, intYear=2024, _soapheaders=self.mock_auth_header)

    def test_get_wagetax_details(self):
        """Test retrieving wage tax details for a specific company and loonaangifte ID."""
        mock_wagetax_details = Mock()
        self.client.service.WageTax_GetXML.return_value = mock_wagetax_details
        result = self.company_wagetax_service.get_wagetax_details(1, 1)
        self.assertIsInstance(result, WageTaxXML)
        self.client.service.WageTax_GetXML.assert_called_once_with(
            CompanyId=1,
            LoonaangifteID=1,
            _soapheaders=self.mock_auth_header,
        )

    def test_set_send_as_external(self):
        """Test setting the wage tax status to Sent as External."""
        company_id = 123
        loonaangifte_id = 456
        expected_response = True
        self.client.service.WageTax_SetSentExternal.return_value = expected_response

        result = self.company_wagetax_service.set_send_as_external(company_id, loonaangifte_id)

        self.assertEqual(result, expected_response)
        self.client.service.WageTax_SetSentExternal.assert_called_once_with(
            CompanyId=company_id, LoonaangifteID=loonaangifte_id, _soapheaders=self.mock_auth_header
        )
