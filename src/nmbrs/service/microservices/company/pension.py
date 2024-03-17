"""Microservice responsible for pension related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyPensionService(MicroService):
    """Microservice responsible for pension related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:PensionExport_GetList"])
    def get(self):
        """
        Returns pension exports that belong to a company for a certain year.

        For more information, refer to the official documentation:
            [PensionExport_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:PensionExport_GetXML"])
    def get_xml(self):
        """
        Returns one XML pension export by ID that belong to a company.

        For more information, refer to the official documentation:
            [PensionExport_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetXML)
        """
        raise NotImplementedError()  # pragma: no cover
