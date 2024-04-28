"""Unit tests for the CompanyPensionService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.pension import CompanyPensionService, Pension, PensionXML


class TestCompanyPensionService(unittest.TestCase):
    """Unit tests for the CompanyPensionService class."""

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
        self.pension_service = CompanyPensionService(self.auth_manager, self.client)

    def test_get_pensions(self):
        """Test retrieving pension exports associated with a company."""
        mock_pensions = [
            {
                "PensionExportID": 1,
                "SerialNumber": 123,
                "Period": 6,
                "Year": 2024,
                "Status": "Completed",
                "SentAt": datetime(2024, 1, 1),
                "CorrectionTijdvakStart": datetime(2024, 2, 2),
                "CorrectionTijdvakEnd": datetime(2024, 3, 3),
            },
            {
                "PensionExportID": 2,
                "SerialNumber": 124,
                "Period": 5,
                "Year": 2024,
                "Status": "Completed",
                "SentAt": datetime(2024, 4, 4),
                "CorrectionTijdvakStart": datetime(2024, 5, 5),
                "CorrectionTijdvakEnd": datetime(2024, 6, 6),
            },
        ]
        self.client.service.PensionExport_GetList.return_value = mock_pensions
        result = self.pension_service.get(1, 2024)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Pension)
        self.assertEqual(result[0].pension_export_id, 1)
        self.assertEqual(result[0].serial_number, 123)
        self.assertEqual(result[0].period, 6)
        self.assertEqual(result[0].year, 2024)
        self.assertEqual(result[0].status, "Completed")
        self.assertEqual(result[0].send_at, datetime(2024, 1, 1))
        self.assertEqual(result[0].correctie_tijdvak_start, datetime(2024, 2, 2))
        self.assertEqual(result[0].correctie_tijdvak_end, datetime(2024, 3, 3))
        self.client.service.PensionExport_GetList.assert_called_once_with(CompanyId=1, intYear=2024, _soapheaders=self.mock_auth_header)

    def test_get_xml_pension(self):
        """Test retrieving XML pension export associated with a company."""
        mock_pension_xml = "<xml>Pension XML</xml>"
        self.client.service.PensionExport_GetXML.return_value = mock_pension_xml
        result = self.pension_service.get_xml(1, 123)
        self.assertIsInstance(result, PensionXML)
        self.assertEqual(result.xml, "<xml>Pension XML</xml>")
        self.client.service.PensionExport_GetXML.assert_called_once_with(
            CompanyId=1, PensionExportID=123, _soapheaders=self.mock_auth_header
        )
