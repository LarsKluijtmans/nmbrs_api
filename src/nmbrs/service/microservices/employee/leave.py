"""Microservice responsible for leave related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeLeaveService(MicroService):
    """Microservice responsible for leave related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:LeaveBalance_Get"])
    def get(self):
        """
        Get the Leave Balance for the given employee.

        For more information, refer to the official documentation:
            [LeaveBalance_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaveBalance_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Leave_GetList"])
    def get_all(self):
        """
        Get a list of leave for the given year, type and usage type.

        For more information, refer to the official documentation:
            [Leave_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Leave_GetList_V2"])
    def get_all_2(self):
        """
        Get a list of leave for the given year, type and usage type.

        For more information, refer to the official documentation:
            [Leave_GetList_V2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_GetList_V2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaveBalance_GetPerType"])
    def get_by_type(self):
        """
        Get the leave balance for the given employee and type.

        For more information, refer to the official documentation:
            [LeaveBalance_GetPerType](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaveBalance_GetPerType)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Leave_Insert"])
    def insert(self):
        """
        Insert a new leave, starting from a specific date.

        For more information, refer to the official documentation:
            [Leave_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Leave_Update"])
    def update(self):
        """
        Insert a new leave, starting from a specific date.

        For more information, refer to the official documentation:
            [Leave_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Leave_Delete"])
    def delete(self):
        """
        Delete a leave entry.

        For more information, refer to the official documentation:
            [Leave_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Delete)
        """
        raise NotImplementedError()  # pragma: no cover
