"""Unit tests for the EmployeeBankAccountService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.employee.bank_account import EmployeeBankAccountService, BankAccount


class TestEmployeeBankAccountService(unittest.TestCase):
    """Unit tests for the EmployeeBankAccountService class."""

    def setUp(self):
        self.client = Mock()
        self.bank_account_service = EmployeeBankAccountService(self.client)
        self.mock_auth_header = Mock()
        self.bank_account_service.set_auth_header(self.mock_auth_header)

    def test_get(self):
        """Test retrieving bank accounts for a given employee, period, and year."""
        employee_id = 123
        period = 1
        year = 2023
        expected_bank_accounts = [
            {
                "Id": 1,
                "Number": "123",
                "Description": "Savings",
                "IBAN": "NL91ABNA0417164300",
                "BIC": "ABNANL2A",
                "City": "Amsterdam",
                "Name": "John Doe",
                "Type": "Savings",
            },
            {
                "Id": 2,
                "Number": "456",
                "Description": "Checking",
                "IBAN": "NL91ABNA0417164301",
                "BIC": "ABNANL2A",
                "City": "Rotterdam",
                "Name": "John Doe",
                "Type": "Checking",
            },
        ]
        self.client.service.BankAccount_GetList.return_value = expected_bank_accounts

        result = self.bank_account_service.get(employee_id, period, year)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_bank_accounts))
        for idx, expected_bank_account in enumerate(expected_bank_accounts):
            self.assertIsInstance(result[idx], BankAccount)
            self.assertEqual(result[idx].employee_id, employee_id)
            self.assertEqual(result[idx].id, expected_bank_account["Id"])
            self.assertEqual(result[idx].number, expected_bank_account["Number"])
            self.assertEqual(result[idx].description, expected_bank_account["Description"])
            self.assertEqual(result[idx].iban, expected_bank_account["IBAN"])
            self.assertEqual(result[idx].bic, expected_bank_account["BIC"])
            self.assertEqual(result[idx].city, expected_bank_account["City"])
            self.assertEqual(result[idx].name, expected_bank_account["Name"])
            self.assertEqual(result[idx].type, expected_bank_account["Type"])
        self.client.service.BankAccount_GetList.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test retrieving current bank accounts for a given employee."""
        employee_id = 123
        expected_bank_accounts = [
            {
                "Id": 1,
                "Number": "123",
                "Description": "Savings",
                "IBAN": "NL91ABNA0417164300",
                "BIC": "ABNANL2A",
                "City": "Amsterdam",
                "Name": "John Doe",
                "Type": "Savings",
            },
            {
                "Id": 2,
                "Number": "456",
                "Description": "Checking",
                "IBAN": "NL91ABNA0417164301",
                "BIC": "ABNANL2A",
                "City": "Rotterdam",
                "Name": "John Doe",
                "Type": "Checking",
            },
        ]
        self.client.service.BankAccount_GetListCurrent.return_value = expected_bank_accounts

        result = self.bank_account_service.get_current(employee_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_bank_accounts))
        for idx, expected_bank_account in enumerate(expected_bank_accounts):
            self.assertIsInstance(result[idx], BankAccount)
            self.assertEqual(result[idx].employee_id, employee_id)
            self.assertEqual(result[idx].id, expected_bank_account["Id"])
            self.assertEqual(result[idx].number, expected_bank_account["Number"])
            self.assertEqual(result[idx].description, expected_bank_account["Description"])
            self.assertEqual(result[idx].iban, expected_bank_account["IBAN"])
            self.assertEqual(result[idx].bic, expected_bank_account["BIC"])
            self.assertEqual(result[idx].city, expected_bank_account["City"])
            self.assertEqual(result[idx].name, expected_bank_account["Name"])
            self.assertEqual(result[idx].type, expected_bank_account["Type"])
        self.client.service.BankAccount_GetListCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_delete(self):
        """Test deleting a bank account for a given employee."""
        employee_id = 123
        bank_account_id = 1
        self.client.service.BankAccount_DeleteCurrent.return_value = "Success"

        result = self.bank_account_service.delete(employee_id, bank_account_id)

        self.assertEqual(result, "Success")
        self.client.service.BankAccount_DeleteCurrent.assert_called_once_with(
            EmployeeId=employee_id, BankAccountID=bank_account_id, _soapheaders=self.mock_auth_header
        )

    def test_insert(self):
        """Test inserting a bank account for a given employee, period, and year."""
        employee_id = 123
        period = 1
        year = 2023
        unprotected_mode = True
        bank_account_data = {
            "Id": 1,
            "Number": "123",
            "Description": "Savings",
            "IBAN": "NL91ABNA0417164300",
            "BIC": "ABNANL2A",
            "City": "Amsterdam",
            "Name": "John Doe",
            "Type": "Savings",
        }
        bank_account = BankAccount(employee_id=employee_id, data=bank_account_data)
        self.client.service.BankAccount_Insert.return_value = 1

        result = self.bank_account_service.post(employee_id, bank_account, period, year, unprotected_mode)

        self.assertEqual(result, 1)
        _bank_account = {
            "Id": bank_account.id,
            "Number": bank_account.number,
            "Description": bank_account.description,
            "IBAN": bank_account.iban,
            "BIC": bank_account.bic,
            "City": bank_account.city,
            "Name": bank_account.name,
            "Type": bank_account.type,
        }
        self.client.service.BankAccount_Insert.assert_called_once_with(
            EmployeeId=employee_id,
            BankAccount=_bank_account,
            Period=period,
            Year=year,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_current(self):
        """Test inserting a bank account for a given employee in the current period."""
        employee_id = 123
        bank_account_data = {
            "Id": 1,
            "Number": "123",
            "Description": "Savings",
            "IBAN": "NL91ABNA0417164300",
            "BIC": "ABNANL2A",
            "City": "Amsterdam",
            "Name": "John Doe",
            "Type": "Savings",
        }
        bank_account = BankAccount(employee_id=employee_id, data=bank_account_data)
        self.client.service.BankAccount_InsertCurrent.return_value = 1

        result = self.bank_account_service.post_current(employee_id, bank_account)

        self.assertEqual(result, 1)
        _bank_account = {
            "Id": bank_account.id,
            "Number": bank_account.number,
            "Description": bank_account.description,
            "IBAN": bank_account.iban,
            "BIC": bank_account.bic,
            "City": bank_account.city,
            "Name": bank_account.name,
            "Type": bank_account.type,
        }
        self.client.service.BankAccount_InsertCurrent.assert_called_once_with(
            EmployeeId=employee_id, BankAccount=_bank_account, _soapheaders=self.mock_auth_header
        )
