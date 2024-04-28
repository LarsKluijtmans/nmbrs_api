"""Unit tests for the AuthManager class."""

import unittest

from src.nmbrs.auth.token_manager import AuthManager


class TestAuthManager(unittest.TestCase):
    """Unit tests for the AuthManager class."""

    def test_set_auth_header(self):
        """Test setting the authentication header."""
        auth_manager = AuthManager()
        username = "test_user"
        token = "test_token"
        domain = "test_domain"

        auth_manager.set_auth_header(username, token, domain)

        self.assertEqual(auth_manager.get_username(), username)
        self.assertEqual(auth_manager.get_token(), token)
        self.assertEqual(auth_manager.get_domain(), domain)

    def test_get_username_with_no_header_set(self):
        """Test getting the username when no authentication header is set."""
        auth_manager = AuthManager()

        username = auth_manager.get_username()

        self.assertEqual(username, "")

    def test_get_token_with_no_header_set(self):
        """Test getting the token when no authentication header is set."""
        auth_manager = AuthManager()

        token = auth_manager.get_token()

        self.assertEqual(token, "")

    def test_get_domain_with_no_header_set(self):
        """Test getting the domain when no authentication header is set."""
        auth_manager = AuthManager()

        domain = auth_manager.get_domain()

        self.assertEqual(domain, "")
