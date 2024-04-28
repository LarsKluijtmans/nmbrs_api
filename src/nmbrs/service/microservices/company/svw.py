"""Microservice responsible for svw related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.company import SVW
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanySvwService(MicroService):
    """Microservice responsible for svw related actions on the company level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="CompanyService:SVW_GetCurrent")
    def get_current(self, company_id: int) -> SVW:
        """
        Get the current SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            SVW: object representing svw settings
        """
        svw = self.client.service.SVW_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        return SVW(company_id=company_id, data=serialize_object(svw))

    @nmbrs_exception_handler(resource="CompanyService:SVW_UpdateCurrent")
    def post_current(self, company_id: int, svw: SVW) -> None:
        """
        Update the current SVW settings.

        For more information, refer to the official documentation:
            [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_UpdateCurrent)

        Args:
            company_id (int): The ID of the company.
            svw (SWV): Object containing svw data.

        Returns:
            SVW: object representing svw settings
        """
        self.client.service.SVW_UpdateCurrent(CompanyId=company_id, SVW=svw.insert_dict(), _soapheaders=self.auth_manager.header)
