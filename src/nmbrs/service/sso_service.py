"""
Module for handling Single Sign-On for Nmbrs services.
"""

from zeep import Client

from .service import Service
from ..utils.nmbrs_exception_handler import (
    nmbrs_exception_handler,
    nmbrs_sso_exception_handler,
)


class SingleSingOnService(Service):
    """
    A class responsible for handling Single Sign-On for Nmbrs services.
    """

    def __init__(self, sandbox: bool = True) -> None:
        super().__init__(sandbox)

        # Initialize nmbrs services
        self.sso_service = Client(f"{self.base_uri}{self.sso_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """Function inherited from higher level, but in this case not used."""

    def get_sso_url(self, token: str, nmbrs_env: str, target: str = "nmbrs") -> str:
        """
        Generate the Single Sign-On URL.

        Args:
            token (str): A string representing the authentication token.
            nmbrs_env (str): A string representing the Nmbrs environment subdomain.
            target (str (optional)): A string representing the target application. (default: nmbrs)

        Returns:
            str: The generated Single Sign-On URL.
        """
        if self.sso_url not in nmbrs_env:
            nmbrs_env = f"{nmbrs_env}{self.sso_url}"

        return f"https://{nmbrs_env}/applications/common/externalactions.aspx?login={target}&ID={token}"

    @nmbrs_exception_handler(resources=["SingleSignOn:GetToken"])
    @nmbrs_sso_exception_handler(resources=["SingleSignOn:GetToken"])
    def sso_auth_with_password(self, username: str, password: str) -> str:
        """
        Perform Single Sign-On authentication using username and password.

        Args:
            username (str): A string representing the username for authentication.
            password (str): A string representing the password for authentication.

        Returns:
            str: Single sign-on token, valid for 30 seconds
        """
        token = self.sso_service.service.GetToken(Username=username, Password=password)
        return token

    @nmbrs_exception_handler(resources=["SingleSignOn:GetToken2"])
    @nmbrs_sso_exception_handler(resources=["SingleSignOn:GetToken2"])
    def sso_auth_with_token(self, username: str, token: str) -> str:
        """
        Perform Single Sign-On authentication using username and token.

        Args:
            username (str): A string representing the username for authentication.
            token (str): A string representing the token for authentication.

        Returns:
            str: Single sign-on token, valid for 30 seconds
        """
        token = self.sso_service.service.GetToken2(Username=username, Token=token)
        return token

    @nmbrs_exception_handler(resources=["SingleSignOn:GetTokenWithDomain"])
    @nmbrs_sso_exception_handler(resources=["SingleSignOn:GetTokenWithDomain"])
    def sso_auth_with_domain(self, username: str, password: str, domain: str) -> str:
        """
        Perform Single Sign-On authentication using username, password, and domain.

        Args:
            username (str): A string representing the username for authentication.
            password (str): A string representing the password for authentication.
            domain (str): A string representing the Nmbrs environment subdomain.

        Returns:
            str: Single sign-on token, valid for 30 seconds
        """
        token = self.sso_service.service.GetTokenWithDomain(Username=username, Password=password, Domain=domain)
        return token
