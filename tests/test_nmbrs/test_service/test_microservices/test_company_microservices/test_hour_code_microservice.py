"""Unit tests for the CompanyHourModelService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.company.hour_model import CompanyHourModelService, HourCode


class TestCompanyHourModelService(unittest.TestCase):
    """Unit tests for the CompanyHourModelService class."""

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
        self.hour_model_service = CompanyHourModelService(self.auth_manager, self.client)

    def test_get_hour_codes(self):
        """Test retrieving hour codes associated with a company's hour model."""
        mock_hour_codes = [{"Code": "HC1", "Description": "Hour Code 1"}, {"Code": "HC2", "Description": "Hour Code 2"}]
        self.client.service.HourModel_GetHourCodes.return_value = mock_hour_codes
        result = self.hour_model_service.get_current(1)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], HourCode)
        self.assertEqual(result[0].code, "HC1")
        self.assertEqual(result[0].description, "Hour Code 1")
        self.client.service.HourModel_GetHourCodes.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)

    def test_get_hour_codes_2(self):
        """Test retrieving hour codes associated with a company's hour model 2."""
        mock_hour_codes = [{"Code": "HC3", "Description": "Hour Code 3"}, {"Code": "HC4", "Description": "Hour Code 4"}]
        self.client.service.HourModel2_GetHourCodes.return_value = mock_hour_codes
        result = self.hour_model_service.get_current_2(1)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], HourCode)
        self.assertEqual(result[0].code, "HC3")
        self.assertEqual(result[0].description, "Hour Code 3")
        self.client.service.HourModel2_GetHourCodes.assert_called_once_with(CompanyId=1, _soapheaders=self.mock_auth_header)
