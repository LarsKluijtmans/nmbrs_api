"""Microservice responsible for hour model related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyHourModelService(MicroService):
    """
    Microservice responsible for hour model related actions on the company level.

    Not implemented calls:
        - [HourModel2_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel2_GetHourCodes)
        - [HourModel_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel_GetHourCodes)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanyHourModelService.

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
