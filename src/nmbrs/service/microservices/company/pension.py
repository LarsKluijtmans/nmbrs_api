"""Microservice responsible for pension related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyPensionService(MicroService):
    """
    Microservice responsible for pension related actions on the company level.

    Not implemented calls:
        - [PensionExport_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetList)
        - [PensionExport_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetXML)
    """

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header
