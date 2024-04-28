# pylint: disable=line-too-long
"""Microservice responsible for days related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeDaysService(MicroService):
    """Microservice responsible for days related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Get")
    def get_fixed(self):
        """
        Get fixed days worked for given period.

        For more information, refer to the official documentation:
            [DaysFixed_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_GetCurrent")
    def get_current_fixed(self):
        """
        Get fixed days worked for the current period.

        For more information, refer to the official documentation:
            [DaysFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Set")
    def post_fixed(self):
        """
        Set fixed days for given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysFixed_Set](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Set)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_SetCurrent")
    def post_current_fixed(self):
        """
        Set fixed days worked for the current period.

        For more information, refer to the official documentation:
            [DaysFixed_SetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_SetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Set_Batch")
    def post_batch_fixed(self):
        """
        Set fixed days for given period for a batch of Employees. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysFixed_Set_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Set_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Stop")
    def stop_fixed(self):
        """
        Stop fixed days, the given period is the last for these days. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysFixed_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Stop)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVar_Get")
    def get_variable(self):
        """
        Get variable days worked for given period.

        For more information, refer to the official documentation:
            [DaysVar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVar_Set_Batch")
    def post_batch_variable(self):
        """
        Set variable days for given period for a batch of Employees. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysVar_Set_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVar_Set_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_Get")
    def get_days_worked(self):
        """
        Get days worked and +/- days for wage components per day filled in for given period.

        For more information, refer to the official documentation:
            [DaysVarWorked_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_GetCurrent")
    def get_current_days_worked(self):
        """
        Get days worked and +/- days for wage components per day for the current period.

        For more information, refer to the official documentation:
            [DaysVarWorked_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_Set")
    def post_days_worked(self):
        """
        Get days worked and +/- days for wage components per day for the current period.

        For more information, refer to the official documentation:
            [DaysVarWorked_Set](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_Set)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_SetCurrent")
    def post_current_days_worked(self):
        """
        Set days worked and +/- days for wage components per day for the given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysVarWorked_SetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_SetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
