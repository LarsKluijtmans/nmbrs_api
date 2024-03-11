"""
Unit tests for: src/nmbrs/utils/nmbrs_exception_handler.py
"""
from unittest import TestCase

import zeep.exceptions

from src.nmbrs.exceptions import InvalidCredentials, LoginSecurityFailure, MultipleEnvironmentAccounts, \
    DomainNotFoundError, AuthenticationError, AuthorizationError
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_sso_exception_handler, nmbrs_exception_handler


class TestNmbrsSSOExceptionHandler(TestCase):
    """
    Unit tests for the nmbrs_sso_exception_handler decorator.
    """

    def test_handle_login_security_failure(self):
        """
        Test handling of LoginSecurityFailure exception.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def raise_login_security_failure():
            raise zeep.exceptions.Fault("---> 1006: Generic Login Security Failure")

        with self.assertRaises(LoginSecurityFailure) as context:
            raise_login_security_failure()

        self.assertEqual(context.exception.resources, ["resource1", "resource2"])

    def test_handle_multiple_environment_accounts(self):
        """
        Test handling of MultipleEnvironmentAccounts exception.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def raise_multiple_environment_accounts():
            raise zeep.exceptions.Fault("---> 2042: This username belongs to multiple environments")

        with self.assertRaises(MultipleEnvironmentAccounts):
            raise_multiple_environment_accounts()

    def test_handle_domain_not_found_error(self):
        """
        Test handling of DomainNotFoundError exception.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def raise_domain_not_found_error():
            raise zeep.exceptions.Fault("---> 2043: Invalid Domain")

        with self.assertRaises(DomainNotFoundError) as context:
            raise_domain_not_found_error()

        self.assertEqual(context.exception.resources, ["resource1", "resource2"])

    def test_handle_invalid_credentials(self):
        """
        Test handling of InvalidCredentials exception.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def raise_invalid_credentials():
            raise zeep.exceptions.Fault("---> Invalid combination email/password")

        with self.assertRaises(InvalidCredentials) as context:
            raise_invalid_credentials()

        self.assertEqual(context.exception.resources, ["resource1", "resource2"])

    def test_no_exception(self):
        """
        Test when no exception is raised.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def no_exception():
            return "No exception"

        self.assertEqual(no_exception(), "No exception")

    def test_raise_zeep_exception(self):
        """
        Test when a zeep exception is raised, and the message is not blocked.
        """

        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def exception_raised():
            raise zeep.exceptions.Fault("custom error message")

        with self.assertRaises(Exception) as context:
            exception_raised()

        self.assertEqual(str(context.exception), "custom error message")

    def test_raise_exception(self):
        """
        Test when an exception is raised.
        """
        @nmbrs_sso_exception_handler(resources=["resource1", "resource2"])
        def exception_raised():
            raise TypeError("custom error message")

        with self.assertRaises(Exception) as context:
            exception_raised()

        self.assertEqual(str(context.exception), "custom error message")


class TestNmbrsExceptionHandler(TestCase):
    """
    Unit tests for the nmbrs_exception_handler decorator.
    """

    def test_handle_authentication_error(self):
        """
        Test handling of AuthenticationError exception.
        """

        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def raise_authentication_error():
            raise zeep.exceptions.Fault("---> 1001: Invalid Authentication")

        with self.assertRaises(AuthenticationError):
            raise_authentication_error()

    def test_handle_authorization_error(self):
        """
        Test handling of AuthorizationError exception.
        """

        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def raise_authorization_error():
            raise zeep.exceptions.Fault("---> 1002: Unauthorized access")

        with self.assertRaises(AuthorizationError) as context:
            raise_authorization_error()

        self.assertEqual(context.exception.resources, ["resource1", "resource2"])

    def test_handle_multiple_authorization_error(self):
        """
        Test handling of AuthorizationError exception with different error message.
        """

        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def raise_authorization_error():
            raise zeep.exceptions.Fault("---> 1003: Unauthorized access")

        with self.assertRaises(AuthorizationError) as context:
            raise_authorization_error()

        self.assertEqual(context.exception.resources, ["resource1", "resource2"])

    def test_no_exception(self):
        """
        Test when no exception is raised.
        """

        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def no_exception():
            return "No exception"

        self.assertEqual(no_exception(), "No exception")

    def test_raise_zeep_exception(self):
        """
        Test when a zeep exception is raised, and the message is not blocked.
        """

        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def exception_raised():
            raise zeep.exceptions.Fault("custom error message")

        with self.assertRaises(Exception) as context:
            exception_raised()

        self.assertEqual(str(context.exception), "custom error message")

    def test_raise_exception(self):
        """
        Test when an exception is raised.
        """
        @nmbrs_exception_handler(resources=["resource1", "resource2"])
        def exception_raised():
            raise TypeError("custom error message")

        with self.assertRaises(Exception) as context:
            exception_raised()

        self.assertEqual(str(context.exception), "custom error message")
