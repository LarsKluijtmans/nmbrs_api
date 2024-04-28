"""Microservice responsible for bank account related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import BankAccount
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeBankAccountService(MicroService):
    """Microservice responsible for bank account related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:BankAccount_GetList")
    def get(self, employee_id: int, period: int, year: int) -> list[BankAccount]:
        """
        Get all active bank accounts for given period.

        For more information, refer to the official documentation:
            [BankAccount_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_GetList)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            list[BankAccount]: A list of BankAccount objects representing the bank accounts.
        """
        bank_accounts = self.client.service.BankAccount_GetList(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return [BankAccount(employee_id=employee_id, data=bank_account) for bank_account in serialize_object(bank_accounts)]

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:BankAccount_GetListCurrent")
    def get_current(self, employee_id: int) -> list[BankAccount]:
        """
        Get all active bank accounts for the current period.

        For more information, refer to the official documentation:
            [BankAccount_GetListCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_GetListCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[BankAccount]: A list of BankAccount objects representing the bank accounts.
        """
        bank_accounts = self.client.service.BankAccount_GetListCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return [BankAccount(employee_id=employee_id, data=bank_account) for bank_account in serialize_object(bank_accounts)]

    @nmbrs_exception_handler(resource="EmployeeService:BankAccount_DeleteCurrent")
    def delete(self, employee_id: int, bank_account_id: int) -> str:
        """
        Delete given bank account.

        For more information, refer to the official documentation:
            [BankAccount_DeleteCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_DeleteCurrent)

        Args:
            employee_id (int): The ID of the employee.
            bank_account_id (int): The ID of the bank account.

        Returns:
            str: A str indicating the success of the operation.
        """
        response = self.client.service.BankAccount_DeleteCurrent(
            EmployeeId=employee_id, BankAccountID=bank_account_id, _soapheaders=self.auth_manager.header
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:BankAccount_Insert")
    def post(self, employee_id: int, bank_account: BankAccount, period: int, year: int, unprotected_mode: bool) -> int:
        """
        Insert given bank account to the given period. Unprotected mode flag is required.

        For more information, refer to the official documentation:
            [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_Insert)

        Args:
            employee_id (int): The ID of the employee.
            bank_account (BankAccount): The BankAccount object to insert.
            period (int): The period.
            year (int): The year.
            unprotected_mode (bool): Flag indicating whether unprotected mode is enabled.

        Returns:
            int: The response indicating the success of the operation.
        """
        _bank_account = {
            "Id": bank_account.id,
            "Number": bank_account.number,
            "Description": bank_account.description,
            "IBAN": bank_account.iban,
            "BIC": bank_account.bic,
            "City": bank_account.city,
            "Name": bank_account.name,
            "Type": bank_account.type,
        }
        response = self.client.service.BankAccount_Insert(
            EmployeeId=employee_id,
            BankAccount=_bank_account,
            Period=period,
            Year=year,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:BankAccount_InsertCurrent")
    def post_current(self, employee_id: int, bank_account: BankAccount) -> int:
        """
        Insert given bank account to the current period.

        For more information, refer to the official documentation:
            [BankAccount_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=BankAccount_InsertCurrent)

        Args:
            employee_id (int): The ID of the employee.
            bank_account (BankAccount): The BankAccount object to insert.

        Returns:
            int: The response indicating the success of the operation.
        """
        _bank_account = {
            "Id": bank_account.id,
            "Number": bank_account.number,
            "Description": bank_account.description,
            "IBAN": bank_account.iban,
            "BIC": bank_account.bic,
            "City": bank_account.city,
            "Name": bank_account.name,
            "Type": bank_account.type,
        }
        response = self.client.service.BankAccount_InsertCurrent(
            EmployeeId=employee_id,
            BankAccount=_bank_account,
            _soapheaders=self.auth_manager.header,
        )
        return response
