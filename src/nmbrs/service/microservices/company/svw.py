"""Microservice responsible for svw related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanySVWService(MicroService):
    """
    Microservice responsible for svw related actions on the company level.

    Not implemented calls:
        - [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_GetCurrent)
        - [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_UpdateCurrent)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanySVWService.

        Args:
            client (Client): A Zeep Client object representing the connection to the Nmbrs API.
        """
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Set the authentication header for requests to the Nmbrs API.

        Args:
            auth_header (dict): The authentication header to be set.
        """
        self.auth_header = auth_header
