"""
Module for handling the Company Nmbrs services.
"""

from zeep import Client
from zeep.helpers import serialize_object

from .microservices.company import (
    CompanyAddressService,
    CompanyBankAccountService,
    CompanyCostCenterService,
    CompanyCostUnitService,
    CompanyHourModelService,
    CompanyJournalService,
    CompanyLabourAgreementService,
    CompanyPensionService,
    CompanyReportService,
    CompanyRunService,
    CompanySalaryDocumentService,
    CompanySalaryTableService,
    CompanyWageComponentFixedService,
    CompanySVWService,
    CompanyWageComponentVarService,
    CompanyWageCostService,
    CompanyWageModelService,
    CompanyWageTaxService,
)
from .service import Service
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list
from ..data_classes.company import Company, Period, ContactPerson, GuidConvertor


class CompanyService(Service):
    """
    A class representing Company Service for interacting with Nmbrs company-related functionalities.

    Not implemented calls:
        - [DefaultEmployeeTemplates_GetByCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=DefaultEmployeeTemplates_GetByCompany)
        - [FileExplorer_UploadFile](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=FileExplorer_UploadFile)
        - [HrDocuments_EmployerCostPerHour_Year](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HrDocuments_EmployerCostPerHour_Year)
        - [PayrollWorkflow_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PayrollWorkflow_Get)
        - [Schedule_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Schedule_GetCurrent)
        - [CompanyLeaveTypeGroups_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=CompanyLeaveTypeGroups_Get)
    """

    def __init__(self, sandbox: bool = True) -> None:
        """
        Constructor method for CompanyService class.

        Args:
            sandbox (bool (optional)): A boolean indicating whether to use the sandbox environment (default: True).
        """
        super().__init__(sandbox)

        # Initialize nmbrs client
        self.company_service = Client(f"{self.base_uri}{self.company_uri}")

        # Micro services
        self.address = CompanyAddressService(self.company_service)
        self.bank_account = CompanyBankAccountService(self.company_service)
        self.cost_center = CompanyCostCenterService(self.company_service)
        self.cost_unit = CompanyCostUnitService(self.company_service)
        self.hour_model = CompanyHourModelService(self.company_service)
        self.journal = CompanyJournalService(self.company_service)
        self.labour_agreement = CompanyLabourAgreementService(self.company_service)
        self.pension = CompanyPensionService(self.company_service)
        self.reports = CompanyReportService(self.company_service)
        self.run = CompanyRunService(self.company_service)
        self.salary_documents = CompanySalaryDocumentService(self.company_service)
        self.salary_table = CompanySalaryTableService(self.company_service)
        self.svw = CompanySVWService(self.company_service)
        self.wage_component_fixed = CompanyWageComponentFixedService(self.company_service)
        self.wage_component_var = CompanyWageComponentVarService(self.company_service)
        self.wage_cost = CompanyWageCostService(self.company_service)
        self.wage_model = CompanyWageModelService(self.company_service)
        self.wage_tax = CompanyWageTaxService(self.company_service)

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
             auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

        self.address.set_auth_header(auth_header)
        self.bank_account.set_auth_header(auth_header)
        self.cost_center.set_auth_header(auth_header)
        self.cost_unit.set_auth_header(auth_header)
        self.hour_model.set_auth_header(auth_header)
        self.journal.set_auth_header(auth_header)
        self.labour_agreement.set_auth_header(auth_header)
        self.pension.set_auth_header(auth_header)
        self.reports.set_auth_header(auth_header)
        self.run.set_auth_header(auth_header)
        self.salary_documents.set_auth_header(auth_header)
        self.salary_table.set_auth_header(auth_header)
        self.svw.set_auth_header(auth_header)
        self.wage_component_fixed.set_auth_header(auth_header)
        self.wage_component_var.set_auth_header(auth_header)
        self.wage_cost.set_auth_header(auth_header)
        self.wage_model.set_auth_header(auth_header)
        self.wage_tax.set_auth_header(auth_header)

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:List_GetAll"])
    def get_all(self) -> list[Company]:
        """
        Retrieve all companies.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetAll)

        Returns:
            list[Company]: A list of Company objects.
        """
        companies = self.company_service.service.List_GetAll(_soapheaders=self.auth_header)
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:List_GetByDebtor"])
    def get_by_debtor(self, debtor_id: int) -> list[Company]:
        """
        Get all the companies belonging to a debtor.

        For more information, refer to the official documentation:
            [Soap call List_GetByDebtor](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetByDebtor)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[Company]: A list of Company objects.
        """
        companies = self.company_service.service.List_GetByDebtor(DebtorId=debtor_id, _soapheaders=self.auth_header)
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @nmbrs_exception_handler(resources=["CompanyService:Company_GetCurrentByEmployeeId"])
    def get_by_employee(self, employee_id: int) -> Company | None:
        """
        Get company by employee id.

        For more information, refer to the official documentation:
            [Company_GetCurrentByEmployeeId](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_GetCurrentByEmployeeId)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Company: A list of Company objects.
        """
        company = self.company_service.service.Company_GetCurrentByEmployeeId(EmployeeId=employee_id, _soapheaders=self.auth_header)
        if company is None:
            return None
        return Company(serialize_object(company))

    @nmbrs_exception_handler(resources=["CompanyService:Company_GetCurrentPeriod"])
    def get_current_period(self, company_id: int) -> Period | None:
        """
        Get the current period of the company.

        For more information, refer to the official documentation:
            [Soap call Company_GetCurrentPeriod](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_GetCurrentPeriod)

        Args:
            company_id (int): The ID of the company.

        Returns:
            Period: year, period and period type and the company.
        """
        period = self.company_service.service.Company_GetCurrentPeriod(CompanyId=company_id, _soapheaders=self.auth_header)
        if period is None:
            return None
        return Period(serialize_object(period))

    @nmbrs_exception_handler(resources=["CompanyService:Company_Insert"])
    def insert(
        self, debtor_id: int, name: str, period_type: int, default_id: int, labour_agreement_group_id: str, pay_in_advance: bool
    ) -> int:
        """
        Insert a new company.

        This method inserts a new debtor with the provided details into the Nmbrs system.

        For more information, refer to the official documentation:
            [Company_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Company_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            name (str): The name of the debtor.
            period_type (int): The period type.
            default_id (int): The default company ID.
            labour_agreement_group_id (str): The GUID of the labour agreement group.
            pay_in_advance (bool): Indicates whether payments are made in advance.

        Returns:
            int: The ID of the inserted debtor if successful.
        """
        inserted = self.company_service.service.Company_Insert(
            DebtorId=debtor_id,
            CompanyName=name,
            PeriodType=period_type,
            DefaultCompanyId=default_id,
            LabourAgreementSettingsGroupGuid=labour_agreement_group_id,
            PayInAdvance=pay_in_advance,
            _soapheaders=self.auth_header,
        )
        return inserted

    @nmbrs_exception_handler(resources=["CompanyService:ContactPerson_Get"])
    def get_contact_person(self, company_id: int) -> ContactPerson:
        """
        Get contact person by company ID.

        For more information, refer to the official documentation:
            [ContactPerson_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=ContactPerson_Get)

        Args:
            company_id (int): The ID of the company.

        Returns:
            ContactPerson: The contact person details.
        """
        contact_person = self.company_service.service.ContactPerson_Get(CompanyId=company_id, _soapheaders=self.auth_header)
        return ContactPerson(serialize_object(contact_person))

    @nmbrs_exception_handler(resources=["CompanyService:Converter_GetByCompany_IntToGuid"])
    def get_converter_mappings(self, company_id: int, entity: str) -> GuidConvertor:
        """
        Get converter mappings for the given entity and company ID.

        For more information, refer to the official documentation:
            [Converter_GetByCompany_IntToGuid](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Converter_GetByCompany_IntToGuid)

        Args:
            company_id (int): The ID of the company.
            entity (str): The entity type (e.g., Employee, Company, Debtor).

        Returns:
            GuidConvertor: The converter mappings response.
        """
        guids = self.company_service.service.Converter_GetByCompany_IntToGuid(
            Entity=entity, CompanyId=company_id, _soapheaders=self.auth_header
        )
        return GuidConvertor(serialize_object(guids))
