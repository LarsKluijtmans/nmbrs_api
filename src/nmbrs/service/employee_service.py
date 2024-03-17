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


class EmployeeService(Service):
    """
    A class representing Employee Service for interacting with Nmbrs employee-related functionalities.

    Not implemented calls:
        1 [EmployeeType_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeType_GetList)
        62 [Employee_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_GetCurrent)
        63 [Employee_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Insert)
        64 [Employee_InsertBasedOnDefault](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertBasedOnDefault)
        65 [Employee_InsertByEmployeeType](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_InsertByEmployeeType)
        66 [Employee_Transition](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Employee_Transition)
        73 [List_GetByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByCompany)
        120 [List_GetByDebtor](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=List_GetByDebtor)

        # microservice???
        69 [EndServiceReason_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetList)
        70 [EndServiceReason_GetListByYear](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EndServiceReason_GetListByYear)
        71 [ExtraFieldsWithStartDate_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFieldsWithStartDate_GetList)
        72 [ExtraFields_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=ExtraFields_GetList)
        121 [PerformanceReview_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_Get)
        128 [PerformanceReview_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PerformanceReview_GetAll_AllEmployeesByCompany)
        129 [Reports_GetJournalsReportByEmployee](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reports_GetJournalsReportByEmployee)
        137 [Reservations_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Reservations_GetList)
    """

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
