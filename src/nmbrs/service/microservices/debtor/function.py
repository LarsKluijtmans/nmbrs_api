"""Microservice responsible for function related actions on the debtor level."""

from zeep import Client
from zeep.helpers import serialize_object

from ....data_classes.debtor import Function
from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class DebtorFunctionService(MicroService):
    """Microservice responsible for function related actions on the debtor level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["DebtorService:Function_Delete"])
    def delete(self, debtor_id: int, function_id: int) -> None:
        """
        Delete a function of a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function to be deleted.
        """
        self.client.service.Function_Delete(DebtorId=debtor_id, id=function_id, _soapheaders=self.auth_header)

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Function_GetList"])
    def get_all(self, debtor_id: int) -> list[Function]:
        """
        Retrieve all functions of a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_GetList)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.

        Returns:
            list[Function]: A list of Function objects representing all functions of the debtor.
        """
        functions = self.client.service.Function_GetList(DebtorId=debtor_id, _soapheaders=self.auth_header)
        functions = [Function(debtor_id=debtor_id, data=function) for function in serialize_object(functions)]
        return functions

    @nmbrs_exception_handler(resources=["DebtorService:Function_Insert"])
    def insert(self, debtor_id: int, function_id: int, code: int, description: str) -> int:
        """
        Insert a new function for a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.
            code (int): The code of the function.
            description (str): The description of the function.

        Returns:
            int: The ID of the inserted function if successful.
        """
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        inserted = self.client.service.Function_Insert(**data, _soapheaders=self.auth_header)
        return inserted

    @nmbrs_exception_handler(resources=["DebtorService:Function_Update"])
    def update(self, debtor_id: int, function_id: int, code: int, description: str) -> None:
        """
        Update a function for a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Update](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Update)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.
            code (int): The code of the function.
            description (str): The description of the function.
        """
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        self.client.service.Function_Update(**data, _soapheaders=self.auth_header)
