"""Unit tests for the Nmbrs class."""

from unittest.mock import patch
import unittest
from src.nmbrs import Nmbrs
from src.nmbrs.exceptions import ParameterMissingError


class TestNmbrs(unittest.TestCase):
    """Unit tests for the Nmbrs class."""

    def test_empty_initializer(self):
        """Test initialization of Nmbrs class with default parameters."""
        nmbrs = Nmbrs()

        self.assertIsNotNone(nmbrs.sso)
        self.assertIsNotNone(nmbrs.debtor)
        self.assertIsNotNone(nmbrs.company)
        self.assertIsNotNone(nmbrs.employee)

    def test_standard_auth_with_missing_params(self):
        """Test standard authentication with missing parameters."""
        with self.assertRaises(ParameterMissingError) as e:
            Nmbrs(username="test_user", auth_type="token")
        self.assertEqual(e.exception.params, ["token"])

    def test_standard_auth_with_domain_with_missing_params(self):
        """Test standard authentication with domain with missing parameters."""
        with self.assertRaises(ParameterMissingError) as e:
            Nmbrs(username="test_user", auth_type="domain")
        self.assertEqual(e.exception.params, ["token", "domain"])

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    def test_standard_auth(self, mock_get_domain):
        """Test standard authentication with correct parameters."""
        username = "test_user"
        token = "test_token"
        domain = "test_domain"

        # Mocking the DebtorService.get_domain method
        mock_get_domain.return_value = domain
        nmbrs = Nmbrs()
        nmbrs.standard_auth(username=username, token=token)

        expected_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }

        self.assertEqual(nmbrs.debtor.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.company.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.employee.auth_header, expected_auth_header)

        # Check if DebtorService.get_domain method is called with the correct parameters
        mock_get_domain.assert_called_once_with("test_user", "test_token")

    @patch("src.nmbrs.service.debtor_service.DebtorService.get_domain")
    def test_standard_auth_constructor(self, mock_get_domain):
        """Test standard authentication with correct parameters, initialized using the constructor."""
        username = "test_user"
        token = "test_token"
        domain = "test_domain"
        # Mocking the DebtorService.get_domain method
        mock_get_domain.return_value = domain

        nmbrs = Nmbrs(username=username, token=token, auth_type="token")

        expected_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }

        self.assertEqual(nmbrs.debtor.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.company.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.employee.auth_header, expected_auth_header)

        # Check if DebtorService.get_domain method is called with the correct parameters
        mock_get_domain.assert_called_once_with("test_user", "test_token")

    def test_standard_auth_with_domain(self):
        """Test standard authentication with domain parameter."""
        nmbrs = Nmbrs()
        username = "test_user"
        token = "test_token"
        domain = "test_domain"
        nmbrs.standard_auth_with_domain(username=username, token=token, domain=domain)

        expected_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }

        self.assertEqual(nmbrs.debtor.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.company.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.employee.auth_header, expected_auth_header)

    def test_standard_auth_with_domain_constructor(self):
        """Test standard authentication with domain parameter, initialized using the constructor."""
        username = "test_user"
        token = "test_token"
        domain = "test_domain"
        nmbrs = Nmbrs(username=username, token=token, domain=domain, auth_type="domain")

        expected_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }

        self.assertEqual(nmbrs.debtor.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.company.auth_header, expected_auth_header)
        self.assertEqual(nmbrs.employee.auth_header, expected_auth_header)
