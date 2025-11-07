"""Unit tests for Nmbrs class with transport and settings parameters."""

from unittest.mock import patch, MagicMock
import unittest

from zeep import Settings
from zeep.transports import Transport

from src.nmbrs.data_classes.debtor import Domain
from src.nmbrs import Nmbrs


class TestNmbrsTransportSettings(unittest.TestCase):
    """Unit tests for Nmbrs class with transport and settings parameters."""

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    @patch("src.nmbrs.service.company_service.Client")
    @patch("src.nmbrs.service.employee_service.Client")
    @patch("src.nmbrs.service.report_service.Client")
    def test_transport_passed_to_services(self, mock_report_client, mock_employee_client, mock_company_client, mock_debtor_client, mock_get_domain):
        """Test that transport parameter is passed to all service clients."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        # Create a mock transport
        mock_transport = MagicMock(spec=Transport)
        
        # Initialize Nmbrs with transport
        nmbrs = Nmbrs(username="test_user", token="test_token", transport=mock_transport, auth_type="token")
        
        # Access services to trigger client creation
        _ = nmbrs.debtor
        _ = nmbrs.company
        _ = nmbrs.employee
        _ = nmbrs.report
        
        # Verify all clients were created with transport
        mock_debtor_client.assert_called_once()
        mock_company_client.assert_called_once()
        mock_employee_client.assert_called_once()
        mock_report_client.assert_called_once()
        
        # Check that transport was passed to each client
        for mock_client_call in [mock_debtor_client, mock_company_client, mock_employee_client, mock_report_client]:
            call_kwargs = mock_client_call.call_args[1]
            self.assertIn('transport', call_kwargs)
            self.assertEqual(call_kwargs['transport'], mock_transport)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    @patch("src.nmbrs.service.company_service.Client")
    @patch("src.nmbrs.service.employee_service.Client")
    @patch("src.nmbrs.service.report_service.Client")
    def test_settings_passed_to_services(self, mock_report_client, mock_employee_client, mock_company_client, mock_debtor_client, mock_get_domain):
        """Test that settings parameter is passed to all service clients."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        # Create a mock settings
        mock_settings = MagicMock(spec=Settings)
        
        # Initialize Nmbrs with settings
        nmbrs = Nmbrs(username="test_user", token="test_token", settings=mock_settings, auth_type="token")
        
        # Access services to trigger client creation
        _ = nmbrs.debtor
        _ = nmbrs.company
        _ = nmbrs.employee
        _ = nmbrs.report
        
        # Verify all clients were created with settings
        mock_debtor_client.assert_called_once()
        mock_company_client.assert_called_once()
        mock_employee_client.assert_called_once()
        mock_report_client.assert_called_once()
        
        # Check that settings was passed to each client
        for mock_client_call in [mock_debtor_client, mock_company_client, mock_employee_client, mock_report_client]:
            call_kwargs = mock_client_call.call_args[1]
            self.assertIn('settings', call_kwargs)
            self.assertEqual(call_kwargs['settings'], mock_settings)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    @patch("src.nmbrs.service.company_service.Client")
    @patch("src.nmbrs.service.employee_service.Client")
    @patch("src.nmbrs.service.report_service.Client")
    def test_transport_and_settings_passed_together(self, mock_report_client, mock_employee_client, mock_company_client, mock_debtor_client, mock_get_domain):
        """Test that both transport and settings can be passed together."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        mock_transport = MagicMock(spec=Transport)
        mock_settings = MagicMock(spec=Settings)
        
        # Initialize Nmbrs with both transport and settings
        nmbrs = Nmbrs(username="test_user", token="test_token", transport=mock_transport, settings=mock_settings, auth_type="token")
        
        # Access services to trigger client creation
        _ = nmbrs.debtor
        _ = nmbrs.company
        _ = nmbrs.employee
        _ = nmbrs.report
        
        # Check that both transport and settings were passed to each client
        for mock_client_call in [mock_debtor_client, mock_company_client, mock_employee_client, mock_report_client]:
            call_kwargs = mock_client_call.call_args[1]
            self.assertIn('transport', call_kwargs)
            self.assertIn('settings', call_kwargs)
            self.assertEqual(call_kwargs['transport'], mock_transport)
            self.assertEqual(call_kwargs['settings'], mock_settings)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    @patch("src.nmbrs.service.company_service.Client")
    @patch("src.nmbrs.service.employee_service.Client")
    @patch("src.nmbrs.service.report_service.Client")
    def test_backward_compatibility_no_transport_or_settings(self, mock_report_client, mock_employee_client, mock_company_client, mock_debtor_client, mock_get_domain):
        """Test that services work correctly without transport or settings (backward compatibility)."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        # Initialize Nmbrs without transport or settings
        nmbrs = Nmbrs(username="test_user", token="test_token", auth_type="token")
        
        # Access services to trigger client creation
        _ = nmbrs.debtor
        _ = nmbrs.company
        _ = nmbrs.employee
        _ = nmbrs.report
        
        # Verify all clients were created
        mock_debtor_client.assert_called_once()
        mock_company_client.assert_called_once()
        mock_employee_client.assert_called_once()
        mock_report_client.assert_called_once()
        
        # Check that transport and settings are not in kwargs when not provided
        for mock_client_call in [mock_debtor_client, mock_company_client, mock_employee_client, mock_report_client]:
            call_kwargs = mock_client_call.call_args[1] if mock_client_call.call_args else {}
            # When not provided, they should not be in kwargs (or should be None)
            # The actual behavior depends on how we implemented it - let's check they're not passed
            if call_kwargs:
                # If kwargs exist, transport and settings should not be present
                self.assertNotIn('transport', call_kwargs)
                self.assertNotIn('settings', call_kwargs)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    def test_transport_stored_in_nmbrs(self, mock_client, mock_get_domain):
        """Test that transport is stored as an attribute in Nmbrs instance."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        mock_transport = MagicMock(spec=Transport)
        nmbrs = Nmbrs(username="test_user", token="test_token", transport=mock_transport, auth_type="token")
        
        self.assertEqual(nmbrs.transport, mock_transport)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    def test_settings_stored_in_nmbrs(self, mock_client, mock_get_domain):
        """Test that settings is stored as an attribute in Nmbrs instance."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        mock_settings = MagicMock(spec=Settings)
        nmbrs = Nmbrs(username="test_user", token="test_token", settings=mock_settings, auth_type="token")
        
        self.assertEqual(nmbrs.settings, mock_settings)

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    @patch("src.nmbrs.service.debtor_service.Client")
    def test_transport_and_settings_stored_together(self, mock_client, mock_get_domain):
        """Test that both transport and settings are stored as attributes."""
        mock_get_domain.return_value = Domain(data={"Domain": "test", "SubDomain": "test"})
        
        mock_transport = MagicMock(spec=Transport)
        mock_settings = MagicMock(spec=Settings)
        nmbrs = Nmbrs(username="test_user", token="test_token", transport=mock_transport, settings=mock_settings, auth_type="token")
        
        self.assertEqual(nmbrs.transport, mock_transport)
        self.assertEqual(nmbrs.settings, mock_settings)

