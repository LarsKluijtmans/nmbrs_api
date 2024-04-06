# pylint: disable=line-too-long
"""Microservice responsible for contract related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.employee import Contract
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


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

    @return_list
    @nmbrs_exception_handler(resources=["EmployeeService:Contract_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self, company_id: int) -> list[Contract]:
        """
        Get all contracts of all employees.

        For more information, refer to the official documentation:
            [Contract_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Contract]: a list of contract objects
        """
        contracts = self.client.service.Contract_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_header)
        contracts = serialize_object(contracts)
        _contracts = []
        for employee in contracts:
            for contract in employee["EmployeeContracts"]["EmployeeContract"]:
                _contracts.append(Contract(employee_id=employee["EmployeeId"], data=contract))
        return _contracts

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
