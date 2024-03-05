from nmbrs.service.auth_service import AuthService
from nmbrs.service.company_service import CompanyService
from nmbrs.service.debtor_service import DebtorService
from nmbrs.service.employee_service import EmployeeService


class NmbrsSoapAPI:
    """
    A class representing the Nmbrs SOAP API.

    This class provides an interface to interact with various Nmbrs SOAP API services.
    """

    def __init__(self, auth: dict, auth_type: str = "token", sandbox: bool = True):
        """
        Constructor method for NmbrsSoapAPI class.

        Initializes NmbrsSoapAPI instance with authentication details and settings.

        :param auth: A dictionary containing authentication details.
        :param auth_type: A string representing the type of authentication (default: "token").
        :param sandbox: A boolean indicating whether to use the sandbox environment (default: True).
        """
        self.sandbox = sandbox
        self.auth_type = auth_type

        # Setup auth
        self.auth_service: AuthService = AuthService(auth, auth_type, sandbox)
        self.auth_header = self.auth_service.auth_header

        # Initialize other classes
        self.debtor_service: DebtorService = DebtorService(
            self.auth_service.auth_header, sandbox
        )
        self.company_service: CompanyService = CompanyService(
            self.auth_service.auth_header, sandbox
        )
        self.employee_service: EmployeeService = EmployeeService(
            self.auth_service.auth_header, sandbox
        )
