"""Unit tests for the EmployeeDaysService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.data_classes.employee import DaysWorked, VariableDaysWorked
from src.nmbrs.service.microservices.employee.days import EmployeeDaysService
from src.nmbrs.auth.token_manager import AuthManager


class TestEmployeeDaysService(unittest.TestCase):
    """Unit tests for the EmployeeDaysService class."""

    def setUp(self):
        """Set up test dependencies."""
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
        self.employee_days_service = EmployeeDaysService(self.auth_manager, self.client)

    def test_get_fixed(self):
        """Test the get_fixed method of EmployeeDaysService."""
        employee_id = 123
        period = 4
        year = 2024
        expected_days = 5
        self.client.service.DaysFixed_Get.return_value = expected_days

        result = self.employee_days_service.get_fixed(employee_id, period, year)

        self.assertEqual(result, expected_days)
        self.client.service.DaysFixed_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current_fixed(self):
        """Test the get_current_fixed method of EmployeeDaysService."""
        employee_id = 123
        expected_days = 3
        self.client.service.DaysFixed_GetCurrent.return_value = expected_days

        result = self.employee_days_service.get_current_fixed(employee_id)

        self.assertEqual(result, expected_days)
        self.client.service.DaysFixed_GetCurrent.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_post_fixed(self):
        """Test the post_fixed method of EmployeeDaysService."""
        employee_id = 123
        period = 4
        year = 2024
        days = 5
        unprotected_mode = False

        self.employee_days_service.post_fixed(employee_id, period, year, days, unprotected_mode)

        self.client.service.DaysFixed_Set.assert_called_once_with(
            EmployeeId=employee_id,
            Period=period,
            Year=year,
            Days=days,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_post_current_fixed(self):
        """Test the post_current_fixed method of EmployeeDaysService."""
        employee_id = 123
        days = 3

        self.employee_days_service.post_current_fixed(employee_id, days)

        self.client.service.DaysFixed_Set.assert_called_once_with(EmployeeId=employee_id, Days=days, _soapheaders=self.mock_auth_header)

    def test_post_batch_fixed(self):
        """Test the post_batch_fixed method of EmployeeDaysService."""
        days_worked = [DaysWorked(123, 5, 4, 2024), DaysWorked(456, 6, 5, 2024)]
        unprotected_mode = False

        self.employee_days_service.post_batch_fixed(days_worked, unprotected_mode)

        expected_days_worked = [
            {"EmployeeId": 123, "Days": 5, "Period": 4, "Year": 2024},
            {"EmployeeId": 456, "Days": 6, "Period": 5, "Year": 2024},
        ]
        self.client.service.DaysFixed_Set_Batch.assert_called_once_with(
            EmployeesDaysWorked={"DaysWorked": expected_days_worked}, UnprotectedMode=unprotected_mode, _soapheaders=self.mock_auth_header
        )

    def test_stop_fixed(self):
        """Test the stop_fixed method of EmployeeDaysService."""
        employee_id = 123
        period = 4
        year = 2024
        unprotected_mode = False

        self.employee_days_service.stop_fixed(employee_id, period, year, unprotected_mode)

        self.client.service.DaysFixed_Stop.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, UnprotectedMode=unprotected_mode, _soapheaders=self.mock_auth_header
        )

    def test_get_variable(self):
        """Test the get_variable method of EmployeeDaysService."""
        employee_id = 123
        period = 4
        year = 2024
        expected_days = 8
        self.client.service.DaysVar_Get.return_value = expected_days

        result = self.employee_days_service.get_variable(employee_id, period, year)

        self.assertEqual(result, expected_days)
        self.client.service.DaysVar_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_post_batch_variable(self):
        """Test the post_batch_variable method of EmployeeDaysService."""
        days_worked = [DaysWorked(123, 5, 4, 2024), DaysWorked(456, 6, 5, 2024)]
        unprotected_mode = False

        self.employee_days_service.post_batch_variable(days_worked, unprotected_mode)

        expected_days_worked = [
            {"EmployeeId": 123, "Days": 5, "Period": 4, "Year": 2024},
            {"EmployeeId": 456, "Days": 6, "Period": 5, "Year": 2024},
        ]
        self.client.service.DaysVar_Set_Batch.assert_called_once_with(
            EmployeesDaysWorked={"DaysWorked": expected_days_worked}, UnprotectedMode=unprotected_mode, _soapheaders=self.mock_auth_header
        )

    def test_get_days_worked(self):
        """Test the get_days_worked method of EmployeeDaysService."""
        employee_id = 123
        period = 4
        year = 2024
        self.client.service.DaysVarWorked_Get.return_value = {"Days": 1, "PlusMinusDaysForWageComp": 2}

        result = self.employee_days_service.get_days_worked(employee_id, period, year)
        self.assertIsInstance(result, VariableDaysWorked)
        self.assertEqual(result.days, 1)
        self.assertEqual(result.plus_min_days_for_wage_comp, 2)

        self.client.service.DaysVarWorked_Get.assert_called_once_with(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_get_current_days_worked(self):
        """Test the get_current_days_worked method of EmployeeDaysService."""
        employee_id = 123
        self.client.service.DaysVarWorked_Get.return_value = {"Days": 1, "PlusMinusDaysForWageComp": 2}

        result = self.employee_days_service.get_current_days_worked(employee_id)

        self.assertIsInstance(result, VariableDaysWorked)
        self.assertEqual(result.days, 1)
        self.assertEqual(result.plus_min_days_for_wage_comp, 2)

        self.client.service.DaysVarWorked_Get.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_post_days_worked(self):
        """Test the post_days_worked method of EmployeeDaysService."""
        employee_id = 123
        period = 1
        year = 2024
        days = 5
        plus_min_days_for_wage_comp = 2
        unprotected_mode = False

        self.employee_days_service.post_days_worked(employee_id, period, year, days, plus_min_days_for_wage_comp, unprotected_mode)

        self.client.service.DaysVarWorked_Set.assert_called_once_with(
            EmployeeId=employee_id,
            Period=period,
            Year=year,
            Days=days,
            PlusMinusDaysForWageComp=plus_min_days_for_wage_comp,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_post_current_days_worked(self):
        """Test the post_current_days_worked method of EmployeeDaysService."""
        employee_id = 123
        days = 5
        plus_min_days_for_wage_comp = 2

        self.employee_days_service.post_current_days_worked(employee_id, days, plus_min_days_for_wage_comp)

        self.client.service.DaysVarWorked_Set.assert_called_once_with(
            EmployeeId=employee_id,
            Days=days,
            PlusMinusDaysForWageComp=plus_min_days_for_wage_comp,
            _soapheaders=self.mock_auth_header,
        )
