# pylint: disable=line-too-long
"""Microservice responsible for service related actions on the employee level."""
import logging
from datetime import datetime

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Service
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler

logger = logging.getLogger(__name__)


class EmployeeServiceService(MicroService):
    """Microservice responsible for service related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Service_GetList")
    def get_all(self, employee_id: int) -> list[Service]:
        """
        Get all service intervals for a given employee.

        For more information, refer to the official documentation:
            [Service_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_GetList)

        Args:
            employee_id (int): The ID of the employee for whom to fetch service intervals.

        Returns:
            list[dict]: A list of dictionaries representing service intervals with start/end dates, seniority, and reason for service end.
        """
        services = self.client.service.Service_GetList(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)

        return [Service(employee_id=employee_id, data=service) for service in serialize_object(services)]

    @nmbrs_exception_handler(resource="EmployeeService:Service_Insert")
    def post(self, employee_id: int, start_date: datetime, unprotected_mode: bool):
        """
        Start a new service interval for an employee.

        Args:
            employee_id (int): The ID of the employee.
            start_date (datetime): The start date of the service interval.
            unprotected_mode (bool): Whether the service interval should bypass period protection (when starting in the past).

        Returns: None
        """
        self.client.service.Service_Insert(
            EmployeeId=employee_id, Start=start_date, UnprotectedMode=unprotected_mode, _soapheaders=self.auth_manager.header
        )

    @nmbrs_exception_handler(resource="EmployeeService:Service_Insert2")
    def post_2(self, employee_id: int, start_date: datetime, ancienniteitsdatum: datetime, unprotected_mode: bool):
        """
        Start a new service interval with the specified seniority date.
        If the date is before the company's current period, the unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Service_Insert2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_Insert2)

        Args:
            employee_id (int): The ID of the employee.
            start_date (datetime): The start date of the service interval.
            ancienniteitsdatum (datetime): The seniority date of the service interval.
            unprotected_mode (bool): Whether to bypass period protection.

        Returns: None
        """
        self.client.service.Service_Insert2(
            EmployeeId=employee_id,
            Start=start_date,
            Ancienniteitsdatum=ancienniteitsdatum,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )

    @nmbrs_exception_handler(resource="EmployeeService:Service_Delete")
    def delete(self, employee_id: int) -> bool:
        """
        Delete a service interval for the specified employee.

        For more information, refer to the official documentation:
            [Service_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_Delete)

        Args:
            employee_id (int): The ID of the employee for whom the service interval should be deleted.

        Returns:
            bool: True if the service interval was successfully deleted, otherwise False.
        """
        response = self.client.service.Service_Delete(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Service_StopCurrent")
    @nmbrs_exception_handler(resource="EmployeeService:Service_StopCurrent")
    def stop_current(self, employee_id: int, end_date: datetime, end_service_reason_id: int, unprotected_mode: bool) -> bool:
        """
        Stop the current service interval. If the date is before the company's current period, unprotected mode flag is required.
        If the employee income type requires and the employee is an applicant, the EndServiceReasonId is mandatory; otherwise, this field is ignored.

        For more information, refer to the official documentation:
            [Service_StopCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_StopCurrent)

        Args:
            employee_id (int): The ID of the employee whose service interval is to be stopped.
            end_date (datetime): The date the service interval should end.
            end_service_reason_id (int): The reason for ending the service interval (applicant-related).
            unprotected_mode (bool): Indicates whether to use unprotected mode for stopping the service interval.

        Returns:
            bool: True if the service interval was successfully stopped, otherwise False.
        """
        response = self.client.service.Service_StopCurrent(
            EmployeeId=employee_id,
            End=end_date,
            EndServiceReasonId=end_service_reason_id,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Service_RemoveOutService")
    def remove_out_service(self, employee_id: int, unprotected_mode: bool) -> bool:
        """
        Remove the out of service date for an employee. If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Service_RemoveOutService](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_RemoveOutService)

        Args:
            employee_id (int): The ID of the employee whose out of service date is to be removed.
            unprotected_mode (bool): Indicates whether to use unprotected mode for removing the out of service date.

        Returns:
            bool: True if the out of service date was successfully removed, otherwise False.
        """
        response = self.client.service.Service_RemoveOutService(
            EmployeeId=employee_id, UnprotectedMode=unprotected_mode, _soapheaders=self.auth_manager.header
        )
        return response
