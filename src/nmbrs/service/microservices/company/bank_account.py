"""Microservice responsible for bank account related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanyBankAccountService(MicroService):
    """
    Microservice responsible for bank account related actions on the company level.

    Not implemented calls:
        - [BankAccount_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_GetCurrent)
        - [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Insert)
        - [BankAccount_Update](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Update)
    """

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header
