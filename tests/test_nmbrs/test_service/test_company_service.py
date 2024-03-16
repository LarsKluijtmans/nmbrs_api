"""Unit tests for the CompanyService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.company_service import CompanyService, Company
from src.nmbrs.service.microservices.company import *


class TestCompanyService(unittest.TestCase):
    """Unit tests for the CompanyService class."""

    def setUp(self):
        self.company_service = CompanyService()
        self.mock_auth_header = Mock()
        self.mock_company_service = Mock()
        self.company_service.company_service = self.mock_company_service
        self.company_service.set_auth_header(self.mock_auth_header)

    def test_initiation_of_microservices(self):
        """Test initialization of all microservices."""
        self.assertIsInstance(self.company_service.address, CompanyAddressService)
        self.assertIsInstance(self.company_service.bank_account, CompanyBankAccountService)
        self.assertIsInstance(self.company_service.cost_center, CompanyCostCenterService)
        self.assertIsInstance(self.company_service.cost_unit, CompanyCostUnitService)
        self.assertIsInstance(self.company_service.hour_model, CompanyHourModelService)
        self.assertIsInstance(self.company_service.journal, CompanyJournalService)
        self.assertIsInstance(self.company_service.labour_agreement, CompanyLabourAgreementService)
        self.assertIsInstance(self.company_service.pension, CompanyPensionService)
        self.assertIsInstance(self.company_service.reports, CompanyReportService)
        self.assertIsInstance(self.company_service.run, CompanyRunService)
        self.assertIsInstance(self.company_service.salary_documents, CompanySalaryDocumentService)
        self.assertIsInstance(self.company_service.salary_table, CompanySalaryTableService)
        self.assertIsInstance(self.company_service.svw, CompanySVWService)
        self.assertIsInstance(self.company_service.wage_component_fixed, CompanyWageComponentFixedService)
        self.assertIsInstance(self.company_service.wage_component_var, CompanyWageComponentVarService)
        self.assertIsInstance(self.company_service.wage_cost, CompanyWageCostService)
        self.assertIsInstance(self.company_service.wage_model, CompanyWageModelService)
        self.assertIsInstance(self.company_service.wage_tax, CompanyWageTaxService)

    def test_set_auth_headers(self):
        """Test setting authentication headers for all microservices."""
        # Setup mocks
        self.company_service.address = Mock()
        self.company_service.bank_account = Mock()
        self.company_service.cost_center = Mock()
        self.company_service.cost_unit = Mock()
        self.company_service.hour_model = Mock()
        self.company_service.journal = Mock()
        self.company_service.labour_agreement = Mock()
        self.company_service.pension = Mock()
        self.company_service.reports = Mock()
        self.company_service.run = Mock()
        self.company_service.salary_documents = Mock()
        self.company_service.salary_table = Mock()
        self.company_service.svw = Mock()
        self.company_service.wage_component_fixed = Mock()
        self.company_service.wage_component_var = Mock()
        self.company_service.wage_cost = Mock()
        self.company_service.wage_model = Mock()
        self.company_service.wage_tax = Mock()

        auth_header = {'Authorization': 'Bearer token'}

        # Call the set_auth_header method on the mocked CompanyService
        self.company_service.set_auth_header(auth_header)

        self.company_service.address.set_auth_header.assert_called_once()
        self.company_service.bank_account.set_auth_header.assert_called_once()
        self.company_service.cost_center.set_auth_header.assert_called_once()
        self.company_service.cost_unit.set_auth_header.assert_called_once()
        self.company_service.hour_model.set_auth_header.assert_called_once()
        self.company_service.journal.set_auth_header.assert_called_once()
        self.company_service.labour_agreement.set_auth_header.assert_called_once()
        self.company_service.pension.set_auth_header.assert_called_once()
        self.company_service.reports.set_auth_header.assert_called_once()
        self.company_service.run.set_auth_header.assert_called_once()
        self.company_service.salary_documents.set_auth_header.assert_called_once()
        self.company_service.salary_table.set_auth_header.assert_called_once()
        self.company_service.svw.set_auth_header.assert_called_once()
        self.company_service.wage_component_fixed.set_auth_header.assert_called_once()
        self.company_service.wage_component_var.set_auth_header.assert_called_once()
        self.company_service.wage_cost.set_auth_header.assert_called_once()
        self.company_service.wage_model.set_auth_header.assert_called_once()
        self.company_service.wage_tax.set_auth_header.assert_called_once()

    def test_get_all(self):
        """Test retrieving all companies."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_company_service.service.List_GetAll.return_value = mock_companies
        result = self.company_service.get_all()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(company, Company) for company in result))
        self.mock_company_service.service.List_GetAll.assert_called_once_with(
            _soapheaders=self.mock_auth_header
        )

    def test_get_by_debtor(self):
        """Test retrieving all companies belonging to a debtor."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_company_service.service.List_GetByDebtor.return_value = mock_companies
        result = self.company_service.get_by_debtor(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(company, Company) for company in result))
        self.mock_company_service.service.List_GetByDebtor.assert_called_once_with(
            DebtorId=1,
            _soapheaders=self.mock_auth_header
        )

    def test_get_current_period(self):
        """Test retrieving the current period of a company."""
        mock_period = "2024-03-M"
        self.mock_company_service.service.Company_GetCurrentPeriod.return_value = mock_period
        result = self.company_service.get_current_period(1)
        self.assertEqual(result, mock_period)
        self.mock_company_service.service.Company_GetCurrentPeriod.assert_called_once_with(
            CompanyId=1,
            _soapheaders=self.mock_auth_header
        )
