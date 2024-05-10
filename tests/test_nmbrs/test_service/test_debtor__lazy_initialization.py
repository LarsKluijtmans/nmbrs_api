"""Test cases for the DebtorService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service import DebtorService
from src.nmbrs.service.microservices.debtor import (
    DebtorDepartmentService,
    DebtorFunctionService,
    DebtorTitleService,
    DebtorWebHooksService,
)


class TestDebtorService(unittest.TestCase):
    """Test cases for the DebtorService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.client = Mock()
        self.debtor_service = DebtorService(self.auth_manager)

    def test_department_lazy_initialization(self):
        """Test lazy initialization of the department property."""
        self.assertIsNone(self.debtor_service._department)
        department = self.debtor_service.department
        self.assertIsInstance(department, DebtorDepartmentService)
        self.assertIsNotNone(self.debtor_service._department)

    def test_function_lazy_initialization(self):
        """Test lazy initialization of the function property."""
        self.assertIsNone(self.debtor_service._function)
        function = self.debtor_service.function
        self.assertIsInstance(function, DebtorFunctionService)
        self.assertIsNotNone(self.debtor_service._function)

    def test_webhook_lazy_initialization(self):
        """Test lazy initialization of the webhook property."""
        self.assertIsNone(self.debtor_service._webhook)
        webhook = self.debtor_service.webhook
        self.assertIsInstance(webhook, DebtorWebHooksService)
        self.assertIsNotNone(self.debtor_service._webhook)

    def test_title_lazy_initialization(self):
        """Test lazy initialization of the title property."""
        self.assertIsNone(self.debtor_service._title)
        title = self.debtor_service.title
        self.assertIsInstance(title, DebtorTitleService)
        self.assertIsNotNone(self.debtor_service._title)
