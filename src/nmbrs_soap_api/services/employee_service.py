from nmbrs_soap_api.services.service import Service
from zeep import Client

from nmbrs_soap_api.global_variables import (
    employee_uri,
    nmbrs_sandbox_base_uri,
    nmbrs_base_uri,
)


class EmployeeService(Service):
    """
    A class representing Employee Service for interacting with Nmbrs employee-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for EmployeeService class.

        Initializes EmployeeService instance with authentication and sandbox settings.

        :param auth_header: A dictionary containing authentication details.
        :param sandbox: A boolean indicating whether to use the sandbox environment.
        """
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = nmbrs_base_uri
        if sandbox:
            base_uri = nmbrs_sandbox_base_uri
        self.employee_service = Client(f"{base_uri}{employee_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header
