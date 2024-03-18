# pylint: disable=line-too-long
"""Microservice responsible for function related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeFunctionService(MicroService):
    """Microservice responsible for function related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Function_GetFunction"])
    def get_by_id(self):
        """
        Get Function by functionID.

        For more information, refer to the official documentation:
            [Function_GetFunction](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetFunction)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Function_GetCurrent"])
    def get_current(self):
        """
        Get the currently active function.

        For more information, refer to the official documentation:
            [Function_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Function_GetAll_AllEmployeesByCompany_V2"])
    def get_all_by_company(self):
        """
        Get all Function history of all employees.

        For more information, refer to the official documentation:
            [Function_GetAll_AllEmployeesByCompany_V2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_GetAll_AllEmployeesByCompany_V2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Function_Update"])
    def update(self):
        """
        Update the function starting from the given period.

        For more information, refer to the official documentation:
            [Function_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Function_UpdateCurrent"])
    def update_current(self):
        """
        Update the function starting from current period.

        For more information, refer to the official documentation:
            [Function_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Function_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
