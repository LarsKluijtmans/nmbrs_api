# pylint: disable=line-too-long
"""Microservice responsible for journal related actions on the company level."""
from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyJournalService(MicroService):
    """
    Microservice responsible for journal related actions on the company level.

    Not implemented calls:
        - [Journals_GetByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCompany)
        - [Journals_GetByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCompany_v2)
        - [Journals_GetByRunCostCenter](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenter)
        - [Journals_GetByRunCostCenterCostUnit](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenterCostUnit)
        - [Journals_GetByRunCostCenterCostUnitPerYear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenterCostUnitPerYear)
        - [Journals_GetByRunCostCenter_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenter_v2)
        - [Journals_GetByRunDepartment](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunDepartment)
        - [Journals_GetByRunDepartment_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunDepartment_v2)
        - [Journals_GetByRunEmployee](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunEmployee)
        - [Journals_GetByRunEmployee_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunEmployee_v2)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanyJournalService.

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
