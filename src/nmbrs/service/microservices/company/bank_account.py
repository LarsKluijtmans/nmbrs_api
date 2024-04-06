"""Microservice responsible for bank account related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import BankAccount
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyBankAccountService(MicroService):
    """Microservice responsible for bank account related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_GetCurrent"])
    def get_current(self, company_id: int) -> BankAccount | None:
        """
        Get the company's current bank account.

        For more information, refer to the official documentation:
            [BankAccount_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            BankAccount: An BankAccount object.
        """
        bank_account = self.client.service.BankAccount_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_header)
        if bank_account is None:
            return None
        return BankAccount(company_id=company_id, data=serialize_object(bank_account))

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_Insert"])
    def insert(
        self,
        company_id: int,
        account_id: int,
        account_number: str,
        description: str,
        iban: str,
        bic: str,
        city: str,
        name: str,
        account_type: str,
    ) -> int:
        """
        Insert a company bank account.

        For more information, refer to the official documentation:
            [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Insert)

        Args:
            company_id (int): The ID of the company.
            account_id (int): The ID of the bank account.
            account_number (str): The bank account number.
            description (str): Description of the bank account.
            iban (str): The IBAN of the bank account.
            bic (str): The BIC of the bank account.
            city (str): The city of the bank account.
            name (str): The name of the bank account.
            account_type (str): The type of the bank account (Options: None, Bankrekening1, Spaarloon, Bankrekening2,
                Bankrekening3, Bankrekening4,  Bankrekening5,  Standaard, Levensloop).

        Returns:
            int | None: The ID of the inserted bank account if successful, otherwise None.
        """
        bank_account = {
            "Id": account_id,
            "Number": account_number,
            "Description": description,
            "IBAN": iban,
            "BIC": bic,
            "City": city,
            "Name": name,
            "Type": account_type,
        }
        response = self.client.service.BankAccount_Insert(CompanyId=company_id, BankAccount=bank_account, _soapheaders=self.auth_header)
        return response

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_Update"])
    def update(
        self,
        company_id: int,
        account_id: int,
        account_number: str,
        description: str,
        iban: str,
        bic: str,
        city: str,
        name: str,
        account_type: str,
    ) -> None:
        """
        Insert a company bank account.

        For more information, refer to the official documentation:
            [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Update)

        Args:
            company_id (int): The ID of the company.
            account_id (int): The ID of the bank account.
            account_number (str): The bank account number.
            description (str): Description of the bank account.
            iban (str): The IBAN of the bank account.
            bic (str): The BIC of the bank account.
            city (str): The city of the bank account.
            name (str): The name of the bank account.
            account_type (str): The type of the bank account (Options: None, Bankrekening1, Spaarloon, Bankrekening2,
                Bankrekening3, Bankrekening4,  Bankrekening5,  Standaard, Levensloop).

        Returns: None
        """
        bank_account = {
            "Id": account_id,
            "Number": account_number,
            "Description": description,
            "IBAN": iban,
            "BIC": bic,
            "City": city,
            "Name": name,
            "Type": account_type,
        }
        self.client.service.BankAccount_Update(CompanyId=company_id, BankAccount=bank_account, _soapheaders=self.auth_header)
