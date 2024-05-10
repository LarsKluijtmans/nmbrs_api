"""Test cases for the Nmbrs class."""

import unittest

from src.nmbrs.service import DebtorService, CompanyService, EmployeeService, ReportService
from src.nmbrs.api import Nmbrs


class TestNmbrs(unittest.TestCase):
    """Test cases for the Nmbrs class."""

    def setUp(self):
        self.nmbrs_api = Nmbrs("test_username", "test_token", domain="test_domain", auth_type="domain")

    def test_debtor_lazy_initialization(self):
        """Test lazy initialization of the debtor property."""
        self.assertIsNone(self.nmbrs_api._debtor_service)
        debtor = self.nmbrs_api.debtor
        self.assertIsInstance(debtor, DebtorService)
        self.assertIsNotNone(self.nmbrs_api._debtor_service)

    def test_company_lazy_initialization(self):
        """Test lazy initialization of the company property."""
        self.assertIsNone(self.nmbrs_api._company_service)
        company = self.nmbrs_api.company
        self.assertIsInstance(company, CompanyService)
        self.assertIsNotNone(self.nmbrs_api._company_service)

    def test_employee_lazy_initialization(self):
        """Test lazy initialization of the employee property."""
        self.assertIsNone(self.nmbrs_api._employee_service)
        employee = self.nmbrs_api.employee
        self.assertIsInstance(employee, EmployeeService)
        self.assertIsNotNone(self.nmbrs_api._employee_service)

    def test_report_lazy_initialization(self):
        """Test lazy initialization of the report property."""
        self.assertIsNone(self.nmbrs_api._report_service)
        report = self.nmbrs_api.report
        self.assertIsInstance(report, ReportService)
        self.assertIsNotNone(self.nmbrs_api._report_service)
