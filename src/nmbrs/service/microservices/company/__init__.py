"""This module provides access to all the company level microservices."""

from .address import CompanyAddressService
from .bank_account import CompanyBankAccountService
from .cost_center import CompanyCostCenterService
from .cost_unit import CompanyCostUnitService
from .hour_model import CompanyHourModelService
from .journal import CompanyJournalService
from .labout_aggreement import CompanyLabourAgreementService
from .pension import CompanyPensionService
from .report import CompanyReportService
from .run import CompanyRunService
from .salary_document import CompanySalaryDocumentService
from .salary_table import CompanySalaryTableService
from .svw import CompanySVWService
from .wage_component_fixed import CompanyWageComponentFixedService
from .wage_component_var import CompanyWageComponentVarService
from .wage_cost import CompanyWageCostService
from .wage_model import CompanyWageModelService
from .wage_tax import CompanyWageTaxService
