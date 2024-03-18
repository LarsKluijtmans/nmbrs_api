"""Unit tests for the CompanyLabourAgreementService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs_soap.data_classes.company import LabourAgreement
from src.nmbrs_soap.service.microservices.company import CompanyLabourAgreementService


class TestCompanyLabourAgreementService(unittest.TestCase):
    """Unit tests for the CompanyLabourAgreementService class."""

    def setUp(self):
        self.client = Mock()
        self.labour_agreement_service = CompanyLabourAgreementService(self.client)
        self.mock_auth_header = Mock()
        self.labour_agreement_service.set_auth_header(self.mock_auth_header)

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
