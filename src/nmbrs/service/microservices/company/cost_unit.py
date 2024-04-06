"""Microservice responsible for cost unit related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import CostUnit
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyCostUnitService(MicroService):
    """Microservice responsible for cost unit related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:CostUnit_GetList"])
    def get(self, company_id: int) -> list[CostUnit]:
        """
        Get cost units that belong to a company

        For more information, refer to the official documentation:
            [CostUnit_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_GetList)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[CostUnit]: A list of cost unit objects.
        """
        cost_units = self.client.service.CostUnit_GetList(CompanyId=company_id, _soapheaders=self.auth_header)
        return [CostUnit(company_id=company_id, data=cost_unit) for cost_unit in serialize_object(cost_units)]

    @nmbrs_exception_handler(resources=["CompanyService:CostUnit_Insert"])
    def insert(self, company_id: int, cost_unit_id: int, code: str, description: str) -> int:
        """
        Update or insert a Cost Unit into a company.

        For more information, refer to the official documentation:
            [CostUnit_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_Insert)

        Args:
            company_id (int): The ID of the company.
            cost_unit_id (int): The ID of the cost unit.
            code (str): The code of the cost unit.
            description (str): The description of the cost unit.

        Returns:
            int: The ID of the inserted or updated cost unit.
        """
        cost_unit = {"Id": cost_unit_id, "Code": code, "Description": description}
        cost_unit_id = self.client.service.CostUnit_Insert(CompanyId=company_id, costunit=cost_unit, _soapheaders=self.auth_header)
        return cost_unit_id
