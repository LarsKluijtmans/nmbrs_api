import zeep.exceptions

from nmbrs.exceptions.InvalidAuthentication import InvalidAuthentication


def nmbrs_exception_handler(func):
    """
    Decorator

    :param func: The function to be decorated.
    :return: The decorated function.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except zeep.exceptions.Fault as e:
            if "---> 1001:" in str(e):
                raise InvalidAuthentication(str(e))

    return wrapper
