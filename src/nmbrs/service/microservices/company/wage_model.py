"""Microservice responsible for wage model related actions on the company level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyWageModelService(MicroService):
    """Microservice responsible for wage model related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:WageModel_GetWageCodes"])
    def get(self):
        """
        Returns wage codes that belong to a company's wage model.

        For more information, refer to the official documentation:
            [WageModel_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel_GetWageCodes)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageModel2_GetWageCodes"])
    def get_2(self):
        """
        Returns wage codes that belong to a company's wage model.

        For more information, refer to the official documentation:
            [WageModel2_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel2_GetWageCodes)
        """
        raise NotImplementedError()  # pragma: no cover
