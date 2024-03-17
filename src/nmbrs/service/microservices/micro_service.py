"""
Abstract base class for defining microservice interfaces.
"""

from abc import ABC, abstractmethod

from zeep import Client


class MicroService(ABC):
    """
    Abstract base class for defining microservice interfaces.

    This class defines the common structure and methods required for interacting with microservices.

    Attributes:
        client (Client): A Zeep Client object used for communication with the microservice.
        auth_header (dict | None): The authentication header used by Nmbrs.
    """

    @abstractmethod
    def __init__(self, client: Client) -> None:
        self.client = client
        self.auth_header: dict | None = None

    @abstractmethod
    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication header for requests to the microservice.

        Args:
            auth_header (dict): New authentication header to be set.
        """
