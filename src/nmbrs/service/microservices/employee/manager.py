"""Microservice responsible for manager related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Manager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeManagerService(MicroService):
    """Microservice responsible for manager related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Manager_Get")
    def get(self, employee_id: int, period: int, year: int) -> Manager:
        """
        Get the manager of an employee to the specified period.

        For more information, refer to the official documentation:
            [Manager_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Manager_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            Manager: The Manager objects representing the manager of the employee.
        """
        manager = self.client.service.Manager_Get(EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header)
        return Manager(employee_id=employee_id, data=serialize_object(manager))

    @nmbrs_exception_handler(resource="EmployeeService:Manager_GetCurrent")
    def get_current(self, employee_id: int) -> Manager:
        """
        Get the manager of an employee.

        For more information, refer to the official documentation:
            [Manager_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Manager_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Manager: The Manager objects representing the manager of the employee.
        """
        manager = self.client.service.Manager_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return Manager(employee_id=employee_id, data=serialize_object(manager))
