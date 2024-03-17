"""Microservice responsible for cost unit related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyCostUnitService(MicroService):
    """Microservice responsible for cost unit related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:CostUnit_GetList"])
    def get(self):
        """
        Get cost units that belong to a company

        For more information, refer to the official documentation:
            [CostUnit_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:CostUnit_Insert"])
    def insert(self):
        """
        Update or insert a Cost Unit into a company.

        For more information, refer to the official documentation:
            [CostUnit_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_Insert)
        """
        raise NotImplementedError()  # pragma: no cover
