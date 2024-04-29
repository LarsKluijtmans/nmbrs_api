"""Main class provided by the package."""

import logging
from .auth.token_manager import AuthManager
from .exceptions import ParameterMissingError
from .service.company_service import CompanyService
from .service.debtor_service import DebtorService
from .service.employee_service import EmployeeService
from .service.report_service import ReportService
from .utils.find_empty_params import find_empty_params

logger = logging.getLogger(__name__)


class Nmbrs:
    """
    A class representing the Nmbrs SOAP API.

    This class provides an interface to interact with various Nmbrs SOAP API services.

    [Nmbrs SOAP API](https://api.nmbrs.nl/soap/v3/)
    """

    def __init__(
        self,
        username: str,
        token: str,
        auth_type: str = "token",
        domain: str = None,
        sandbox: bool = True,
    ):
        """
        Initializes a Nmbrs SOAP API instance with authentication details and settings.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
            auth_type (str): The type of authentication to be used. Options: "token", "domain". Default "token"
            domain (str, optional): Nmbrs environment subdomain (used when the auth_type paramater is set to "domain").
            sandbox (bool, optional): A boolean indicating whether to use the sandbox environment. Default is True.
        """
        if not sandbox:
            logger.warning("Live environment is activated")  # pragma: no cover

        self.sandbox = sandbox
        self.auth_manager = AuthManager()
        self.debtor = DebtorService(self.auth_manager, self.sandbox)
        self.company = CompanyService(self.auth_manager, self.sandbox)
        self.employee = EmployeeService(self.auth_manager, self.sandbox)
        self.report = ReportService(self.auth_manager, self.sandbox)

        if auth_type == "token":
            self.auth_with_token(username, token)
        elif auth_type == "domain":
            self.auth_with_domain(username, token, domain)

    def auth_with_token(self, username: str, token: str):
        """
        Perform standard authentication using token and initialize related services.

        Args:
            username (str): Username for Nmbrs.
            token (str): Token for the Nmbrs SOAP API.
        """
        params = find_empty_params(**{"username": username, "token": token})
        if params:
            logger.error("Parameter missing: %s", params)
            raise ParameterMissingError(params=params)
        domain = self.debtor.get_domain(username, token)
        self.auth_manager.set_auth_header(username, token, domain.sub_domain)
        logger.info("Authentication with token successful")

    def auth_with_domain(self, username: str, token: str, domain: str):
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
            logger.error("Parameter missing: %s", params)
            raise ParameterMissingError(params=params)
        self.auth_manager.set_auth_header(username, token, domain)
        logger.info("Authentication with domain successful")
