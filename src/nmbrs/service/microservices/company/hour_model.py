"""Microservice responsible for hour model related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyHourModelService(MicroService):
    """Microservice responsible for hour model related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:HourModel_GetHourCodes"])
    def get(self):
        """
        Get hour codes that belong to a company's hour model.

        For more information, refer to the official documentation:
            [HourModel_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel_GetHourCodes)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:HourModel2_GetHourCodes"])
    def get_2(self):
        """
        Get hour codes that belong to a company's hour model 2.

        For more information, refer to the official documentation:
            [HourModel2_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel2_GetHourCodes)
        """
        raise NotImplementedError()  # pragma: no cover
