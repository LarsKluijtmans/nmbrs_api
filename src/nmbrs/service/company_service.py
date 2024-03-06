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

        :param auth_header: A dictionary containing authentication details.
        :param sandbox: A boolean indicating whether to use the sandbox environment.
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

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler
    def get_all(self) -> list[Company]:
        companies = self.company_service.service.List_GetAll(
            _soapheaders=self.auth_header
        )
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @nmbrs_exception_handler
    @return_list
    def get_all_wagetax(self, company_id: int, year: int) -> list[WageTax]:
        data = {"CompanyId": company_id, "intYear": year}
        wage_taxes = self.company_service.service.WageTax_GetList(
            **data, _soapheaders=self.auth_header
        )
        wage_taxes = [WageTax(wage_tax) for wage_tax in serialize_object(wage_taxes)]
        return wage_taxes

    @nmbrs_exception_handler
    def get_wagetax_details(self, company_id: int, loonaangifte_id) -> WageTaxXML:
        data = {"CompanyId": company_id, "LoonaangifteID": loonaangifte_id}
        wage_tax_details = self.company_service.service.WageTax_GetXML(
            **data, _soapheaders=self.auth_header
        )
        wage_tax_details = WageTaxXML(wage_tax_details)
        return wage_tax_details
