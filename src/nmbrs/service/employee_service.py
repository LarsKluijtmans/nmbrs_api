"""
Module for handling the Employee Nmbrs services.
"""
from zeep import Client
from .service import Service


class EmployeeService(Service):
    """
    A class representing Employee Service for interacting with Nmbrs employee-related functionalities.
    """

    def __init__(self, sandbox: bool = True) -> None:
        """
        Constructor method for EmployeeService class.

        Args:
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
        """
        super().__init__(sandbox)
        self.auth_header: dict | None = None

        # Initialize nmbrs services
        self.employee_service = Client(f"{self.base_uri}{self.employee_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header
