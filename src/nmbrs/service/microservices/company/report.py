"""Microservice responsible for report related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyReportService(MicroService):
    """
    Microservice responsible for report related actions on the company level.

    Not implemented calls:
        - [Reports_GetJournalsReportByCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetJournalsReportByCompany)
        - [Reports_GetPayslipByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetPayslipByRunCompany)
        - [Reports_GetPayslipByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetPayslipByRunCompany_v2)
        - [Reports_GetWageCodesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByRunCompany)
        - [Reports_GetWageCodesByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByRunCompany_v2)
        - [Reports_GetWageCodesByYear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByYear)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanyReportService.

        Args:
            client (Client): A Zeep Client object representing the connection to the Nmbrs API.
        """
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Set the authentication header for requests to the Nmbrs API.

        Args:
            auth_header (dict): The authentication header to be set.
        """
        self.auth_header = auth_header
