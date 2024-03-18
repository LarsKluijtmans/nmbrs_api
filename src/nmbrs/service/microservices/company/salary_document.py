# pylint: disable=line-too-long
"""Microservice responsible for salary documents related actions on the company level."""
from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanySalaryDocumentService(MicroService):
    """Microservice responsible for salary documents related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_AnualStatement"])
    def get_annual_statement(self):
        """
        Get Annual Statement in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_AnualStatement](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_AnualStatement)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative"])
    def get_annual_wage_components(self):
        """
        Get Annual Company Wage Components Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_CompanyWageComponentsCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative"])
    def get_annual_journal_entries_company(self):
        """
        Get Annual Journal Entries company Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCompanyrCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative"])
    def get_annual_journal_entries_cost_center(self):
        """
        Get Annual Journal Entries Cost Center Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesCostCenterCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative"])
    def get_annual_journal_entries_department(self):
        """
        Get Annual Journal Entries Department Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesDepartmentCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative"])
    def get_annual_journal_entries_employee(self):
        """
        Get Annual Journal Entries Employee Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_JournalEntriesEmployeeCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_LeaveSaldos"])
    def get_annual_leave_saldo(self):
        """
        Get Annual Leave Saldos in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_LeaveSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_LeaveSaldos)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_PaymentListCumulative"])
    def get_annual_payment_list(self):
        """
        Get Annual Payment List Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_PaymentListCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PaymentListCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_PayrollRegister"])
    def get_annual_payroll(self):
        """
        Get Annual Journal Entries Department Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_PayrollRegister](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegister)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees"])
    def get_annual_payroll_employees(self):
        """
        Get Annual PayrollRegister All Employee in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterAllEmployees)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative"])
    def get_annual_payroll_summary(self):
        """
        Get Annual Payroll Register Summary Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_PayrollRegisterSummaryCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_ReservationSaldos"])
    def get_annual_reservation_saldo(self):
        """
        Get Annual Reservation Saldo in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_ReservationSaldos](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_ReservationSaldos)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_SentWageTaxDeclarations"])
    def get_annual_wage_tax_declaration(self):
        """
        Get Annual Document Sent Wage Tax Declarations in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_SentWageTaxDeclarations](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_SentWageTaxDeclarations)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod"])
    def get_annual_wage_tax_declaration_by_period(self):
        """
        Get Annual Document WageTax Declaration Overview Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewByPeriod)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative"])
    def get_annual_wage_tax_declaration_cumulative(self):
        """
        Get Annual Document WageTax Declaration Overview Cumulative in PDF.

        For more information, refer to the official documentation:
            [SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_AnnualDocument_WageTaxDeclarationOverviewCumulative)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetAllPayslipsPDFByRunCompany"])
    def get_annual_all_payslips(self):
        """
        Get all payslip PDF's of a company for a specific run period, takes year from active year of the company.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetAllPayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2"])
    def get_annual_all_payslips_2(self):
        """
        Get all payslip PDF's of a company for a specific run period.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetAllPayslipsPDFByRunCompany_v2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany"])
    def get_annual_all_payslips_as_one(self):
        """
        Get all employees payslips in one PDF by run company for a specific run period.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsInOnePDFByRunCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetEmployeePayslipsPDFByRunCompany"])
    def get_annual_all_payslips_by_employee(self):
        """
        Get employee payslips in PDF by run company for a specific run period, takes year from active year of the company

        For more information, refer to the official documentation:
            [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2"])
    def get_annual_all_payslips_by_employee_2(self):
        """
        Get employee payslips in PDF by run company for a specific run period.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetEmployeePayslipsPDFByRunCompany_v2)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetSEPA"])
    def get_SEPA(self):
        """
        Get SEPA file.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetSEPA](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:SalaryDocuments_GetSEPA_Tax"])
    def get_SEPA_tax(self):
        """
        Get SEPA Tax file.

        For more information, refer to the official documentation:
            [SalaryDocuments_GetSEPA_Tax](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=SalaryDocuments_GetSEPA_Tax)
        """
        raise NotImplementedError()  # pragma: no cover
