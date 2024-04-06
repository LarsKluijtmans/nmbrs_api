"""Microservice responsible for run related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import RunRequest, RunInfo
from ....data_classes.employee import Employee
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyRunService(MicroService):
    """Microservice responsible for run related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:RunRequest_GetList"])
    def get_requests(self, company_id: int, year: int) -> list[RunRequest]:
        """
        Returns a list of requested runs with status for given company and year.

        For more information, refer to the official documentation:
            [RunRequest_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_GetList)

        Args:
            company_id (int): The ID of the company.
            year (int): year.

        Returns:
            list[RunRequest]: A list of run requests objects.
        """
        run_requests = self.client.service.RunRequest_GetList(CompanyId=company_id, Year=year, _soapheaders=self.auth_header)
        return [RunRequest(company_id=company_id, data=run_request) for run_request in serialize_object(run_requests)]

    @nmbrs_exception_handler(resources=["CompanyService:RunRequest_Insert"])
    def insert_request(self, company_id: int):
        """
        Requests a run for given company.

        For more information, refer to the official documentation:
            [RunRequest_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_Insert)

        Args:
            company_id (int): The ID of the company.
        """
        self.client.service.RunRequest_Insert(CompanyId=company_id, _soapheaders=self.auth_header)

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:Run_GetList"])
    def get(self, company_id: int, year: int) -> list[RunInfo]:
        """
        Get the company's run list for a specified year.

        For more information, refer to the official documentation:
            [Run_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetList)

        Args:
            company_id (int): The ID of the company.
            year (int): year.

        Returns:
            list[RunInfo]: A list of run info objects.
        """
        runs = self.client.service.Run_GetList(CompanyId=company_id, Year=year, _soapheaders=self.auth_header)
        return [RunInfo(company_id=company_id, data=run) for run in serialize_object(runs)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:Run_GetEmployeesByRunCompany"])
    def get_all_employees_by_run(self, company_id: int, year: int, run_id: int) -> list[Employee]:
        """
        Get the employee's list for a specified company id, run id and year

        For more information, refer to the official documentation:
            [Run_GetEmployeesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetEmployeesByRunCompany)

        Args:
            company_id (int): The ID of the company.
            year (int): Year.
            run_id (int): The unique identifier for a run.

        Returns:
            list[Employee]: A list of employee objects, with the name field empty.
        """
        employees = self.client.service.Run_GetEmployeesByRunCompany(
            CompanyId=company_id, Year=year, RunId=run_id, _soapheaders=self.auth_header
        )
        return [
            Employee({"Id": employee.get("EmployeeId"), "Number": employee.get("EmployeeNumber")})
            for employee in serialize_object(employees)
        ]

    @nmbrs_exception_handler(resources=["CompanyService:HrDocuments_EmployerCostPerHour_Year"])
    def get_hr_documents_cost_per_hour_year(self, company_id: int, run_id: int, year: int, period: int) -> bytes:
        """
        Get HR Document: Employer Cost per Hour per company per period.

        For further details, see the official documentation:
            [HrDocuments_EmployerCostPerHour_Year](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HrDocuments_EmployerCostPerHour_Year)

        Args:
            company_id (int): The ID of the company.
            run_id (int): The ID of the run.
            year (int): The year.
            period (int): The period.

        Returns:
            bytes: The HR document as base64Binary.
        """
        response = self.client.service.HrDocuments_EmployerCostPerHour_Year(
            CompanyId=company_id, RunId=run_id, Year=year, Period=period, _soapheaders=self.auth_header
        )
        return response
