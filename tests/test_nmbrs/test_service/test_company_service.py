"""Unit tests for the CompanyService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.data_classes.company import (
    Period,
    ContactPerson,
    GuidConvertor,
    PayrollWorkflowTrack,
    FulltimeSchedules,
    DefaultEmployeeTemplate,
    FulltimeSchedule,
)
from src.nmbrs.service.company_service import CompanyService, Company
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
    CompanyWageComponentService,
    CompanySvwService,
    CompanyWageCostService,
    CompanyWageModelService,
    CompanyWageTaxService,
)


class TestCompanyService(unittest.TestCase):
    """Unit tests for the CompanyService class."""

    def setUp(self):
        self.client = CompanyService()
        self.mock_auth_header = Mock()
        self.mock_client = Mock()
        self.client.client = self.mock_client
        self.client.set_auth_header(self.mock_auth_header)

    def test_initiation_of_microservices(self):
        """Test initialization of all microservices."""
        self.assertIsInstance(self.client.address, CompanyAddressService)
        self.assertIsInstance(self.client.bank_account, CompanyBankAccountService)
        self.assertIsInstance(self.client.cost_center, CompanyCostCenterService)
        self.assertIsInstance(self.client.cost_unit, CompanyCostUnitService)
        self.assertIsInstance(self.client.hour_model, CompanyHourModelService)
        self.assertIsInstance(self.client.journal, CompanyJournalService)
        self.assertIsInstance(self.client.labour_agreement, CompanyLabourAgreementService)
        self.assertIsInstance(self.client.pension, CompanyPensionService)
        self.assertIsInstance(self.client.run, CompanyRunService)
        self.assertIsInstance(self.client.salary_documents, CompanySalaryDocumentService)
        self.assertIsInstance(self.client.salary_table, CompanySalaryTableService)
        self.assertIsInstance(self.client.svw, CompanySvwService)
        self.assertIsInstance(self.client.wage_component, CompanyWageComponentService)
        self.assertIsInstance(self.client.wage_cost, CompanyWageCostService)
        self.assertIsInstance(self.client.wage_model, CompanyWageModelService)
        self.assertIsInstance(self.client.wage_tax, CompanyWageTaxService)

    def test_set_auth_headers(self):
        """Test setting authentication headers for all microservices."""
        # Setup mocks
        self.client.address = Mock()
        self.client.bank_account = Mock()
        self.client.cost_center = Mock()
        self.client.cost_unit = Mock()
        self.client.hour_model = Mock()
        self.client.journal = Mock()
        self.client.labour_agreement = Mock()
        self.client.pension = Mock()
        self.client.reports = Mock()
        self.client.run = Mock()
        self.client.salary_documents = Mock()
        self.client.salary_table = Mock()
        self.client.svw = Mock()
        self.client.wage_component = Mock()
        self.client.wage_cost = Mock()
        self.client.wage_model = Mock()
        self.client.wage_tax = Mock()

        auth_header = {"Authorization": "Bearer token"}

        # Call the set_auth_header method on the mocked CompanyService
        self.client.set_auth_header(auth_header)

        self.client.address.set_auth_header.assert_called_once_with(auth_header)
        self.client.bank_account.set_auth_header.assert_called_once_with(auth_header)
        self.client.cost_center.set_auth_header.assert_called_once_with(auth_header)
        self.client.cost_unit.set_auth_header.assert_called_once_with(auth_header)
        self.client.hour_model.set_auth_header.assert_called_once_with(auth_header)
        self.client.journal.set_auth_header.assert_called_once_with(auth_header)
        self.client.labour_agreement.set_auth_header.assert_called_once_with(auth_header)
        self.client.pension.set_auth_header.assert_called_once_with(auth_header)
        self.client.run.set_auth_header.assert_called_once_with(auth_header)
        self.client.salary_documents.set_auth_header.assert_called_once_with(auth_header)
        self.client.salary_table.set_auth_header.assert_called_once_with(auth_header)
        self.client.svw.set_auth_header.assert_called_once_with(auth_header)
        self.client.wage_component.set_auth_header.assert_called_once_with(auth_header)
        self.client.wage_cost.set_auth_header.assert_called_once_with(auth_header)
        self.client.wage_model.set_auth_header.assert_called_once_with(auth_header)
        self.client.wage_tax.set_auth_header.assert_called_once_with(auth_header)

    def test_get_all(self):
        """Test retrieving all companies."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetAll.return_value = mock_companies
        result = self.client.get_all()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(company, Company) for company in result))
        self.mock_client.service.List_GetAll.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_by_debtor(self):
        """Test retrieving all companies belonging to a debtor."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByDebtor.return_value = mock_companies
        result = self.client.get_by_debtor(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(company, Company) for company in result))
        self.mock_client.service.List_GetByDebtor.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_current_period(self):
        """Test retrieving the current period of a company."""
        mock_period = "2024-03-M"
        self.mock_client.service.Company_GetCurrentPeriod.return_value = mock_period
        result = self.client.get_current_period(1)
        self.assertIsInstance(result, Period)
        self.mock_client.service.Company_GetCurrentPeriod.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_current_period_return_none(self):
        """Test retrieving the current period of a company, returns none."""
        self.mock_client.service.Company_GetCurrentPeriod.return_value = None
        result = self.client.get_current_period(1)
        self.assertIsNone(result)
        self.mock_client.service.Company_GetCurrentPeriod.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_by_employee(self):
        """Test retrieving company by employee ID."""
        mock_company = Mock()
        self.mock_client.service.Company_GetCurrentByEmployeeId.return_value = mock_company
        result = self.client.get_by_employee(1)
        self.assertIsInstance(result, Company)
        self.mock_client.service.Company_GetCurrentByEmployeeId.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_get_by_employee_return_none(self):
        """Test retrieving company by employee ID, returns none."""
        self.mock_client.service.Company_GetCurrentByEmployeeId.return_value = None
        result = self.client.get_by_employee(1)
        self.assertIsNone(result)
        self.mock_client.service.Company_GetCurrentByEmployeeId.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_insert(self):
        """Test inserting a new company."""
        mock_inserted_id = 123
        self.mock_client.service.Company_Insert.return_value = mock_inserted_id
        result = self.client.insert(1, "Test Company", 1, 1, "labour_agreement_group_id", True)
        self.assertEqual(result, mock_inserted_id)
        self.mock_client.service.Company_Insert.assert_called_once_with(
            DebtorId=1,
            CompanyName="Test Company",
            PeriodType=1,
            DefaultCompanyId=1,
            LabourAgreementSettingsGroupGuid="labour_agreement_group_id",
            PayInAdvance=True,
            _soapheaders=self.mock_auth_header,
        )

    def test_get_contact_person(self):
        """Test retrieving contact person by company ID."""
        mock_contact_person = Mock()
        self.mock_client.service.ContactPerson_Get.return_value = mock_contact_person
        result = self.client.get_contact_person(1)
        self.assertIsInstance(result, ContactPerson)
        self.mock_client.service.ContactPerson_Get.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_converter_mappings(self):
        """Test retrieving converter mappings for the given entity and company ID."""
        mock_guids = Mock()
        self.mock_client.service.Converter_GetByCompany_IntToGuid.return_value = mock_guids
        result = self.client.get_converter_mappings(1, "Employee")
        self.assertIsInstance(result, GuidConvertor)
        self.mock_client.service.Converter_GetByCompany_IntToGuid.assert_called_once_with(
            Entity="Employee", CompanyId=1, _soapheaders=self.mock_auth_header
        )

    def test_get_default_employee_templates(self):
        """Test retrieving default employee templates by company."""
        company_id = 123
        expected_templates = [
            {"DefaultEmployeeTemplateId": "1", "Description": "Template 1"},
            {"DefaultEmployeeTemplateId": "2", "Description": "Template 2"},
        ]
        self.mock_client.service.DefaultEmployeeTemplates_GetByCompany.return_value = expected_templates

        result = self.client.get_default_employee_templates(company_id)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], DefaultEmployeeTemplate)
        self.assertEqual(result[0].id, "1")
        self.assertEqual(result[0].description, "Template 1")
        self.assertEqual(result[1].id, "2")
        self.assertEqual(result[1].description, "Template 2")
        self.mock_client.service.DefaultEmployeeTemplates_GetByCompany.assert_called_once_with(
            CompanyId=company_id, _soapheaders=self.mock_auth_header
        )

    def test_upload_file(self):
        """Test uploading a document for a company."""
        company_id = 123
        document_name = "test_document"
        document_sub_folder = "sub_folder"
        data = b"test_data"

        self.client.upload_file(company_id, document_name, document_sub_folder, data)

        self.mock_client.service.FileExplorer_UploadFile.assert_called_once_with(
            CompanyId=company_id,
            StrDocumentName=document_name,
            StrDocumentSubFolder=document_sub_folder,
            Body=data,
            _soapheaders=self.mock_auth_header,
        )

    def test_get_current_schedule(self):
        """Test retrieving the current schedules for a company."""
        company_id = 123
        schedule = {
            "ScheduleCalcMethod": "Method",
            "HoursMonday": 8,
            "HoursTuesday": 8,
            "HoursWednesday": 8,
            "HoursThursday": 8,
            "HoursFriday": 8,
            "HoursSaturday": 0,
            "HoursSunday": 0,
            "HoursMonday2": 0,
            "HoursTuesday2": 0,
            "HoursWednesday2": 0,
            "HoursThursday2": 0,
            "HoursFriday2": 0,
            "HoursSaturday2": 0,
            "HoursSunday2": 0,
        }
        expected_response = {
            "FulltimeScheduleOne": schedule,
            "FulltimeScheduleTwo": schedule,
            "FulltimeScheduleThree": schedule,
            "FulltimeScheduleFour": schedule,
        }
        self.mock_client.service.Schedule_GetCurrent.return_value = expected_response

        result = self.client.get_current_schedule(company_id)

        self.assertIsInstance(result, FulltimeSchedules)
        self.assertIsInstance(result.schedule_one, FulltimeSchedule)
        self.assertEqual(result.schedule_one.schedule_calc_method, "Method")
        self.assertEqual(result.schedule_one.hours_monday, 8)

        self.mock_client.service.Schedule_GetCurrent.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)

    def test_get_payroll_workflow(self):
        """Test retrieving the company's payroll workflow tracks and actions."""
        company_id = 123
        year = 2024
        period = 1
        expected_responses = [
            {
                "TrackName": "Track 1",
                "TrackStatus": "Status 1",
                "Actions": [
                    {"ActionId": 1, "ActionName": "Action 1", "ActionStatusId": 1, "ActionStatus": "Pending", "RunAt": datetime(2024, 1, 1)}
                ],
            },
            {
                "TrackName": "Track 2",
                "TrackStatus": "Status 2",
                "Actions": [
                    {
                        "ActionId": 2,
                        "ActionName": "Action 2",
                        "ActionStatusId": 2,
                        "ActionStatus": "Completed",
                        "RunAt": datetime(2024, 2, 2),
                    }
                ],
            },
        ]
        self.mock_client.service.PayrollWorkflow_Get.return_value = expected_responses

        result = self.client.get_payroll_workflow(company_id, year, period)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], PayrollWorkflowTrack)
        self.assertEqual(result[0].track_name, "Track 1")
        self.assertEqual(result[0].track_status, "Status 1")
        self.assertEqual(result[1].track_name, "Track 2")
        self.assertEqual(result[1].track_status, "Status 2")

        self.mock_client.service.PayrollWorkflow_Get.assert_called_once_with(
            CompanyId=company_id, Year=year, Period=period, _soapheaders=self.mock_auth_header
        )
