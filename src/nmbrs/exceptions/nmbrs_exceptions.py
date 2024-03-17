# pylint: disable=line-too-long
"""
This module defines custom exceptions related to authorization failures and invalid authentication in nmbrs.

Classes:
    - AuthorizationError(Exception): Exception raised when unauthorized access occurs.
    - AuthenticationError(Exception): Exception raised for invalid authentication.
"""


class AuthorizationError(Exception):
    """
    Exception raised when unauthorized access occurs.

    [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "Unauthorized access: You do not have the necessary permissions for the required resources. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for AuthorizationError class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        self.resources = resources
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)


class AuthenticationError(Exception):
    """
    Exception raised for invalid authentication.

    [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-error-1001-Invalid-Authentication)
    """

    def __init__(
        self,
        message: str = "Invalid Authentication: The provided credentials are not valid.",
    ) -> None:
        """
        Constructor for AuthenticationError class.

        Args:
            message (str): Explanation of the error.
        """
        super().__init__(message)


class UnknownNmbrsError(Exception):
    """
    Exception raised when encountering unknown errors related to Nmbrs API.

    For more details on Nmbrs API error codes, refer to: [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "Unknown error occurred in Nmbrs API.",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for UnknownNmbrsError class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources related to the error.
        """
        self.resources = resources
        self.message = f"{message} Resources: {', '.join(resources) if resources else 'None'}"
        super().__init__(self.message)
