from zeep import Client
from nmbrs.service.service import Service
from nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class AuthService(Service):
    """
    A class responsible for handling authentication for Nmbrs services.
    """

    def __init__(self, sandbox: bool) -> None:
        """
        Constructor method for AuthService class.

        Initializes AuthService instance with authentication details and settings.

        Args:
            sandbox (bool): A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.sandbox = sandbox
        self.auth_header: dict | None = None

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.debtor_service = Client(f"{base_uri}{self.debtor_uri}")
        self.sso_service = Client(f"{base_uri}{self.sso_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication header.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler(["DebtorService:Environment_Get"])
    def authenticate_using_standard_token(self, username: str, token: str) -> dict:
        """
        Generate authentication header for standard token-based authentication.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Environment_Get)

        Args:
            username (str): A string representing the username for authentication.
            token (str): A string representing the token for authentication.

        Returns:
            dict: Authentication header with domain information.
        """
        env = self.debtor_service.service.Environment_Get(
            _soapheaders={"AuthHeader": {"Username": username, "Token": token}}
        )
        return {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": env.SubDomain,
            }
        }
