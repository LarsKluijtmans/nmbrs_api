"""Main class provided by the package."""

from .auth.token_manager import AuthManager
from .exceptions import ParameterMissingError
from .service.company_service import CompanyService
from .service.debtor_service import DebtorService
from .service.employee_service import EmployeeService
from .service.sso_service import SingleSingOnService
from .utils.find_empty_params import find_empty_params


class Nmbrs:
    """
    A class representing the Nmbrs SOAP API.

    This class provides an interface to interact with various Nmbrs SOAP API services.

    [Nmbrs SOAP API](https://api.nmbrs.nl/soap/v3/)
    """

    def __init__(
        self,
        username: str = None,
        token: str = None,
        domain: str = None,
        sandbox: bool = True,
        auth_type: str = None,
    ):
        """
        Initializes a Nmbrs SOAP API instance with authentication details and settings.

        Args:
            username (str, optional): Username for Nmbrs.
            token (str, optional): Token for the Nmbrs SOAP API.
            domain (str, optional): Nmbrs environment subdomain.
            sandbox (bool, optional): A boolean indicating whether to use the sandbox environment. Default is True.
            auth_type (str, optional): The type of authentication to be used. Options: "token", "domain", None (default).
        """
        self.sandbox = sandbox
        self.auth_manager = AuthManager()
        self.sso = SingleSingOnService(self.auth_manager, self.sandbox)
        self.debtor = DebtorService(self.auth_manager, self.sandbox)
        self.company = CompanyService(self.auth_manager, self.sandbox)
        self.employee = EmployeeService(self.auth_manager, self.sandbox)

        if auth_type == "token":
            self.auth_with_token(username, token)
        elif auth_type == "domain":
            self.auth_with_domain(username, token, domain)

    def auth_with_token(self, username: str, token: str) -> None:
        """
        Perform standard authentication using token and initialize related services.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
        """
        params = find_empty_params(**{"username": username, "token": token})
        if params:
            raise ParameterMissingError(params=params)
        domain = self.debtor.get_domain(username, token)
        self.auth_manager.set_auth_header(username, token, domain.sub_domain)

    def auth_with_domain(self, username: str, token: str, domain: str) -> None:
        """
        Create the auth header with domain object and initialize related services.
        Note: The username, token, and domain are not validated in this routine.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
            domain (str): Nmbrs environment subdomain.
        """
        params = find_empty_params(**{"username": username, "token": token, "domain": domain})
        if params:
            raise ParameterMissingError(params=params)
        self.auth_manager.set_auth_header(username, token, domain)
