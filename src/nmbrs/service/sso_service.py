"""
Module for handling Single Sign-On (SSO) for Nmbrs services.
"""

from zeep import Client

from .service import Service
from ..auth.token_manager import AuthManager
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler


class SingleSingOnService(Service):
    """
    A class responsible for managing Single Sign-On (SSO) for Nmbrs services.
    """

    def __init__(self, auth_manager: AuthManager, sandbox: bool = True):
        super().__init__(auth_manager, sandbox)

        # Initialize nmbrs services
        self.sso_service = Client(f"{self.base_uri}{self.sso_uri}")

    def get_sso_url(self, token: str, nmbrs_env: str, target: str = "nmbrs") -> str:
        """
        Generate the Single Sign-On (SSO) URL.

        Args:
            token (str): The authentication token.
            nmbrs_env (str): The Nmbrs environment subdomain.
            target (str, (optional)): The target application. Defaults to "nmbrs".

        Returns:
            str: The generated Single Sign-On URL.
        """
        if self.sso_url not in nmbrs_env:
            nmbrs_env = f"{nmbrs_env}{self.sso_url}"
        return f"https://{nmbrs_env}/applications/common/externalactions.aspx?login={target}&ID={token}"

    @nmbrs_exception_handler(resource="SingleSignOn:GetToken")
    def get_token_with_password(self, username: str, password: str) -> str:
        """
        Get token for user. Valid for 30 seconds

        For more information, refer to the official documentation:
            [GetToken](https://api.nmbrs.nl/soap/v3/SingleSignOn.asmx?op=GetToken)

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.

        Returns:
            str: Single sign-on token (valid for 30 seconds).
        """
        token = self.sso_service.service.GetToken(Username=username, Password=password)
        return token

    @nmbrs_exception_handler(resource="SingleSignOn:GetToken2")
    def get_token_with_api_token(self, username: str, token: str) -> str:
        """
        Get token for user, by API token. Valid for 30 seconds

        For more information, refer to the official documentation:
            [GetToken2](https://api.nmbrs.nl/soap/v3/SingleSignOn.asmx?op=GetToken2)

        Args:
            username (str): The username for authentication.
            token (str): The token for authentication.

        Returns:
            str: Single sign-on token (valid for 30 seconds).
        """
        token = self.sso_service.service.GetToken2(Username=username, Token=token)
        return token

    @nmbrs_exception_handler(resource="SingleSignOn:GetTokenWithDomain")
    def get_token_with_domain(self, username: str, password: str, domain: str) -> str:
        """
        Get token for user of an environment. Valid for 30 seconds.

        For more information, refer to the official documentation:
            [GetTokenWithDomain](https://api.nmbrs.nl/soap/v3/SingleSignOn.asmx?op=GetTokenWithDomain)

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.
            domain (str): The Nmbrs environment subdomain.

        Returns:
            str: Single sign-on token (valid for 30 seconds).
        """
        token = self.sso_service.service.GetTokenWithDomain(Username=username, Password=password, Domain=domain)
        return token
