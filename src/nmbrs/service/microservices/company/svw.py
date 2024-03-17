"""Microservice responsible for svw related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanySvwService(MicroService):
    """Microservice responsible for svw related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:SVW_GetCurrent"])
    def get_current(self):
        """
        Get the current SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SVW_UpdateCurrent"])
    def insert_current(self):
        """
        Update the current SVW settings.

        For more information, refer to the official documentation:
            [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
