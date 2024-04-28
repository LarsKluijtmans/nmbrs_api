"""Unit tests for the EmployeeEmploymentService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.employment import EmployeeEmploymentService, Employment


class TestEmployeeEmploymentService(unittest.TestCase):
    """Unit tests for the EmployeeEmploymentService class."""

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
        self.employment_service = EmployeeEmploymentService(self.auth_manager, self.client)

    def test_get_all_by_company(self):
        """Test getting all employment records for all employees in a company."""
        company_id = 123
        self.client.service.Employment_GetAll_AllEmployeesByCompany.return_value = [
            {
                "EmployeeId": 1,
                "EmployeeEmployments": {
                    "Employment": [
                        {
                            "EmploymentId": 1,
                            "CreationDate": datetime.now(),
                            "StartDate": datetime.now(),
                            "EndDate": None,
                            "InitialStartDate": datetime.now(),
                        }
                    ]
                },
            },
            {
                "EmployeeId": 2,
                "EmployeeEmployments": {
                    "Employment": [
                        {
                            "EmploymentId": 2,
                            "CreationDate": datetime.now(),
                            "StartDate": datetime.now(),
                            "EndDate": None,
                            "InitialStartDate": datetime.now(),
                        }
                    ]
                },
            },
        ]

        result = self.employment_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, Employment)
        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].id, 1)
        self.assertIsInstance(result[0].creation_date, datetime)
        self.assertIsInstance(result[0].start_date, datetime)
        self.assertIsNone(result[0].end_date)
        self.assertIsInstance(result[0].initial_start_date, datetime)

        self.assertEqual(result[1].employee_id, 2)
        self.assertEqual(result[1].id, 2)
        self.assertIsInstance(result[1].creation_date, datetime)
        self.assertIsInstance(result[1].start_date, datetime)
        self.assertIsNone(result[1].end_date)
        self.assertIsInstance(result[1].initial_start_date, datetime)

        self.client.service.Employment_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )
