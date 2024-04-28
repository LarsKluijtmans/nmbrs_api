"""Unit tests for the CompanyLabourAgreementService class."""

import unittest
from unittest.mock import Mock

from decimal import Decimal

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.company import LabourAgreement, LeaveTypeGroup
from src.nmbrs.service.microservices.company import CompanyLabourAgreementService


class TestCompanyLabourAgreementService(unittest.TestCase):
    """Unit tests for the CompanyLabourAgreementService class."""

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
        self.labour_agreement_service = CompanyLabourAgreementService(self.auth_manager, self.client)

    def test_get(self):
        """Test retrieving labour agreements for a specific company, period, and year."""
        mock_labour_agreements = [Mock() for _ in range(3)]
        self.client.service.LabourAgreements_Get.return_value = mock_labour_agreements
        result = self.labour_agreement_service.get(1, 3, 2024)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(labour_agreement, LabourAgreement) for labour_agreement in result))
        self.client.service.LabourAgreements_Get.assert_called_once_with(
            CompanyId=1, Period=3, Year=2024, _soapheaders=self.mock_auth_header
        )

    def test_get_current(self):
        """Test retrieving current labour agreements for a specific company."""
        mock_labour_agreements = [Mock() for _ in range(3)]
        self.client.service.LabourAgreements_GetCurrent.return_value = mock_labour_agreements
        result = self.labour_agreement_service.get_current(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(labour_agreement, LabourAgreement) for labour_agreement in result))
        self.client.service.LabourAgreements_GetCurrent.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_leave_type_groups(self):
        """Test retrieving the company's leave type groups."""
        company_id = 123
        labour_agreement_settings_group_id = 456
        year = 2023
        period = 6
        expected_responses = [
            {
                "Type": "1",
                "Description": "Group 1",
                "CompanyLeaveBalance": [
                    {"DescriptionLeaveBalance": "leave balance", "FullTimeBalance": Decimal(10.1), "LeaveRoundingMethod": "Rounding Model"}
                ],
            },
            {"Type": "2", "Description": "Group 2"},
        ]
        self.client.service.CompanyLeaveTypeGroups_Get.return_value = expected_responses

        result = self.labour_agreement_service.get_leave_type_groups(company_id, labour_agreement_settings_group_id, period, year)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], LeaveTypeGroup)
        self.assertEqual(result[0].type, "1")
        self.assertEqual(result[0].description, "Group 1")
        self.assertEqual(result[1].type, "2")
        self.assertEqual(result[1].description, "Group 2")
        self.client.service.CompanyLeaveTypeGroups_Get.assert_called_once_with(
            CompanyId=company_id,
            LabourAgreementSettingsGroupId=labour_agreement_settings_group_id,
            Year=year,
            Period=period,
            _soapheaders=self.mock_auth_header,
        )
