import zeep.exceptions
from ..exceptions.InvalidAuthentication import InvalidAuthentication
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
                if "---> 1001: " in error_message:
                    raise InvalidAuthentication()
                elif "---> 1002: " in error_message:
                    raise UnauthorizedAccess(resources=resources)
                elif "---> 1003: Unauthorized access" in error_message:
                    raise UnauthorizedAccess(resources=resources)

        return wrapper

    return decorator
