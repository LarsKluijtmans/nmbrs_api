from zeep import Client
from nmbrs.service.service import Service


class EmployeeService(Service):
    """
    A class representing Employee Service for interacting with Nmbrs employee-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for EmployeeService class.

        Initializes EmployeeService instance with authentication and sandbox settings.

        Args:
            auth_header (dict): A dictionary containing authentication details.
            sandbox (bool): A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.employee_service = Client(f"{base_uri}{self.employee_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header
