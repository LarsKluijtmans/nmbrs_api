"""Main class provided by the package."""

import logging
import time
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

        # Initialize service attributes to None
        self._debtor_service = None
        self._company_service = None
        self._employee_service = None
        self._report_service = None

        # Handle auth
        if auth_type == "token":
            self.auth_with_token(username, token)
        elif auth_type == "domain":
            self.auth_with_domain(username, token, domain)

    @property
    def debtor(self):
        """
        Lazily initializes and returns the DebtorService instance.
        """
        if self._debtor_service is None:
            start_time = time.time()
            self._debtor_service = DebtorService(self.auth_manager, self.sandbox)
            end_time = time.time()
            logger.debug("DebtorService initialization time: %s seconds", end_time - start_time)
        return self._debtor_service

    @property
    def company(self):
        """
        Lazily initializes and returns the CompanyService instance.
        """
        if self._company_service is None:
            start_time = time.time()
            self._company_service = CompanyService(self.auth_manager, self.sandbox)
            end_time = time.time()
            logger.debug("CompanyService initialization time: %s seconds", end_time - start_time)
        return self._company_service

    @property
    def employee(self):
        """
        Lazily initializes and returns the EmployeeService instance.
        """
        if self._employee_service is None:
            start_time = time.time()
            self._employee_service = EmployeeService(self.auth_manager, self.sandbox)
            end_time = time.time()
            logger.debug("EmployeeService initialization time: %s seconds", end_time - start_time)
        return self._employee_service

    @property
    def report(self):
        """
        Lazily initializes and returns the ReportService instance.
        """
        if self._report_service is None:
            start_time = time.time()
            self._report_service = ReportService(self.auth_manager, self.sandbox)
            end_time = time.time()
            logger.debug("ReportService initialization time: %s seconds", end_time - start_time)
        return self._report_service

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
