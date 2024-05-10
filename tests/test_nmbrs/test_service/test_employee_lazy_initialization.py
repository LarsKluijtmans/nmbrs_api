"""Test cases for the EmployeeService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.employee_service import EmployeeService
from src.nmbrs.service.microservices.employee import (
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
    EmployeeManagerService,
    EmployeePartnerService,
    EmployeePersonalInfoService,
    EmployeeSalaryService,
    EmployeeScheduleService,
    EmployeeServiceService,
    EmployeeSpaarloonService,
    EmployeeSvwService,
    EmployeeTimeRegistrationService,
    EmployeeTimeScheduleService,
    EmployeeWageComponentsService,
    EmployeeWageTaxService,
)


class TestEmployeeService(unittest.TestCase):
    """Test cases for the EmployeeService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.client = Mock()
        self.employee_service = EmployeeService(self.auth_manager)

    def test_absence_lazy_initialization(self):
        """Test lazy initialization of the absence property."""
        self.assertIsNone(self.employee_service._absence)
        absence = self.employee_service.absence
        self.assertIsInstance(absence, EmployeeAbsenceService)
        self.assertIsNotNone(self.employee_service._absence)

    def test_address_lazy_initialization(self):
        """Test lazy initialization of the address property."""
        self.assertIsNone(self.employee_service._address)
        address = self.employee_service.address
        self.assertIsInstance(address, EmployeeAddressService)
        self.assertIsNotNone(self.employee_service._address)

    def test_bank_account_lazy_initialization(self):
        """Test lazy initialization of the bank_account property."""
        self.assertIsNone(self.employee_service._bank_account)
        bank_account = self.employee_service.bank_account
        self.assertIsInstance(bank_account, EmployeeBankAccountService)
        self.assertIsNotNone(self.employee_service._bank_account)

    def test_child_lazy_initialization(self):
        """Test lazy initialization of the child property."""
        self.assertIsNone(self.employee_service._child)
        child = self.employee_service.child
        self.assertIsInstance(child, EmployeeChildService)
        self.assertIsNotNone(self.employee_service._child)

    def test_wage_component_lazy_initialization(self):
        """Test lazy initialization of the wage_component property."""
        self.assertIsNone(self.employee_service._wage_component)
        wage_component = self.employee_service.wage_component
        self.assertIsInstance(wage_component, EmployeeWageComponentsService)
        self.assertIsNotNone(self.employee_service._wage_component)

    def test_wage_tax_lazy_initialization(self):
        """Test lazy initialization of the wage_tax property."""
        self.assertIsNone(self.employee_service._wage_tax)
        wage_tax = self.employee_service.wage_tax
        self.assertIsInstance(wage_tax, EmployeeWageTaxService)
        self.assertIsNotNone(self.employee_service._wage_tax)

    def test_time_registration_lazy_initialization(self):
        """Test lazy initialization of the time_registration property."""
        self.assertIsNone(self.employee_service._time_registration)
        time_registration = self.employee_service.time_registration
        self.assertIsInstance(time_registration, EmployeeTimeRegistrationService)
        self.assertIsNotNone(self.employee_service._time_registration)

    def test_time_schedule_lazy_initialization(self):
        """Test lazy initialization of the time_schedule property."""
        self.assertIsNone(self.employee_service._time_schedule)
        time_schedule = self.employee_service.time_schedule
        self.assertIsInstance(time_schedule, EmployeeTimeScheduleService)
        self.assertIsNotNone(self.employee_service._time_schedule)

    def test_contract_lazy_initialization(self):
        """Test lazy initialization of the contract property."""
        self.assertIsNone(self.employee_service._contract)
        contract = self.employee_service.contract
        self.assertIsInstance(contract, EmployeeContractService)
        self.assertIsNotNone(self.employee_service._contract)

    def test_cost_center_lazy_initialization(self):
        """Test lazy initialization of the cost_center property."""
        self.assertIsNone(self.employee_service._cost_center)
        cost_center = self.employee_service.cost_center
        self.assertIsInstance(cost_center, EmployeeCostCenterService)
        self.assertIsNotNone(self.employee_service._cost_center)

    def test_days_lazy_initialization(self):
        """Test lazy initialization of the days property."""
        self.assertIsNone(self.employee_service._days)
        days = self.employee_service.days
        self.assertIsInstance(days, EmployeeDaysService)
        self.assertIsNotNone(self.employee_service._days)

    def test_department_lazy_initialization(self):
        """Test lazy initialization of the department property."""
        self.assertIsNone(self.employee_service._department)
        department = self.employee_service.department
        self.assertIsInstance(department, EmployeeDepartmentsService)
        self.assertIsNotNone(self.employee_service._department)

    def test_document_lazy_initialization(self):
        """Test lazy initialization of the document property."""
        self.assertIsNone(self.employee_service._document)
        document = self.employee_service.document
        self.assertIsInstance(document, EmployeeDocumentService)
        self.assertIsNotNone(self.employee_service._document)

    def test_employment_lazy_initialization(self):
        """Test lazy initialization of the employment property."""
        self.assertIsNone(self.employee_service._employment)
        employment = self.employee_service.employment
        self.assertIsInstance(employment, EmployeeEmploymentService)
        self.assertIsNotNone(self.employee_service._employment)

    def test_function_lazy_initialization(self):
        """Test lazy initialization of the function property."""
        self.assertIsNone(self.employee_service._function)
        function = self.employee_service.function
        self.assertIsInstance(function, EmployeeFunctionService)
        self.assertIsNotNone(self.employee_service._function)

    def test_hour_component_lazy_initialization(self):
        """Test lazy initialization of the hour_component property."""
        self.assertIsNone(self.employee_service._hour_component)
        hour_component = self.employee_service.hour_component
        self.assertIsInstance(hour_component, EmployeeHourComponentFixedService)
        self.assertIsNotNone(self.employee_service._hour_component)

    def test_labour_agreement_lazy_initialization(self):
        """Test lazy initialization of the labour_agreement property."""
        self.assertIsNone(self.employee_service._labour_agreement)
        labour_agreement = self.employee_service.labour_agreement
        self.assertIsInstance(labour_agreement, EmployeeLabourAgreementService)
        self.assertIsNotNone(self.employee_service._labour_agreement)

    def test_lease_car_lazy_initialization(self):
        """Test lazy initialization of the lease_car property."""
        self.assertIsNone(self.employee_service._lease_car)
        lease_car = self.employee_service.lease_car
        self.assertIsInstance(lease_car, EmployeeLeaseCarService)
        self.assertIsNotNone(self.employee_service._lease_car)

    def test_leave_lazy_initialization(self):
        """Test lazy initialization of the leave property."""
        self.assertIsNone(self.employee_service._leave)
        leave = self.employee_service.leave
        self.assertIsInstance(leave, EmployeeLeaveService)
        self.assertIsNotNone(self.employee_service._leave)

    def test_levensloop_lazy_initialization(self):
        """Test lazy initialization of the levensloop property."""
        self.assertIsNone(self.employee_service._levensloop)
        levensloop = self.employee_service.levensloop
        self.assertIsInstance(levensloop, EmployeeLevensLoopService)
        self.assertIsNotNone(self.employee_service._levensloop)

    def test_manager_lazy_initialization(self):
        """Test lazy initialization of the manager property."""
        self.assertIsNone(self.employee_service._manager)
        manager = self.employee_service.manager
        self.assertIsInstance(manager, EmployeeManagerService)
        self.assertIsNotNone(self.employee_service._manager)

    def test_partner_lazy_initialization(self):
        """Test lazy initialization of the partner property."""
        self.assertIsNone(self.employee_service._partner)
        partner = self.employee_service.partner
        self.assertIsInstance(partner, EmployeePartnerService)
        self.assertIsNotNone(self.employee_service._partner)

    def test_personal_info_lazy_initialization(self):
        """Test lazy initialization of the personal_info property."""
        self.assertIsNone(self.employee_service._personal_info)
        personal_info = self.employee_service.personal_info
        self.assertIsInstance(personal_info, EmployeePersonalInfoService)
        self.assertIsNotNone(self.employee_service._personal_info)

    def test_salary_lazy_initialization(self):
        """Test lazy initialization of the salary property."""
        self.assertIsNone(self.employee_service._salary)
        salary = self.employee_service.salary
        self.assertIsInstance(salary, EmployeeSalaryService)
        self.assertIsNotNone(self.employee_service._salary)

    def test_schedule_lazy_initialization(self):
        """Test lazy initialization of the schedule property."""
        self.assertIsNone(self.employee_service._schedule)
        schedule = self.employee_service.schedule
        self.assertIsInstance(schedule, EmployeeScheduleService)
        self.assertIsNotNone(self.employee_service._schedule)

    def test_service_lazy_initialization(self):
        """Test lazy initialization of the service property."""
        self.assertIsNone(self.employee_service._service)
        service = self.employee_service.service
        self.assertIsInstance(service, EmployeeServiceService)
        self.assertIsNotNone(self.employee_service._service)

    def test_spaarloon_lazy_initialization(self):
        """Test lazy initialization of the spaarloon property."""
        self.assertIsNone(self.employee_service._spaarloon)
        spaarloon = self.employee_service.spaarloon
        self.assertIsInstance(spaarloon, EmployeeSpaarloonService)
        self.assertIsNotNone(self.employee_service._spaarloon)

    def test_svw_lazy_initialization(self):
        """Test lazy initialization of the svw property."""
        self.assertIsNone(self.employee_service._svw)
        svw = self.employee_service.svw
        self.assertIsInstance(svw, EmployeeSvwService)
        self.assertIsNotNone(self.employee_service._svw)
