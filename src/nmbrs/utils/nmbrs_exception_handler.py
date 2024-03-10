"""
Exception Handling Decorators for Nmbrs SOAP API

Provides decorators to handle exceptions raised by the Nmbrs SOAP API and customize exception handling
based on specific error codes.

Functions:
    - nmbrs_exception_handler(resources: list[str]): Decorator for handling exceptions from the Nmbrs SOAP API.
    - nmbrs_sso_exception_handler(resources: list[str]): Decorator for handling Single Sign-On (SSO) exceptions
      from the Nmbrs SOAP API.

Dependencies:
    - zeep.exceptions: Exception classes provided by Zeep library for SOAP web service communication.
    - Custom exception classes: DefaultLoginFailure, InvalidAuthentication, InvalidDomain,
      InvalidEmailPassword, MultipleEnvironments, UnauthorizedAccess.

Note:
    These decorators are intended to be used with functions that interact with the Nmbrs SOAP API.
"""
import zeep.exceptions

from ..exceptions.DefaultLoginFailure import DefaultLoginFailure
from ..exceptions.InvalidAuthentication import InvalidAuthentication
from ..exceptions.InvalidDomain import InvalidDomain
from ..exceptions.InvalidEmailPassword import InvalidEmailPassword
from ..exceptions.MultipleEnvironments import MultipleEnvironments
from ..exceptions.UnauthorizedAccess import UnauthorizedAccess


def nmbrs_exception_handler(resources: list[str]):
    """
    Decorator to handle exceptions raised by Nmbrs SOAP API.

    Args:
        resources (list[str]): List of resources being used.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except zeep.exceptions.Fault as e:
                error_message = str(e)
                if "---> 1001: Invalid Authentication" in error_message:
                    raise InvalidAuthentication() from e
                if "---> 1002: Unauthorized access" in error_message:
                    raise UnauthorizedAccess(resources=resources) from e
                if "---> 1003: Unauthorized access" in error_message:
                    raise UnauthorizedAccess(resources=resources) from e
                raise e

        return wrapper

    return decorator


def nmbrs_sso_exception_handler(resources: list[str]):
    """
    Decorator to handle exceptions raised by Nmbrs SOAP API.

    Args:
        resources (list[str]): List of resources being used.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except zeep.exceptions.Fault as e:
                error_message = str(e)
                if "---> 1006: Generic Login Security Failure" in error_message:
                    raise DefaultLoginFailure(resources=resources) from e
                if (
                    "---> 2042: This username belongs to multiple environments"
                    in error_message
                ):
                    raise MultipleEnvironments() from e
                if " ---> 2043: Invalid Domain" in error_message:
                    raise InvalidDomain(resources=resources) from e
                if "---> Invalid combination email/password" in error_message:
                    raise InvalidEmailPassword(resources=resources) from e
                raise e

        return wrapper

    return decorator
