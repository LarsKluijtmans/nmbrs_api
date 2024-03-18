# pylint: disable=line-too-long
"""Microservice responsible for service related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeServiceService(MicroService):
    """Microservice responsible for service related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Service_GetList"])
    def get_all(self):
        """
        Get all service intervals.

        For more information, refer to the official documentation:
            [Service_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Service_Insert"])
    def insert(self):
        """
        Start a new service interval. If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Service_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Service_Insert2"])
    def insert_2(self):
        """
        Start a new service interval. If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Service_Insert2](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_Insert2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Service_Delete"])
    def delete(self):
        """
        Delete a service interval.

        For more information, refer to the official documentation:
            [Service_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Service_StopCurrent"])
    def stop_current(self):
        """
        Stop the current service interval. If the date is before the company's current period, unprotected mode flag is required.
        If the employee income type requires and the employee is an applicant the EndServiceReasonId is mandatory, otherwise this field is ignored whatever the value is passed.

        For more information, refer to the official documentation:
            [Service_StopCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_StopCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Service_RemoveOutService"])
    def remove_out_service(self):
        """
        Remove out of service date.

        For more information, refer to the official documentation:
            [Service_RemoveOutService](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Service_RemoveOutService)
        """
        raise NotImplementedError()  # pragma: no cover
