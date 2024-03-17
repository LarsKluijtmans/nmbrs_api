"""Microservice responsible for salary table related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanySalaryTableService(MicroService):
    """
    Microservice responsible for salary table related actions on the company level.

    Not implemented calls:
        - [SalaryTable2_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_Get)
        - [SalaryTable2_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetScales)
        - [SalaryTable2_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetSteps)
        - [SalaryTable_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_Get)
        - [SalaryTable_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetScales)
        - [SalaryTable_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetSteps)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanySalaryTableService.

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
