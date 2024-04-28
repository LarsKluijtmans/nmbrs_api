"""Unit tests for the CompanyBankAccountService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.bank_account import (
    CompanyBankAccountService,
    BankAccount,
)


class TestCompanyBankAccountService(unittest.TestCase):
    """Unit tests for the CompanyBankAccountService class."""

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
        self.bank_account_service = CompanyBankAccountService(self.auth_manager, self.client)

    def test_get_current_bank_account(self):
        """Test retrieving the current bank account of the company."""
        mock_bank_account = Mock()
        self.client.service.BankAccount_GetCurrent.return_value = mock_bank_account
        result = self.bank_account_service.get_current(1)
        self.assertIsInstance(result, BankAccount)
        self.client.service.BankAccount_GetCurrent.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_current_bank_account_returns_none(self):
        """Test that get_current returns None when bank account is not found."""
        self.client.service.BankAccount_GetCurrent.return_value = None
        result = self.bank_account_service.get_current(1)
        self.assertEqual(result, None)
        self.client.service.BankAccount_GetCurrent.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_insert_bank_account(self):
        """Test inserting a new bank account for the company."""
        self.client.service.BankAccount_Insert.return_value = 123
        result = self.bank_account_service.post(
            company_id=1,
            account_id=456,
            account_number="123456789",
            description="Mock Bank Account",
            iban="IBAN123",
            bic="BIC123",
            city="Mock City",
            name="Mock Bank",
            account_type="Bankrekening1",
        )
        self.assertEqual(result, 123)
        self.client.service.BankAccount_Insert.assert_called_once_with(
            CompanyId=1,
            BankAccount={
                "Id": 456,
                "Number": "123456789",
                "Description": "Mock Bank Account",
                "IBAN": "IBAN123",
                "BIC": "BIC123",
                "City": "Mock City",
                "Name": "Mock Bank",
                "Type": "Bankrekening1",
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_update_bank_account(self):
        """Test updating an existing bank account for the company."""
        self.bank_account_service.update(
            company_id=1,
            account_id=456,
            account_number="123456789",
            description="Mock Bank Account",
            iban="IBAN123",
            bic="BIC123",
            city="Mock City",
            name="Mock Bank",
            account_type="Bankrekening1",
        )
        self.client.service.BankAccount_Update.assert_called_once_with(
            CompanyId=1,
            BankAccount={
                "Id": 456,
                "Number": "123456789",
                "Description": "Mock Bank Account",
                "IBAN": "IBAN123",
                "BIC": "BIC123",
                "City": "Mock City",
                "Name": "Mock Bank",
                "Type": "Bankrekening1",
            },
            _soapheaders=self.mock_auth_header,
        )
