"""
This module defines a custom exception class for invalid email and password combination.

Classes:
    InvalidEmailPassword (Exception): Exception raised when the combination email and password is not valid.

Dependencies:
    None
"""


class InvalidEmailPassword(Exception):
    """
    Exception raised when the combination email and password is not valid.
    """

    def __init__(
        self,
        message: str = "Invalid email/password: The combination email/password was not recognized by nmbrs. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for InvalidEmailPassword class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources used that might cause the error.
        """
        if resources is None:
            resources = []
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)
