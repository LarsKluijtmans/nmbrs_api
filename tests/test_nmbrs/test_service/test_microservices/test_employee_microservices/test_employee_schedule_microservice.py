"""Unit tests for the EmployeeScheduleService class."""

import unittest
from unittest.mock import Mock
from decimal import Decimal

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.schedule import EmployeeScheduleService, Schedule


class TestEmployeeScheduleService(unittest.TestCase):
    """Unit tests for the EmployeeScheduleService class."""

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
        self.employee_schedule_service = EmployeeScheduleService(self.auth_manager, self.client)

    def test_get_all_by_company(self):
        """Test retrieving all schedules of all employees by company."""
        company_id = 123
        expected_schedules = [
            {
                "EmployeeId": 1,
                "EmployeeSchedules": {
                    "Schedule_V2": [
                        {
                            "ScheduleCalcMethod": "Method1",
                            "HoursMonday": Decimal("8.0"),
                            "HoursTuesday": Decimal("8.0"),
                            "HoursWednesday": Decimal("8.0"),
                            "HoursThursday": Decimal("8.0"),
                            "HoursFriday": Decimal("8.0"),
                            "HoursSaturday": Decimal("0.0"),
                            "HoursSunday": Decimal("0.0"),
                            # Add more schedule data
                        },
                        {
                            "ScheduleCalcMethod": "Method2",
                            "HoursMonday": Decimal("7.5"),
                            "HoursTuesday": Decimal("7.5"),
                            "HoursWednesday": Decimal("7.5"),
                            "HoursThursday": Decimal("7.5"),
                            "HoursFriday": Decimal("7.5"),
                            "HoursSaturday": Decimal("0.0"),
                            "HoursSunday": Decimal("0.0"),
                            # Add more schedule data
                        },
                    ]
                },
            },
            # Add more employee schedules
        ]
        self.client.service.Schedule_GetAll_AllEmployeesByCompany.return_value = expected_schedules

        result = self.employee_schedule_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Schedule)
        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].schedule_calc_method, "Method1")
        self.assertEqual(result[0].hours_monday, Decimal("8.0"))
        # Add more assertions for other schedules

        self.client.service.Schedule_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )
