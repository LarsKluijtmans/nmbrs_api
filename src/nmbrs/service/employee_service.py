# pylint: disable=line-too-long
"""
Module for handling the Employee Nmbrs services.
"""
from zeep import Client

from .microservices.employee import (
    EmployeeWageTaxService,
    EmployeeWageComponentsService,
    EmployeeAbsenceService,
    EmployeeAddressService,
    EmployeeBankAccountService,
    EmployeeChildService,
    EmployeeContractService,
    EmployeeCostCenterService,
    EmployeeDaysService,
    EmployeeDocumentService,
    EmployeeDepartmentsService,
    EmployeeEmploymentService,
    EmployeeFunctionService,
    EmployeeHourComponentFixedService,
    EmployeeLabourAgreementService,
    EmployeeLeaseCarService,
    EmployeeLeaveService,
    EmployeeLevensLoopService,
    EmployeePartnerService,
    EmployeeManagerService,
    EmployeePersonalInfoService,
    EmployeeSalaryService,
    EmployeeScheduleService,
    EmployeeServiceService,
    EmployeeSpaarloonService,
    EmployeeSvwService,
    EmployeeTimeRegistrationService,
    EmployeeTimeScheduleService,
)
from .service import Service
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeService(Service):
    """A class representing Employee Service for interacting with Nmbrs employee-related functionalities."""

    def __init__(self, sandbox: bool = True) -> None:
        super().__init__(sandbox)

        # Initialize nmbrs services
        self.employee_service = Client(f"{self.base_uri}{self.employee_uri}")

        # Micro services
        self.absence = EmployeeAbsenceService(self.employee_service)
        self.address = EmployeeAddressService(self.employee_service)
        self.bank_account = EmployeeBankAccountService(self.employee_service)
        self.child = EmployeeChildService(self.employee_service)
        self.contract = EmployeeContractService(self.employee_service)
        self.cost_center = EmployeeCostCenterService(self.employee_service)
        self.days = EmployeeDaysService(self.employee_service)
        self.department = EmployeeDepartmentsService(self.employee_service)
        self.document = EmployeeDocumentService(self.employee_service)
        self.employment = EmployeeEmploymentService(self.employee_service)
        self.function = EmployeeFunctionService(self.employee_service)
        self.hour_component = EmployeeHourComponentFixedService(self.employee_service)
        self.labour_agreement = EmployeeLabourAgreementService(self.employee_service)
        self.lease_car = EmployeeLeaseCarService(self.employee_service)
        self.leave = EmployeeLeaveService(self.employee_service)
        self.levensloop = EmployeeLevensLoopService(self.employee_service)
        self.manager = EmployeeManagerService(self.employee_service)
        self.partner = EmployeePartnerService(self.employee_service)
        self.personal_info = EmployeePersonalInfoService(self.employee_service)
        self.salary = EmployeeSalaryService(self.employee_service)
        self.schedule = EmployeeScheduleService(self.employee_service)
        self.service = EmployeeServiceService(self.employee_service)
        self.spaarloon = EmployeeSpaarloonService(self.employee_service)
        self.svw = EmployeeSvwService(self.employee_service)
        self.time_registration = EmployeeTimeRegistrationService(self.employee_service)
        self.time_schedule = EmployeeTimeScheduleService(self.employee_service)
        self.wage_component = EmployeeWageComponentsService(self.employee_service)
        self.wage_tax = EmployeeWageTaxService(self.employee_service)

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

        # Micro services
        self.absence.set_auth_header(auth_header)
        self.address.set_auth_header(auth_header)
        self.bank_account.set_auth_header(auth_header)
        self.child.set_auth_header(auth_header)
        self.contract.set_auth_header(auth_header)
        self.cost_center.set_auth_header(auth_header)
        self.days.set_auth_header(auth_header)
        self.department.set_auth_header(auth_header)
        self.document.set_auth_header(auth_header)
        self.employment.set_auth_header(auth_header)
        self.function.set_auth_header(auth_header)
        self.hour_component.set_auth_header(auth_header)
        self.labour_agreement.set_auth_header(auth_header)
        self.lease_car.set_auth_header(auth_header)
        self.leave.set_auth_header(auth_header)
        self.levensloop.set_auth_header(auth_header)
        self.manager.set_auth_header(auth_header)
        self.partner.set_auth_header(auth_header)
        self.personal_info.set_auth_header(auth_header)
        self.salary.set_auth_header(auth_header)
        self.schedule.set_auth_header(auth_header)
        self.service.set_auth_header(auth_header)
        self.spaarloon.set_auth_header(auth_header)
        self.svw.set_auth_header(auth_header)
        self.time_registration.set_auth_header(auth_header)
        self.time_schedule.set_auth_header(auth_header)
        self.wage_component.set_auth_header(auth_header)
        self.wage_tax.set_auth_header(auth_header)

    @nmbrs_exception_handler(resources=["EmployeeService:EmployeeType_GetList"])
    def get_types(self):
        """
        Get the list of all employee types available.

        For more information, refer to the official documentation:
            [Address_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeType_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employee_GetCurrent"])
    def get_current_period(self):
        """
        Get the employees current period, Format = yyyy-pp-type, example: 2010-5-M or 2010-4-4W.

        For more information, refer to the official documentation:
            [Address_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:List_GetByCompany"])
    def get_by_company(self):
        """
        Get all employees that belong to a company and to a specific employee type.

        For more information, refer to the official documentation:
            [Address_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:List_GetByDebtor"])
    def get_by_debtor(self):
        """
        Get all employees that belong to a debtor and to a specific employee type.

        For more information, refer to the official documentation:
            [List_GetByDebtor](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByDebtor)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employee_Insert"])
    def insert(self):
        """
        Create a new Employee, returns the id of this Employee.
        If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employee_InsertBasedOnDefault"])
    def insert_based_on_default(self):
        """
        Insert new employee based on default employee.
        If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_InsertBasedOnDefault](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertBasedOnDefault)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employee_InsertByEmployeeType"])
    def insert_with_type(self):
        """
        Create a new employee based on the employee type and returns the Id of this employee.
        If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_InsertByEmployeeType](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertByEmployeeType)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Employee_Transition"])
    def transition(self):
        """
        Transition employee to a different employee type. For example, from applicant to new hire. Or from new hire to payroll.

        For more information, refer to the official documentation:
            [Employee_Transition](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Transition)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:EndServiceReason_GetList"])
    def get_all_end_service_reasons(self):
        """
        Get all End Service Reasons.

        For more information, refer to the official documentation:
            [EndServiceReason_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:EndServiceReason_GetListByYear"])
    def get_all_end_service_reasons_by_year(self):
        """
        Get all End Service Reasons of given year.

        For more information, refer to the official documentation:
            [EndServiceReason_GetListByYear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetListByYear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:ExtraFieldsWithStartDate_GetList"])
    def get_extra_fields_with_start_date(self):
        """
        Get employee extra fields list, including the ones of type Text+Date.

        For more information, refer to the official documentation:
            [ExtraFieldsWithStartDate_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFieldsWithStartDate_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:ExtraFields_GetList"])
    def get_extra_fields(self):
        """
        Get employee extra fields list.

        For more information, refer to the official documentation:
            [ExtraFields_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFields_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PerformanceReview_Get"])
    def get_performance(self):
        """
        Get the HR Performance Review for the given Employee ID.

        For more information, refer to the official documentation:
            [PerformanceReview_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PerformanceReview_GetAll_AllEmployeesByCompany"])
    def get_all_performance_by_company(self):
        """
        Get the HR Performance Reviews for all the employees in the given Company ID.

        For more information, refer to the official documentation:
            [PerformanceReview_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Reports_GetJournalsReportByEmployee"])
    def get_journal(self):
        """
        Returns the Journal Report for Employee.

        For more information, refer to the official documentation:
            [Reports_GetJournalsReportByEmployee](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reports_GetJournalsReportByEmployee)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Reservations_GetList"])
    def get_reservations(self):
        """
        Get the reservation items for the given employee.

        For more information, refer to the official documentation:
            [Reservations_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reservations_GetList)
        """
        raise NotImplementedError()  # pragma: no cover
