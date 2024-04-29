"""
A class for managing the Nmbrs authentication header.
"""

import logging

logger = logging.getLogger(__name__)


class AuthManager:
    """
    A class for managing the Nmbrs authentication header.
    """

    def __init__(self):
        self.header = None

    def set_auth_header(self, username: str, token: str, domain: str):
        """
        Sets the authentication header.

        Args:
            username (str): The username.
            token (str): The authentication token.
            domain (str): The domain.
        """
        self.header = {
            "AuthHeaderWithDomain": {
                "Username": username,
                "Token": token,
                "Domain": domain,
            }
        }
        logger.info("Authentication header set successfully.")

    def get_username(self) -> str:
        """
        Gets the username from the authentication header.

        Returns:
            str: The username or None if the authentication header is not set.
        """
        if self.header:
            return self.header["AuthHeaderWithDomain"]["Username"]
        logger.warning("Authentication header is not set.")
        return ""

    def get_token(self) -> str:
        """
        Gets the authentication token from the authentication header.

        Returns:
            str: The authentication token or None if the authentication header is not set.
        """
        if self.header:
            return self.header["AuthHeaderWithDomain"]["Token"]
        logger.warning("Authentication header is not set.")
        return ""

    def get_domain(self) -> str:
        """
        Gets the domain from the authentication header.

        Returns:
            str: The domain or None if the authentication header is not set.
        """
        if self.header:
            return self.header["AuthHeaderWithDomain"]["Domain"]
        logger.warning("Authentication header is not set.")
        return ""
