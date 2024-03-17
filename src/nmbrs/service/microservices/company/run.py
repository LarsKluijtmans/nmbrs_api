"""Microservice responsible for run related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyRunService(MicroService):
    """Microservice responsible for run related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:RunRequest_GetList"])
    def get_requests(self):
        """
        Returns a list of requested runs with status for given company and year.

        For more information, refer to the official documentation:
            [RunRequest_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:RunRequest_Insert"])
    def insert_request(self):
        """
        Requests a run for given company.

        For more information, refer to the official documentation:
            [RunRequest_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:Run_GetList"])
    def get_run(self):
        """
        Get the company's run list for a specified year.

        For more information, refer to the official documentation:
            [Run_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:Run_GetEmployeesByRunCompany"])
    def get_all_by_run(self):
        """
        Get the employee's list for a specified company id, run id and year

        For more information, refer to the official documentation:
            [Run_GetEmployeesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetEmployeesByRunCompany)
        """
        raise NotImplementedError()  # pragma: no cover
