"""This module defines custom exceptions related to authorization failures and invalid authentication in nmbrs."""

from .exceptions import Error


class AuthorizationError(Error):
    """
    Exception raised when unauthorized access occurs.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "You do not have the necessary permissions for the required resources. Resources: ",
        resources: list[str] = None,
    ) -> None:
        self.cause = "You do not have the rights for the debtor, company or the employee services."
        self.solution = "Contact the administrator of the environment and review the API user template."
        self.resources = resources
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(message)


class AuthenticationError(Error):
    """
    Exception raised for invalid authentication.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
        - [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-error-1001-Invalid-Authentication)
    """

    def __init__(
        self,
        message: str = "Invalid Authentication: The email address, API token or domain is not valid.",
    ) -> None:
        self.cause = "The email address, API token or domain is not valid. "
        self.solution = "Make sure that the email and the token that you use are right."
        self.message = message
        super().__init__(message)


class AuthorizationDataError(Error):
    """
    Exception raised for when you do not have the rights for the debtor or company.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "You do not have the rights for the debtor or company.",
    ) -> None:
        self.cause = "You do not have the rights for the debtor or company."
        self.solution = "Contact the administrator of the environment and review access rights by tags/filters. "
        super().__init__(message)


class UnknownNmbrsError(Error):
    """
    Exception raised when encountering unknown errors related to Nmbrs API.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "Unknown error occurred in Nmbrs API.",
        resources: list[str] = None,
    ) -> None:
        self.resources = resources
        self.message = f"{message} Resources: {', '.join(resources) if resources else 'None'}"
        super().__init__(message)


class AuthorizationEmployeeError(Error):
    """
    Exception raised when you are trying to access an employee you do not have access to.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(self, message: str = "You do not have the rights to the employee that you are using the API method for.") -> None:
        self.cause = "You do not have the rights to the employee that you are using the API method for."
        self.solution = "Make sure you have the right EmployeeID."
        self.message = message
        super().__init__(message)


class AuthorizationCompanyError(Error):
    """
    Exception raised when you are trying to access a company you do not have access to.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "You do not have the rights to the company that you are using the API method for. ",
        resources: list[str] = None,
    ) -> None:
        self.cause = "You do not have the rights to the company that you are using the API method for."
        self.solution = "Make sure you have the right CompanyID."
        self.resources = resources
        self.message = f"{message} Resources: {', '.join(resources) if resources else 'None'}"
        super().__init__(message)


class AuthorizationDebtorError(Error):
    """
    Exception raised when you are trying to access a debtor you do not have access to.

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "You do not have the rights to the debtor that you are using the API method for.",
    ) -> None:
        self.cause = "You do not have the rights to the debtor that you are using the API method for."
        self.solution = "Make sure you have the right DebtorId."
        self.message = message
        super().__init__(message)
