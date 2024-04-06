"""Microservice responsible for pension related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import Pension, PensionXML
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyPensionService(MicroService):
    """Microservice responsible for pension related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:PensionExport_GetList"])
    def get(self, company_id: int) -> list[Pension]:
        """
        Returns pension exports that belong to a company for a certain year.

        For more information, refer to the official documentation:
            [PensionExport_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetList)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Pension]: A list of pension objects.
        """
        pensions = self.client.service.PensionExport_GetList(CompanyId=company_id, _soapheaders=self.auth_header)
        return [Pension(company_id=company_id, data=pension) for pension in serialize_object(pensions)]

    @nmbrs_exception_handler(resources=["CompanyService:PensionExport_GetXML"])
    def get_xml(self, company_id: int, pension_export_id: int) -> PensionXML:
        """
        Returns one XML pension export by ID that belong to a company.

        For more information, refer to the official documentation:
            [PensionExport_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetXML)

        Args:
            company_id (int): The ID of the company.
            pension_export_id (int): Unique id of a pension export.

        Returns:
            list[CostCenter]: A list of cost center objects.
        """
        pension_xml = self.client.service.PensionExport_GetXML(
            CompanyId=company_id, PensionExportID=pension_export_id, _soapheaders=self.auth_header
        )
        return PensionXML(serialize_object(pension_xml))
