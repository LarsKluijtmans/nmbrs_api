"""Test cases for the EmployeeAddressService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.address import EmployeeAddressService, Address


class TestEmployeeAddressService(unittest.TestCase):
    """Test cases for the EmployeeAddressService class."""

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
        self.employee_address_service = EmployeeAddressService(self.auth_manager, self.client)

    def test_get(self):
        """Test the get method."""
        employee_id = 123
        period = 1
        year = 2024
        response_data = [
            {
                "Id": 1,
                "Default": True,
                "Street": "123 Main St",
                "HouseNumber": "1",
                "HouseNumberAddition": None,
                "PostalCode": "12345",
                "City": "City1",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Home",
            },
            {
                "Id": 2,
                "Default": False,
                "Street": "456 Elm St",
                "HouseNumber": "2",
                "HouseNumberAddition": None,
                "PostalCode": "23456",
                "City": "City2",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Work",
            },
        ]
        self.client.service.Address_GetList.return_value = response_data

        response = self.employee_address_service.get(employee_id, period, year)

        self.assertEqual(len(response), 2)
        self.client.service.Address_GetList.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test the get_current method."""
        employee_id = 123
        response_data = [
            {
                "Id": 1,
                "Default": True,
                "Street": "123 Main St",
                "HouseNumber": "1",
                "HouseNumberAddition": None,
                "PostalCode": "12345",
                "City": "City1",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Home",
            },
            {
                "Id": 2,
                "Default": False,
                "Street": "456 Elm St",
                "HouseNumber": "2",
                "HouseNumberAddition": None,
                "PostalCode": "23456",
                "City": "City2",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Work",
            },
        ]
        self.client.service.Address_GetListCurrent.return_value = response_data

        response = self.employee_address_service.get_current(employee_id)

        self.assertEqual(len(response), 2)
        for item in response:
            self.assertIsInstance(item, Address)
        self.client.service.Address_GetListCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test the get_all_by_company method."""
        company_id = 456
        response_data = [
            {
                "EmployeeId": 123,
                "EmployeeAddresses": {
                    "EmployeeAddress_V2": [
                        {
                            "Id": 1,
                            "Default": True,
                            "Street": "123 Main St",
                            "HouseNumber": "1",
                            "HouseNumberAddition": None,
                            "PostalCode": "12345",
                            "City": "City1",
                            "StateProvince": None,
                            "CountryISOCode": "US",
                            "Type": "Home",
                        },
                        {
                            "Id": 2,
                            "Default": False,
                            "Street": "456 Elm St",
                            "HouseNumber": "2",
                            "HouseNumberAddition": None,
                            "PostalCode": "23456",
                            "City": "City2",
                            "StateProvince": None,
                            "CountryISOCode": "US",
                            "Type": "Work",
                        },
                    ]
                },
            },
            {
                "EmployeeId": 456,
                "EmployeeAddresses": {
                    "EmployeeAddress_V2": [
                        {
                            "Id": 3,
                            "Default": True,
                            "Street": "789 Oak St",
                            "HouseNumber": "3",
                            "HouseNumberAddition": None,
                            "PostalCode": "34567",
                            "City": "City3",
                            "StateProvince": None,
                            "CountryISOCode": "US",
                            "Type": "Home",
                        },
                    ]
                },
            },
        ]
        self.client.service.Address_GetAll_AllEmployeesByCompany.return_value = response_data

        response = self.employee_address_service.get_all_by_company(company_id)

        self.assertEqual(len(response), 3)
        for item in response:
            self.assertIsInstance(item, Address)
        self.client.service.Address_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_delete(self):
        """Test the delete method."""
        employee_id = 123
        address_id = 1
        self.client.service.Address_Delete.return_value = True

        response = self.employee_address_service.delete(employee_id, address_id)

        self.assertTrue(response)
        self.client.service.Address_Delete.assert_called_once_with(
            EmployeeId=employee_id, AddressID=address_id, _soapheaders=self.mock_auth_header
        )

    def test_update(self):
        """Test the update method."""
        employee_id = 123
        address = Address(
            employee_id=employee_id,
            data={
                "Id": 1,
                "Default": True,
                "Street": "123 Main St",
                "HouseNumber": "1",
                "HouseNumberAddition": None,
                "PostalCode": "12345",
                "City": "City1",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Home",
            },
        )
        self.client.service.Address_Update.return_value = True

        response = self.employee_address_service.update(employee_id, address)

        self.assertTrue(response)
        self.client.service.Address_Update.assert_called_once_with(
            EmployeeId=employee_id,
            Address={
                "Id": address.id,
                "Default": address.default,
                "Street": address.street,
                "HouseNumber": address.house_number,
                "HouseNumberAddition": address.house_number_addition,
                "PostalCode": address.postcode,
                "City": address.city,
                "StateProvince": address.state_province,
                "CountryISOCode": address.country_iso_code,
                "Type": address.type,
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_insert(self):
        """Test the insert method."""
        employee_id = 123
        period = 1
        year = 2024
        unprotected_mode = False
        address = Address(
            employee_id=employee_id,
            data={
                "Id": 1,
                "Default": True,
                "Street": "123 Main St",
                "HouseNumber": "1",
                "HouseNumberAddition": None,
                "PostalCode": "12345",
                "City": "City1",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Home",
            },
        )
        self.client.service.Address_Insert.return_value = 1

        response = self.employee_address_service.post(employee_id, address, period, year, unprotected_mode)

        self.assertEqual(response, 1)
        self.client.service.Address_Insert.assert_called_once_with(
            EmployeeId=employee_id,
            Address={
                "Id": address.id,
                "Default": address.default,
                "Street": address.street,
                "HouseNumber": address.house_number,
                "HouseNumberAddition": address.house_number_addition,
                "PostalCode": address.postcode,
                "City": address.city,
                "StateProvince": address.state_province,
                "CountryISOCode": address.country_iso_code,
                "Type": address.type,
            },
            Period=period,
            Year=year,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_current(self):
        """Test the insert_current method."""
        employee_id = 123
        address = Address(
            employee_id=employee_id,
            data={
                "Id": 1,
                "Default": True,
                "Street": "123 Main St",
                "HouseNumber": "1",
                "HouseNumberAddition": None,
                "PostalCode": "12345",
                "City": "City1",
                "StateProvince": None,
                "CountryISOCode": "US",
                "Type": "Home",
            },
        )
        self.client.service.Address_InsertCurrent.return_value = 1

        response = self.employee_address_service.post_current(employee_id, address)

        self.assertEqual(response, 1)
        self.client.service.Address_InsertCurrent.assert_called_once_with(
            EmployeeId=employee_id,
            Address={
                "Id": address.id,
                "Default": address.default,
                "Street": address.street,
                "HouseNumber": address.house_number,
                "HouseNumberAddition": address.house_number_addition,
                "PostalCode": address.postcode,
                "City": address.city,
                "StateProvince": address.state_province,
                "CountryISOCode": address.country_iso_code,
                "Type": address.type,
            },
            _soapheaders=self.mock_auth_header,
        )
