"""Microservice responsible for wage cost related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyWageCostService(MicroService):
    """
    Microservice responsible for wage cost related actions on the company level.

    Not implemented calls:
        - [WorkCost_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_GetList)
        - [WorkCost_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_Insert)
    """

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header
