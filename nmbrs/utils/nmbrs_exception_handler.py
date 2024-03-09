import zeep.exceptions

from nmbrs.exceptions.DefaultLoginFailure import DefaultLoginFailure
from nmbrs.exceptions.InvalidAuthentication import InvalidAuthentication
from nmbrs.exceptions.InvalidDomain import InvalidDomain
from nmbrs.exceptions.InvalidEmailPassword import InvalidEmailPassword
from nmbrs.exceptions.MultipleEnvironments import MultipleEnvironments
from nmbrs.exceptions.UnauthorizedAccess import UnauthorizedAccess


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
                    raise InvalidAuthentication()
                elif "---> 1002: Unauthorized access" in error_message:
                    raise UnauthorizedAccess(resources=resources)
                elif "---> 1003: Unauthorized access" in error_message:
                    raise UnauthorizedAccess(resources=resources)
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
                    raise DefaultLoginFailure(resources=resources)
                elif "---> 2042: This username belongs to multiple environments" in error_message:
                    raise MultipleEnvironments()
                elif " ---> 2043: Invalid Domain" in error_message:
                    raise InvalidDomain(resources=resources)
                elif "---> Invalid combination email/password" in error_message:
                    raise InvalidEmailPassword(resources=resources)

                raise e

        return wrapper

    return decorator
