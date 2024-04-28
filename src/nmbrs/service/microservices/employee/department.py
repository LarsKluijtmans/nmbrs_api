# pylint: disable=line-too-long
"""Microservice responsible for departments related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Department, DepartmentAll
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeDepartmentsService(MicroService):
    """Microservice responsible for departments related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Department_GetCurrent")
    def get_current(self, employee_id: int) -> Department:
        """
        Get the currently active department.

        For more information, refer to the official documentation:
            [Department_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Department: The Department objects representing the department of the employee.
        """
        department = self.client.service.Department_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return Department(employee_id=employee_id, data=serialize_object(department))

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Department_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[DepartmentAll]:
        """
        Get all department history of all employees.

        For more information, refer to the official documentation:
            [Department_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[DepartmentAll]: a list of Department objects
        """
        departments = self.client.service.Department_GetAll_AllEmployeesByCompany(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )
        departments = serialize_object(departments)
        _departments = []
        for employee in departments:
            for department in employee["EmployeeDepartments"]["Department_V2"]:
                _departments.append(DepartmentAll(employee_id=employee["EmployeeId"], data=department))
        return _departments

    @nmbrs_exception_handler(resource="EmployeeService:Department_UpdateCurrent")
    def update_current(self):
        """
        Update the department starting the current period.

        For more information, refer to the official documentation:
            [Department_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
