# pylint: disable=line-too-long
"""Microservice responsible for time schedule related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeTimeScheduleService(MicroService):
    """Microservice responsible for time schedule related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:TimeSchedule_AllEmployee_GetListByPeriod")
    def get_all_by_company(self):
        """
        Get Time Schedules from employee and period.

        For more information, refer to the official documentation:
            [TimeSchedule_AllEmployee_GetListByPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeSchedule_AllEmployee_GetListByPeriod)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:TimeSchedule_GetAll")
    def get_all(self):
        """
        Get all Time Schedules from employee.

        For more information, refer to the official documentation:
            [TimeSchedule_GetAll](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeSchedule_GetAll)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:TimeSchedule_GetListByPeriod")
    def get(self):
        """
        Get Time Schedules from employee and period.

        For more information, refer to the official documentation:
            [TimeSchedule_GetListByPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeSchedule_GetListByPeriod)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:TimeSchedule_Insert")
    def post(self):
        """
        Add a new TimeSchedule.

        For more information, refer to the official documentation:
            [TimeSchedule_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeSchedule_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:TimeSchedule_DeleteByID")
    def delete(self):
        """
        Delete employee time schedule.

        For more information, refer to the official documentation:
            [TimeSchedule_DeleteByID](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeSchedule_DeleteByID)
        """
        raise NotImplementedError()  # pragma: no cover
