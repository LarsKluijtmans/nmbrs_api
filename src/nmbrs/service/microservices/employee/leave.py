"""Microservice responsible for leave related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeLeaveService(MicroService):
    """Microservice responsible for leave related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:LeaveBalance_Get")
    def get_current(self):
        """
        Get the Leave Balance for the given employee.

        For more information, refer to the official documentation:
            [LeaveBalance_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaveBalance_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Leave_GetList")
    def get_all(self):
        """
        Get a list of leave for the given year, type and usage type.

        For more information, refer to the official documentation:
            [Leave_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Leave_GetList_V2")
    def get_all_2(self):
        """
        Get a list of leave for the given year, type and usage type.

        For more information, refer to the official documentation:
            [Leave_GetList_V2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_GetList_V2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaveBalance_GetPerType")
    def get_by_type(self):
        """
        Get the leave balance for the given employee and type.

        For more information, refer to the official documentation:
            [LeaveBalance_GetPerType](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaveBalance_GetPerType)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Leave_Insert")
    def post(self):
        """
        Insert a new leave, starting from a specific date.

        For more information, refer to the official documentation:
            [Leave_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Leave_Update")
    def update(self):
        """
        Insert a new leave, starting from a specific date.

        For more information, refer to the official documentation:
            [Leave_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Leave_Delete")
    def delete(self):
        """
        Delete a leave entry.

        For more information, refer to the official documentation:
            [Leave_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Leave_Delete)
        """
        raise NotImplementedError()  # pragma: no cover
