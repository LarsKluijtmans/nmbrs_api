# pylint: disable=line-too-long
"""Microservice responsible for contract related actions on the employee level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeContractService(MicroService):
    """Microservice responsible for contract related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_GetAll"])
    def get_all(self):
        """
        Get all contracts for the specified employee.

        For more information, refer to the official documentation:
            [Contract_GetAll](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetAll)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_GetCurrentPeriod"])
    def get_current(self):
        """
        Get a list of all active contracts for specified employee in current period.

        For more information, refer to the official documentation:
            [Contract_GetCurrentPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetCurrentPeriod)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all contracts of all employees.

        For more information, refer to the official documentation:
            [Contract_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_Delete"])
    def delete(self):
        """
        Delete a contract from the system. This action can not be undone.

        For more information, refer to the official documentation:
            [Contract_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_Update"])
    def update(self):
        """
        Update the specified contract for specified employee. Contract start date can’t be updated, this field will be ignored.

        For more information, refer to the official documentation:
            [Contract_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_Insert"])
    def insert(self):
        """
        Insert Contract. If the start date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Contract_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Contract_InsertCurrentPeriod"])
    def insert_current(self):
        """
        Insert Contract in current period for specified employee.

        For more information, refer to the official documentation:
            [Contract_InsertCurrentPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_InsertCurrentPeriod)
        """
        raise NotImplementedError()  # pragma: no cover
