"""Unit tests for the ReportService class."""

import unittest
from unittest.mock import Mock, MagicMock

from src.nmbrs.service.report_service import ReportService
from src.nmbrs.exceptions.nmbrs_exceptions.background_task import (
    BackgroundTaskException,
    UnknownBackgroundTaskException,
    UnknownCall,
)
from src.nmbrs.auth.token_manager import AuthManager


class TestReportService(unittest.TestCase):
    """Unit tests for the ReportService class."""

    def setUp(self):
        """Set up test dependencies."""
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.mock_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": "test_username",
                "Token": "test_token",
                "Domain": "test_domain",
            }
        }
        self.report_service = ReportService(self.auth_manager)
        self.mock_client = Mock()

        # Mock the settings
        self.mock_settings = MagicMock()
        self.mock_client.settings = self.mock_settings
        self.mock_settings.__enter__.return_value = None

        self.report_service.client = self.mock_client

    def test_background_task_result_success(self):
        """Test retrieving background task result successfully."""
        mock_response = {
            "Status": "Success",
            "Content": "<report>test</report>",
        }

        self.mock_client.service.Reports_BackgroundTask_Result.return_value = mock_response

        expected_result = {"report": "test"}
        result = self.report_service.background_task_result("task_id")

        self.assertEqual(result, expected_result)
        self.mock_client.service.Reports_BackgroundTask_Result.assert_called_once_with(TaskId="task_id", _soapheaders=self.mock_auth_header)

    def test_background_task_result_error(self):
        """Test retrieving background task result with error status."""
        mock_response = {"Status": "Error"}
        self.mock_client.service.Reports_BackgroundTask_Result.return_value = mock_response

        with self.assertRaises(BackgroundTaskException):
            self.report_service.background_task_result("task_id")

        self.mock_client.service.Reports_BackgroundTask_Result.assert_called_once_with(TaskId="task_id", _soapheaders=self.mock_auth_header)

    def test_background_task_result_unknown_status(self):
        """Test retrieving background task result with unknown status."""
        mock_response = {"Status": "Unknown"}
        self.mock_client.service.Reports_BackgroundTask_Result.return_value = mock_response

        with self.assertRaises(UnknownBackgroundTaskException):
            self.report_service.background_task_result("task_id")

        self.mock_client.service.Reports_BackgroundTask_Result.assert_called_once_with(TaskId="task_id", _soapheaders=self.mock_auth_header)

    def test_background_task_result_timeout(self):
        """Test retrieving background task result timeout."""
        mock_response = {"Status": "Executing"}
        self.mock_client.service.Reports_BackgroundTask_Result.return_value = mock_response

        result = self.report_service.background_task_result("task_id", wait_limit=1)
        self.assertIsNone(result)

        self.mock_client.service.Reports_BackgroundTask_Result.assert_called_once_with(TaskId="task_id", _soapheaders=self.mock_auth_header)

    def test_get_task_id_success(self):
        """Test getting task ID successfully."""
        mock_response = "task_id"

        mock_func = Mock()
        mock_func.return_value = mock_response
        mock_call = Mock()
        mock_call.return_value = mock_func

        self.mock_client.service.__getitem__ = mock_call

        task_id = self.report_service.get_task_id("task_name", {})

        self.assertEqual(task_id, mock_response)
        mock_func.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_task_id_unknown_call(self):
        """Test getting task ID with unknown call."""

        def raise_attribute_error(*args, **kwargs):
            """Raise AttributeError exception"""
            raise AttributeError

        self.mock_client.service.__getitem__ = raise_attribute_error

        with self.assertRaises(UnknownCall):
            self.report_service.get_task_id("unknown_task_name", {})
