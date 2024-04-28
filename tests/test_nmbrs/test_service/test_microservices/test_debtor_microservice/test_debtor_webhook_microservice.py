"""Unit tests for the DebtorWebHooksService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.data_classes.debtor import WebhookSetting, Event
from src.nmbrs.service.microservices.debtor import DebtorWebHooksService


class TestDebtorWebhookService(unittest.TestCase):
    """Unit tests for the DebtorWebHooksService class."""

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
        self.debtor_webhook_service = DebtorWebHooksService(self.auth_manager, self.client)

    def test_delete_webhook(self):
        """Test deleting a webhook for a debtor."""
        self.client.service.WebhookSettings_Delete.return_value = True
        result = self.debtor_webhook_service.delete(1, 123)
        self.assertTrue(result)
        self.client.service.WebhookSettings_Delete.assert_called_once_with(
            DebtorId=1, WebhookSettingId=123, _soapheaders=self.mock_auth_header
        )

    def test_get_webhooks(self):
        """Test retrieving all webhooks for a debtor."""
        mock_webhooks = [Mock() for _ in range(3)]
        self.client.service.WebhookSettings_Get.return_value = mock_webhooks
        result = self.debtor_webhook_service.get_all(1)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(webhook, WebhookSetting) for webhook in result))
        self.client.service.WebhookSettings_Get.assert_called_once_with(DebtorId=1, _soapheaders=self.mock_auth_header)

    def test_get_webhook_events(self):
        """Test retrieving all webhook events."""
        mock_events = [Mock() for _ in range(3)]
        self.client.service.WebhookSettings_GetEvents.return_value = mock_events
        result = self.debtor_webhook_service.get_all_events()
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(event, Event) for event in result))
        self.client.service.WebhookSettings_GetEvents.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_insert_webhook(self):
        """Test inserting a webhook for a debtor."""
        mock_webhook_setting = Mock(to_insert_dict=Mock(return_value={"TestKey": "TestValue"}))
        self.client.service.WebhookSettings_Insert.return_value = 123
        result = self.debtor_webhook_service.insert(1, mock_webhook_setting)
        self.assertEqual(result, 123)
        self.client.service.WebhookSettings_Insert.assert_called_once_with(
            DebtorId=1,
            WebhookSetting={"TestKey": "TestValue"},
            _soapheaders=self.mock_auth_header,
        )
