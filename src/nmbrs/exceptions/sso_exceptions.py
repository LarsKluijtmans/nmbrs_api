"""
This module defines custom exceptions related to authentication and authorization failures in nmbrs.

Classes:
    - LoginSecurityFailure(Exception): Exception raised when nmbrs raises the exception: "1006: Generic Login Security Failure".
    - InvalidCredentials(Exception): Exception raised when the combination email and password is not valid.
    - MultipleEnvironmentAccounts(Exception): Exception raised when the user has accounts in multiple environments.
    - DomainNotFoundError(Exception): Exception raised when the specified domain (Nmbrs environment subdomain) does not exist.
"""


class LoginSecurityFailure(Exception):
    """
    Exception raised when nmbrs raises the exception: "1006: Generic Login Security Failure".
    """

    def __init__(
        self,
        message: str = "Login failure: Login failed. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for LoginSecurityFailure class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        self.resources = resources
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)


class InvalidCredentials(Exception):
    """
    Exception raised when the combination email and password is not valid.
    """

    def __init__(
        self,
        message: str = "Invalid email/password: The combination email/password was not recognized by nmbrs. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for InvalidCredentials class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources used that might cause the error.
        """
        self.resources = resources
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)


class MultipleEnvironmentAccounts(Exception):
    """
    Exception raised when the SSO service is used but the user has accounts in multiple environments.
    """

    def __init__(
        self,
        message: str = "Multiple environments: User has multiple environments use the call sso_auth_with_domain, "
        "to specify the environments you want to use.",
    ) -> None:
        """
        Constructor for MultipleEnvironmentAccounts class.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)


class DomainNotFoundError(Exception):
    """
    Exception raised when the specified domain (Nmbrs environment subdomain) does not exist.
    """

    def __init__(
        self,
        message: str = "Invalid domain: The specified domain does not exist. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for DomainNotFoundError class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        self.resources = resources
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)
