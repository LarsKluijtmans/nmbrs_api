"""Unit tests for the EmployeeService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.data_classes.company import Period
from src.nmbrs.data_classes.employee import Employee, EmployeeTypes
from src.nmbrs.service.employee_service import EmployeeService
from src.nmbrs.service.microservices.employee import (
    EmployeeServiceService,
    EmployeeAbsenceService,
    EmployeeAddressService,
    EmployeeBankAccountService,
    EmployeeChildService,
    EmployeeContractService,
    EmployeeCostCenterService,
    EmployeeDaysService,
    EmployeeDocumentService,
    EmployeeEmploymentService,
    EmployeeFunctionService,
    EmployeeHourComponentFixedService,
    EmployeeDepartmentsService,
    EmployeeLabourAgreementService,
    EmployeeLeaseCarService,
    EmployeeLeaveService,
    EmployeeLevensLoopService,
    EmployeeManagerService,
    EmployeePartnerService,
    EmployeePersonalInfoService,
    EmployeeSalaryService,
    EmployeeScheduleService,
    EmployeeSpaarloonService,
    EmployeeSvwService,
    EmployeeTimeRegistrationService,
    EmployeeTimeScheduleService,
    EmployeeWageComponentsService,
    EmployeeWageTaxService,
)


class TesteEmployeeService(unittest.TestCase):
    """Unit tests for the EmployeeService class."""

    def setUp(self):
        self.employee_service = EmployeeService()
        self.mock_auth_header = Mock()
        self.mock_client = Mock()
        self.employee_service.client = self.mock_client
        self.employee_service.set_auth_header(self.mock_auth_header)

    def test_initiation_of_microservices(self):
        """Test initialization of all microservices."""
        self.assertIsInstance(self.employee_service.absence, EmployeeAbsenceService)
        self.assertIsInstance(self.employee_service.address, EmployeeAddressService)
        self.assertIsInstance(self.employee_service.bank_account, EmployeeBankAccountService)
        self.assertIsInstance(self.employee_service.child, EmployeeChildService)
        self.assertIsInstance(self.employee_service.contract, EmployeeContractService)
        self.assertIsInstance(self.employee_service.cost_center, EmployeeCostCenterService)
        self.assertIsInstance(self.employee_service.days, EmployeeDaysService)
        self.assertIsInstance(self.employee_service.department, EmployeeDepartmentsService)
        self.assertIsInstance(self.employee_service.document, EmployeeDocumentService)
        self.assertIsInstance(self.employee_service.employment, EmployeeEmploymentService)
        self.assertIsInstance(self.employee_service.function, EmployeeFunctionService)
        self.assertIsInstance(self.employee_service.hour_component, EmployeeHourComponentFixedService)
        self.assertIsInstance(self.employee_service.labour_agreement, EmployeeLabourAgreementService)
        self.assertIsInstance(self.employee_service.lease_car, EmployeeLeaseCarService)
        self.assertIsInstance(self.employee_service.leave, EmployeeLeaveService)
        self.assertIsInstance(self.employee_service.levensloop, EmployeeLevensLoopService)
        self.assertIsInstance(self.employee_service.manager, EmployeeManagerService)
        self.assertIsInstance(self.employee_service.partner, EmployeePartnerService)
        self.assertIsInstance(self.employee_service.personal_info, EmployeePersonalInfoService)
        self.assertIsInstance(self.employee_service.salary, EmployeeSalaryService)
        self.assertIsInstance(self.employee_service.schedule, EmployeeScheduleService)
        self.assertIsInstance(self.employee_service.service, EmployeeServiceService)
        self.assertIsInstance(self.employee_service.spaarloon, EmployeeSpaarloonService)
        self.assertIsInstance(self.employee_service.svw, EmployeeSvwService)
        self.assertIsInstance(self.employee_service.time_registration, EmployeeTimeRegistrationService)
        self.assertIsInstance(self.employee_service.time_schedule, EmployeeTimeScheduleService)
        self.assertIsInstance(self.employee_service.wage_component, EmployeeWageComponentsService)
        self.assertIsInstance(self.employee_service.wage_tax, EmployeeWageTaxService)

    def test_set_auth_headers(self):
        """Test setting authentication headers for all microservices."""
        # Setup mocks
        self.employee_service.absence = Mock()
        self.employee_service.address = Mock()
        self.employee_service.bank_account = Mock()
        self.employee_service.child = Mock()
        self.employee_service.contract = Mock()
        self.employee_service.cost_center = Mock()
        self.employee_service.days = Mock()
        self.employee_service.department = Mock()
        self.employee_service.document = Mock()
        self.employee_service.employment = Mock()
        self.employee_service.function = Mock()
        self.employee_service.hour_component = Mock()
        self.employee_service.labour_agreement = Mock()
        self.employee_service.lease_car = Mock()
        self.employee_service.leave = Mock()
        self.employee_service.levensloop = Mock()
        self.employee_service.manager = Mock()
        self.employee_service.partner = Mock()
        self.employee_service.personal_info = Mock()
        self.employee_service.salary = Mock()
        self.employee_service.schedule = Mock()
        self.employee_service.service = Mock()
        self.employee_service.spaarloon = Mock()
        self.employee_service.svw = Mock()
        self.employee_service.time_registration = Mock()
        self.employee_service.time_schedule = Mock()
        self.employee_service.wage_component = Mock()
        self.employee_service.wage_tax = Mock()

        auth_header = {"Authorization": "Bearer token"}

        # Call the set_auth_header method on the mocked employeeService
        self.employee_service.set_auth_header(auth_header)

        self.employee_service.absence.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.address.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.bank_account.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.child.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.contract.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.cost_center.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.days.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.department.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.document.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.employment.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.function.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.hour_component.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.labour_agreement.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.lease_car.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.leave.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.levensloop.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.manager.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.partner.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.personal_info.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.salary.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.schedule.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.service.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.spaarloon.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.svw.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.time_registration.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.time_schedule.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.wage_component.set_auth_header.assert_called_once_with(auth_header)
        self.employee_service.wage_tax.set_auth_header.assert_called_once_with(auth_header)

    def test_get_types(self):
        """Test retrieving all companies."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.EmployeeType_GetList.return_value = mock_companies
        result = self.employee_service.get_types()
        self.assertEqual(len(result), 3)
        for _type in result:
            self.assertIsInstance(_type, EmployeeTypes)
        self.mock_client.service.EmployeeType_GetList.assert_called_once_with(_soapheaders=self.mock_auth_header)

    def test_get_current_period(self):
        """Test retrieving the current period of an employee."""
        mock_period = "2024-03-M"
        self.mock_client.service.Employee_GetCurrent.return_value = mock_period
        result = self.employee_service.get_current_period(1)
        self.assertIsInstance(result, Period)
        self.mock_client.service.Employee_GetCurrent.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_get_current_period_return_none(self):
        """Test retrieving the current period of an employee, return None"""
        self.mock_client.service.Employee_GetCurrent.return_value = None
        result = self.employee_service.get_current_period(1)
        self.assertIsNone(result)
        self.mock_client.service.Employee_GetCurrent.assert_called_once_with(EmployeeId=1, _soapheaders=self.mock_auth_header)

    def test_get_by_company(self):
        """Test retrieving all employees from a company."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByCompany.return_value = mock_companies
        employees = self.employee_service.get_by_company(1, 1)
        self.assertEqual(len(employees), 3)
        for employee in employees:
            self.assertIsInstance(employee, Employee)
        self.mock_client.service.List_GetByCompany.assert_called_once_with(CompanyId=1, EmployeeType=1, _soapheaders=self.mock_auth_header)

    def test_get_by_debtor(self):
        """Test retrieving all employees from a debtor."""
        mock_companies = [Mock() for _ in range(3)]
        self.mock_client.service.List_GetByDebtor.return_value = mock_companies
        employees = self.employee_service.get_by_debtor(1, 1)
        self.assertEqual(len(employees), 3)
        for employee in employees:
            self.assertIsInstance(employee, Employee)
        self.mock_client.service.List_GetByDebtor.assert_called_once_with(DebtorId=1, EmployeeType=1, _soapheaders=self.mock_auth_header)
