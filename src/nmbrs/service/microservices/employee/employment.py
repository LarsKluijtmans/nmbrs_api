# pylint: disable=line-too-long
"""Microservice responsible for employment related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeEmploymentService(MicroService):
    """Microservice responsible for employment related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Employment_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all (historical) employment records for all employees that belong to the company.

        For more information, refer to the official documentation:
            [Employment_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employment_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employment_UpdateEmploymentInitialStartDate"])
    def update_start_date(self):
        """
        Update employee service initial start date.

        For more information, refer to the official documentation:
            [Employment_UpdateEmploymentInitialStartDate](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employment_UpdateEmploymentInitialStartDate)
        """
        raise NotImplementedError()  # pragma: no cover
