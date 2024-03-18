# pylint: disable=line-too-long
"""Microservice responsible for hour component related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeHourComponentFixedService(MicroService):
    """Microservice responsible for hour component related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_Get"])
    def fixed_get(self):
        """
        Get all extra hour components for given period.

        For more information, refer to the official documentation:
            [HourComponentFixed_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_GetCurrent"])
    def fixed_get_current(self):
        """
        Get all extra hour components for the current period.

        For more information, refer to the official documentation:
            [HourComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_Insert"])
    def fixed_insert(self):
        """
        Insert an extra hour component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentFixed_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_InsertCurrent"])
    def fixed_insert_current(self):
        """
        Insert an extra hour component to the current period.

        For more information, refer to the official documentation:
            [HourComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_Insert_Batch"])
    def fixed_insert_batch(self):
        """
        Insert a batch of extra hour components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_Insert_With_End"])
    def fixed_insert_with_end(self):
        """
        Insert an extra hour component with end to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentFixed_Insert_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_Insert_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentFixed_Stop"])
    def fixed_stop(self):
        """
        Stop an hour component. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentFixed_Stop)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_Get"])
    def variable_get(self):
        """
        Get all extra hour components for given period.

        For more information, refer to the official documentation:
            [HourComponentVar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_GetCurrent"])
    def variable_get_current(self):
        """
        Get all extra hour components for the current period.

        For more information, refer to the official documentation:
            [HourComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_Insert"])
    def variable_insert(self):
        """
        Insert an extra hour component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentVar_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_InsertCurrent"])
    def variable_insert_current(self):
        """
        Insert an extra hour component to the current period.

        For more information, refer to the official documentation:
            [HourComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_Insert_Batch"])
    def variable_insert_batch(self):
        """
        Insert a batch of extra hour components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_Clear"])
    def variable_clear(self):
        """
        Clear all extra hour components for given period.

        For more information, refer to the official documentation:
            [HourComponentVar_Clear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_Clear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponentVar_ClearCurrent"])
    def variable_clear_current(self):
        """
        Clear all extra hour components for current period.

        For more information, refer to the official documentation:
            [HourComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponentVar_ClearCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponent_Delete"])
    def delete(self):
        """
        Delete an hour component linked to an employee by HourComponentID.

        For more information, refer to the official documentation:
            [HourComponent_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponent_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:HourComponent_Update"])
    def update(self):
        """
        Update any Hour Component Variable or Fixed.
        In case of being a Fixed Hour Component the parameters EndYear and EndPeriod inside the method can be specified.
        If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [HourComponent_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=HourComponent_Update)
        """
        raise NotImplementedError()  # pragma: no cover
