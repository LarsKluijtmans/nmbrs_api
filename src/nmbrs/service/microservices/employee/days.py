"""Microservice responsible for days related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....data_classes.serialize import serialize
from ....auth.token_manager import AuthManager
from ....data_classes.employee import DaysWorked, VariableDaysWorked
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeDaysService(MicroService):
    """Microservice responsible for days related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Get")
    def get_fixed(self, employee_id: int, period: int, year: int) -> int:
        """
        Get fixed days worked for given period.

        For more information, refer to the official documentation:
            [DaysFixed_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            int: number of fixed days in given period
        """
        fixed_days = self.client.service.DaysFixed_Get(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return fixed_days

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_GetCurrent")
    def get_current_fixed(self, employee_id: int) -> int:
        """
        Get fixed days worked for the current period.

        For more information, refer to the official documentation:
            [DaysFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            int: number of fixed days in current period
        """
        fixed_days = self.client.service.DaysFixed_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return fixed_days

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Set")
    def post_fixed(self, employee_id: int, period: int, year: int, days: int, unprotected_mode: bool):
        """
        Set fixed days for given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [DaysFixed_Set](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Set)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.
            days (int): The amount of days to insert.
            unprotected_mode (bool): Flag indicating whether the operation is protected.
        """
        self.client.service.DaysFixed_Set(
            EmployeeId=employee_id,
            Period=period,
            Year=year,
            Days=days,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_SetCurrent")
    def post_current_fixed(self, employee_id: int, days: int):
        """
        Set fixed days worked for the current period.

        For more information, refer to the official documentation:
            [DaysFixed_SetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_SetCurrent)

        Args:
            employee_id (int): The ID of the employee.
            days (int): The amount of days to insert.
        """
        self.client.service.DaysFixed_Set(EmployeeId=employee_id, Days=days, _soapheaders=self.auth_manager.header)

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Set_Batch")
    def post_batch_fixed(self, days_worked: list[DaysWorked], unprotected_mode: bool):
        """
        Set fixed days for given period for a batch of Employees. If the period is before the company's current period, unprotected mode flag is required.  # pylint: disable=line-too-long

        For more information, refer to the official documentation:
            [DaysFixed_Set_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Set_Batch)

        Args:
            days_worked (list[DaysWorked]): List of DaysWorked objects that will be inserted.
            unprotected_mode (bool): Flag indicating whether the operation is protected.
        """
        _days_worked = []
        for day_worked in days_worked:
            _days_worked.append(
                {
                    "EmployeeId": day_worked.employee_id,
                    "Days": day_worked.days,
                    "Period": day_worked.period,
                    "Year": day_worked.year,
                }
            )
        self.client.service.DaysFixed_Set_Batch(
            EmployeesDaysWorked={"DaysWorked": _days_worked}, UnprotectedMode=unprotected_mode, _soapheaders=self.auth_manager.header
        )

    @nmbrs_exception_handler(resource="EmployeeService:DaysFixed_Stop")
    def stop_fixed(self, employee_id: int, period: int, year: int, unprotected_mode: bool):
        """
        Stop fixed days, the given period is the last for these days. If the period is before the company's current period, unprotected mode flag is required.  # pylint: disable=line-too-long

        For more information, refer to the official documentation:
            [DaysFixed_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysFixed_Stop)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.
            unprotected_mode (bool): Flag indicating whether the operation is protected.
        """
        self.client.service.DaysFixed_Stop(
            EmployeeId=employee_id, Period=period, Year=year, UnprotectedMode=unprotected_mode, _soapheaders=self.auth_manager.header
        )

    @nmbrs_exception_handler(resource="EmployeeService:DaysVar_Get")
    def get_variable(self, employee_id: int, period: int, year: int) -> int:
        """
        Get variable days worked for given period.

        For more information, refer to the official documentation:
            [DaysVar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVar_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.
        """
        var_days_worked = self.client.service.DaysVar_Get(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return var_days_worked

    @nmbrs_exception_handler(resource="EmployeeService:DaysVar_Set_Batch")
    def post_batch_variable(self, days_worked: list[DaysWorked], unprotected_mode: bool):
        """
        Set variable days for given period for a batch of Employees. If the period is before the company's current period, unprotected mode flag is required.  # pylint: disable=line-too-long

        For more information, refer to the official documentation:
            [DaysVar_Set_Batch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVar_Set_Batch)

        Args:
            days_worked (list[DaysWorked]): List of DaysWorked objects that will be inserted.
            unprotected_mode (bool): Flag indicating whether the operation is protected.
        """
        _days_worked = []
        for day_worked in days_worked:
            _days_worked.append(
                {
                    "EmployeeId": day_worked.employee_id,
                    "Days": day_worked.days,
                    "Period": day_worked.period,
                    "Year": day_worked.year,
                }
            )
        self.client.service.DaysVar_Set_Batch(
            EmployeesDaysWorked={"DaysWorked": _days_worked}, UnprotectedMode=unprotected_mode, _soapheaders=self.auth_manager.header
        )

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_Get")
    def get_days_worked(self, employee_id: int, period: int, year: int) -> VariableDaysWorked:
        """
        Get days worked and +/- days for wage components per day filled in for given period.

        For more information, refer to the official documentation:
            [DaysVarWorked_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        return:
            VariableDaysWorked: variable days object of the given period.
        """
        days = self.client.service.DaysVarWorked_Get(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return VariableDaysWorked(employee_id=employee_id, data=serialize(days))

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_GetCurrent")
    def get_current_days_worked(self, employee_id: int) -> VariableDaysWorked:
        """
        Get days worked and +/- days for wage components per day for the current period.

        For more information, refer to the official documentation:
            [DaysVarWorked_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        return:
            VariableDaysWorked: variable days object for the current period.
        """
        days = self.client.service.DaysVarWorked_Get(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return VariableDaysWorked(employee_id=employee_id, data=serialize(days))

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_Set")
    def post_days_worked(
        self, employee_id: int, period: int, year: int, days: int, plus_min_days_for_wage_comp: int, unprotected_mode: bool
    ):
        """
        Get days worked and +/- days for wage components per day for the current period.

        For more information, refer to the official documentation:
            [DaysVarWorked_Set](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_Set)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.
            days (int): Days to insert.
            plus_min_days_for_wage_comp (int):
            unprotected_mode (bool): Flag indicating whether the operation is protected.
        """
        self.client.service.DaysVarWorked_Set(
            EmployeeId=employee_id,
            Period=period,
            Year=year,
            Days=days,
            PlusMinusDaysForWageComp=plus_min_days_for_wage_comp,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )

    @nmbrs_exception_handler(resource="EmployeeService:DaysVarWorked_SetCurrent")
    def post_current_days_worked(self, employee_id: int, days: int, plus_min_days_for_wage_comp: int):
        """
        Set days worked and +/- days for wage components per day for the given period. If the period is before the company's current period, unprotected mode flag is required.  # pylint: disable=line-too-long

        For more information, refer to the official documentation:
            [DaysVarWorked_SetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=DaysVarWorked_SetCurrent)

        Args:
            employee_id (int): The ID of the employee.
            days (int): Days to insert.
            plus_min_days_for_wage_comp (int):
        """
        self.client.service.DaysVarWorked_Set(
            EmployeeId=employee_id, Days=days, PlusMinusDaysForWageComp=plus_min_days_for_wage_comp, _soapheaders=self.auth_manager.header
        )
