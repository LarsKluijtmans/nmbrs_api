from zeep import Client

from nmbrs.service.service import Service


class AuthService(Service):
    """
    A class responsible for handling authentication for Nmbrs services.
    """

    def __init__(self, auth: dict, auth_type: str, sandbox: bool) -> None:
        """
        Constructor method for AuthService class.

        Initializes AuthService instance with authentication details and settings.

        :param auth: A dictionary containing authentication details.
        :param auth_type: A string representing the type of authentication (e.g., "token").
        :param sandbox: A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.auth_type = auth_type
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.debtor_service = Client(f"{base_uri}{self.debtor_uri}")
        self.sso_service = Client(f"{base_uri}{self.sso_uri}")

        if auth_type == "token":
            self.auth_header = self.auth_standard_token(auth)
        else:
            self.auth_header = None

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    def auth_standard_token(self, auth: dict):
        """
        Generate authentication header for standard token-based authentication.

        :param auth: A dictionary containing authentication details.
        :return: Authentication header with domain information.
        """
        username = auth.get("Username", None)
        token = auth.get("Token", None)

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
