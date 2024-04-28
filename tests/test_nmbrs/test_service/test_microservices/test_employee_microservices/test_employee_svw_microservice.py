"""Unit tests for the EmployeeSvwService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.svw import EmployeeSvwService, SVW


class TestEmployeeSvwService(unittest.TestCase):
    """Unit tests for the EmployeeSvwService class."""

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
        self.svw_service = EmployeeSvwService(self.auth_manager, self.client)

    def test_get_all_by_company(self):
        """Test getting all SVW settings of all employees in a company."""
        company_id = 123
        self.client.service.SVW_GetAll_AllEmployeesByCompany.return_value = [
            {
                "EmployeeId": 1,
                "EmployeeSVWSettings": {
                    "EmployeeSVWSettings": [
                        {
                            "Id": 1,
                            "CreateDate": "2023-01-01",
                            "StartYear": 2023,
                            "StartPeriod": 1,
                            "InfluenceObligedInsuranced": True,
                            "Wao_Wia": True,
                            "Ww": True,
                            "Zw": True,
                            "IncomeRelatedContributionZvw": True,
                            "CodeZvw": "CODE123",
                            "EmploymentType": "Full-time",
                            "PhaseClassification": "Phase 1",
                            "EmploymentSequenceTaxId": 123,
                            "CAO": {"CAOId": 1, "CAOCode": "CAO123", "CAODescription": "Description 1"},
                            "RiskGroup": {"RiskGroupId": 2, "RiskGroupCode": "RG123", "RiskGroupDescription": "Description 2"},
                            "Sector": {"SectorId": 3, "SectorCode": "SEC123", "SectorDescription": "Description 3"},
                            "WageCostBenefit": {"WageCostBenefitCode": "WCB123", "EndPeriod": 6, "EndYear": 2024},
                        }
                    ]
                },
            }
        ]

        result = self.svw_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 1)

        for item in result:
            self.assertIsInstance(item, SVW)

        svw = result[0]
        self.assertEqual(svw.employee_id, 1)
        self.assertEqual(svw.id, 1)
        self.assertEqual(svw.create_date, "2023-01-01")
        self.assertEqual(svw.start_year, 2023)
        self.assertEqual(svw.start_period, 1)
        self.assertTrue(svw.influence_obliged_insurance)
        self.assertTrue(svw.wao_wia)
        self.assertTrue(svw.ww)
        self.assertTrue(svw.zw)
        self.assertTrue(svw.income_related_contribution_zvw)
        self.assertEqual(svw.code_zvw, "CODE123")
        self.assertEqual(svw.employment_type, "Full-time")
        self.assertEqual(svw.phase_classification, "Phase 1")
        self.assertEqual(svw.employment_sequence_tax_id, 123)
        self.assertEqual(svw.cao_id, 1)
        self.assertEqual(svw.cao_code, "CAO123")
        self.assertEqual(svw.cao_description, "Description 1")
        self.assertEqual(svw.risk_group_id, 2)
        self.assertEqual(svw.risk_group_code, "RG123")
        self.assertEqual(svw.risk_group_description, "Description 2")
        self.assertEqual(svw.sector_id, 3)
        self.assertEqual(svw.sector_code, "SEC123")
        self.assertEqual(svw.sector_description, "Description 3")
        self.assertEqual(svw.wage_cost_benefit_code, "WCB123")
        self.assertEqual(svw.wage_cost_benefit_end_period, 6)
        self.assertEqual(svw.wage_cost_benefit_end_year, 2024)

        self.client.service.SVW_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )
