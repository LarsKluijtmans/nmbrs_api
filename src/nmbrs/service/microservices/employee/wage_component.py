# pylint: disable=line-too-long
"""Microservice responsible for wage components related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeWageComponentsService(MicroService):
    """Microservice responsible for wage components related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:WageComponent_Delete")
    def delete(self):
        """
        Delete a wage component by ID.

        For more information, refer to the official documentation:
            [WageComponent_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponent_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponent_Update")
    def update(self):
        """
        Update any wage Component Variable or Fixed.
        In case of being a Fixed Wage Component the parameters EndYear and EndPeriod inside the method can be specified.
        If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponent_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponent_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_Get")
    def get_fixed(self):
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_GetCurrent")
    def get_current_fixed(self):
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_GetCurrent")
    def post_fixed(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_Insert_With_End")
    def insert_fixed_with_end(self):
        """
        Insert a wage component to given period of time. If the start period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_InsertCurrent")
    def post_current_fixed(self):
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_InsertCurrent_With_End")
    def post_current_fixed_with_end(self):
        """
        Insert a wage component to the current period with end period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_InsertCurrent_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_Insert_Batch")
    def post_batch_fixed(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_Insert_Batch_With_End")
    def post_batch_fixed_with_end(self):
        """
        Insert a batch of wage components to given period of time. If the start period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_Batch_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentFixed_Stop")
    def stop_fixed(self):
        """
        Stop a wage component ending after given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Stop)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_Get")
    def get_variable(self):
        """
        Get all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_GetCurrent")
    def get_current_variable(self):
        """
        Get all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_Insert")
    def post_variable(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_InsertCurrent")
    def post_current_varaible(self):
        """
        Insert a wage components to the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_Insert_Batch")
    def post_batch_variable(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_Clear")
    def clear_variable(self):
        """
        Clear all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Clear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:WageComponentVar_ClearCurrent")
    def clear_current_variable(self):
        """
        Clear all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_ClearCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
