"""Microservice responsible for department related actions on the debtor level."""

from zeep import Client
from zeep.helpers import serialize_object

from ....auth.token_manager import AuthManager
from ....data_classes.debtor import Department
from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class DebtorDepartmentService(MicroService):
    """Microservice responsible for department related actions on the debtor level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="DebtorService:Department_Delete")
    def delete(self, debtor_id: int, department_id: int) -> None:
        """
        Delete a department of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department to delete.
        """
        self.client.service.Department_Delete(DebtorId=debtor_id, id=department_id, _soapheaders=self.auth_manager.header)

    @return_list
    @nmbrs_exception_handler(resource="DebtorService:Department_GetList")
    def get_all(self, debtor_id: int) -> list[Department]:
        """
        Retrieve all departments of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_GetList)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[Department]: A list of Department objects representing all departments of the debtor.
        """
        departments = self.client.service.Department_GetList(DebtorId=debtor_id, _soapheaders=self.auth_manager.header)
        departments = [Department(debtor_id=debtor_id, data=department) for department in serialize_object(departments)]
        return departments

    @nmbrs_exception_handler(resource="DebtorService:Department_Insert")
    def post(self, debtor_id: int, department_id: int, code: int, description: str) -> int:
        """
        Insert a new department for a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department.
            code (int): The code of the department.
            description (str): The description of the department.

        Returns:
            int: The ID of the inserted department if successful.
        """
        data = {
            "DebtorId": debtor_id,
            "department": {
                "Id": department_id,
                "Code": code,
                "Description": description,
            },
        }
        inserted = self.client.service.Department_Insert(**data, _soapheaders=self.auth_manager.header)
        return inserted

    @nmbrs_exception_handler(resource="DebtorService:Department_Update")
    def update(self, debtor_id: int, department_id: int, code: int, description: str) -> None:
        """
        Update an existing department of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Update](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Update)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department.
            code (int): The code of the department.
            description (str): The description of the department.
        """
        data = {
            "DebtorId": debtor_id,
            "department": {
                "Id": department_id,
                "Code": code,
                "Description": description,
            },
        }
        self.client.service.Department_Update(**data, _soapheaders=self.auth_manager.header)
