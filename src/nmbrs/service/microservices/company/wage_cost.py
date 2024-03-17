"""Microservice responsible for wage cost related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyWageCostService(MicroService):
    """Microservice responsible for wage cost related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:WorkCost_GetList"])
    def get(self):
        """
        Returns the work cost value for the given company and year.

        For more information, refer to the official documentation:
            [WorkCost_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WorkCost_Insert"])
    def insert(self):
        """
        Insert work cost value from financial administration in a specific period.

        For more information, refer to the official documentation:
            [WorkCost_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_Insert)
        """
        raise NotImplementedError()  # pragma: no cover
