"""Unit tests for the EmployeeService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.employee import Employee, EmployeeTypes, Period
from src.nmbrs.service.employee_service import EmployeeService


class TesteEmployeeService(unittest.TestCase):
    """Unit tests for the EmployeeService class."""

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
        self.employee_service = EmployeeService(self.auth_manager)
        self.mock_client = Mock()
        self.employee_service.client = self.mock_client

    def test_get_types(self):
        """Test retrieving all companies."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.EmployeeType_GetList.return_value = mock_companies
        result = self.employee_service.get_types()
        self.assertEqual(len(result), 3)
        for _type in result:
            self.assertIsInstance(_type, EmployeeTypes)
        self.mock_client.service.EmployeeType_GetList.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_current_period(self):
        """Test retrieving the current period of an employee."""
        mock_period = "2024-03-M"
        self.mock_client.service.Employee_GetCurrent.return_value = mock_period
        result = self.employee_service.get_current_period(1)
        self.assertIsInstance(result, Period)
        self.mock_client.service.Employee_GetCurrent.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_get_current_period_return_none(self):
        """Test retrieving the current period of an employee, return None"""
        self.mock_client.service.Employee_GetCurrent.return_value = None
        result = self.employee_service.get_current_period(1)
        self.assertIsNone(result)
        self.mock_client.service.Employee_GetCurrent.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_get_by_company(self):
        """Test retrieving all employees from a company."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByCompany.return_value = mock_companies
        employees = self.employee_service.get_by_company(1, 1)
        self.assertEqual(len(employees), 3)
        for employee in employees:
            self.assertIsInstance(employee, Employee)
        self.mock_client.service.List_GetByCompany.assert_called_once_with(CompanyId=1, EmployeeType=1, _soapheaders=self.mock_auth_header)

    def test_get_by_debtor(self):
        """Test retrieving all employees from a debtor."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByDebtor.return_value = mock_companies
        employees = self.employee_service.get_by_debtor(1, 1)
        self.assertEqual(len(employees), 3)
        for employee in employees:
            self.assertIsInstance(employee, Employee)
        self.mock_client.service.List_GetByDebtor.assert_called_once_with(DebtorId=1, EmployeeType=1, _soapheaders=self.mock_auth_header)

    def test_post_based_on_default(self):
        """Test inserting a new employee based on a default template."""
        # Setup mock data
        company_id = 1
        template_id = 2
        first_name = "John"
        last_name = "Doe"
        employment_id = 123
        create_date = datetime(2024, 1, 1)
        start_date = datetime(2024, 1, 10)
        end_date = datetime(2025, 1, 10)
        initial_start_date = datetime(2023, 12, 25)
        unprotected_mode = True
        expected_employee_id = 456

        # Configure the mock to return the expected employee ID
        self.mock_client.service.Employee_InsertBasedOnDefault.return_value = expected_employee_id

        # Call the method
        result = self.employee_service.post_based_on_default(
            company_id=company_id,
            template_id=template_id,
            first_name=first_name,
            last_name=last_name,
            employment_id=employment_id,
            create_date=create_date,
            start_date=start_date,
            unprotected_mode=unprotected_mode,
            end_date=end_date,
            initial_start_date=initial_start_date,
        )

        # Assertions
        self.assertEqual(result, expected_employee_id)
        self.mock_client.service.Employee_InsertBasedOnDefault.assert_called_once_with(
            CompanyId=company_id,
            DefaultEmployeeTemplate=template_id,
            FirstName=first_name,
            LastName=last_name,
            employment={
                "EmploymentId": employment_id,
                "CreationDate": create_date,
                "StartDate": start_date,
                "EndDate": end_date,
                "InitialStartDate": initial_start_date,
            },
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )
