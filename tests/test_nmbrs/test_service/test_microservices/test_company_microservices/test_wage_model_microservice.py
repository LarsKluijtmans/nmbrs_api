"""Unit tests for the CompanyWageModelService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.wage_model import CompanyWageModelService, WageModel


class TestCompanyWageModelService(unittest.TestCase):
    """Unit tests for the CompanyWageModelService class."""

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
        self.wage_model_service = CompanyWageModelService(self.auth_manager, self.client)

    def test_get(self):
        """Test retrieving wage codes that belong to a company's wage model."""
        company_id = 123
        expected_wage_model_data = [
            {"Code": "W001", "Description": "Wage Code 1"},
            {"Code": "W002", "Description": "Wage Code 2"},
        ]
        self.client.service.WageModel_GetWageCodes.return_value = expected_wage_model_data

        result = self.wage_model_service.get_current(company_id)

        self.assertEqual(len(result), len(expected_wage_model_data))
        for i, wage_model in enumerate(result):
            self.assertIsInstance(wage_model, WageModel)
            self.assertEqual(wage_model.company_id, company_id)
            self.assertEqual(wage_model.code, expected_wage_model_data[i]["Code"])
            self.assertEqual(wage_model.description, expected_wage_model_data[i]["Description"])
        self.client.service.WageModel_GetWageCodes.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)

    def test_get_2(self):
        """Test retrieving wage codes using an alternate method."""
        company_id = 123
        expected_wage_model_data = [
            {"Code": "W001", "Description": "Wage Code 1"},
            {"Code": "W002", "Description": "Wage Code 2"},
        ]
        self.client.service.WageModel2_GetWageCodes.return_value = expected_wage_model_data

        result = self.wage_model_service.get_current_2(company_id)

        self.assertEqual(len(result), len(expected_wage_model_data))
        for i, wage_model in enumerate(result):
            self.assertEqual(wage_model.company_id, company_id)
            self.assertEqual(wage_model.code, expected_wage_model_data[i]["Code"])
            self.assertEqual(wage_model.description, expected_wage_model_data[i]["Description"])
        self.client.service.WageModel2_GetWageCodes.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)
