"""Unit tests for the EmployeePersonalInfoService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from src.nmbrs.service.microservices.employee.personal_info import (
    EmployeePersonalInfoService,
    PersonalInfo,
    PersonalInfoContractSalaryAddress,
)


class TestEmployeePersonalInfoService(unittest.TestCase):
    """Unit tests for the EmployeePersonalInfoService class."""

    def setUp(self):
        self.client = Mock()
        self.personal_info_service = EmployeePersonalInfoService(self.client)
        self.mock_auth_header = Mock()
        self.personal_info_service.set_auth_header(self.mock_auth_header)

    def test_get(self):
        """Test retrieving personal information for a given employee, period, and year."""
        employee_id = 123
        period = 1
        year = 2023
        expected_personal_info = {
            "EmployeeNumber": 123,
            "BSN": "123456789",
            "FirstName": "John",
            "LastName": "Doe",
            "Gender": "Male",
            "NationalityCode": 1,
            "PlaceOfBirth": "New York",
            "CountryOfBirthISOCode": "US",
            "IdentificationNumber": "ID123",
            "IdentificationType": 1,
            "PartnerPrefix": "Mr.",
            "PartnerLastName": "Smith",
            "TelephonePrivate": "123456789",
            "TelephoneWork": "987654321",
            "TelephoneMobilePrivate": "987654321",
            "TelephoneMobileWork": "123456789",
            "TelephoneOther": "456789123",
            "EmailPrivate": "john.doe@example.com",
            "EmailWork": "john.doe@work.com",
            "BurgerlijkeStaat": "Single",
            "Naamstelling": "Doe",
            "Birthday": datetime(1990, 1, 1),
            "DeceasedDate": None,
            "InCaseOfEmergency": "Jane Doe",
            "InCaseOfEmergencyPhone": "987654321",
            "InCaseOfEmergencyRelation": "Spouse",
            "TitleAfter": "Mr.",
        }
        self.client.service.PersonalInfo_Get.return_value = expected_personal_info

        result = self.personal_info_service.get(employee_id, period, year)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, PersonalInfo)

        self.client.service.PersonalInfo_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_return_none(self):
        """Test retrieving personal information for a given employee, period, and year. Nothing is returned."""
        employee_id = 123
        period = 1
        year = 2023

        self.client.service.PersonalInfo_Get.return_value = None

        result = self.personal_info_service.get(employee_id, period, year)

        self.assertIsNone(result)

        self.client.service.PersonalInfo_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test retrieving the currently active personal information for a given employee."""
        employee_id = 123
        expected_personal_info = {
            "EmployeeNumber": 123,
            "BSN": "123456789",
            "FirstName": "John",
            "LastName": "Doe",
            "Gender": "Male",
            "NationalityCode": 1,
            "PlaceOfBirth": "New York",
            "CountryOfBirthISOCode": "US",
            "IdentificationNumber": "ID123",
            "IdentificationType": 1,
            "PartnerPrefix": "Mr.",
            "PartnerLastName": "Smith",
            "TelephonePrivate": "123456789",
            "TelephoneWork": "987654321",
            "TelephoneMobilePrivate": "987654321",
            "TelephoneMobileWork": "123456789",
            "TelephoneOther": "456789123",
            "EmailPrivate": "john.doe@example.com",
            "EmailWork": "john.doe@work.com",
            "BurgerlijkeStaat": "Single",
            "Naamstelling": "Doe",
            "Birthday": datetime(1990, 1, 1),
            "DeceasedDate": None,
            "InCaseOfEmergency": "Jane Doe",
            "InCaseOfEmergencyPhone": "987654321",
            "InCaseOfEmergencyRelation": "Spouse",
            "TitleAfter": "Mr.",
        }
        self.client.service.PersonalInfo_GetCurrent.return_value = expected_personal_info

        result = self.personal_info_service.get_current(employee_id)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, PersonalInfo)

        self.client.service.PersonalInfo_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_current_return_none(self):
        """Test retrieving the currently active personal information for a given employee. Nothing is returned."""
        employee_id = 123

        self.client.service.PersonalInfo_GetCurrent.return_value = None

        result = self.personal_info_service.get_current(employee_id)

        self.assertIsNone(result)

        self.client.service.PersonalInfo_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test retrieving personal information for all employees within a company."""
        company_id = 321
        expected_personal_info = [
            {
                "EmployeeId": 444,
                "EmployeePersonalInfos": {
                    "PersonalInfo_V2": [
                        {
                            "EmployeeNumber": 555,
                        },
                        {
                            "EmployeeNumber": 666,
                        },
                    ]
                },
            },
            {
                "EmployeeId": 111,
                "EmployeePersonalInfos": {
                    "PersonalInfo_V2": [
                        {
                            "EmployeeNumber": 222,
                        },
                        {
                            "EmployeeNumber": 333,
                        },
                    ]
                },
            },
        ]
        self.client.service.PersonalInfo_GetAll_AllEmployeesByCompany.return_value = expected_personal_info

        result = self.personal_info_service.get_all_by_company(company_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        for item in result:
            self.assertIsInstance(item, PersonalInfo)
        self.client.service.PersonalInfo_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_get_all_by_company_without_bsn(self):
        """Test retrieving personal information for all employees within a company excluding BSN."""
        company_id = 321
        expected_personal_info = [
            {
                "EmployeeId": 444,
                "EmployeePersonalInfos": {
                    "PersonalInfo_V2": [
                        {
                            "EmployeeNumber": 555,
                        },
                        {
                            "EmployeeNumber": 666,
                        },
                    ]
                },
            },
            {
                "EmployeeId": 111,
                "EmployeePersonalInfos": {
                    "PersonalInfo_V2": [
                        {
                            "EmployeeNumber": 222,
                        },
                        {
                            "EmployeeNumber": 333,
                        },
                    ]
                },
            },
        ]
        self.client.service.PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany.return_value = expected_personal_info

        result = self.personal_info_service.get_all_by_company_without_bsn(company_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        for item in result:
            self.assertIsInstance(item, PersonalInfo)
        self.client.service.PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_get_all_by_company_contract_address_salary(self):
        """Test retrieving personal, contract, salary, and address information for all employees within a company."""
        company_id = 101112
        expected_personal_info = [
            {
                "EmployeeID": 123,
            },
            {
                "EmployeeID": 456,
            },
        ]
        self.client.service.PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany.return_value = expected_personal_info

        result = self.personal_info_service.get_all_by_company_contract_address_salary(company_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        for item in result:
            self.assertIsInstance(item, PersonalInfoContractSalaryAddress)

        self.client.service.PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_update(self):
        """Test updating personal info starting from a given period."""
        employee_id = 123
        period = 202203
        year = 2022
        personal_info = PersonalInfo(
            employee_id=employee_id,
            data={
                "EmployeeNumber": 123,
                "BSN": "123456789",
                "FirstName": "John",
                "LastName": "Doe",
                "Gender": "Male",
                "NationalityCode": 1,
                "PlaceOfBirth": "New York",
                "CountryOfBirthISOCode": "US",
                "IdentificationNumber": "ID123",
                "IdentificationType": 1,
                "PartnerPrefix": "Mr.",
                "PartnerLastName": "Smith",
                "TelephonePrivate": "123456789",
                "TelephoneWork": "987654321",
                "TelephoneMobilePrivate": "987654321",
                "TelephoneMobileWork": "123456789",
                "TelephoneOther": "456789123",
                "EmailPrivate": "john.doe@example.com",
                "EmailWork": "john.doe@work.com",
                "BurgerlijkeStaat": "Single",
                "Naamstelling": "Doe",
                "Birthday": datetime(1990, 1, 1),
                "DeceasedDate": None,
                "InCaseOfEmergency": "Jane Doe",
                "InCaseOfEmergencyPhone": "987654321",
                "InCaseOfEmergencyRelation": "Spouse",
                "TitleAfter": "Mr.",
            },
        )
        self.client.service.PersonalInfo_Update.return_value = True

        result = self.personal_info_service.update(employee_id, personal_info, period, year)

        self.assertTrue(result)
        self.client.service.PersonalInfo_Update.assert_called_once_with(
            EmployeeId=employee_id,
            PersonalInfo={
                "Id": employee_id,
                "Number": 123,
                "EmployeeNumber": 123,
                "BSN": "123456789",
                "Title": None,
                "FirstName": "John",
                "Initials": None,
                "Prefix": None,
                "LastName": "Doe",
                "Nickname": None,
                "Gender": "Male",
                "NationalityCode": 1,
                "PlaceOfBirth": "New York",
                "CountryOfBirthISOCode": "US",
                "IdentificationNumber": "ID123",
                "IdentificationType": 1,
                "PartnerPrefix": "Mr.",
                "PartnerLastName": "Smith",
                "TelephonePrivate": "123456789",
                "TelephoneWork": "987654321",
                "TelephoneMobilePrivate": "987654321",
                "TelephoneMobileWork": "123456789",
                "TelephoneOther": "456789123",
                "EmailPrivate": "john.doe@example.com",
                "EmailWork": "john.doe@work.com",
                "BurgerlijkeStaat": "Single",
                "Naamstelling": "Doe",
                "Birthday": datetime(1990, 1, 1),
                "DeceasedDate": None,
                "InCaseOfEmergency": "Jane Doe",
                "InCaseOfEmergencyPhone": "987654321",
                "InCaseOfEmergencyRelation": "Spouse",
                "TitleAfter": "Mr.",
            },
            Period=period,
            Year=year,
            _soapheaders=self.mock_auth_header,
        )

    def test_update_current(self):
        """Test updating personal info starting from the current period."""
        employee_id = 123
        personal_info = PersonalInfo(
            employee_id=employee_id,
            data={
                "EmployeeNumber": 123,
                "BSN": "123456789",
                "FirstName": "John",
                "LastName": "Doe",
                "Gender": "Male",
                "NationalityCode": 1,
                "PlaceOfBirth": "New York",
                "CountryOfBirthISOCode": "US",
                "IdentificationNumber": "ID123",
                "IdentificationType": 1,
                "PartnerPrefix": "Mr.",
                "PartnerLastName": "Smith",
                "TelephonePrivate": "123456789",
                "TelephoneWork": "987654321",
                "TelephoneMobilePrivate": "987654321",
                "TelephoneMobileWork": "123456789",
                "TelephoneOther": "456789123",
                "EmailPrivate": "john.doe@example.com",
                "EmailWork": "john.doe@work.com",
                "BurgerlijkeStaat": "Single",
                "Naamstelling": "Doe",
                "Birthday": datetime(1990, 1, 1),
                "DeceasedDate": None,
                "InCaseOfEmergency": "Jane Doe",
                "InCaseOfEmergencyPhone": "987654321",
                "InCaseOfEmergencyRelation": "Spouse",
                "TitleAfter": "Mr.",
            },
        )
        self.client.service.PersonalInfo_UpdateCurrent.return_value = True

        result = self.personal_info_service.update_current(employee_id, personal_info)

        self.assertTrue(result)
        self.client.service.PersonalInfo_UpdateCurrent.assert_called_once_with(
            EmployeeId=employee_id,
            PersonalInfo={
                "Id": employee_id,
                "Number": 123,
                "EmployeeNumber": 123,
                "BSN": "123456789",
                "Title": None,
                "FirstName": "John",
                "Initials": None,
                "Prefix": None,
                "LastName": "Doe",
                "Nickname": None,
                "Gender": "Male",
                "NationalityCode": 1,
                "PlaceOfBirth": "New York",
                "CountryOfBirthISOCode": "US",
                "IdentificationNumber": "ID123",
                "IdentificationType": 1,
                "PartnerPrefix": "Mr.",
                "PartnerLastName": "Smith",
                "TelephonePrivate": "123456789",
                "TelephoneWork": "987654321",
                "TelephoneMobilePrivate": "987654321",
                "TelephoneMobileWork": "123456789",
                "TelephoneOther": "456789123",
                "EmailPrivate": "john.doe@example.com",
                "EmailWork": "john.doe@work.com",
                "BurgerlijkeStaat": "Single",
                "Naamstelling": "Doe",
                "Birthday": datetime(1990, 1, 1),
                "DeceasedDate": None,
                "InCaseOfEmergency": "Jane Doe",
                "InCaseOfEmergencyPhone": "987654321",
                "InCaseOfEmergencyRelation": "Spouse",
                "TitleAfter": "Mr.",
            },
            _soapheaders=self.mock_auth_header,
        )
