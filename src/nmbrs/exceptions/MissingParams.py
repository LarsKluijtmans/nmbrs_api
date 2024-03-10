"""
This module defines a custom exception class for missing parameters.

Classes:
    MissingParams (Exception): Exception raised when a required parameter is missing, empty, or None.

Dependencies:
    None
"""


class MissingParams(Exception):
    """
    Exception raised when a required parameter is missing, empty or None.
    """

    def __init__(
        self,
        message: str = "Missing parameters: The following paramater are missing, empty, or None: ",
        params: list[str] = None,
    ) -> None:
        """
        Constructor for UnauthorizedAccess class.

        Args:
            message (str): Explanation of the error.
            params (list[str]): List of parameters that are missing.
        """
        if params is None:
            params = []
        self.message = f"{message}{', '.join(params)}"
        super().__init__(self.message)
