# pylint: disable=line-too-long
"""Microservice responsible for employment related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Employment
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeEmploymentService(MicroService):
    """Microservice responsible for employment related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Employment_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Employment]:
        """
        Get all (historical) employment records for all employees that belong to the company.

        For more information, refer to the official documentation:
            [Employment_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employment_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Employment]: a list of Employment objects
        """
        employments = self.client.service.Employment_GetAll_AllEmployeesByCompany(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )
        employments = serialize_object(employments)
        _employments = []
        for employee in employments:
            for employment in employee["EmployeeEmployments"]["Employment"]:
                _employments.append(Employment(employee_id=employee["EmployeeId"], data=employment))
        return _employments

    @nmbrs_exception_handler(resource="EmployeeService:Employment_UpdateEmploymentInitialStartDate")
    def update_start_date(self):
        """
        Update employee service initial start date.

        For more information, refer to the official documentation:
            [Employment_UpdateEmploymentInitialStartDate](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employment_UpdateEmploymentInitialStartDate)
        """
        raise NotImplementedError()  # pragma: no cover
