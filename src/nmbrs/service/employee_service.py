"""
Module for handling the Employee Nmbrs services.
"""

import logging

from zeep import Client
from zeep.helpers import serialize_object

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
from ..auth.token_manager import AuthManager
from ..data_classes.employee import EmployeeTypes, Employee, Period
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler
from ..utils.return_list import return_list


logger = logging.getLogger(__name__)


class EmployeeService(Service):
    """A class representing Employee Service for interacting with Nmbrs employee-related functionalities."""

    def __init__(self, auth_manager: AuthManager, sandbox: bool = True):
        super().__init__(auth_manager, sandbox)

        # Initialize nmbrs services
        self.client = Client(f"{self.base_uri}{self.employee_uri}")

        # Micro services
        self._absence = None
        self._address = None
        self._bank_account = None
        self._child = None
        self._contract = None
        self._cost_center = None
        self._days = None
        self._department = None
        self._document = None
        self._employment = None
        self._function = None
        self._hour_component = None
        self._labour_agreement = None
        self._lease_car = None
        self._leave = None
        self._levensloop = None
        self._manager = None
        self._partner = None
        self._personal_info = None
        self._salary = None
        self._schedule = None
        self._service = None
        self._spaarloon = None
        self._svw = None
        self._time_registration = None
        self._time_schedule = None
        self._wage_component = None
        self._wage_tax = None

        logger.info("EmployeeService initialized.")

    @property
    def absence(self):
        """
        Lazily initializes and returns the EmployeeAbsenceService instance.
        """
        if self._absence is None:
            self._absence = EmployeeAbsenceService(self.auth_manager, self.client)
        return self._absence

    @property
    def address(self):
        """
        Lazily initializes and returns the EmployeeAddressService instance.
        """
        if self._address is None:
            self._address = EmployeeAddressService(self.auth_manager, self.client)
        return self._address

    @property
    def bank_account(self):
        """
        Lazily initializes and returns the EmployeeBankAccountService instance.
        """
        if self._bank_account is None:
            self._bank_account = EmployeeBankAccountService(self.auth_manager, self.client)
        return self._bank_account

    @property
    def child(self):
        """
        Lazily initializes and returns the EmployeeChildService instance.
        """
        if self._child is None:
            self._child = EmployeeChildService(self.auth_manager, self.client)
        return self._child

    @property
    def contract(self):
        """
        Lazily initializes and returns the EmployeeContractService instance.
        """
        if self._contract is None:
            self._contract = EmployeeContractService(self.auth_manager, self.client)
        return self._contract

    @property
    def cost_center(self):
        """
        Lazily initializes and returns the EmployeeCostCenterService instance.
        """
        if self._cost_center is None:
            self._cost_center = EmployeeCostCenterService(self.auth_manager, self.client)
        return self._cost_center

    @property
    def days(self):
        """
        Lazily initializes and returns the EmployeeDaysService instance.
        """
        if self._days is None:
            self._days = EmployeeDaysService(self.auth_manager, self.client)
        return self._days

    @property
    def department(self):
        """
        Lazily initializes and returns the EmployeeDepartmentsService instance.
        """
        if self._department is None:
            self._department = EmployeeDepartmentsService(self.auth_manager, self.client)
        return self._department

    @property
    def document(self):
        """
        Lazily initializes and returns the EmployeeDocumentService instance.
        """
        if self._document is None:
            self._document = EmployeeDocumentService(self.auth_manager, self.client)
        return self._document

    @property
    def employment(self):
        """
        Lazily initializes and returns the EmployeeEmploymentService instance.
        """
        if self._employment is None:
            self._employment = EmployeeEmploymentService(self.auth_manager, self.client)
        return self._employment

    @property
    def function(self):
        """
        Lazily initializes and returns the EmployeeFunctionService instance.
        """
        if self._function is None:
            self._function = EmployeeFunctionService(self.auth_manager, self.client)
        return self._function

    @property
    def hour_component(self):
        """
        Lazily initializes and returns the EmployeeHourComponentFixedService instance.
        """
        if self._hour_component is None:
            self._hour_component = EmployeeHourComponentFixedService(self.auth_manager, self.client)
        return self._hour_component

    @property
    def labour_agreement(self):
        """
        Lazily initializes and returns the EmployeeLabourAgreementService instance.
        """
        if self._labour_agreement is None:
            self._labour_agreement = EmployeeLabourAgreementService(self.auth_manager, self.client)
        return self._labour_agreement

    @property
    def lease_car(self):
        """
        Lazily initializes and returns the EmployeeLeaseCarService instance.
        """
        if self._lease_car is None:
            self._lease_car = EmployeeLeaseCarService(self.auth_manager, self.client)
        return self._lease_car

    @property
    def leave(self):
        """
        Lazily initializes and returns the EmployeeLeaveService instance.
        """
        if self._leave is None:
            self._leave = EmployeeLeaveService(self.auth_manager, self.client)
        return self._leave

    @property
    def levensloop(self):
        """
        Lazily initializes and returns the EmployeeLevensLoopService instance.
        """
        if self._levensloop is None:
            self._levensloop = EmployeeLevensLoopService(self.auth_manager, self.client)
        return self._levensloop

    @property
    def manager(self):
        """
        Lazily initializes and returns the EmployeeManagerService instance.
        """
        if self._manager is None:
            self._manager = EmployeeManagerService(self.auth_manager, self.client)
        return self._manager

    @property
    def partner(self):
        """
        Lazily initializes and returns the EmployeePartnerService instance.
        """
        if self._partner is None:
            self._partner = EmployeePartnerService(self.auth_manager, self.client)
        return self._partner

    @property
    def personal_info(self):
        """
        Lazily initializes and returns the EmployeePersonalInfoService instance.
        """
        if self._personal_info is None:
            self._personal_info = EmployeePersonalInfoService(self.auth_manager, self.client)
        return self._personal_info

    @property
    def salary(self):
        """
        Lazily initializes and returns the EmployeeSalaryService instance.
        """
        if self._salary is None:
            self._salary = EmployeeSalaryService(self.auth_manager, self.client)
        return self._salary

    @property
    def schedule(self):
        """
        Lazily initializes and returns the EmployeeScheduleService instance.
        """
        if self._schedule is None:
            self._schedule = EmployeeScheduleService(self.auth_manager, self.client)
        return self._schedule

    @property
    def service(self):
        """
        Lazily initializes and returns the EmployeeServiceService instance.
        """
        if self._service is None:
            self._service = EmployeeServiceService(self.auth_manager, self.client)
        return self._service

    @property
    def spaarloon(self):
        """
        Lazily initializes and returns the EmployeeSpaarloonService instance.
        """
        if self._spaarloon is None:
            self._spaarloon = EmployeeSpaarloonService(self.auth_manager, self.client)
        return self._spaarloon

    @property
    def svw(self):
        """
        Lazily initializes and returns the EmployeePartnerService instance.
        """
        if self._svw is None:
            self._svw = EmployeeSvwService(self.auth_manager, self.client)
        return self._svw

    @property
    def time_registration(self):
        """
        Lazily initializes and returns the EmployeeTimeRegistrationService instance.
        """
        if self._time_registration is None:
            self._time_registration = EmployeeTimeRegistrationService(self.auth_manager, self.client)
        return self._time_registration

    @property
    def time_schedule(self):
        """
        Lazily initializes and returns the EmployeeTimeScheduleService instance.
        """
        if self._time_schedule is None:
            self._time_schedule = EmployeeTimeScheduleService(self.auth_manager, self.client)
        return self._time_schedule

    @property
    def wage_component(self):
        """
        Lazily initializes and returns the EmployeeWageComponentsService instance.
        """
        if self._wage_component is None:
            self._wage_component = EmployeeWageComponentsService(self.auth_manager, self.client)
        return self._wage_component

    @property
    def wage_tax(self):
        """
        Lazily initializes and returns the EmployeeWageTaxService instance.
        """
        if self._wage_tax is None:
            self._wage_tax = EmployeeWageTaxService(self.auth_manager, self.client)
        return self._wage_tax

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:EmployeeType_GetList")
    def get_types(self) -> list[EmployeeTypes]:
        """
        Get the list of all employee types available.

        For more information, refer to the official documentation:
            [EmployeeType_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeType_GetList)

        Returns:
            list[EmployeeTypes]: A list of employee type objects.
        """
        employee_types = self.client.service.EmployeeType_GetList(_soapheaders=self.auth_manager.header)
        employee_types = [EmployeeTypes(employee_type) for employee_type in serialize_object(employee_types)]
        return employee_types

    @nmbrs_exception_handler(resource="EmployeeService:Employee_GetCurrent")
    def get_current_period(self, employee_id: int) -> Period | None:
        """
        Get the employees current period, Format = yyyy-pp-type, example: 2010-5-M or 2010-4-4W.

        For more information, refer to the official documentation:
            [Employee_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            Period: year, period and period type and the company.
        """
        period = self.client.service.Employee_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        if period is None:
            logger.debug("No current period found for employee, ID: %s.", employee_id)
            return None
        return Period(employee_id=employee_id, data=serialize_object(period))

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:List_GetByCompany")
    def get_by_company(self, company_id: int, employee_type: int) -> list[Employee]:
        """
        Get all employees that belong to a company and to a specific employee type.

        For more information, refer to the official documentation:
            [List_GetByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByCompany)

        Args:
            company_id (int): The ID of the company.
            employee_type (int): The type of employees to be returned.

        Returns:
            list[Employee]: A list of employee objects.
        """
        employees = self.client.service.List_GetByCompany(
            CompanyId=company_id, EmployeeType=employee_type, _soapheaders=self.auth_manager.header
        )
        employees = [Employee(employee) for employee in serialize_object(employees)]
        return employees

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:List_GetByDebtor")
    def get_by_debtor(self, debtor_id: int, employee_type: int) -> list[Employee]:
        """
        Get all employees that belong to a debtor and to a specific employee type.

        For more information, refer to the official documentation:
            [List_GetByDebtor](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByDebtor)

        Args:
            debtor_id (int): The ID of the company.
            employee_type (int): The type of employees to be returned.

        Returns:
            list[Employee]: A list of employee objects.
        """
        employees = self.client.service.List_GetByDebtor(
            DebtorId=debtor_id, EmployeeType=employee_type, _soapheaders=self.auth_manager.header
        )
        employees = [Employee(employee) for employee in serialize_object(employees)]
        return employees

    @nmbrs_exception_handler(resource="EmployeeService:Employee_Insert")
    def post(self):
        """
        Create a new Employee, returns the id of this Employee.
        If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Employee_InsertBasedOnDefault")
    def post_based_on_default(self):
        """
        Insert new employee based on default employee.
        If the date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_InsertBasedOnDefault](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertBasedOnDefault)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Employee_InsertByEmployeeType")
    def post_with_type(self):
        """
        Create a new employee based on the employee type and returns the Id of this employee.
        If the date is before th
        e company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Employee_InsertByEmployeeType](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertByEmployeeType)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Employee_Transition")
    def transition(self):
        """
        Transition employee to a different employee type. For example, from applicant to new hire. Or from new hire to payroll.

        For more information, refer to the official documentation:
            [Employee_Transition](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Transition)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:EndServiceReason_GetList")
    def get_all_end_service_reasons(self):
        """
        Get all End Service Reasons.

        For more information, refer to the official documentation:
            [EndServiceReason_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:EndServiceReason_GetListByYear")
    def get_all_end_service_reasons_by_year(self):
        """
        Get all End Service Reasons of given year.

        For more information, refer to the official documentation:
            [EndServiceReason_GetListByYear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetListByYear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:ExtraFieldsWithStartDate_GetList")
    def get_extra_fields_with_start_date(self):
        """
        Get employee extra fields list, including the ones of type Text+Date.

        For more information, refer to the official documentation:
            [ExtraFieldsWithStartDate_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFieldsWithStartDate_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:ExtraFields_GetList")
    def get_extra_fields(self):
        """
        Get employee extra fields list.

        For more information, refer to the official documentation:
            [ExtraFields_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFields_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:PerformanceReview_Get")
    def get_performance_reviews(self):
        """
        Get the HR Performance Review for the given Employee ID.

        For more information, refer to the official documentation:
            [PerformanceReview_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:PerformanceReview_GetAll_AllEmployeesByCompany")
    def get_all_performance_review_by_company(self):
        """
        Get the HR Performance Reviews for all the employees in the given Company ID.

        For more information, refer to the official documentation:
            [PerformanceReview_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_GetAll_AllEmployeesByCompany)  # pylint: disable=line-too-long
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Reports_GetJournalsReportByEmployee")
    def get_journal(self):
        """
        Returns the Journal Report for Employee.

        For more information, refer to the official documentation:
            [Reports_GetJournalsReportByEmployee](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reports_GetJournalsReportByEmployee)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Reservations_GetList")
    def get_reservations(self):
        """
        Get the reservation items for the given employee.

        For more information, refer to the official documentation:
            [Reservations_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reservations_GetList)
        """
        raise NotImplementedError()  # pragma: no cover
