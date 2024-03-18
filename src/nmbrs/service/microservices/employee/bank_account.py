"""Microservice responsible for bank account related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeBankAccountService(MicroService):
    """Microservice responsible for bank account related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:BankAccount_GetList"])
    def get(self):
        """
        Get all active bank accounts for given period.

        For more information, refer to the official documentation:
            [BankAccount_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:BankAccount_GetListCurrent"])
    def get_current(self):
        """
        Get all active bank accounts for the current period.

        For more information, refer to the official documentation:
            [BankAccount_GetListCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_GetListCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:BankAccount_DeleteCurrent"])
    def delete(self):
        """
        Delete given bank account.

        For more information, refer to the official documentation:
            [BankAccount_DeleteCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_DeleteCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:BankAccount_Insert"])
    def insert(self):
        """
        Insert given bank account to the given period. Unprotected mode flag is required.

        For more information, refer to the official documentation:
            [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:BankAccount_InsertCurrent"])
    def insert_current(self):
        """
        Insert given bank account to the current period.

        For more information, refer to the official documentation:
            [BankAccount_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
