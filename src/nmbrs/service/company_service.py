"""Module for handling the Company Nmbrs services."""

import logging

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
    CompanyRunService,
    CompanySalaryDocumentService,
    CompanySalaryTableService,
    CompanyWageComponentService,
    CompanySvwService,
    CompanyWageCostService,
    CompanyWageModelService,
    CompanyWageTaxService,
)
from .service import Service
from ..auth.token_manager import AuthManager
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list
from ..data_classes.company import (
    Company,
    Period,
    ContactPerson,
    GuidConvertor,
    DefaultEmployeeTemplate,
    FulltimeSchedules,
    PayrollWorkflowTrack,
)

logger = logging.getLogger(__name__)


class CompanyService(Service):
    """A class representing Company Service for interacting with Nmbrs company-related functionalities."""

    def __init__(self, auth_manager: AuthManager, sandbox: bool = True):
        super().__init__(auth_manager, sandbox)

        # Initialize nmbrs client
        self.client = Client(f"{self.base_uri}{self.company_uri}")

        # Micro services
        self._address = None
        self._bank_account = None
        self._cost_center = None
        self._cost_unit = None
        self._hour_model = None
        self._journal = None
        self._labour_agreement = None
        self._pension = None
        self._run = None
        self._salary_documents = None
        self._salary_table = None
        self._svw = None
        self._wage_component = None
        self._wage_cost = None
        self._wage_model = None
        self._wage_tax = None

        logger.info("CompanyService initialized.")

    @property
    def address(self):
        """
        Lazily initializes and returns the CompanyAddressService instance.
        """
        if self._address is None:
            self._address = CompanyAddressService(self.auth_manager, self.client)
        return self._address

    @property
    def bank_account(self):
        """
        Lazily initializes and returns the CompanyBankAccountService instance.
        """
        if self._bank_account is None:
            self._bank_account = CompanyBankAccountService(self.auth_manager, self.client)
        return self._bank_account

    @property
    def cost_center(self):
        """
        Lazily initializes and returns the CompanyCostCenterService instance.
        """
        if self._cost_center is None:
            self._cost_center = CompanyCostCenterService(self.auth_manager, self.client)
        return self._cost_center

    @property
    def cost_unit(self):
        """
        Lazily initializes and returns the CompanyCostUnitService instance.
        """
        if self._cost_unit is None:
            self._cost_unit = CompanyCostUnitService(self.auth_manager, self.client)
        return self._cost_unit

    @property
    def hour_model(self):
        """
        Lazily initializes and returns the CompanyHourModelService instance.
        """
        if self._hour_model is None:
            self._hour_model = CompanyHourModelService(self.auth_manager, self.client)
        return self._hour_model

    @property
    def journal(self):
        """
        Lazily initializes and returns the CompanyJournalService instance.
        """
        if self._journal is None:
            self._journal = CompanyJournalService(self.auth_manager, self.client)
        return self._journal

    @property
    def labour_agreement(self):
        """
        Lazily initializes and returns the CompanyLabourAgreementService instance.
        """
        if self._labour_agreement is None:
            self._labour_agreement = CompanyLabourAgreementService(self.auth_manager, self.client)
        return self._labour_agreement

    @property
    def pension(self):
        """
        Lazily initializes and returns the CompanyPensionService instance.
        """
        if self._pension is None:
            self._pension = CompanyPensionService(self.auth_manager, self.client)
        return self._pension

    @property
    def run(self):
        """
        Lazily initializes and returns the CompanyRunService instance.
        """
        if self._run is None:
            self._run = CompanyRunService(self.auth_manager, self.client)
        return self._run

    @property
    def salary_documents(self):
        """
        Lazily initializes and returns the CompanySalaryDocumentService instance.
        """
        if self._salary_documents is None:
            self._salary_documents = CompanySalaryDocumentService(self.auth_manager, self.client)
        return self._salary_documents

    @property
    def salary_table(self):
        """
        Lazily initializes and returns the CompanySalaryTableService instance.
        """
        if self._salary_table is None:
            self._salary_table = CompanySalaryTableService(self.auth_manager, self.client)
        return self._salary_table

    @property
    def svw(self):
        """
        Lazily initializes and returns the CompanySvwService instance.
        """
        if self._svw is None:
            self._svw = CompanySvwService(self.auth_manager, self.client)
        return self._svw

    @property
    def wage_component(self):
        """
        Lazily initializes and returns the CompanyWageComponentService instance.
        """
        if self._wage_component is None:
            self._wage_component = CompanyWageComponentService(self.auth_manager, self.client)
        return self._wage_component

    @property
    def wage_cost(self):
        """
        Lazily initializes and returns the CompanyWageCostService instance.
        """
        if self._wage_cost is None:
            self._wage_cost = CompanyWageCostService(self.auth_manager, self.client)
        return self._wage_cost

    @property
    def wage_model(self):
        """
        Lazily initializes and returns the CompanyWageModelService instance.
        """
        if self._wage_model is None:
            self._wage_model = CompanyWageModelService(self.auth_manager, self.client)
        return self._wage_model

    @property
    def wage_tax(self):
        """
        Lazily initializes and returns the CompanyWageTaxService instance.
        """
        if self._wage_tax is None:
            self._wage_tax = CompanyWageTaxService(self.auth_manager, self.client)
        return self._wage_tax

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:List_GetAll")
    def get_all(self) -> list[Company]:
        """
        Retrieve all companies.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=List_GetAll)

        Returns:
            list[Company]: A list of Company objects.
        """
        companies = self.client.service.List_GetAll(_soapheaders=self.auth_manager.header)
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:List_GetByDebtor")
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
        companies = self.client.service.List_GetByDebtor(DebtorId=debtor_id, _soapheaders=self.auth_manager.header)
        companies = [Company(company) for company in serialize_object(companies)]
        return companies

    @nmbrs_exception_handler(resource="CompanyService:Company_GetCurrentByEmployeeId")
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
        company = self.client.service.Company_GetCurrentByEmployeeId(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        if company is None:
            logger.debug("No company found, for employee, ID: %s.", employee_id)
            return None
        return Company(serialize_object(company))

    @nmbrs_exception_handler(resource="CompanyService:Company_GetCurrentPeriod")
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
        period = self.client.service.Company_GetCurrentPeriod(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        if period is None:
            logger.debug("No current period found, for company, ID: %s.", company_id)
            return None
        return Period(company_id=company_id, data=serialize_object(period))

    @nmbrs_exception_handler(resource="CompanyService:Company_Insert")
    def post(
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
        inserted = self.client.service.Company_Insert(
            DebtorId=debtor_id,
            CompanyName=name,
            PeriodType=period_type,
            DefaultCompanyId=default_id,
            LabourAgreementSettingsGroupGuid=labour_agreement_group_id,
            PayInAdvance=pay_in_advance,
            _soapheaders=self.auth_manager.header,
        )
        return inserted

    @nmbrs_exception_handler(resource="CompanyService:ContactPerson_Get")
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
        contact_person = self.client.service.ContactPerson_Get(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        return ContactPerson(company_id=company_id, data=serialize_object(contact_person))

    @nmbrs_exception_handler(resource="CompanyService:Converter_GetByCompany_IntToGuid")
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
        guids = self.client.service.Converter_GetByCompany_IntToGuid(
            Entity=entity, CompanyId=company_id, _soapheaders=self.auth_manager.header
        )
        return GuidConvertor(company_id=company_id, data=serialize_object(guids))

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:DefaultEmployeeTemplates_GetByCompany")
    def get_default_employee_templates(self, company_id: int) -> list[DefaultEmployeeTemplate]:
        """
        Get available default employee templates by company.

        For more information, refer to the official documentation:
            [Converter_GetByCompany_IntToGuid](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=DefaultEmployeeTemplates_GetByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Company]: A list of Company objects.
        """
        employee_templates = self.client.service.DefaultEmployeeTemplates_GetByCompany(
            CompanyId=company_id, _soapheaders=self.auth_manager.header
        )
        employee_templates = [
            DefaultEmployeeTemplate(company_id=company_id, data=employee_template)
            for employee_template in serialize_object(employee_templates)
        ]
        return employee_templates

    @nmbrs_exception_handler(resource="CompanyService:FileExplorer_UploadFile")
    def upload_file(self, company_id: int, document_name: str, document_sub_folder: str, data: bytes) -> None:
        """
        Upload a document for a company.

        For further details, see the official documentation:
            [FileExplorer_UploadFile](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=FileExplorer_UploadFile)

        Args:
            company_id (int): The ID of the company.
            document_name (str): The name of the document.
            document_sub_folder (str): The subfolder in which the document will be uploaded.
            data (bytes): The data of the document.

        Returns:
            None
        """
        self.client.service.FileExplorer_UploadFile(
            **{
                "CompanyId": company_id,
                "StrDocumentName": document_name,
                "StrDocumentSubFolder": document_sub_folder,
                "Body": data,
            },
            _soapheaders=self.auth_manager.header,
        )

    @nmbrs_exception_handler(resource="CompanyService:Schedule_GetCurrent")
    def get_current_schedule(self, company_id: int) -> FulltimeSchedules:
        """
        Retrieve the current schedules for a company.

        For further details, see the official documentation:
            [Schedule_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Schedule_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            FulltimeSchedules: A FulltimeSchedules object.
        """
        response = self.client.service.Schedule_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        return FulltimeSchedules(company_id=company_id, data=serialize_object(response))

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:PayrollWorkflow_Get")
    def get_payroll_workflows(self, company_id: int, period: int, year: int) -> list[PayrollWorkflowTrack]:
        """
        Get the company's payroll workflow tracks and actions.

        For further details, see the official documentation:
            [PayrollWorkflow_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=PayrollWorkflow_Get)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.

        Returns:
            List[PayrollWorkflowTrack]: A list of PayrollWorkflowTrack objects.
        """
        responses = self.client.service.PayrollWorkflow_Get(
            CompanyId=company_id, Year=year, Period=period, _soapheaders=self.auth_manager.header
        )
        responses = [PayrollWorkflowTrack(company_id=company_id, data=response) for response in serialize_object(responses)]
        return responses
