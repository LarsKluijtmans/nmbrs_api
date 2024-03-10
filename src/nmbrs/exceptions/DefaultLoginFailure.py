"""
This module defines a custom exception class for default login failure.

Classes:
    DefaultLoginFailure (Exception): Exception raised when nmbrs raises the exception: "1006: Generic Login Security Failure".

Dependencies:
    None
"""


class DefaultLoginFailure(Exception):
    """
    Exception raised when nmbrs raises the exception: "1006: Generic Login Security Failure".
    """

    def __init__(
        self,
        message: str = "Login failure: Login failed. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for UnauthorizedAccess class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        if resources is None:
            resources = []
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)
