"""Unit tests for the DebtorService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.service.debtor_service import DebtorService
from src.nmbrs.data_classes.debtor import (
    Debtor,
    AbsenceVerzuim,
    ContactInfo,
    Department,
    BankAccount,
    Address,
    Function,
    ServiceLevel,
    Tag,
    Manager,
    LabourAgreementSettings,
    Event,
    WebhookSetting,
)


class TestDebtorService(unittest.TestCase):
    """Unit tests for the DebtorService class."""

    def setUp(self):
        self.mock_auth_header = {
            "AuthHeader": {"Username": "test_username", "Token": "test_token"}
        }
        self.mock_debtor_service = Mock()
        self.debtor_service = DebtorService()
        self.debtor_service.debtor_service = self.mock_debtor_service
        self.debtor_service.set_auth_header(self.mock_auth_header)

    def test_get_domain(self):
        """Test getting the domain associated with the token."""
        self.mock_debtor_service.service.Environment_Get.return_value = Mock(
            SubDomain="test_domain"
        )
        domain = self.debtor_service.get_domain("test_username", "test_token")
        self.assertEqual(domain, "test_domain")
        self.mock_debtor_service.service.Environment_Get.assert_called_once_with(
            _soapheaders=self.mock_auth_header
        )

    def test_get_all(self):
        """Test retrieving all debtors."""
        mock_debtors = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.List_GetAll.return_value = mock_debtors
        result = self.debtor_service.get_all()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(debtor, Debtor) for debtor in result))
        self.mock_debtor_service.service.List_GetAll.assert_called_once_with(
            _soapheaders=self.mock_auth_header
        )

    def test_get_absence_xml(self):
        """Test retrieving absence data for a debtor within a specified date range."""
        mock_absences = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.AbsenceXML_Get.return_value = mock_absences
        start_date = datetime.now()
        end_date = datetime.now()
        result = self.debtor_service.get_absence_xml(1, start_date, end_date)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(absence, AbsenceVerzuim) for absence in result))
        self.mock_debtor_service.service.AbsenceXML_Get.assert_called_once_with(
            **{"DebtorId": 1, "from": start_date, "to": end_date},
            _soapheaders=self.mock_auth_header,
        )

    def test_get_all_accountant_contact_info(self):
        """Test retrieving all accountant contact information for a debtor."""
        mock_contact_info = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.AccountantContact_GetList.return_value = (
            mock_contact_info
        )
        result = self.debtor_service.get_all_accountant_contact_info(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(
            all(isinstance(contact_info, ContactInfo) for contact_info in result)
        )
        self.mock_debtor_service.service.AccountantContact_GetList.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_all_departments(self):
        """Test retrieving all departments of a debtor."""
        mock_departments = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.Department_GetList.return_value = (
            mock_departments
        )
        result = self.debtor_service.get_all_departments(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(
            all(isinstance(department, Department) for department in result)
        )
        self.mock_debtor_service.service.Department_GetList.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_all_by_number(self):
        """Test retrieving all debtors by number."""
        mock_debtors = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.List_GetByNumber.return_value = mock_debtors
        result = self.debtor_service.get_all_by_number("test_number")
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(debtor, Debtor) for debtor in result))
        self.mock_debtor_service.service.List_GetByNumber.assert_called_once_with(
            Number="test_number", _soapheaders=self.mock_auth_header
        )

    def test_get(self):
        """Test retrieving a debtor by ID."""
        mock_debtor = Mock()
        self.mock_debtor_service.service.Debtor_Get.return_value = mock_debtor
        result = self.debtor_service.get(1)
        self.assertIsInstance(result, Debtor)
        self.mock_debtor_service.service.Debtor_Get.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_returns_none(self):
        """Test that get returns None when debtor is not found."""
        self.mock_debtor_service.service.Debtor_Get.return_value = None
        result = self.debtor_service.get(0)
        self.assertIsNone(result)
        self.mock_debtor_service.service.Debtor_Get.assert_called_once_with(
            DebtorId=0, _soapheaders=self.mock_auth_header
        )

    def test_insert(self):
        """Test inserting a new debtor."""
        mock_inserted_id = 123
        self.mock_debtor_service.service.Debtor_Insert.return_value = mock_inserted_id
        result = self.debtor_service.insert(1, "test_number", "test_name")
        self.assertEqual(result, mock_inserted_id)
        self.mock_debtor_service.service.Debtor_Insert.assert_called_once_with(
            Debtor={"Id": 1, "Number": "test_number", "Name": "test_name"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update(self):
        """Test updating an existing debtor."""
        self.debtor_service.update(1, "test_number", "test_name")
        self.mock_debtor_service.service.Debtor_Update.assert_called_once_with(
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
        self.mock_debtor_service.service.Address_Get.return_value = mock_address_data
        result = self.debtor_service.get_address(1)
        self.assertIsInstance(result, Address)
        self.mock_debtor_service.service.Address_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_address_returns_none(self):
        """Test that get_address returns None when address is not found."""
        self.mock_debtor_service.service.Address_Get.return_value = None
        result = self.debtor_service.get_address(1)
        self.assertIsNone(result)
        self.mock_debtor_service.service.Address_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_bank_account_returns_bank_account(self):
        """Test that get_bank_account returns a BankAccount object when bank account is found."""
        mock_bank_account_data = {"AccountNumber": "1234567890", "BankName": "Bank XYZ"}
        self.mock_debtor_service.service.BankAccount_Get.return_value = (
            mock_bank_account_data
        )
        result = self.debtor_service.get_bank_account(1)
        self.assertIsInstance(result, BankAccount)
        self.mock_debtor_service.service.BankAccount_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_bank_account_returns_none(self):
        """Test that get_bank_account returns None when bank account is not found."""
        self.mock_debtor_service.service.BankAccount_Get.return_value = None
        result = self.debtor_service.get_bank_account(1)
        self.assertIsNone(result)
        self.mock_debtor_service.service.BankAccount_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_contact_person_returns_contact_info(self):
        """Test that get_contact_person returns a ContactInfo object when contact person is found."""
        mock_contact_person_data = {"Name": "John Doe", "Email": "john@example.com"}
        self.mock_debtor_service.service.ContactPerson_Get.return_value = (
            mock_contact_person_data
        )
        result = self.debtor_service.get_contact_person(1)
        self.assertIsInstance(result, ContactInfo)
        self.mock_debtor_service.service.ContactPerson_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_contact_person_returns_none(self):
        """Test that get_contact_person returns None when contact person is not found."""
        self.mock_debtor_service.service.ContactPerson_Get.return_value = None
        result = self.debtor_service.get_contact_person(1)
        self.assertIsNone(result)
        self.mock_debtor_service.service.ContactPerson_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_is_owner(self):
        """Test that is_owner returns a boolean value."""
        self.debtor_service.is_owner()
        self.mock_debtor_service.service.Debtor_IsOwner.assert_called_with(
            _soapheaders=self.mock_auth_header
        )

    def test_delete_department(self):
        """Test delete_department method."""
        self.debtor_service.delete_department(1, 1)
        self.mock_debtor_service.service.Department_Delete.assert_called_with(
            DebtorId=1, id=1, _soapheaders=self.mock_auth_header
        )

    def test_insert_department(self):
        """Test inserting a new department for a debtor."""
        self.mock_debtor_service.service.Department_Insert.return_value = 123
        result = self.debtor_service.insert_department(1, 2, 3, "test_description")
        self.assertEqual(result, 123)
        self.mock_debtor_service.service.Department_Insert.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update_department(self):
        """Test updating an existing department of a debtor."""
        self.debtor_service.update_department(1, 2, 3, "test_description")
        self.mock_debtor_service.service.Department_Update.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_delete_function(self):
        """Test deleting a function of a debtor."""
        self.debtor_service.delete_function(1, 2)
        self.mock_debtor_service.service.Function_Delete.assert_called_once_with(
            DebtorId=1, id=2, _soapheaders=self.mock_auth_header
        )

    def test_get_all_functions(self):
        """Test retrieving all functions of a debtor."""
        mock_functions = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.Function_GetList.return_value = mock_functions
        result = self.debtor_service.get_all_functions(1, 2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(func, Function) for func in result))
        self.mock_debtor_service.service.Function_GetList.assert_called_once_with(
            DebtorId=1, id=2, _soapheaders=self.mock_auth_header
        )

    def test_insert_function(self):
        """Test inserting a new function for a debtor."""
        self.mock_debtor_service.service.Function_Insert.return_value = 123
        result = self.debtor_service.insert_function(1, 2, 3, "test_description")
        self.assertEqual(result, 123)
        self.mock_debtor_service.service.Function_Insert.assert_called_once_with(
            DebtorId=1,
            function={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update_function(self):
        """Test updating a function for a debtor."""
        self.debtor_service.update_function(1, 2, 3, "test_description")
        self.mock_debtor_service.service.Function_Update.assert_called_once_with(
            DebtorId=1,
            function={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_get_all_labour_agreements(self):
        """Test retrieving all labour agreement settings for a debtor."""
        mock_labour_agreements = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.LabourAgreementSettings_GetList.return_value = (
            mock_labour_agreements
        )
        result = self.debtor_service.get_all_labour_agreements(1, 2024, 3)
        self.assertEqual(len(result), 3)
        self.assertTrue(
            all(
                isinstance(labour_agreement, LabourAgreementSettings)
                for labour_agreement in result
            )
        )
        self.mock_debtor_service.service.LabourAgreementSettings_GetList.assert_called_once_with(
            DebtorId=1, Year=2024, Period=3, _soapheaders=self.mock_auth_header
        )

    def test_get_all_managers(self):
        """Test retrieving all managers for a debtor."""
        mock_managers = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.Manager_GetList.return_value = mock_managers
        result = self.debtor_service.get_all_managers(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(manager, Manager) for manager in result))
        self.mock_debtor_service.service.Manager_GetList.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_service_level(self):
        """Test retrieving service level information for a debtor."""
        self.mock_debtor_service.service.ServiceLevel_Get.return_value = {
            "Level": "Test Level"
        }
        result = self.debtor_service.get_service_level(1)
        self.assertIsInstance(result, ServiceLevel)
        self.mock_debtor_service.service.ServiceLevel_Get.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_service_level_returns_none(self):
        """Test that retrieving service level information for a debtor returns None when information not found."""
        self.mock_debtor_service.service.ServiceLevel_Get.return_value = None
        result = self.debtor_service.get_service_level(1)
        self.assertIsNone(result)
        self.mock_debtor_service.service.ServiceLevel_Get.assert_called_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_tags(self):
        """Test retrieving all tags for a debtor."""
        mock_tags = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.Tags_Get.return_value = mock_tags
        result = self.debtor_service.get_tags(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(tag, Tag) for tag in result))
        self.mock_debtor_service.service.Tags_Get.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_all_titles(self):
        """Test retrieving all titles for a debtor."""
        mock_titles = [
            {"TitleName": "Title1"},
            {"TitleName": "Title2"},
            {"TitleName": "Title3"},
        ]
        self.mock_debtor_service.service.Title_GetList.return_value = mock_titles
        result = self.debtor_service.get_all_titles(1)
        self.assertEqual(result, ["Title1", "Title2", "Title3"])
        self.mock_debtor_service.service.Title_GetList.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_insert_titles(self):
        """Test inserting a title for a debtor."""
        self.debtor_service.insert_titles(1, "Test Title")
        self.mock_debtor_service.service.Title_Insert.assert_called_once_with(
            DebtorId=1,
            title={"TitleName": "Test Title"},
            _soapheaders=self.mock_auth_header,
        )

    def test_delete_webhook(self):
        """Test deleting a webhook for a debtor."""
        self.mock_debtor_service.service.WebhookSettings_Delete.return_value = True
        result = self.debtor_service.delete_webhook(1, 123)
        self.assertTrue(result)
        self.mock_debtor_service.service.WebhookSettings_Delete.assert_called_once_with(
            DebtorId=1, WebhookSettingId=123, _soapheaders=self.mock_auth_header
        )

    def test_get_webhooks(self):
        """Test retrieving all webhooks for a debtor."""
        mock_webhooks = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.WebhookSettings_Get.return_value = (
            mock_webhooks
        )
        result = self.debtor_service.get_webhooks(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(webhook, WebhookSetting) for webhook in result))
        self.mock_debtor_service.service.WebhookSettings_Get.assert_called_once_with(
            DebtorId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_webhook_events(self):
        """Test retrieving all webhook events."""
        mock_events = [Mock() for _ in range(3)]
        self.mock_debtor_service.service.WebhookSettings_GetEvents.return_value = (
            mock_events
        )
        result = self.debtor_service.get_webhook_events()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(event, Event) for event in result))
        self.mock_debtor_service.service.WebhookSettings_GetEvents.assert_called_once_with(
            _soapheaders=self.mock_auth_header
        )

    def test_insert_webhook(self):
        """Test inserting a webhook for a debtor."""
        mock_webhook_setting = Mock(
            to_insert_dict=Mock(return_value={"TestKey": "TestValue"})
        )
        self.mock_debtor_service.service.WebhookSettings_Insert.return_value = 123
        result = self.debtor_service.insert_webhook(1, mock_webhook_setting)
        self.assertEqual(result, 123)
        self.mock_debtor_service.service.WebhookSettings_Insert.assert_called_once_with(
            DebtorId=1,
            WebhookSetting={"TestKey": "TestValue"},
            _soapheaders=self.mock_auth_header,
        )
