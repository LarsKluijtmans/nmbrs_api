"""Unit tests for the nmbrs_sso_exception_handler decorator."""

from unittest import TestCase
import zeep.exceptions

from src.nmbrs.exceptions import (
    UnknownNmbrsException,
    AuthorizationDataException,
    AuthorizationException,
    AuthenticationException,
    InvalidHourComponentException,
    UnauthorizedDebtorException,
    UnauthorizedCompanyException,
    InvalidPeriodException,
    UnauthorizedEmployeeException,
    InvalidWageComponentException,
    UnknownException,
    NoValidSubscriptionException,
)
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class TestNmbrsExceptionHandler(TestCase):
    """Unit tests for the nmbrs_exception_handler decorator."""

    def test_handle_authentication_error(self):
        """Test handling of AuthenticationException exception."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authentication_error():
            raise zeep.exceptions.Fault("---> 1001: Invalid Authentication")

        with self.assertRaises(AuthenticationException) as context:
            raise_authentication_error()

        self.assertEqual(context.exception.resource, "resource1")

    def test_handle_authorization_error(self):
        """Test handling of AuthorizationException exception."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_error():
            raise zeep.exceptions.Fault("---> 1002: Unauthorized access")

        with self.assertRaises(AuthorizationException) as context:
            raise_authorization_error()

        self.assertEqual(context.exception.resource, "resource1")

    def test_handle_unauthorized_data_error(self):
        """Test handling of AuthorizationDataException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_data_error():
            raise zeep.exceptions.Fault("---> 1003: Unauthorized access")

        with self.assertRaises(AuthorizationDataException):
            raise_authorization_data_error()

    def test_handle_no_valid_subscription_error(self):
        """Test handling of NoValidSubscriptionException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def handle_no_valid_subscription_error():
            raise zeep.exceptions.Fault("---> 1004: Disabled, no valid subscription")

        with self.assertRaises(NoValidSubscriptionException):
            handle_no_valid_subscription_error()

    def test_handle_invalid_hour_component_error(self):
        """Test handling of InvalidHourComponentException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def handle_invalid_hour_component_error():
            raise zeep.exceptions.Fault("---> 2001: Invalid Hour component")

        with self.assertRaises(InvalidHourComponentException):
            handle_invalid_hour_component_error()

    def test_handle_invalid_wage_component_error(self):
        """Test handling of InvalidWageComponentException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def handle_invalid_wage_component_error():
            raise zeep.exceptions.Fault("---> 2002: Invalid Wage component")

        with self.assertRaises(InvalidWageComponentException):
            handle_invalid_wage_component_error()

    def test_handle_authorization_employee_error(self):
        """Test handling of UnauthorizedEmployeeException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_employee_error():
            raise zeep.exceptions.Fault("---> 2003: Unauthorized access")

        with self.assertRaises(UnauthorizedEmployeeException):
            raise_authorization_employee_error()

    def test_handle_authorization_company_error(self):
        """Test handling of UnauthorizedCompanyException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_company_error():
            raise zeep.exceptions.Fault("---> 2004: Unauthorized access")

        with self.assertRaises(UnauthorizedCompanyException):
            raise_authorization_company_error()

    def test_handle_invalid_period_error(self):
        """Test handling of InvalidPeriodException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def handle_invalid_period_error():
            raise zeep.exceptions.Fault("---> 2006: Invalid Period")

        with self.assertRaises(InvalidPeriodException):
            handle_invalid_period_error()

    def test_handle_authorization_debtor_error(self):
        """Test handling of UnauthorizedDebtorException exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_debtor_error():
            raise zeep.exceptions.Fault("---> 2009: Unauthorized access")

        with self.assertRaises(UnauthorizedDebtorException):
            raise_authorization_debtor_error()

    def test_handle_unknown_error(self):
        """Test handling of UnknownNmbrsError exception with different error message."""

        @nmbrs_exception_handler(resource="resource1")
        def raise_authorization_error():
            raise zeep.exceptions.Fault("---> 9999: Unkown")

        with self.assertRaises(UnknownNmbrsException) as context:
            raise_authorization_error()

        self.assertEqual(context.exception.resource, "resource1")

    def test_no_exception(self):
        """Test when no exception is raised."""

        @nmbrs_exception_handler(resource="resource1")
        def no_exception():
            return "No exception"

        self.assertEqual(no_exception(), "No exception")

    def test_raise_zeep_exception(self):
        """Test when a zeep exception is raised, and the message is not blocked."""

        @nmbrs_exception_handler(resource="resource1")
        def exception_raised():
            raise zeep.exceptions.Fault("custom error message")

        with self.assertRaises(UnknownException) as context:
            exception_raised()

        self.assertEqual(context.exception.resource, "resource1")

    def test_raise_exception(self):
        """Test when an exception is raised."""

        @nmbrs_exception_handler(resource="resource1")
        def exception_raised():
            raise TypeError("custom error message")

        with self.assertRaises(Exception) as context:
            exception_raised()

        self.assertEqual(str(context.exception), "custom error message")
