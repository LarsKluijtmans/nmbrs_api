# pylint: disable=line-too-long
"""Microservice responsible for time registration related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeTimeRegistrationService(MicroService):
    """Microservice responsible for time registration related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_GetList"])
    def get_all(self):
        """
        Get Time Registration items filtered by time.

        For more information, refer to the official documentation:
            [TimeRegistration_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_Insert"])
    def insert(self):
        """
        Register item into the calendar of an employee.

        For more information, refer to the official documentation:
            [TimeRegistration_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_Insert_Batch"])
    def insert_batch(self):
        """
        Register items into the calendars.

        For more information, refer to the official documentation:
            [TimeRegistration_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_GetAll_AllTimeRegistrationCodes"])
    def get_codes(self):
        """
        Get available TimeRegistrationCodes.

        For more information, refer to the official documentation:
            [TimeRegistration_GetAll_AllTimeRegistrationCodes](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_GetAll_AllTimeRegistrationCodes)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_Delete"])
    def delete(self):
        """
        Delete Time Registration Item By ID.

        For more information, refer to the official documentation:
            [TimeRegistration_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_Clear"])
    def clear(self):
        """
        Delete Time Registration Item By EmployeeId and given dates.

        For more information, refer to the official documentation:
            [TimeRegistration_Clear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_Clear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:TimeRegistration_ClearCurrent"])
    def clear_current(self):
        """
        Delete Time Registration Item By EmployeeId.

        For more information, refer to the official documentation:
            [TimeRegistration_ClearCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=TimeRegistration_ClearCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
