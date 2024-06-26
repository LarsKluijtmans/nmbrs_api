"""Unit tests for the DebtorService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.service import DebtorService
from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.debtor import (
    Debtor,
    AbsenceVerzuim,
    ContactInfo,
    BankAccount,
    Address,
    ServiceLevel,
    Tag,
    Manager,
    LabourAgreementSettings,
    Domain,
)


class TestDebtorService(unittest.TestCase):
    """Unit tests for the DebtorService class."""

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
        self.debtor_service = DebtorService(self.auth_manager)
        self.mock_client = Mock()
        self.debtor_service.client = self.mock_client

    def test_get_domain(self):
        """Test getting the domain associated with the token."""
        self.mock_client.service.Environment_Get.return_value = {"Domain": "domain", "SubDomain": "test_domain"}
        domain = self.debtor_service.get_domain("test_username", "test_token")
        self.assertIsInstance(domain, Domain)
        self.assertEqual(domain.domain, "domain")
        self.assertEqual(domain.sub_domain, "test_domain")
        self.mock_client.service.Environment_Get.assert_called_once_with(
            _soapheaders={"AuthHeader": {"Username": "test_username", "Token": "test_token"}}
        )

    def test_get_all(self):
        """Test retrieving all debtors."""
        mock_debtors = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetAll.return_value = mock_debtors
        result = self.debtor_service.get_all()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(debtor, Debtor) for debtor in result))
        self.mock_client.service.List_GetAll.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_absence_xml(self):
        """Test retrieving absence data for a debtor within a specified date range."""
        mock_absences = [Mock() for _ in range(3)]
        self.mock_client.service.AbsenceXML_Get.return_value = mock_absences
        start_date = datetime.now()
        end_date = datetime.now()
        result = self.debtor_service.get_absence_xml(1, start_date, end_date)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(absence, AbsenceVerzuim) for absence in result))
        self.mock_client.service.AbsenceXML_Get.assert_called_once_with(
            **{"DebtorId": 1, "from": start_date, "to": end_date},
            _soapheaders=self.mock_auth_header,
        )

    def test_get_all_accountant_contact_info(self):
        """Test retrieving all accountant contact information for a debtor."""
        mock_contact_info = [Mock() for _ in range(3)]
        self.mock_client.service.AccountantContact_GetList.return_value = mock_contact_info
        result = self.debtor_service.get_all_accountant_contact_info(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(contact_info, ContactInfo) for contact_info in result))
        self.mock_client.service.AccountantContact_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_all_by_number(self):
        """Test retrieving all debtors by number."""
        mock_debtors = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByNumber.return_value = mock_debtors
        result = self.debtor_service.get_all_by_number("test_number")
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(debtor, Debtor) for debtor in result))
        self.mock_client.service.List_GetByNumber.assert_called_once_with(Number="test_number", _soapheaders=self.mock_auth_header)

    def test_get(self):
        """Test retrieving a debtor by ID."""
        mock_debtor = Mock()
        self.mock_client.service.Debtor_Get.return_value = mock_debtor
        result = self.debtor_service.get(1)
        self.assertIsInstance(result, Debtor)
        self.mock_client.service.Debtor_Get.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_returns_none(self):
        """Test that get returns None when debtor is not found."""
        self.mock_client.service.Debtor_Get.return_value = None
        result = self.debtor_service.get(0)
        self.assertIsNone(result)
        self.mock_client.service.Debtor_Get.assert_called_once_with(DebtorId=0, _soapheaders=self.mock_auth_header)

    def test_insert(self):
        """Test inserting a new debtor."""
        mock_inserted_id = 123
        self.mock_client.service.Debtor_Insert.return_value = mock_inserted_id
        result = self.debtor_service.post(1, "test_number", "test_name")
        self.assertEqual(result, mock_inserted_id)
        self.mock_client.service.Debtor_Insert.assert_called_once_with(
            Debtor={"Id": 1, "Number": "test_number", "Name": "test_name"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update(self):
        """Test updating an existing debtor."""
        self.debtor_service.update(1, "test_number", "test_name")
        self.mock_client.service.Debtor_Update.assert_called_once_with(
            Debtor={"Id": 1, "Number": "test_number", "Name": "test_name"},
            _soapheaders=self.mock_auth_header,
        )

    def test_get_address_returns_address(self):
        """Test that get_address returns an Address object when address is found."""
        mock_address_data = {
            "Street": "123 Main St",
            "City": "City",
            "PostalCode": "12345",
        }
        self.mock_client.service.Address_Get.return_value = mock_address_data
        result = self.debtor_service.get_address(1)
        self.assertIsInstance(result, Address)
        self.mock_client.service.Address_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_address_returns_none(self):
        """Test that get_address returns None when address is not found."""
        self.mock_client.service.Address_Get.return_value = None
        result = self.debtor_service.get_address(1)
        self.assertIsNone(result)
        self.mock_client.service.Address_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_bank_account_returns_bank_account(self):
        """Test that get_bank_account returns a BankAccount object when bank account is found."""
        mock_bank_account_data = {"AccountNumber": "1234567890", "BankName": "Bank XYZ"}
        self.mock_client.service.BankAccount_Get.return_value = mock_bank_account_data
        result = self.debtor_service.get_bank_account(1)
        self.assertIsInstance(result, BankAccount)
        self.mock_client.service.BankAccount_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_bank_account_returns_none(self):
        """Test that get_bank_account returns None when bank account is not found."""
        self.mock_client.service.BankAccount_Get.return_value = None
        result = self.debtor_service.get_bank_account(1)
        self.assertIsNone(result)
        self.mock_client.service.BankAccount_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_contact_person_returns_contact_info(self):
        """Test that get_contact_person returns a ContactInfo object when contact person is found."""
        mock_contact_person_data = {"Name": "John Doe", "Email": "john@example.com"}
        self.mock_client.service.ContactPerson_Get.return_value = mock_contact_person_data
        result = self.debtor_service.get_contact_person(1)
        self.assertIsInstance(result, ContactInfo)
        self.mock_client.service.ContactPerson_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_contact_person_returns_none(self):
        """Test that get_contact_person returns None when contact person is not found."""
        self.mock_client.service.ContactPerson_Get.return_value = None
        result = self.debtor_service.get_contact_person(1)
        self.assertIsNone(result)
        self.mock_client.service.ContactPerson_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_is_owner(self):
        """Test that is_owner returns a boolean value."""
        self.debtor_service.is_owner()
        self.mock_client.service.Debtor_IsOwner.assert_called_with(_soapheaders=self.mock_auth_header)

    def test_get_all_labour_agreements(self):
        """Test retrieving all labour agreement settings for a debtor."""
        mock_labour_agreements = [Mock() for _ in range(3)]
        self.mock_client.service.LabourAgreementSettings_GetList.return_value = mock_labour_agreements
        result = self.debtor_service.get_all_labour_agreements(1, 3, 2024)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(labour_agreement, LabourAgreementSettings) for labour_agreement in result))
        self.mock_client.service.LabourAgreementSettings_GetList.assert_called_once_with(
            DebtorId=1, Year=2024, Period=3, _soapheaders=self.mock_auth_header
        )

    def test_get_all_managers(self):
        """Test retrieving all managers for a debtor."""
        mock_managers = [Mock() for _ in range(3)]
        self.mock_client.service.Manager_GetList.return_value = mock_managers
        result = self.debtor_service.get_all_managers(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(manager, Manager) for manager in result))
        self.mock_client.service.Manager_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_service_level(self):
        """Test retrieving service level information for a debtor."""
        self.mock_client.service.ServiceLevel_Get.return_value = {"Level": "Test Level"}
        result = self.debtor_service.get_service_level(1)
        self.assertIsInstance(result, ServiceLevel)
        self.mock_client.service.ServiceLevel_Get.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_service_level_returns_none(self):
        """Test that retrieving service level information for a debtor returns None when information not found."""
        self.mock_client.service.ServiceLevel_Get.return_value = None
        result = self.debtor_service.get_service_level(1)
        self.assertIsNone(result)
        self.mock_client.service.ServiceLevel_Get.assert_called_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_tags(self):
        """Test retrieving all tags for a debtor."""
        mock_tags = [Mock() for _ in range(3)]
        self.mock_client.service.Tags_Get.return_value = mock_tags
        result = self.debtor_service.get_tags(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(tag, Tag) for tag in result))
        self.mock_client.service.Tags_Get.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)
