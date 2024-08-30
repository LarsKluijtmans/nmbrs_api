# pylint: disable=line-too-long
"""Microservice responsible for schedule related actions on the employee level."""
import logging

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import ScheduleAll, Schedule
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler

logger = logging.getLogger(__name__)


class EmployeeScheduleService(MicroService):
    """Microservice responsible for schedule related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_GetList")
    def get_all(self):
        """
        Get all schedules, until given period.

        For more information, refer to the official documentation:
            [Schedule_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_Get")
    def get(self, employee_id: int, period: int, year: int) -> Schedule:
        """
        Get schedule the active schedule for given period.

        For more information, refer to the official documentation:
            [Schedule_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            Schedule: Employees schedule for the given period
        """
        schedule = self.client.service.Schedule_Get(EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header)
        return Schedule(employee_id=employee_id, data=serialize_object(schedule))

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_GetCurrent")
    def get_current(self, employee_id: int) -> Schedule:
        """
        Get currently active schedule.

        For more information, refer to the official documentation:
            [Schedule_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Schedule: Employees schedule for the given period
        """
        schedule = self.client.service.Schedule_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return Schedule(employee_id=employee_id, data=serialize_object(schedule))

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[ScheduleAll]:
        """
        Get all schedules of all employees from company.

        For more information, refer to the official documentation:
            [Schedule_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[ScheduleAll]: a list of contract objects
        """
        schedules = self.client.service.Schedule_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_manager.header)
        schedules = serialize_object(schedules)
        _schedules = []
        for employee in schedules:
            for schedule in employee["EmployeeSchedules"]["Schedule_V2"]:
                _schedules.append(ScheduleAll(employee_id=employee["EmployeeId"], data=schedule))
        return _schedules

    @nmbrs_exception_handler(resource="EmployeeService:ScheduleCalendar_Get")
    def get_calender(self):
        """
        Get the employee's schedule calendar for given period.

        For more information, refer to the official documentation:
            [ScheduleCalendar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ScheduleCalendar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_Update")
    def update(self):
        """
        Update schedule starting from the given date. The company default rooster number can be specified.

        For more information, refer to the official documentation:
            [Schedule_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Schedule_UpdateCurrent")
    def update_current(self, employee_id: int, schedule: Schedule) -> None:
        """
        Update schedule starting from the current period. The company default rooster number can be specified.

        For more information, refer to the official documentation:
            [Schedule_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Schedule_UpdateCurrent)

        Args:
            employee_id (int): The ID of the employee.
            schedule (Schedule): The users new schedule.
        """
        schedule_dict = {
            "HoursMonday": schedule.hours_monday,
            "HoursTuesday": schedule.hours_tuesday,
            "HoursWednesday": schedule.hours_wednesday,
            "HoursThursday": schedule.hours_thursday,
            "HoursFriday": schedule.hours_friday,
            "HoursSaturday": schedule.hours_saturday,
            "HoursSunday": schedule.hours_sunday,
            "HoursMonday2": schedule.hours_monday2,
            "HoursTuesday2": schedule.hours_tuesday2,
            "HoursWednesday2": schedule.hours_wednesday2,
            "HoursThursday2": schedule.hours_thursday2,
            "HoursFriday2": schedule.hours_friday2,
            "HoursSaturday2": schedule.hours_saturday2,
            "HoursSunday2": schedule.hours_sunday2,
            "ParttimePercentage": schedule.part_time_percentage,
            "StartDate": schedule.start_date,
        }
        self.client.service.Schedule_UpdateCurrent(
            EmployeeId=employee_id, Schedule=schedule_dict, CompanyRoosterNr=1, _soapheaders=self.auth_manager.header
        )
