"""Unit tests for the CompanyService class."""
import unittest
from unittest.mock import Mock
from src.nmbrs.service.company_service import CompanyService, Company, WageTax, WageTaxXML


class TestCompanyService(unittest.TestCase):
    """Unit tests for the CompanyService class."""

    def setUp(self):
        self.company_service = CompanyService()
        self.mock_auth_header = Mock()
        self.mock_company_service = Mock()
        self.company_service.company_service = self.mock_company_service
        self.company_service.set_auth_header(self.mock_auth_header)

    def test_get_all(self):
        """Test retrieving all companies."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_company_service.service.List_GetAll.return_value = mock_companies
        result = self.company_service.get_all()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(company, Company) for company in result))
        self.mock_company_service.service.List_GetAll.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_all_wagetax(self):
        """Test retrieving all wage taxes for a specific company and year."""
        mock_wagetaxes = [Mock() for _ in range(3)]
        self.mock_company_service.service.WageTax_GetList.return_value = mock_wagetaxes
        result = self.company_service.get_all_wagetax(1, 2024)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(wagetax, WageTax) for wagetax in result))
        self.mock_company_service.service.WageTax_GetList.assert_called_once_with(
            CompanyId=1,
            intYear=2024,
            _soapheaders=self.mock_auth_header
        )

    def test_get_wagetax_details(self):
        """Test retrieving wage tax details for a specific company and loonaangifte ID."""
        mock_wagetax_details = Mock()
        self.mock_company_service.service.WageTax_GetXML.return_value = mock_wagetax_details
        result = self.company_service.get_wagetax_details(1, 'loonaangifte_id')
        self.assertIsInstance(result, WageTaxXML)
        self.mock_company_service.service.WageTax_GetXML.assert_called_once_with(
            CompanyId=1,
            LoonaangifteID='loonaangifte_id',
            _soapheaders=self.mock_auth_header
        )
