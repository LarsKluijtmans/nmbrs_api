"""Microservice responsible for salary table related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanySalaryTableService(MicroService):
    """Microservice responsible for salary table related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_Get"])
    def get(self):
        """
        Returns a list of available tables for the company.

        For more information, refer to the official documentation:
            [SalaryTable_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_Get"])
    def get_2(self):
        """
        Returns a list of available tables for the company with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_GetScales"])
    def get_scale(self):
        """
        Returns a list of available scales for the company salary table.

        For more information, refer to the official documentation:
            [SalaryTable_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetScales)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_GetScales"])
    def get_scale_2(self):
        """
        Returns a list of available scales for the company salary table with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetScales)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_GetSteps"])
    def get_step(self):
        """
        Returns a list of available steps for the company salary table and selected scale.

        For more information, refer to the official documentation:
            [SalaryTable_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetSteps)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_GetSteps"])
    def get_step_2(self):
        """
        Returns a list of available steps for the company salary table and selected scale with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetSteps)
        """
        raise NotImplementedError()  # pragma: no cover
