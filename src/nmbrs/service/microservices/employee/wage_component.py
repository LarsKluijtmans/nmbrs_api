# pylint: disable=line-too-long
"""Microservice responsible for wage components related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeWageComponentsService(MicroService):
    """Microservice responsible for wage components related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponent_Delete"])
    def delete(self):
        """
        Delete a wage component by ID.

        For more information, refer to the official documentation:
            [WageComponent_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponent_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponent_Update"])
    def update(self):
        """
        Update any wage Component Variable or Fixed.
        In case of being a Fixed Wage Component the parameters EndYear and EndPeriod inside the method can be specified.
        If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponent_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponent_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_Get"])
    def fixed_get(self):
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_GetCurrent"])
    def fixed_get_current(self):
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_GetCurrent"])
    def fixed_insert(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_Insert_With_End"])
    def fixed_insert_with_end(self):
        """
        Insert a wage component to given period of time. If the start period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_InsertCurrent"])
    def fixed_insert_current(self):
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_InsertCurrent_With_End"])
    def fixed_insert_current_with_end(self):
        """
        Insert a wage component to the current period with end period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_InsertCurrent_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_Insert_Batch"])
    def fixed_insert_batch(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_Insert_Batch_With_End"])
    def fixed_insert_batch_with_end(self):
        """
        Insert a batch of wage components to given period of time. If the start period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch_With_End](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Insert_Batch_With_End)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentFixed_Stop"])
    def fixed_stop(self):
        """
        Stop a wage component ending after given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentFixed_Stop)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_Get"])
    def variable_get(self):
        """
        Get all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_GetCurrent"])
    def variable_get_current(self):
        """
        Get all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_Insert"])
    def variable_insert(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_InsertCurrent"])
    def variable_insert_current(self):
        """
        Insert a wage components to the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_Insert_Batch"])
    def variable_insert_batch(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_Clear"])
    def variable_clear(self):
        """
        Clear all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_Clear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageComponentVar_ClearCurrent"])
    def variable_clear_current(self):
        """
        Clear all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageComponentVar_ClearCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
