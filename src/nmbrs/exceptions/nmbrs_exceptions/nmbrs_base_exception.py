"""Base for nmbrs errors"""

from nmbrs.__version__ import __git_issues__


class NmbrsBaseException(Exception):
    """
    Base for nmbrs errors

    For more details on Nmbrs API error codes, refer to:
        - [Nmbrs API Error Codes](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
        - [API Invalid Authentication](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-error-1001-Invalid-Authentication)
        - [API User Template](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template)
    """

    def __init__(self, error_code: int, resource: str):
        self.error_code = error_code
        self.resource = resource

        self.name = ""
        self.cause = ""
        self.solution = ""

        self.get_error()

        self.message = f"Error: {self.name}\n" f"  Resource: {self.resource}\n" f"  Cause: {self.cause}\n" f"  Solution: {self.solution}\n"
        super(Exception, self).__init__(self.message)

    def get_error(self):
        """Get the name, cause and solution of an exception."""
        match self.error_code:
            case 1001:
                self.name = "Invalid Authentication"
                self.cause = "The email address, API token or domain is not valid. "
                self.solution = (
                    "Make sure that the email and the token that you use are right. For more information see"
                    " [API Invalid Authentication](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-"
                    "error-1001-Invalid-Authentication)"
                )
            case 1002:
                self.name = "Unauthorized Access"
                self.cause = "You do not have the rights for the debtor, company or the employee services. "
                self.solution = (
                    "Contact the administrator of the environment and review the API template. See"
                    " [API User Template](https://support.nmbrs.com/hc/en-us/articles/360013527371-API-User-Template)"
                )
            case 1003:
                self.name = "Unauthorized Access Data"
                self.cause = "You do not have the rights for the debtor or company."
                self.solution = "Contact the administrator of the environment and review access rights by tags/filters."
            case _:
                self.name = "Unknown Nmbrs error"
                self.cause = "Unknown"
                self.solution = f"Create a issue on our git page: {__git_issues__}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message})"
