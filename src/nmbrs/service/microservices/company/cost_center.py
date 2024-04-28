"""Microservice responsible for managing cost centers at the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.company import CostCenter
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyCostCenterService(MicroService):
    """Microservice responsible for managing cost centers at the company level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:CostCenter_GetList")
    def get_current(self, company_id: int) -> list[CostCenter]:
        """
        Retrieve cost centers associated with a company.

        For further details, see the official documentation:
            [CostCenter_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostCenter_GetList)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[CostCenter]: A list of cost center objects.
        """
        cost_centers = self.client.service.CostCenter_GetList(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        return [CostCenter(company_id=company_id, data=cost_center) for cost_center in serialize_object(cost_centers)]

    @nmbrs_exception_handler(resource="CompanyService:CostCenter_Insert")
    def post(self, company_id: int, cost_center_id: int, code: str, description: str) -> int:
        """
        Insert or update a cost center within a company.

        For further details, see the official documentation:
            [CostCenter_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostCenter_Insert)

        Args:
            company_id (int): The ID of the company.
            cost_center_id (int): The ID of the cost center.
            code (str): The code of the cost center.
            description (str): The description of the cost center.

        Returns:
            int: The ID of the inserted or updated cost center.
        """
        cost_center = {"Id": cost_center_id, "Code": code, "Description": description}
        cost_center_id = self.client.service.CostCenter_Insert(
            CompanyId=company_id, kostenplaats=cost_center, _soapheaders=self.auth_manager.header
        )
        return cost_center_id
