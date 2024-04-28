"""Unit tests for the DebtorDepartmentService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.data_classes.debtor import Department
from src.nmbrs.service.microservices.debtor import DebtorDepartmentService


class TestDebtorDepartmentService(unittest.TestCase):
    """Unit tests for the DebtorDepartmentService class."""

    def setUp(self):
        self.mock_client = Mock()
        self.debtor_department_service = DebtorDepartmentService(self.mock_client)
        self.mock_auth_header = Mock()
        self.debtor_department_service.set_auth_header(self.mock_auth_header)

    def test_get_all_departments(self):
        """Test retrieving all departments of a debtor."""
        mock_departments = [Mock() for _ in range(3)]
        self.mock_client.service.Department_GetList.return_value = mock_departments
        result = self.debtor_department_service.get_all(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(department, Department) for department in result))
        self.mock_client.service.Department_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_delete_department(self):
        """Test delete_department method."""
        self.debtor_department_service.delete(1, 1)
        self.mock_client.service.Department_Delete.assert_called_with(DebtorId=1, id=1, _soapheaders=self.mock_auth_header)

    def test_insert_department(self):
        """Test inserting a new department for a debtor."""
        self.mock_client.service.Department_Insert.return_value = 123
        result = self.debtor_department_service.post(1, 2, 3, "test_description")
        self.assertEqual(result, 123)
        self.mock_client.service.Department_Insert.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update_department(self):
        """Test updating an existing department of a debtor."""
        self.debtor_department_service.update(1, 2, 3, "test_description")
        self.mock_client.service.Department_Update.assert_called_once_with(
            DebtorId=1,
            department={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )
