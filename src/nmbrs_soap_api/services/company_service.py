from nmbrs_soap_api.services.service import Service
from zeep import Client

from nmbrs_soap_api.global_variables import (
    company_uri,
    nmbrs_sandbox_base_uri,
    nmbrs_base_uri,
)


class CompanyService(Service):
    """
    A class representing Company Service for interacting with Nmbrs company-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for CompanyService class.

        Initializes CompanyService instance with authentication and sandbox settings.

        :param auth_header: A dictionary containing authentication details.
        :param sandbox: A boolean indicating whether to use the sandbox environment.
        """
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = nmbrs_base_uri
        if sandbox:
            base_uri = nmbrs_sandbox_base_uri
        self.company_service = Client(f"{base_uri}{company_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header
