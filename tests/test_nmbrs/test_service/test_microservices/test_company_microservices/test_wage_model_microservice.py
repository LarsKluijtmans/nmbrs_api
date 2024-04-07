"""Unit tests for the CompanyWageModelService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.company.wage_model import CompanyWageModelService, WageModel


class TestCompanyWageModelService(unittest.TestCase):
    """Unit tests for the CompanyWageModelService class."""

    def setUp(self):
        self.client = Mock()
        self.wage_model_service = CompanyWageModelService(self.client)
        self.mock_auth_header = Mock()
        self.wage_model_service.set_auth_header(self.mock_auth_header)

    def test_get(self):
        """Test retrieving wage codes that belong to a company's wage model."""
        company_id = 123
        expected_wage_model_data = [
            {"Code": "W001", "Description": "Wage Code 1"},
            {"Code": "W002", "Description": "Wage Code 2"},
        ]
        self.client.service.WageModel_GetWageCodes.return_value = expected_wage_model_data

        result = self.wage_model_service.get(company_id)

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

        result = self.wage_model_service.get_2(company_id)

        self.assertEqual(len(result), len(expected_wage_model_data))
        for i, wage_model in enumerate(result):
            self.assertEqual(wage_model.company_id, company_id)
            self.assertEqual(wage_model.code, expected_wage_model_data[i]["Code"])
            self.assertEqual(wage_model.description, expected_wage_model_data[i]["Description"])
        self.client.service.WageModel2_GetWageCodes.assert_called_once_with(CompanyId=company_id, _soapheaders=self.mock_auth_header)
