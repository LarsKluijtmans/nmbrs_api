"""Microservice responsible for title related actions on the debtor level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class DebtorTitleService(MicroService):
    """Microservice responsible for title related actions on the debtor level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Title_GetList"])
    def get_all(self, debtor_id: int) -> list[str]:
        """
        Retrieve all titles for a debtor.

        For more information, refer to the official documentation:
            [Soap call Title_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Title_GetList)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[str]: A list of strings representing all titles associated with the debtor.
        """
        titles = self.client.service.Title_GetList(DebtorId=debtor_id, _soapheaders=self.auth_header)
        titles = [title["TitleName"] for title in serialize_object(titles)]
        return titles

    @nmbrs_exception_handler(resources=["DebtorService:Title_Insert"])
    def insert(self, debtor_id: int, title: str) -> None:
        """
        Insert a title for a debtor.

        For more information, refer to the official documentation:
            [Soap call Title_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Title_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            title (str): The title to be inserted.
        """
        data = {"DebtorId": debtor_id, "title": {"TitleName": title}}
        self.client.service.Title_Insert(**data, _soapheaders=self.auth_header)
