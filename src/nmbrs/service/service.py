"""Abstract base class for defining service interfaces."""

from abc import ABC, abstractmethod
from src.nmbrs.auth.token_manager import AuthManager


class Service(ABC):
    """
    Abstract base class for defining service interfaces.

    This class serves as an abstract base class for defining interfaces for Nmbrs SOAP API services.
    It provides common attributes and methods used by various service classes.

    Attributes:
        auth_manager (AuthManager): An instance of the AuthManager class for managing authentication.
        sandbox (bool): A boolean indicating whether to use the sandbox environment (default: True).
        nmbrs_base_uri (str): Base URI for the Nmbrs SOAP API.
        nmbrs_sandbox_base_uri (str): Base URI for the Nmbrs sandbox environment.
        sso_url (str): URL suffix for Single Sign-On (SSO) service.
        base_uri (str): Base URI determined by the environment (sandbox or production).
        sso_uri (str): URI for the Single Sign-On (SSO) service WSDL.
        employee_uri (str): URI for the EmployeeService WSDL.
        company_uri (str): URI for the CompanyService WSDL.
        debtor_uri (str): URI for the DebtorService WSDL.
        report_uri (str): URI for the ReportService WSDL.
    """

    @abstractmethod
    def __init__(self, auth_manager: AuthManager, sandbox: bool = True):
        self.auth_manager = auth_manager
        self.sandbox = sandbox

        self.nmbrs_base_uri = "https://api.nmbrs.nl/soap/v3/"
        self.nmbrs_sandbox_base_uri = "https://api-sandbox.nmbrs.nl/soap/v3/"

        self.sso_url = ".nmbrs.nl"
        self.base_uri = self.nmbrs_base_uri
        if self.sandbox:
            self.sso_url = ".nmbrs-sandbox.nl"
            self.base_uri = self.nmbrs_sandbox_base_uri

        self.sso_uri = "SingleSignOn.asmx?WSDL"
        self.employee_uri = "EmployeeService.asmx?WSDL"
        self.company_uri = "CompanyService.asmx?WSDL"
        self.debtor_uri = "DebtorService.asmx?WSDL"
        self.report_uri = "ReportService.asmx?WSDL"
