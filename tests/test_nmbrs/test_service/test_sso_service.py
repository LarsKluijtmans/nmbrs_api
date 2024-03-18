"""Unit tests for the SingleSingOnService class."""

from unittest import TestCase, mock

from src.nmbrs_soap.service.sso_service import SingleSingOnService


class TestSingleSingOnService(TestCase):
    """Unit tests for the SingleSingOnService class."""

    mock_service = None

    def setUp(self):
        self.mock_service = mock.Mock()
        self.mock_client = mock.Mock(service=self.mock_service)
        self.service = SingleSingOnService(sandbox=False)
        self.service.sso_service = self.mock_client

    def test_get_sso_url(self):
        """Test get_sso_url method."""
        token = "test_token"
        nmbrs_env = "test_env.nmbrs.nl"
        expected_url = f"https://{nmbrs_env}/applications/common/externalactions.aspx?login=nmbrs&ID={token}"
        actual_url = self.service.get_sso_url(token, nmbrs_env)
        self.assertEqual(actual_url, expected_url)

    def test_get_sso_url_missing_nmbrs_domain(self):
        """Test get_sso_url method, without .nmbrs.nl in the nmbrs_env."""
        token = "test_token"
        nmbrs_env = "test_env"
        expected_url = f"https://{nmbrs_env}.nmbrs.nl/applications/common/externalactions.aspx?login=nmbrs&ID={token}"
        actual_url = self.service.get_sso_url(token, nmbrs_env)
        self.assertEqual(actual_url, expected_url)

    def test_sso_auth_with_password(self):
        """Test sso_auth_with_password method."""
        self.mock_service.GetToken.return_value = "test_token"
        username = "test_user"
        password = "test_password"
        token = self.service.sso_auth_with_password(username, password)
        self.assertEqual(token, "test_token")
        self.mock_service.GetToken.assert_called_once_with(Username=username, Password=password)

    def test_sso_auth_with_token(self):
        """Test sso_auth_with_token method."""
        self.mock_service.GetToken2.return_value = "test_token"
        username = "test_user"
        token = "test_token"
        result = self.service.sso_auth_with_token(username, token)
        self.assertEqual(result, "test_token")
        self.mock_service.GetToken2.assert_called_once_with(Username=username, Token=token)

    def test_sso_auth_with_domain(self):
        """Test sso_auth_with_domain method."""
        self.mock_service.GetTokenWithDomain.return_value = "test_token"
        username = "test_user"
        password = "test_password"
        domain = "test_domain"
        token = self.service.sso_auth_with_domain(username, password, domain)
        self.assertEqual(token, "test_token")
        self.mock_service.GetTokenWithDomain.assert_called_once_with(Username=username, Password=password, Domain=domain)

    def test_sso_auth_with_password_exception(self):
        """Test sso_auth_with_password method with an exception."""
        self.mock_service.GetToken.side_effect = Exception("Test Exception")
        username = "test_user"
        password = "test_password"
        with self.assertRaises(Exception):
            self.service.sso_auth_with_password(username, password)
        self.mock_service.GetToken.assert_called_once_with(Username=username, Password=password)

    def test_sso_auth_with_token_exception(self):
        """Test sso_auth_with_token method with an exception."""
        self.mock_service.GetToken2.side_effect = Exception("Test Exception")
        username = "test_user"
        token = "test_token"
        with self.assertRaises(Exception):
            self.service.sso_auth_with_token(username, token)
        self.mock_service.GetToken2.assert_called_once_with(Username=username, Token=token)

    def test_sso_auth_with_domain_exception(self):
        """Test sso_auth_with_domain method with an exception."""
        self.mock_service.GetTokenWithDomain.side_effect = Exception("Test Exception")
        username = "test_user"
        password = "test_password"
        domain = "test_domain"
        with self.assertRaises(Exception):
            self.service.sso_auth_with_domain(username, password, domain)
        self.mock_service.GetTokenWithDomain.assert_called_once_with(
            Username=username,
            Password=password,
            Domain=domain,
        )
