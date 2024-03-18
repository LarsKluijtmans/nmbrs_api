# pylint: disable=line-too-long
"""Microservice responsible for salary related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeSalaryService(MicroService):
    """Microservice responsible for salary related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_Get"])
    def get(self):
        """
        Get the active salary for the given period.

        For more information, refer to the official documentation:
            [Salary_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_GetCurrent"])
    def get_current(self):
        """
        Get the active salary for the given period.

        For more information, refer to the official documentation:
            [Salary_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_GetList"])
    def get_all(self):
        """
        Get all salary, within given period.

        For more information, refer to the official documentation:
            [Salary_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all salary, until current period.

        For more information, refer to the official documentation:
            [Salary_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SalaryDocuments_GetAnnualStatementPDF"])
    def get_annual_pdf(self):
        """
        Get employee annual statement in PDF

        For more information, refer to the official documentation:
            [SalaryDocuments_GetAnnualStatementPDF](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SalaryDocuments_GetAnnualStatementPDF)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_GetEstimatedCostPerHour"])
    def get_hourly_cost(self):
        """
        Get estimated cost per hour for a given employee and period.

        For more information, refer to the official documentation:
            [Salary_GetEstimatedCostPerHour](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_GetEstimatedCostPerHour)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SalaryTable_Insert"])
    def insert(self):
        """
        Insert salary table to salary.

        For more information, refer to the official documentation:
            [SalaryTable_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SalaryTable_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SalaryTable_InsertCurrent"])
    def insert_current(self):
        """
        Insert salary table to salary of current salary.

        For more information, refer to the official documentation:
            [SalaryTable_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SalaryTable_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_Update"])
    def update(self):
        """
        Update salary. This salary will start from the date given.

        For more information, refer to the official documentation:
            [Salary_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Salary_UpdateCurrent"])
    def update_current(self):
        """
        Update salary. This salary will start from the first date of the current period.

        For more information, refer to the official documentation:
            [Salary_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Salary_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
