from nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler
from nmbrs.utils.return_list import return_list
from zeep import Client
from zeep.helpers import serialize_object

from nmbrs.service.service import Service
from nmbrs.data_classes.company.company import Company
from nmbrs.data_classes.company.wage_tax import WageTax
from nmbrs.data_classes.company.wage_tax_xml import WageTaxXML


class CompanyService(Service):
    """
    A class representing Company Service for interacting with Nmbrs company-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for CompanyService class.

        Initializes CompanyService instance with authentication and sandbox settings.

        Args:
            auth_header (dict): A dictionary containing authentication details.
            sandbox (bool): A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.company_service = Client(f"{base_uri}{self.company_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
             auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler(["CompanyService:List_GetAll"])
    def get_all(self) -> list[Company]:
        """
        Retrieve all companies.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetAll)

        Returns:
            list[Company]: A list of Company objects representing all companies.
        """
        companies = self.company_service.service.List_GetAll(
            _soapheaders=self.auth_header
        )
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @return_list
    @nmbrs_exception_handler(["CompanyService:WageTax_GetList"])
    def get_all_wagetax(self, company_id: int, year: int) -> list[WageTax]:
        """
        Retrieve all wage taxes for a specific company and year.

        For more information, refer to the official documentation:
            [Soap call WageTax_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageTax_GetList)

        Args:
            company_id (int): The ID of the company.
            year (int): The year for which wage taxes are retrieved.

        Returns:
            list[WageTax]: A list of WageTax objects representing all wage taxes for the specified company and year.
        """
        data = {"CompanyId": company_id, "intYear": year}
        wage_taxes = self.company_service.service.WageTax_GetList(
            **data, _soapheaders=self.auth_header
        )
        wage_taxes = [WageTax(wage_tax) for wage_tax in serialize_object(wage_taxes)]
        return wage_taxes

    @nmbrs_exception_handler(["CompanyService:WageTax_GetXML"])
    def get_wagetax_details(self, company_id: int, loonaangifte_id) -> WageTaxXML:
        """
        Retrieve wage tax details for a specific company and loonaangifte ID.

        For more information, refer to the official documentation:
            [Soap call WageTax_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageTax_GetXML)

        Args:
            company_id (int): The ID of the company.
            loonaangifte_id: The loonaangifte ID.

        Returns:
            WageTaxXML: An object representing the wage tax details for the specified company and loonaangifte ID.
        """
        data = {"CompanyId": company_id, "LoonaangifteID": loonaangifte_id}
        wage_tax_details = self.company_service.service.WageTax_GetXML(
            **data, _soapheaders=self.auth_header
        )
        wage_tax_details = WageTaxXML(wage_tax_details)
        return wage_tax_details
