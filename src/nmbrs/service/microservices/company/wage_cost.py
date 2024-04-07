"""Microservice responsible for managing wage cost related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import WageCost
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyWageCostService(MicroService):
    """Microservice responsible for managing wage cost related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WorkCost_GetList"])
    def get(self, company_id: int, year: int) -> list[WageCost]:
        """
        Retrieve the list of work cost values for a given company and year.

        For more information, refer to the official documentation:
            [WorkCost_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_GetList)

        Args:
            company_id (int): The ID of the company.
            year (int): The year.

        Returns:
            list[WageCost]: A list of work cost values.
        """
        wage_costs = self.client.service.WorkCost_GetList(CompanyId=company_id, Year=year, _soapheaders=self.auth_header)
        wage_costs = [WageCost(company_id=company_id, data=wage_cost) for wage_cost in serialize_object(wage_costs)]
        return wage_costs

    @nmbrs_exception_handler(resources=["CompanyService:WorkCost_Insert"])
    def insert(self, company_id: int, value: float, period: int, year: int):
        """
        Insert a work cost value from the financial administration for a specific period.

        For more information, refer to the official documentation:
            [WorkCost_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_Insert)

        Args:
            company_id (int): The ID of the company.
            value (float): The value of the wage cost.
            period (int): The period.
            year (int): The year.

        Returns:
            int: The response indicating the success of the operation.
        """
        response = self.client.service.WorkCost_Insert(
            CompanyId=company_id,
            Value=value,
            Period=period,
            Year=year,
            _soapheaders=self.auth_header,
        )
        return response
