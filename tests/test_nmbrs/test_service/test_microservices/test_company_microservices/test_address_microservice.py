"""Unit tests for the CompanyAddressService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.company.address import (
    CompanyAddressService,
    Address,
)


class TestCompanyAddressService(unittest.TestCase):
    """Unit tests for the CompanyAddressService class."""

    def setUp(self):
        self.client = Mock()
        self.company_address_service = CompanyAddressService(self.client)
        self.mock_auth_header = Mock()
        self.company_address_service.set_auth_header(self.mock_auth_header)

    def test_get_address(self):
        """Test retrieving the current address of the company."""
        mock_address = Mock()
        self.client.service.Address_GetCurrent.return_value = mock_address
        result = self.company_address_service.get_current(1)
        self.assertIsInstance(result, Address)
        self.client.service.Address_GetCurrent.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_address_returns_none(self):
        """Test that get returns None when debtor is not found."""
        self.client.service.Address_GetCurrent.return_value = None
        result = self.company_address_service.get_current(1)
        self.assertEqual(result, None)
        self.client.service.Address_GetCurrent.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_insert_address(self):
        """Test inserting a new address for the company."""
        self.client.service.Address_Insert.return_value = 123
        result = self.company_address_service.post(
            company_id=1,
            address_id=456,
            default=True,
            street="Mock Street",
            house_number="123",
            house_number_addon="A",
            postal_code="12345",
            city="Mock City",
            state_province="Mock State",
            country_iso_code="MO",
        )
        self.assertEqual(result, 123)
        self.client.service.Address_Insert.assert_called_once_with(
            CompanyId=1,
            Address={
                "Id": 456,
                "Default": True,
                "Street": "Mock Street",
                "HouseNumber": "123",
                "HouseNumberAddition": "A",
                "PostalCode": "12345",
                "City": "Mock City",
                "StateProvince": "Mock State",
                "CountryISOCode": "MO",
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_update_address(self):
        """Test updating an existing address for the company."""
        self.company_address_service.update(
            company_id=1,
            address_id=456,
            default=True,
            street="Mock Street",
            house_number="123",
            house_number_addon="A",
            postal_code="12345",
            city="Mock City",
            state_province="Mock State",
            country_iso_code="MO",
        )
        self.client.service.Address_Update.assert_called_once_with(
            CompanyId=1,
            Address={
                "Id": 456,
                "Default": True,
                "Street": "Mock Street",
                "HouseNumber": "123",
                "HouseNumberAddition": "A",
                "PostalCode": "12345",
                "City": "Mock City",
                "StateProvince": "Mock State",
                "CountryISOCode": "MO",
            },
            _soapheaders=self.mock_auth_header,
        )
