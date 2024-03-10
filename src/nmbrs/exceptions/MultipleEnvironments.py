"""
This module defines a custom exception class for multiple environments.

Classes:
    MultipleEnvironments (Exception): Exception raised when the sso service is used but the user has accounts in multiple environments.

Dependencies:
    None
"""


class MultipleEnvironments(Exception):
    """
    Exception raised when the sso service is used but the user has accounts in multiple environments.
    """

    def __init__(
        self,
        message: str = "Multiple environments: User has multiple environments use the call sso_auth_with_domain, "
                       "to specify the environments you want to use.",
    ) -> None:
        """
        Constructor for MultipleEnvironments class.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)
