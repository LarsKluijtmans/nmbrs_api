"""Unit tests for the DebtorTitleService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.service.microservices.debtor import DebtorTitleService


class TestDebtorTitleService(unittest.TestCase):
    """Unit tests for the DebtorTitleService class."""

    def setUp(self):
        self.mock_client = Mock()
        self.debtor_title_service = DebtorTitleService(self.mock_client)
        self.mock_auth_header = Mock()
        self.debtor_title_service.set_auth_header(self.mock_auth_header)

    def test_get_all_titles(self):
        """Test retrieving all titles for a debtor."""
        mock_titles = [
            {"TitleName": "Title1"},
            {"TitleName": "Title2"},
            {"TitleName": "Title3"},
        ]
        self.mock_client.service.Title_GetList.return_value = mock_titles
        result = self.debtor_title_service.get_all(1)
        self.assertEqual(result, ["Title1", "Title2", "Title3"])
        self.mock_client.service.Title_GetList.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_insert_titles(self):
        """Test inserting a title for a debtor."""
        self.debtor_title_service.insert(1, "Test Title")
        self.mock_client.service.Title_Insert.assert_called_once_with(
            DebtorId=1,
            title={"TitleName": "Test Title"},
            _soapheaders=self.mock_auth_header,
        )
