"""Decorator ensuring the decorated function always returns a list."""


def return_list(func):
    """
    Decorator ensuring the decorated function always returns a list.

    If result is None, returns an empty list.
    If result is not a list, wraps it in a list before returning.

    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: The decorated function.
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                return []
            if not isinstance(result, list):
                return [result]
            return result
        except TypeError as e:
            if str(e) == "'NoneType' object is not iterable":
                return []
            raise e

    return wrapper
