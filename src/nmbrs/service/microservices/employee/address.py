# pylint: disable=line-too-long
"""Microservice responsible for address related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeAddressService(MicroService):
    """Microservice responsible for address related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Address_GetList"])
    def get(self):
        """
        Get all addresses which are active in given period.

        For more information, refer to the official documentation:
            [Address_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_GetListCurrent"])
    def get_current(self):
        """
        Get all currently active addresses.

        For more information, refer to the official documentation:
            [Address_GetListCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetListCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all addresses of all employees.

        For more information, refer to the official documentation:
            [Address_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_Delete"])
    def delete(self):
        """
        Get all active bank accounts for given period.

        For more information, refer to the official documentation:
            [Address_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_Update"])
    def update(self):
        """
        Delete Employee Address.

        For more information, refer to the official documentation:
            [Address_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_Insert"])
    def insert(self):
        """
        Insert given address to the specified period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Address_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Address_InsertCurrent"])
    def insert_current(self):
        """
        Insert given address to the current period.

        For more information, refer to the official documentation:
            [Address_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
