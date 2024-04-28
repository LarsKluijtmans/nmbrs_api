"""Unit tests for the DebtorTitleService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.debtor import DebtorTitleService


class TestDebtorTitleService(unittest.TestCase):
    """Unit tests for the DebtorTitleService class."""

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
        self.debtor_title_service = DebtorTitleService(self.auth_manager, self.client)

    def test_get_all_titles(self):
        """Test retrieving all titles for a debtor."""
        mock_titles = [
            {"TitleName": "Title1"},
            {"TitleName": "Title2"},
            {"TitleName": "Title3"},
        ]
        self.client.service.Title_GetList.return_value = mock_titles
        result = self.debtor_title_service.get_all(1)
        self.assertEqual(result, ["Title1", "Title2", "Title3"])
        self.client.service.Title_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_insert_titles(self):
        """Test inserting a title for a debtor."""
        self.debtor_title_service.post(1, "Test Title")
        self.client.service.Title_Insert.assert_called_once_with(
            DebtorId=1,
            title={"TitleName": "Test Title"},
            _soapheaders=self.mock_auth_header,
        )
