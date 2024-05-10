"""Test cases for the CompanyService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.company_service import CompanyService
from src.nmbrs.service.microservices.company import (
    CompanyAddressService,
    CompanyBankAccountService,
    CompanyCostCenterService,
    CompanyCostUnitService,
    CompanyHourModelService,
    CompanyJournalService,
    CompanyLabourAgreementService,
    CompanyPensionService,
    CompanyRunService,
    CompanySalaryDocumentService,
    CompanySalaryTableService,
    CompanySvwService,
    CompanyWageComponentService,
    CompanyWageCostService,
    CompanyWageModelService,
    CompanyWageTaxService,
)


class TestCompanyService(unittest.TestCase):
    """Test cases for the CompanyService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.client = Mock()
        self.company_service = CompanyService(self.auth_manager)

    def test_address_lazy_initialization(self):
        """Test lazy initialization of the address property."""
        self.assertIsNone(self.company_service._address)
        address = self.company_service.address
        self.assertIsInstance(address, CompanyAddressService)
        self.assertIsNotNone(self.company_service._address)

    def test_bank_account_lazy_initialization(self):
        """Test lazy initialization of the bank_account property."""
        self.assertIsNone(self.company_service._bank_account)
        bank_account = self.company_service.bank_account
        self.assertIsInstance(bank_account, CompanyBankAccountService)
        self.assertIsNotNone(self.company_service._bank_account)

    def test_cost_center_lazy_initialization(self):
        """Test lazy initialization of the cost_center property."""
        self.assertIsNone(self.company_service._cost_center)
        cost_center = self.company_service.cost_center
        self.assertIsInstance(cost_center, CompanyCostCenterService)
        self.assertIsNotNone(self.company_service._cost_center)

    def test_cost_unit_lazy_initialization(self):
        """Test lazy initialization of the cost_unit property."""
        self.assertIsNone(self.company_service._cost_unit)
        cost_unit = self.company_service.cost_unit
        self.assertIsInstance(cost_unit, CompanyCostUnitService)
        self.assertIsNotNone(self.company_service._cost_unit)

    def test_hour_model_lazy_initialization(self):
        """Test lazy initialization of the hour_model property."""
        self.assertIsNone(self.company_service._hour_model)
        hour_model = self.company_service.hour_model
        self.assertIsInstance(hour_model, CompanyHourModelService)
        self.assertIsNotNone(self.company_service._hour_model)

    def test_journal_lazy_initialization(self):
        """Test lazy initialization of the journal property."""
        self.assertIsNone(self.company_service._journal)
        journal = self.company_service.journal
        self.assertIsInstance(journal, CompanyJournalService)
        self.assertIsNotNone(self.company_service._journal)

    def test_labour_agreement_lazy_initialization(self):
        """Test lazy initialization of the labour_agreement property."""
        self.assertIsNone(self.company_service._labour_agreement)
        labour_agreement = self.company_service.labour_agreement
        self.assertIsInstance(labour_agreement, CompanyLabourAgreementService)
        self.assertIsNotNone(self.company_service._labour_agreement)

    def test_pension_lazy_initialization(self):
        """Test lazy initialization of the pension property."""
        self.assertIsNone(self.company_service._pension)
        pension = self.company_service.pension
        self.assertIsInstance(pension, CompanyPensionService)
        self.assertIsNotNone(self.company_service._pension)

    def test_run_lazy_initialization(self):
        """Test lazy initialization of the run property."""
        self.assertIsNone(self.company_service._run)
        run = self.company_service.run
        self.assertIsInstance(run, CompanyRunService)
        self.assertIsNotNone(self.company_service._run)

    def test_salary_documents_lazy_initialization(self):
        """Test lazy initialization of the salary_documents property."""
        self.assertIsNone(self.company_service._salary_documents)
        salary_documents = self.company_service.salary_documents
        self.assertIsInstance(salary_documents, CompanySalaryDocumentService)
        self.assertIsNotNone(self.company_service._salary_documents)

    def test_salary_table_lazy_initialization(self):
        """Test lazy initialization of the salary_table property."""
        self.assertIsNone(self.company_service._salary_table)
        salary_table = self.company_service.salary_table
        self.assertIsInstance(salary_table, CompanySalaryTableService)
        self.assertIsNotNone(self.company_service._salary_table)

    def test_svw_lazy_initialization(self):
        """Test lazy initialization of the svw property."""
        self.assertIsNone(self.company_service._svw)
        svw = self.company_service.svw
        self.assertIsInstance(svw, CompanySvwService)
        self.assertIsNotNone(self.company_service._svw)

    def test_wage_component_lazy_initialization(self):
        """Test lazy initialization of the wage_component property."""
        self.assertIsNone(self.company_service._wage_component)
        wage_component = self.company_service.wage_component
        self.assertIsInstance(wage_component, CompanyWageComponentService)
        self.assertIsNotNone(self.company_service._wage_component)

    def test_wage_cost_lazy_initialization(self):
        """Test lazy initialization of the wage_cost property."""
        self.assertIsNone(self.company_service._wage_cost)
        wage_cost = self.company_service.wage_cost
        self.assertIsInstance(wage_cost, CompanyWageCostService)
        self.assertIsNotNone(self.company_service._wage_cost)

    def test_wage_model_lazy_initialization(self):
        """Test lazy initialization of the wage_model property."""
        self.assertIsNone(self.company_service._wage_model)
        wage_model = self.company_service.wage_model
        self.assertIsInstance(wage_model, CompanyWageModelService)
        self.assertIsNotNone(self.company_service._wage_model)

    def test_wage_tax_lazy_initialization(self):
        """Test lazy initialization of the wage_tax property."""
        self.assertIsNone(self.company_service._wage_tax)
        wage_tax = self.company_service.wage_tax
        self.assertIsInstance(wage_tax, CompanyWageTaxService)
        self.assertIsNotNone(self.company_service._wage_tax)
