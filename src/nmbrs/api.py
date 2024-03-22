"""Main class provided by the package."""

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
        Constructor method for NmbrsSoapAPI class.

        Initializes NmbrsSoapAPI instance with authentication details and settings.

        Args:
            username (str (optional)): Username for Nmbrs.
            token (str (optional)): Token for the Nmbrs SOAP API.
            domain (str (optional)): Nmbrs environment subdomain.
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
            auth_type (str (optional)): The type of authentication to be used. Options: "token", "domain", None (default: None).
        """
        self.sandbox = sandbox
        self.sso = SingleSingOnService(self.sandbox)
        self.debtor = DebtorService(self.sandbox)
        self.company = CompanyService(self.sandbox)
        self.employee = EmployeeService(self.sandbox)

        if auth_type == "token":
            params = find_empty_params(**{"username": username, "token": token})
            if params:
                raise ParameterMissingError(params=params)
            self.standard_auth(username, token)
        elif auth_type == "domain":
            params = find_empty_params(**{"username": username, "token": token, "domain": domain})
            if params:
                raise ParameterMissingError(params=params)
            self.standard_auth_with_domain(username, token, domain)

    def _initialize_services(self, auth_header: dict) -> None:
        """
        Initialize the services using the provided auth header.

        Args:
            auth_header (dict): header value used for authentication.
        """
        self.sso.set_auth_header(auth_header)
        self.debtor.set_auth_header(auth_header)
        self.company.set_auth_header(auth_header)
        self.employee.set_auth_header(auth_header)

    def standard_auth(self, username: str, token: str) -> None:
        """
        Perform standard authentication and initialize related services.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
        """
        domain = self.debtor.get_domain(username, token)
        auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }
        self._initialize_services(auth_header)

    def standard_auth_with_domain(self, username: str, token: str, domain: str) -> None:
        """
        Create the auth header with domain object and initialize related services.
        Note:: The username, token and domain are never validated in this routine.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
            domain (str): Nmbrs environment subdomain.
        """
        auth_header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }
        self._initialize_services(auth_header)
