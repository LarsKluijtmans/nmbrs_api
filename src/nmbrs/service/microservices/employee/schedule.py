# pylint: disable=line-too-long
"""Microservice responsible for schedule related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.employee import Schedule
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeScheduleService(MicroService):
    """Microservice responsible for schedule related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_GetList"])
    def get_all(self):
        """
        Get all schedules, until given period.

        For more information, refer to the official documentation:
            [Schedule_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_Get"])
    def get(self):
        """
        Get schedule the active schedule for given period.

        For more information, refer to the official documentation:
            [Schedule_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_GetCurrent"])
    def get_current(self):
        """
        Get currently active schedule.

        For more information, refer to the official documentation:
            [Schedule_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self, company_id: int) -> list[Schedule]:
        """
        Get all schedules of all employees from company.

        For more information, refer to the official documentation:
            [Schedule_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Contract]: a list of contract objects
        """
        schedules = self.client.service.Schedule_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_header)
        schedules = serialize_object(schedules)
        _schedules = []
        for employee in schedules:
            for schedule in employee["EmployeeSchedules"]["Schedule_V2"]:
                _schedules.append(Schedule(employee_id=employee["EmployeeId"], data=schedule))
        return _schedules

    @nmbrs_exception_handler(resources=["EmployeeService:ScheduleCalendar_Get"])
    def get_calender(self):
        """
        Get the employee's schedule calendar for given period.

        For more information, refer to the official documentation:
            [ScheduleCalendar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ScheduleCalendar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_Update"])
    def update(self):
        """
        Update schedule starting from the given date. The company default rooster number can be specified.

        For more information, refer to the official documentation:
            [Schedule_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Schedule_UpdateCurrent"])
    def update_current(self):
        """
        Update schedule starting from the current period. The company default rooster number can be specified.

        For more information, refer to the official documentation:
            [Schedule_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
