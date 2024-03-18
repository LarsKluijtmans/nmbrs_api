"""This module provides a function to find empty parameters in a set of keyword arguments."""


def find_empty_params(**kwargs):
    """
    Finds and returns the names of empty parameters (parameters with value None or an empty string) in the provided keyword arguments.

    Args:
        **kwargs: Keyword arguments where keys represent parameter names and values represent parameter values.

    Returns:
        List: A list containing the names of empty parameters.
    """
    empty_params = []
    for param_name, param_value in kwargs.items():
        if param_value is None or param_value == "":
            empty_params.append(param_name)
    return empty_params
