from nmbrs.service.auth_service import AuthService
from nmbrs.service.company_service import CompanyService
from nmbrs.service.debtor_service import DebtorService
from nmbrs.service.employee_service import EmployeeService


class NmbrsSoapAPI:
    """
    A class representing the Nmbrs SOAP API.

    This class provides an interface to interact with various Nmbrs SOAP API services.
    """

    def __init__(self, sandbox: bool = True, username: str = None, token: str = None):
        """
        Constructor method for NmbrsSoapAPI class.

        Initializes NmbrsSoapAPI instance with authentication details and settings.

        :param sandbox: A boolean indicating whether to use the sandbox environment (default: True).
        :param username: A string representing the username for authentication.
        :param token: A string representing the token for authentication.
        """
        self.sandbox = sandbox

        self.auth_header: dict | None = None
        self.auth_service: AuthService = AuthService(self.sandbox)
        self.debtor_service: DebtorService | None = None
        self.company_service: CompanyService | None = None
        self.employee_service: EmployeeService | None = None

        if username and token:
            self.standard_auth(username, token)

    def standard_auth(self, username: str, token: str) -> None:
        """
        Perform standard authentication and initialize related services.

        :param username: A string representing the username for authentication.
        :param token: A string representing the token for authentication.
        """
        # Setup auth
        self.auth_header = self.auth_service.authenticate_using_standard_token(
            username, token
        )

        # Initialize other classes
        self.debtor_service: DebtorService = DebtorService(
            self.auth_header, self.sandbox
        )
        self.company_service: CompanyService = CompanyService(
            self.auth_header, self.sandbox
        )
        self.employee_service: EmployeeService = EmployeeService(
            self.auth_header, self.sandbox
        )


# Already initialized class using default stats
api = NmbrsSoapAPI()
