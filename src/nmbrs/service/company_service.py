# pylint: disable=line-too-long
"""
Module for handling the Company Nmbrs services.
"""
from zeep import Client
from zeep.helpers import serialize_object

from .service import Service
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list
from ..data_classes.company import Company, WageTax, WageTaxXML


class CompanyService(Service):
    """
    A class representing Company Service for interacting with Nmbrs company-related functionalities.\

    Not implemented calls:
      1 [Address_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Address_GetCurrent)
      2 [Address_GetCurrentWithAddressType](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Address_GetCurrentWithAddressType)
      3 [Address_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Address_Insert)
      4 [Address_Update](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Address_Update)
      5 [BankAccount_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_GetCurrent)
      6 [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Insert)
      7 [BankAccount_Update](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Update)
      8 [CompanyLeaveTypeGroups_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CompanyLeaveTypeGroups_Get)
      9 [Company_GetCurrentByEmployeeId](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_GetCurrentByEmployeeId)
      10 [Company_GetCurrentPeriod](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_GetCurrentPeriod)
      11 [Company_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_Insert)
      12 [ContactPerson_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=ContactPerson_Get)
      13 [Converter_GetByCompany_IntToGuid](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Converter_GetByCompany_IntToGuid)
      14 [CostCenter_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostCenter_GetList)
      15 [CostCenter_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostCenter_Insert)
      16 [CostUnit_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_GetList)
      17 [CostUnit_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CostUnit_Insert)
      18 [DefaultEmployeeTemplates_GetByCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=DefaultEmployeeTemplates_GetByCompany)
      19 [FileExplorer_UploadFile](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=FileExplorer_UploadFile)
      20 [HourModel2_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel2_GetHourCodes)
      21 [HourModel_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel_GetHourCodes)
      22 [HrDocuments_EmployerCostPerHour_Year](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HrDocuments_EmployerCostPerHour_Year)
      23 [Journals_GetByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCompany)
      24 [Journals_GetByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCompany_v2)
      25 [Journals_GetByRunCostCenter](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenter)
      26 [Journals_GetByRunCostCenterCostUnit](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenterCostUnit)
      27 [Journals_GetByRunCostCenterCostUnitPerYear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenterCostUnitPerYear)
      28 [Journals_GetByRunCostCenter_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunCostCenter_v2)
      29 [Journals_GetByRunDepartment](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunDepartment)
      30 [Journals_GetByRunDepartment_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunDepartment_v2)
      31 [Journals_GetByRunEmployee](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunEmployee)
      32 [Journals_GetByRunEmployee_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Journals_GetByRunEmployee_v2)
      33 [LabourAgreements_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=LabourAgreements_Get)
      34 [LabourAgreements_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=LabourAgreements_GetCurrent)
      35 [List_GetByDebtor](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetByDebtor)
      36 [PayrollWorkflow_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PayrollWorkflow_Get)
      37 [PensionExport_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetList)
      38 [PensionExport_GetXML](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PensionExport_GetXML)
      39 [Reports_GetJournalsReportByCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetJournalsReportByCompany)
      40 [Reports_GetPayslipByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetPayslipByRunCompany)
      41 [Reports_GetPayslipByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetPayslipByRunCompany_v2)
      42 [Reports_GetWageCodesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByRunCompany)
      43 [Reports_GetWageCodesByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByRunCompany_v2)
      44 [Reports_GetWageCodesByYear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Reports_GetWageCodesByYear)
      45 [RunRequest_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_GetList)
      46 [RunRequest_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=RunRequest_Insert)
      47 [Run_GetEmployeesByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetEmployeesByRunCompany)
      48 [Run_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Run_GetList)
      49 [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_GetCurrent)
      50 [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SVW_UpdateCurrent)
      51 [SalaryDocuments_AnnualDocument_AnualStatement](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_AnualStatement)
      52 [SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative)
      53 [SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative)
      54 [SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative)
      55 [SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative)
      56 [SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative)
      57 [SalaryDocuments_AnnualDocument_LeaveSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_LeaveSaldos)
      58 [SalaryDocuments_AnnualDocument_PaymentListCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PaymentListCumulative)
      59 [SalaryDocuments_AnnualDocument_PayrollRegister](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegister)
      60 [SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees)
      61 [SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative)
      62 [SalaryDocuments_AnnualDocument_ReservationSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_ReservationSaldos)
      63 [SalaryDocuments_AnnualDocument_SentWageTaxDeclarations](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_SentWageTaxDeclarations)
      64 [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod)
      65 [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative)
      66 [SalaryDocuments_GetAllPayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany)
      67 [SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2)
      68 [SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany)
      69 [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany)
      70 [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2)
      71 [SalaryDocuments_GetSEPA](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA)
      72 [SalaryDocuments_GetSEPA_Tax](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA_Tax)
      73 [SalaryTable2_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_Get)
      74 [SalaryTable2_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetScales)
      75 [SalaryTable2_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable2_GetSteps)
      76 [SalaryTable_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_Get)
      77 [SalaryTable_GetScales](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetScales)
      78 [SalaryTable_GetSteps](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryTable_GetSteps)
      79 [Schedule_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Schedule_GetCurrent)
      80 [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Get)
      81 [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_GetCurrent)
      82 [WageComponentFixed_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert)
      83 [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_InsertCurrent)
      84 [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert_Batch)
      85 [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Stop)
      86 [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Clear)
      87 [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_ClearCurrent)
      88 [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Get)
      89 [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_GetCurrent)
      90 [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert)
      91 [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_InsertCurrent)
      92 [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert_Batch)
      93 [WageModel2_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel2_GetWageCodes)
      94 [WageModel_GetWageCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageModel_GetWageCodes)
      95 [WageTax_SetSentExternal](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageTax_SetSentExternal)
      96 [WorkCost_GetList](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_GetList)
      97 [WorkCost_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WorkCost_Insert)
    """

    def __init__(self, sandbox: bool = True) -> None:
        """
        Constructor method for CompanyService class.

        Args:
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
        """
        super().__init__(sandbox)
        self.auth_header: dict | None = None

        # Initialize nmbrs services
        self.company_service = Client(f"{self.base_uri}{self.company_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
             auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:List_GetAll"])
    def get_all(self) -> list[Company]:
        """
        Retrieve all companies.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetAll)

        Returns:
            list[Company]: A list of Company objects representing all companies.
        """
        companies = self.company_service.service.List_GetAll(_soapheaders=self.auth_header)
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageTax_GetList"])
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

    @nmbrs_exception_handler(resources=["CompanyService:WageTax_GetXML"])
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
