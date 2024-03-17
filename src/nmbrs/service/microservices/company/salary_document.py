# pylint: disable=line-too-long
"""Microservice responsible for salary documents related actions on the company level."""
from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class CompanySalaryDocumentService(MicroService):
    """
    Microservice responsible for salary documents related actions on the company level.

    Not implemented calls:
        - [SalaryDocuments_AnnualDocument_AnualStatement](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_AnualStatement)
        - [SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative)
        - [SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative)
        - [SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative)
        - [SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative)
        - [SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative)
        - [SalaryDocuments_AnnualDocument_LeaveSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_LeaveSaldos)
        - [SalaryDocuments_AnnualDocument_PaymentListCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PaymentListCumulative)
        - [SalaryDocuments_AnnualDocument_PayrollRegister](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegister)
        - [SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees)
        - [SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative)
        - [SalaryDocuments_AnnualDocument_ReservationSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_ReservationSaldos)
        - [SalaryDocuments_AnnualDocument_SentWageTaxDeclarations](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_SentWageTaxDeclarations)
        - [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod)
        - [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative)
        - [SalaryDocuments_GetAllPayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany)
        - [SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2)
        - [SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany)
        - [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany)
        - [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2)
        - [SalaryDocuments_GetSEPA](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA)
        - [SalaryDocuments_GetSEPA_Tax](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA_Tax)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanySalaryDocumentService.

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
