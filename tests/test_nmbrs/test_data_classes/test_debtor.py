"""Unit tests for the Debtor level data classes."""

import unittest

from src.nmbrs.data_classes.debtor import AbsenceVerzuim, Event, WebhookSetting


class TestDebtorClasses(unittest.TestCase):
    """Unit tests for the Debtor level data classes."""

    def test_absence_verzuim_class_to_dict(self):
        """Test the to_dict method of the AbsenceVerzuim class."""
        data = {
            "DebtorID": 123,
            "CompanyID": 456,
            "EmployeeID": 789,
            "XML": "<xml><data>test</data></xml>",
        }
        absence_verzuim = AbsenceVerzuim(data)
        expected_result = {
            "debtor_id": 123,
            "company_id": 456,
            "employee_id": 789,
            "xml": {"xml": {"data": "test"}},
        }
        self.assertEqual(absence_verzuim.to_dict(), expected_result)

    def test_event_class_to_insert_dict(self):
        """Test the to_insert_dict method of the Event class."""
        data = {"EventId": 123, "EventName": "Test Event", "Active": True}
        event = Event(data)
        expected_result = {"EventId": 123, "Active": True}
        self.assertEqual(event.to_insert_dict(), expected_result)

    def test_webhook_setting_class_to_dict(self):
        """Test the to_dict method of the WebhookSetting class."""
        data = {
            "WebhookSettingId": 123,
            "Name": "Test Webhook",
            "Endpoint": "https://example.com/webhook",
            "Active": True,
            "Event": [{"EventId": 456, "EventName": "Test Event", "Active": True}],
        }
        webhook_setting = WebhookSetting(1, data)
        expected_result = {
            "webhook_setting_id": 123,
            "debtor_id": 1,
            "name": "Test Webhook",
            "endpoint": "https://example.com/webhook",
            "active": True,
            "events": [{"active": True, "event_id": 456, "event_name": "Test Event"}],
        }
        self.assertEqual(webhook_setting.to_dict(), expected_result)

    def test_to_insert_dict(self):
        """Test the to_insert_dict method of the WebhookSetting class."""
        obj = {
            "WebhookSettingId": 123,
            "Name": "Sample Webhook",
            "Endpoint": "http://example.com/webhook",
            "Active": True,
            "Event": [{"EventId": 1, "Active": True}, {"EventId": 2, "Active": False}],
        }
        webhook_setting = WebhookSetting(1, obj)
        expected_result = {
            "WebhookSetting": {
                "Name": "Sample Webhook",
                "Endpoint": "http://example.com/webhook",
                "Active": True,
                "Events": [
                    {"EventId": 1, "Active": True},
                    {"EventId": 2, "Active": False},
                ],
            }
        }
        self.assertEqual(webhook_setting.to_insert_dict(), expected_result)
