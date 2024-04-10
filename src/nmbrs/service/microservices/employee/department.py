# pylint: disable=line-too-long
"""Microservice responsible for departments related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.employee import Department
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeDepartmentsService(MicroService):
    """Microservice responsible for departments related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resource="EmployeeService:Department_GetCurrent")
    def get_current(self):
        """
        Get the currently active department.

        For more information, refer to the official documentation:
            [Department_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Department_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Department]:
        """
        Get all department history of all employees.

        For more information, refer to the official documentation:
            [Department_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Department]: a list of Department objects
        """
        departments = self.client.service.Department_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_header)
        departments = serialize_object(departments)
        _departments = []
        for employee in departments:
            for department in employee["EmployeeDepartments"]["Department_V2"]:
                _departments.append(Department(employee_id=employee["EmployeeId"], data=department))
        return _departments

    @nmbrs_exception_handler(resource="EmployeeService:Department_UpdateCurrent")
    def update_current(self):
        """
        Update the department starting the current period.

        For more information, refer to the official documentation:
            [Department_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Department_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
