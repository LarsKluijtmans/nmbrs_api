# pylint: disable=line-too-long
"""Microservice responsible for departments related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeDepartmentsService(MicroService):
    """Microservice responsible for departments related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Department_GetCurrent"])
    def get_current(self):
        """
        Get the currently active department.

        For more information, refer to the official documentation:
            [Department_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Department_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all department history of all employees.

        For more information, refer to the official documentation:
            [Department_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Department_UpdateCurrent"])
    def update_current(self):
        """
        Update the department starting the current period.

        For more information, refer to the official documentation:
            [Department_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
