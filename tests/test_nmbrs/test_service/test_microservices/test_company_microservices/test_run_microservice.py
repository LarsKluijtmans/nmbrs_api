"""Unit tests for the CompanyRunService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.run import CompanyRunService, RunRequest, RunInfo, Employee


class TestCompanyRunService(unittest.TestCase):
    """Unit tests for the CompanyRunService class."""

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
        self.run_service = CompanyRunService(self.auth_manager, self.client)

    def test_get_requests(self):
        """Test retrieving run requests associated with a company."""
        mock_run_requests = [{"Period": 6, "Year": 2023, "Status": "Pending", "HandledDate": datetime(2023, 6, 15)}]
        self.client.service.RunRequest_GetList.return_value = mock_run_requests
        result = self.run_service.get_requests(1, 2023)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RunRequest)
        self.assertEqual(result[0].period, 6)
        self.assertEqual(result[0].year, 2023)
        self.assertEqual(result[0].status, "Pending")
        self.assertEqual(result[0].handle_delete, datetime(2023, 6, 15))
        self.client.service.RunRequest_GetList.assert_called_once_with(CompanyId=1, Year=2023, _soapheaders=self.mock_auth_header)

    def test_insert_request(self):
        """Test inserting a run request for a company."""
        self.run_service.insert_request(1)
        self.client.service.RunRequest_Insert.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_runs(self):
        """Test retrieving runs associated with a company."""
        mock_runs = [{"ID": 1, "Number": 123, "Year": 2023, "PeriodStart": 6, "PeriodEnd": 6}]
        self.client.service.Run_GetList.return_value = mock_runs
        result = self.run_service.get(1, 2023)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RunInfo)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].number, 123)
        self.assertEqual(result[0].year, 2023)
        self.assertEqual(result[0].period_start, 6)
        self.assertEqual(result[0].period_end, 6)
        self.client.service.Run_GetList.assert_called_once_with(CompanyId=1, Year=2023, _soapheaders=self.mock_auth_header)

    def test_get_all_employees_by_run(self):
        """Test retrieving all employees associated with a run for a company."""
        mock_employees = [{"EmployeeId": 1, "EmployeeNumber": 123}]
        self.client.service.Run_GetEmployeesByRunCompany.return_value = mock_employees
        result = self.run_service.get_all_employees_by_run(1, 2023, 123)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Employee)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].number, 123)
        self.client.service.Run_GetEmployeesByRunCompany.assert_called_once_with(
            CompanyId=1, Year=2023, RunId=123, _soapheaders=self.mock_auth_header
        )

    def test_get_hr_documents_cost_per_hour_year(self):
        """Test retrieving HR Document: Employer Cost per Hour per company per period."""
        company_id = 123
        run_id = 456
        year = 2023
        period = 6
        expected_response = b"mocked_hr_document_bytes"
        self.client.service.HrDocuments_EmployerCostPerHour_Year.return_value = expected_response

        result = self.run_service.get_hr_documents_cost_per_hour_year(company_id, run_id, year, period)

        self.assertEqual(result, expected_response)
        self.client.service.HrDocuments_EmployerCostPerHour_Year.assert_called_once_with(
            CompanyId=company_id, RunId=run_id, Year=year, Period=period, _soapheaders=self.mock_auth_header
        )
