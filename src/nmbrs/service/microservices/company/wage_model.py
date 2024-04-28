"""Microservice responsible for managing wage model related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.company import WageModel
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyWageModelService(MicroService):
    """Microservice responsible for managing wage model related actions on the company level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageModel_GetWageCodes")
    def get_current(self, company_id: int) -> list[WageModel]:
        """
        Retrieve the list of wage codes belonging to a company's wage model.

        For more information, refer to the official documentation:
            [WageModel_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel_GetWageCodes)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[WageModel]: A list of wage codes belonging to the company's wage model.
        """
        wage_models = self.client.service.WageModel_GetWageCodes(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        wage_models = [WageModel(company_id=company_id, data=wage_model) for wage_model in serialize_object(wage_models)]
        return wage_models

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageModel2_GetWageCodes")
    def get_current_2(self, company_id: int) -> list[WageModel]:
        """
        Retrieve the list of wage codes belonging to a company's wage model.

        For more information, refer to the official documentation:
            [WageModel2_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel2_GetWageCodes)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[WageModel]: A list of wage codes belonging to the company's wage model.
        """
        wage_models = self.client.service.WageModel2_GetWageCodes(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        wage_models = [WageModel(company_id=company_id, data=wage_model) for wage_model in serialize_object(wage_models)]
        return wage_models
