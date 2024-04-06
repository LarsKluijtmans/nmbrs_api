"""Microservice responsible for salary table related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import SalaryTable, SalaryTableScale, SalaryTableStep
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanySalaryTableService(MicroService):
    """Microservice responsible for salary table related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_Get"])
    def get(self, company_id: int, period: int, year: int) -> list[SalaryTable]:
        """
        Returns a list of available tables for the company.

        For more information, refer to the official documentation:
            [SalaryTable_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_Get)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.

        Returns:
            list[SalaryTable]: A list of salary table objects.
        """
        salary_tables = self.client.service.SalaryTable_Get(CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header)
        return [SalaryTable(company_id=company_id, data=salary_table) for salary_table in serialize_object(salary_tables)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_Get"])
    def get_2(self, company_id: int, period: int, year: int) -> list[str]:
        """
        Returns a list of available tables for the company with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_Get)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.

        Returns:
            list[str]: A list of salary table guids.
        """
        salary_tables = self.client.service.SalaryTable2_Get(CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header)
        return [salary_table.get("GuidSalaryTable") for salary_table in serialize_object(salary_tables)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_GetScales"])
    def get_scale(self, company_id: int, period: int, year: int) -> list[SalaryTableScale]:
        """
        Returns a list of available scales for the company salary table.

        For more information, refer to the official documentation:
            [SalaryTable_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetScales)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.

        Returns:
            list[SalaryTableScale]: A list of salary table scale objects.
        """
        scales = self.client.service.SalaryTable_GetScales(CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header)
        return [SalaryTableScale(company_id=company_id, data=scale) for scale in serialize_object(scales)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_GetScales"])
    def get_scale_2(self, company_id: int, period: int, year: int) -> list[str]:
        """
        Returns a list of available scales for the company salary table with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetScales)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.

        Returns:
            list[str]: A list of salary table scale guids.
        """
        salary_tables = self.client.service.SalaryTable2_GetScales(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header
        )
        return [salary_table.get("GuidSalaryTableScale") for salary_table in serialize_object(salary_tables)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable_GetSteps"])
    def get_step(self, company_id: int, period: int, year: int, scale: SalaryTableScale) -> list[SalaryTableStep]:
        """
        Returns a list of available steps for the company salary table and selected scale.

        For more information, refer to the official documentation:
            [SalaryTable_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetSteps)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.
            scale (SalaryTableScale): selected scale to get the steps for.

        Returns:
            list[SalaryTableScale]: A list of salary table scale objects.
        """
        _scale = {
            "Scale": scale.scale,
            "SchaalDescription": scale.description,
            "ScaleValue": scale.value,
            "ScalePercentageMax": scale.percentage_max,
            "ScalePercentageMin": scale.percentage_min,
        }
        steps = self.client.service.SalaryTable_GetSteps(
            CompanyId=company_id, Period=period, Year=year, Scale=_scale, _soapheaders=self.auth_header
        )
        return [SalaryTableStep(company_id=company_id, data=step) for step in serialize_object(steps)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:SalaryTable2_GetSteps"])
    def get_step_2(self, company_id: int, period: int, year: int) -> list[str]:
        """
        Returns a list of available steps for the company salary table and selected scale with unique identifiers.

        For more information, refer to the official documentation:
            [SalaryTable2_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetSteps)

        Args:
            company_id (int): The ID of the company.
            period (int): Period.
            year (int): Year.

        Returns:
            list[str]: A list of salary table step guids.
        """
        salary_tables = self.client.service.SalaryTable2_GetSteps(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header
        )
        return [salary_table.get("GuidSalaryTableStep") for salary_table in serialize_object(salary_tables)]
