"""Microservice responsible for manager related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeManagerService(MicroService):
    """Microservice responsible for manager related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Manager_Get"])
    def get(self):
        """
        Get the manager of an employee to the specified period.

        For more information, refer to the official documentation:
            [Manager_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Manager_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Manager_GetCurrent"])
    def get_current(self):
        """
        Get the manager of an employee.

        For more information, refer to the official documentation:
            [Manager_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Manager_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
