from abc import ABC, abstractmethod


class Service(ABC):
    """
    Abstract base class for defining service interfaces.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Constructor method for Service.

        :param auth_header: Authentication dictionary.
        :param sandbox: Boolean indicating if sandbox environment is used.
        """
        self.nmbrs_base_uri = "https://api.nmbrs.nl/soap/v3/"
        self.nmbrs_sandbox_base_uri = "https://api-sandbox.nmbrs.nl/soap/v3/"

        self.sso_uri = "SingleSignOn.asmx?WSDL"
        self.employee_uri = "EmployeeService.asmx?WSDL"
        self.company_uri = "CompanyService.asmx?WSDL"
        self.debtor_uri = "DebtorService.asmx?WSDL"
        self.report_uri = "ReportService.asmx?WSDL"

    @abstractmethod
    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication header.

        :param auth_header: New authentication dictionary.
        """
        pass  # Implementation to be provided in subclasses
