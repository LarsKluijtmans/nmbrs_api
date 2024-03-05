from abc import ABC, abstractmethod


class Service(ABC):
    """
    Abstract base class for defining service interfaces.
    """

    @abstractmethod
    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for Service.

        :param auth_header: Authentication dictionary.
        :param sandbox: Boolean indicating if sandbox environment is used.
        """
        self.auth_header = auth_header
        self.sandbox = sandbox

    @abstractmethod
    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication header.

        :param auth_header: New authentication dictionary.
        """
        pass  # Implementation to be provided in subclasses
