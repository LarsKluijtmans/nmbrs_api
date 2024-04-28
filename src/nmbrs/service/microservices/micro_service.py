"""
Abstract base class for defining microservice interfaces.
"""

from abc import ABC, abstractmethod

from zeep import Client

from src.nmbrs.auth.token_manager import AuthManager


class MicroService(ABC):
    """
    Abstract base class for defining microservice interfaces.

    This class defines the common structure and methods required for interacting with microservices.

    Attributes:
        client (Client): A Zeep Client object used for communication with the microservice.
        auth_manager (AuthManager): An instance of the AuthManager class for managing authentication.
    """

    @abstractmethod
    def __init__(self, auth_manager: AuthManager, client: Client):
        self.auth_manager = auth_manager
        self.client = client
