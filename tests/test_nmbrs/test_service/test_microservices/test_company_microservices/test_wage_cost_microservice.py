"""Unit tests for the CompanyWageCostService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.wage_cost import CompanyWageCostService, WageCost


class TestCompanyWageCostService(unittest.TestCase):
    """Unit tests for the CompanyWageCostService class."""

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
        self.wage_cost_service = CompanyWageCostService(self.auth_manager, self.client)

    def test_get(self):
        """Test retrieving the list of work cost values for a given company and year."""
        company_id = 123
        year = 2024
        expected_wage_cost_data = [
            {
                "Period": 1,
                "Year": 2024,
                "WorkCostPayroll": 100,
                "WorkCostFinancial": 200,
                "FiscalWage": 300,
                "WorkCostAvailableSpace": 400,
                "WorkCostBase": 500,
                "WorkCostToPay": 600,
                "WorkCostEstimated": "Yes",
                "WorkCostPaid": "No",
            },
            {
                "Period": 2,
                "Year": 2024,
                "WorkCostPayroll": 150,
                "WorkCostFinancial": 250,
                "FiscalWage": 350,
                "WorkCostAvailableSpace": 450,
                "WorkCostBase": 550,
                "WorkCostToPay": 650,
                "WorkCostEstimated": "No",
                "WorkCostPaid": "Yes",
            },
        ]
        self.client.service.WorkCost_GetList.return_value = expected_wage_cost_data

        result = self.wage_cost_service.get(company_id, year)

        self.assertEqual(len(result), len(expected_wage_cost_data))
        for i, wage_cost in enumerate(result):
            self.assertIsInstance(wage_cost, WageCost)
            self.assertEqual(wage_cost.company_id, company_id)
            self.assertEqual(wage_cost.period, expected_wage_cost_data[i]["Period"])
            self.assertEqual(wage_cost.year, expected_wage_cost_data[i]["Year"])
            self.assertEqual(wage_cost.payroll, expected_wage_cost_data[i]["WorkCostPayroll"])
            self.assertEqual(wage_cost.financial, expected_wage_cost_data[i]["WorkCostFinancial"])
            self.assertEqual(wage_cost.fiscal_wage, expected_wage_cost_data[i]["FiscalWage"])
            self.assertEqual(wage_cost.available_space, expected_wage_cost_data[i]["WorkCostAvailableSpace"])
            self.assertEqual(wage_cost.base, expected_wage_cost_data[i]["WorkCostBase"])
            self.assertEqual(wage_cost.to_pay, expected_wage_cost_data[i]["WorkCostToPay"])
            self.assertEqual(wage_cost.estimated, expected_wage_cost_data[i]["WorkCostEstimated"])
            self.assertEqual(wage_cost.paid, expected_wage_cost_data[i]["WorkCostPaid"])
        self.client.service.WorkCost_GetList.assert_called_once_with(CompanyId=company_id, Year=year, _soapheaders=self.mock_auth_header)

    def test_insert(self):
        """Test inserting a work cost value from the financial administration for a specific period."""
        company_id = 123
        value = 500.0
        period = 6
        year = 2024
        expected_response = 1  # Example response indicating success
        self.client.service.WorkCost_Insert.return_value = expected_response

        result = self.wage_cost_service.post(company_id, value, period, year)

        self.assertEqual(result, expected_response)
        self.client.service.WorkCost_Insert.assert_called_once_with(
            CompanyId=company_id,
            Value=value,
            Period=period,
            Year=year,
            _soapheaders=self.mock_auth_header,
        )
