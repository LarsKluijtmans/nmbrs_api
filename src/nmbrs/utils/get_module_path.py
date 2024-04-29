"""Get the module-style path from the given root path."""

import inspect
import os


def get_module_path(func) -> str:
    """
    Get the module-style path from the given root path.

    Args:
        func (any): The function the location of is needed

    Returns:
        str: The module-style path.

    """
    calling_module = inspect.getmodule(func)
    calling_file = inspect.getfile(calling_module)

    # Split the path based on "nmbrs" and take the last occurrence
    parts = calling_file.split("nmbrs")
    file_path = "nmbrs" + parts[-1]

    directory = os.path.dirname(file_path)

    module_path = directory.replace(os.sep, ".")

    module_name = os.path.splitext(os.path.basename(file_path))[0]

    module_name_with_dots = f"{module_path}.{module_name}"
    return module_name_with_dots
