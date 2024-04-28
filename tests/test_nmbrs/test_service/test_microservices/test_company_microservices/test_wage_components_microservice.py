"""Unit tests for the CompanyWageComponentService class."""

import unittest
from unittest.mock import Mock
from decimal import Decimal

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.wage_component import CompanyWageComponentService, WageComponent


class TestCompanyWageComponentService(unittest.TestCase):
    """Unit tests for the CompanyWageComponentService class."""

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
        self.company_wage_component_service = CompanyWageComponentService(self.auth_manager, self.client)

    def test_fixed_get(self):
        """Test retrieving all fixed wage components for a specified company, year, and period."""
        company_id = 123
        year = 2024
        period = 3
        expected_wage_components = [
            {"Id": 1, "Code": "WageComponent1", "Value": "100.00"},
            {"Id": 2, "Code": "WageComponent2", "Value": "200.00"},
        ]
        self.client.service.WageComponentFixed_Get.return_value = expected_wage_components

        result = self.company_wage_component_service.get_fixed(company_id, year, period)

        self.assertEqual(len(result), len(expected_wage_components))
        self.assertIsInstance(result[0], WageComponent)
        self.assertEqual(result[0].company_id, company_id)
        self.assertEqual(result[0].type, "fixed")
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "WageComponent1")
        self.assertEqual(result[0].value, "100.00")

        self.client.service.WageComponentFixed_Get.assert_called_once_with(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_fixed_get_current(self):
        """Test retrieving all fixed wage components for the current period of a specified company."""
        company_id = 123
        expected_wage_components = [
            {"Id": 1, "Code": "WageComponent1", "Value": "100.00"},
            {"Id": 2, "Code": "WageComponent2", "Value": "200.00"},
        ]
        self.client.service.WageComponentFixed_GetCurrent.return_value = expected_wage_components

        result = self.company_wage_component_service.get_current_fixed(company_id)

        self.assertEqual(len(result), len(expected_wage_components))
        self.assertIsInstance(result[0], WageComponent)
        self.assertEqual(result[0].company_id, company_id)
        self.assertEqual(result[0].type, "fixed")
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "WageComponent1")
        self.assertEqual(result[0].value, "100.00")

        self.client.service.WageComponentFixed_GetCurrent.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)

    def test_fixed_insert(self):
        """Test inserting a fixed wage component for a specified company, year, and period."""
        company_id = 123
        wage_component = WageComponent(company_id, "fixed", {"Id": 1, "Code": "Test", "Value": "100.00"})
        period = 3
        year = 2024
        protected_mode = False
        expected_response = 12345
        self.client.service.WageComponentFixed_Insert.return_value = expected_response

        result = self.company_wage_component_service.post_fixed(wage_component, period, year, protected_mode)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentFixed_Insert.assert_called_once_with(
            CompanyId=company_id,
            WageComponent={"Id": 1, "Code": "Test", "Value": "100.00"},
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_fixed_insert_current(self):
        """Test inserting a fixed wage component for the current period of a specified company."""
        company_id = 123
        wage_component = WageComponent(company_id, "fixed", {"Id": 1, "Code": "Test", "Value": "100.00"})
        expected_response = 12345
        self.client.service.WageComponentFixed_InsertCurrent.return_value = expected_response

        result = self.company_wage_component_service.post_current_fixed(wage_component)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentFixed_InsertCurrent.assert_called_once_with(
            CompanyId=company_id,
            WageComponent={"Id": 1, "Code": "Test", "Value": "100.00"},
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_insert(self):
        """Test inserting a variable wage component for a specified company, year, and period."""
        company_id = 123
        wage_component = WageComponent(company_id, "variable", {"Id": 1, "Code": "Test", "Value": "100.00"})
        period = 3
        year = 2024
        protected_mode = False
        expected_response = 12345
        self.client.service.WageComponentVar_Insert.return_value = expected_response

        result = self.company_wage_component_service.post_variable(wage_component, period, year, protected_mode)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentVar_Insert.assert_called_once_with(
            CompanyId=company_id,
            WageComponent={"Id": 1, "Code": "Test", "Value": "100.00"},
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_insert_current(self):
        """Test inserting a variable wage component for the current period of a specified company."""
        company_id = 123
        wage_component = WageComponent(company_id, "variable", {"Id": 1, "Code": "Test", "Value": "100.00"})
        expected_response = 12345
        self.client.service.WageComponentVar_InsertCurrent.return_value = expected_response

        result = self.company_wage_component_service.post_current_variable(wage_component)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentVar_InsertCurrent.assert_called_once_with(
            CompanyId=company_id,
            WageComponent={"Id": 1, "Code": "Test", "Value": "100.00"},
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_insert_batch(self):
        """Test inserting multiple variable wage components for a specified company, year, and period."""
        company_id = 123
        wage_components = [
            WageComponent(company_id, "variable", {"Id": 1, "Code": "Test1", "Value": "100.00"}),
            WageComponent(company_id, "variable", {"Id": 2, "Code": "Test2", "Value": "200.00"}),
        ]
        period = 3
        year = 2024
        protected_mode = False
        expected_response = [12345, 67890]
        self.client.service.WageComponentVar_Insert_Batch.return_value = expected_response

        result = self.company_wage_component_service.post_batch_variable(wage_components, period, year, protected_mode)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentVar_Insert_Batch.assert_called_once_with(
            WageComponents=[
                {"CompanyId": company_id, "Id": 1, "Code": "Test1", "Value": "100.00"},
                {"CompanyId": company_id, "Id": 2, "Code": "Test2", "Value": "200.00"},
            ],
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_get(self):
        """Test retrieving all variable wage components for a specified company, year, and period."""
        company_id = 123
        year = 2024
        period = 3
        expected_wage_components = [
            {"Id": 1, "Code": "WageComponent1", "Value": "100.00"},
            {"Id": 2, "Code": "WageComponent2", "Value": "200.00"},
        ]
        self.client.service.WageComponentVar_Get.return_value = expected_wage_components

        result = self.company_wage_component_service.get_variable(company_id, year, period)

        self.assertEqual(len(result), len(expected_wage_components))
        self.assertIsInstance(result[0], WageComponent)
        self.assertEqual(result[0].company_id, company_id)
        self.assertEqual(result[0].type, "variable")
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].code, "WageComponent1")
        self.assertEqual(result[0].value, "100.00")

        self.client.service.WageComponentVar_Get.assert_called_once_with(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )

    def test_variable_get_current(self):
        """Test retrieving all variable wage components for the current period of a specified company."""
        company_id = 123
        mock_response = [
            {"Id": 1, "Code": "Test1", "Value": "100.00"},
            {"Id": 2, "Code": "Test2", "Value": "200.00"},
        ]
        self.client.service.WageComponentVar_GetCurrent.return_value = mock_response

        result = self.company_wage_component_service.get_current_variable(company_id)

        expected_result = [
            WageComponent(company_id, "variable", {"Id": 1, "Code": "Test1", "Value": "100.00"}),
            WageComponent(company_id, "variable", {"Id": 2, "Code": "Test2", "Value": "200.00"}),
        ]
        self.assertEqual(result, expected_result)
        self.client.service.WageComponentVar_GetCurrent.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)

    def test_fixed_insert_batch(self):
        """Test inserting multiple fixed wage components for a specified company, year, and period."""
        year = 2024
        period = 3
        protected_mode = False
        wage_components = [
            WageComponent(123, "fixed", {"Id": 1, "Code": "Test1", "Value": Decimal("100.00")}),
            WageComponent(123, "fixed", {"Id": 2, "Code": "Test2", "Value": Decimal("200.00")}),
        ]
        expected_response = [1, 2]
        self.client.service.WageComponentFixed_Insert_Batch.return_value = expected_response

        result = self.company_wage_component_service.post_batch_fixed(wage_components, period, year, protected_mode)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentFixed_Insert_Batch.assert_called_once_with(
            WageComponents=[
                {"CompanyId": 123, "Id": 1, "Code": "Test1", "Value": Decimal("100.00")},
                {"CompanyId": 123, "Id": 2, "Code": "Test2", "Value": Decimal("200.00")},
            ],
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_fixed_stop(self):
        """Test stopping a fixed wage component for a specified company, year, and period."""
        company_id = 123
        component_id = 456
        period = 3
        year = 2024
        protected_mode = False

        self.company_wage_component_service.stop_fixed(company_id, component_id, period, year, protected_mode)

        self.client.service.WageComponentFixed_Stop.assert_called_once_with(
            CompanyId=company_id,
            WageComponentId=component_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_clear(self):
        """Test clearing all variable wage components for a specified company, year, and period."""
        company_id = 123
        period = 3
        year = 2024
        protected_mode = False
        expected_response = [1, 2, 3]
        self.client.service.WageComponentVar_Clear.return_value = expected_response

        result = self.company_wage_component_service.clear_variable(company_id, period, year, protected_mode)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentVar_Clear.assert_called_once_with(
            CompanyId=company_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_variable_clear_current(self):
        """Test clearing all variable wage components for the current period of a specified company."""
        company_id = 123
        expected_response = [1, 2, 3]
        self.client.service.WageComponentVar_ClearCurrent.return_value = expected_response

        result = self.company_wage_component_service.clear_current_variable(company_id)

        self.assertEqual(result, expected_response)
        self.client.service.WageComponentVar_ClearCurrent.assert_called_once_with(
            CompanyId=company_id,
            _soapheaders=self.mock_auth_header,
        )
