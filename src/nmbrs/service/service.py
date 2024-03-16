"""
Abstract base class for defining service interfaces.
"""

from abc import ABC, abstractmethod


class Service(ABC):
    """
    Abstract base class for defining service interfaces.
    """

    @abstractmethod
    def __init__(self, sandbox: bool = True) -> None:
        """
        Constructor method for Service.

        Initializes common attributes for service classes.

        Args:
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
        """
        self.auth_header: dict | None = None
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

    @abstractmethod
    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication header.

        Args:
            auth_header (dict): New authentication dictionary.
        """
