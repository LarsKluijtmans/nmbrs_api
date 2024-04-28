"""Unit tests for the DebtorDepartmentService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.debtor import Department
from src.nmbrs.service.microservices.debtor import DebtorDepartmentService


class TestDebtorDepartmentService(unittest.TestCase):
    """Unit tests for the DebtorDepartmentService class."""

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
        self.debtor_department_service = DebtorDepartmentService(self.auth_manager, self.client)

    def test_get_all_departments(self):
        """Test retrieving all departments of a debtor."""
        mock_departments = [Mock() for _ in range(3)]
        self.client.service.Department_GetList.return_value = mock_departments
        result = self.debtor_department_service.get_all(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(department, Department) for department in result))
        self.client.service.Department_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_delete_department(self):
        """Test delete_department method."""
        self.debtor_department_service.delete(1, 1)
        self.client.service.Department_Delete.assert_called_with(DebtorId=1, id=1, _soapheaders=self.mock_auth_header)

    def test_insert_department(self):
        """Test inserting a new department for a debtor."""
        self.client.service.Department_Insert.return_value = 123
        result = self.debtor_department_service.post(1, 2, 3, "test_description")
        self.assertEqual(result, 123)
        self.client.service.Department_Insert.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update_department(self):
        """Test updating an existing department of a debtor."""
        self.debtor_department_service.update(1, 2, 3, "test_description")
        self.client.service.Department_Update.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )
