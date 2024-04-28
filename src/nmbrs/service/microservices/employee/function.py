# pylint: disable=line-too-long
"""Microservice responsible for function related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Function, FunctionAll
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeFunctionService(MicroService):
    """Microservice responsible for function related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Function_GetFunction")
    def get_by_id(self):
        """
        Get Function by functionID.

        For more information, refer to the official documentation:
            [Function_GetFunction](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetFunction)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Function_GetCurrent")
    def get_current(self, employee_id: int) -> Function:
        """
        Get the currently active function.

        For more information, refer to the official documentation:
            [Function_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Function: The Function objects representing the function of the employee.
        """
        function = self.client.service.Function_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return Function(employee_id=employee_id, data=serialize_object(function))

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Function_GetAll_AllEmployeesByCompany_V2")
    def get_all_by_company(self, company_id: int) -> list[FunctionAll]:
        """
        Get all Function history of all employees.

        For more information, refer to the official documentation:
            [Function_GetAll_AllEmployeesByCompany_V2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetAll_AllEmployeesByCompany_V2)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[FunctionAll]: a list of Function objects
        """
        functions = self.client.service.Function_GetAll_AllEmployeesByCompany_V2(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )
        functions = serialize_object(functions)

        _functions = []
        for employee in functions:
            for function in employee["EmployeeFunctions"]["EmployeeFunction"]:
                _functions.append(FunctionAll(employee_id=employee["EmployeeId"], data=function))
        return _functions

    @nmbrs_exception_handler(resource="EmployeeService:Function_Update")
    def update(self):
        """
        Update the function starting from the given period.

        For more information, refer to the official documentation:
            [Function_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Function_UpdateCurrent")
    def update_current(self):
        """
        Update the function starting from current period.

        For more information, refer to the official documentation:
            [Function_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
