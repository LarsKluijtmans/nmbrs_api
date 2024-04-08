"""Exception Handling Decorators for Nmbrs SOAP API"""

import zeep.exceptions

from ..exceptions import (
    AuthenticationException,
    AuthorizationException,
    AuthorizationDataException,
    NoValidSubscriptionException,
    InvalidHourComponentException,
    InvalidWageComponentException,
    UnauthorizedEmployeeException,
    UnauthorizedCompanyException,
    InvalidPeriodException,
    UnauthorizedDebtorException,
    UnknownNmbrsException,
    UnknownException,
    LoginSecurityFailureException,
    MultipleEnvironmentAccountsException,
    DomainNotFoundException,
    InvalidCredentialsException,
)


def nmbrs_exception_handler(resource: str):
    """
    Decorator to handle exceptions raised by Nmbrs SOAP API.

    Args:
        resource (str): Resources being called.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except zeep.exceptions.Fault as e:
                e_str = str(e)
                if "---> 1001:" in e_str:
                    raise AuthenticationException(resource=resource) from e
                if "---> 1002:" in e_str:
                    raise AuthorizationException(resource=resource) from e
                if "---> 1003:" in e_str:
                    raise AuthorizationDataException(resource=resource) from e
                if "---> 1004:" in e_str:
                    raise NoValidSubscriptionException(resource=resource) from e
                if "---> 2001:" in e_str:
                    raise InvalidHourComponentException(resource=resource) from e
                if "---> 2002:" in e_str:
                    raise InvalidWageComponentException(resource=resource) from e
                if "---> 2003:" in e_str:
                    raise UnauthorizedEmployeeException(resource=resource) from e
                if "---> 2004:" in e_str:
                    raise UnauthorizedCompanyException(resource=resource) from e
                if "---> 2006:" in e_str:
                    raise InvalidPeriodException(resource=resource) from e
                if "---> 2009:" in e_str:
                    raise UnauthorizedDebtorException(resource=resource) from e
                if "---> 9999:" in e_str:
                    raise UnknownNmbrsException(resource=resource) from e

                raise UnknownException(resource=resource) from e

        return wrapper

    return decorator


def nmbrs_sso_exception_handler(resource: str):
    """
    Decorator to handle exceptions raised by Nmbrs SOAP API.

    Args:
        resource (str): Resources being called.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except zeep.exceptions.Fault as e:
                e_str = str(e)
                if "---> 1006: Generic Login Security Failure" in e_str:
                    raise LoginSecurityFailureException(resource=resource) from e
                if "---> 2042: This username belongs to multiple environments" in e_str:
                    raise MultipleEnvironmentAccountsException(resource=resource) from e
                if "---> 2043: Invalid Domain" in e_str:
                    raise DomainNotFoundException(resource=resource) from e
                if "---> Invalid combination email/password" in e_str:
                    raise InvalidCredentialsException(resource=resource) from e
                raise UnknownException(resource=resource) from e

        return wrapper

    return decorator
