"""Microservice responsible for absence related actions on the employee level."""

from datetime import datetime

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Absence
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeAbsenceService(MicroService):
    """Microservice responsible for absence related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Absence_GetList")
    def get_current(self, employee_id: int) -> list[Absence]:
        """
        Get a list of all absences.

        For more information, refer to the official documentation:
            [Absence_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_GetList)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Absence]: A list of Absence objects representing the absences.
        """
        absences = self.client.service.Absence_GetList(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return [Absence(employee_id=employee_id, data=absence) for absence in serialize_object(absences)]

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Absence2_GetList")
    def get_current_2(self, employee_id: int) -> list[Absence]:
        """
        Get a list of all absences with their respective cause.

        For more information, refer to the official documentation:
            [Absence2_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence2_GetList)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Absence]: A list of Absence objects representing the absences.
        """
        absences = self.client.service.Absence2_GetList(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return [Absence(employee_id=employee_id, data=absence) for absence in serialize_object(absences)]

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Absence_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Absence]:
        """
        Get a list of all absence of all company employees.

        For more information, refer to the official documentation:
            [Absence_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_GetAll_AllEmployeesByCompany)  # pylint: disable=line-too-long

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Absence]: A list of Absence objects representing the absences.
        """
        absences = self.client.service.Absence_GetAll_AllEmployeesByCompany(CompanyId=company_id, _soapheaders=self.auth_manager.header)

        _absences = []
        for employee in serialize_object(absences):
            _absences.append(Absence(employee_id=employee["EmployeeId"], data=employee))
        return _absences

    @nmbrs_exception_handler(resource="EmployeeService:Absence_Insert")
    def post(self, employee_id: int, absence: Absence) -> int:
        """
        Insert an absence, this item will start from the given date in the object.

        For more information, refer to the official documentation:
            [Absence_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_Insert)

        Args:
            employee_id (int): The ID of the employee.
            absence (Absence): The absence details to insert.

        Returns:
            int: The response status code indicating the success of the operation.
        """
        _absence = {
            "AbsenceId": absence.id,
            "Comment": absence.comment,
            "Percentage": absence.percentage,
            "Start": absence.start,
            "RegistrationStartDate": absence.registration_start_date,
            "End": absence.end,
            "RegistrationEndDate": absence.registration_end_date,
            "Dossier": absence.dossier,
            "Dossiernr": absence.dossier_number,
        }
        response = self.client.service.Absence_Insert(EmployeeId=employee_id, Absence=_absence, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Absence2_Insert")
    def post_2(self, employee_id: int, absence: Absence) -> int:
        """
        Insert an absence with cause, this item will start from the given date in the object.

        For more information, refer to the official documentation:
            [Absence2_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence2_Insert)

        Args:
            employee_id (int): The ID of the employee.
            absence (Absence): The absence details to insert.

        Returns:
            int: The response status code indicating the success of the operation.
        """
        _absence = {
            "AbsenceCause": {"CauseId": absence.cause.id, "Cause": absence.cause.cause},
            "AbsenceId": absence.id,
            "Comment": absence.comment,
            "Percentage": absence.percentage,
            "Start": absence.start,
            "RegistrationStartDate": absence.registration_start_date,
            "End": absence.end,
            "RegistrationEndDate": absence.registration_end_date,
            "Dossier": absence.dossier,
            "Dossiernr": absence.dossier_number,
        }
        response = self.client.service.Absence2_Insert(EmployeeId=employee_id, Absence=_absence, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Absence_PartialRecoveryInsert")
    def post_partial_recovery(
        self, employee_id: int, absence_id: int, start_date: datetime, report_data: datetime, percentage: int, comment: str
    ) -> int:
        """
        Insert an absence partial recovery message.

        For more information, refer to the official documentation:
            [Absence_PartialRecoveryInsert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_PartialRecoveryInsert)

        Args:
            employee_id (int): The ID of the employee.
            absence_id (int): The ID of the absence.
            start_date (datetime): The start date of the absence recovery.
            report_data (datetime): The report date of the absence recovery.
            percentage (int): The percentage of the recovery.
            comment (str): The comment for the recovery.

        Returns:
            int: The response status code indicating the success of the operation.
        """
        response = self.client.service.Absence_PartialRecoveryInsert(
            EmployeeId=employee_id,
            AbsenceID=absence_id,
            StartDate=start_date,
            Reportdate=report_data,
            Percent=percentage,
            Comment=comment,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Absence_RecoveryInsert")
    def post_recovery(self, employee_id: int, absence_id: int, last_day_absence: datetime, report_data: datetime, comment: str) -> str:
        """
        Insert an absence recovery message.

        For more information, refer to the official documentation:
            [Absence_RecoveryInsert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_RecoveryInsert)

        Args:
            employee_id (int): The ID of the employee.
            absence_id (int): The ID of the absence.
            last_day_absence (datetime): The last day of the absence.
            report_data (datetime): The report date of the absence recovery.
            comment (str): The comment for the recovery.

        Returns:
            str: The response status code indicating the success of the operation.
        """
        response = self.client.service.Absence_RecoveryInsert(
            EmployeeId=employee_id,
            AbsenceID=absence_id,
            Lastdayabsence=last_day_absence,
            Reportdate=report_data,
            Comment=comment,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:AbsenceNotification_Insert")
    def post_notification(self, employee_id: int, absence: Absence) -> int:
        """
        Insert a new absence date, this item will start from the given date in the object to the requested absence dossier.

        For more information, refer to the official documentation:
            [AbsenceNotification_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=AbsenceNotification_Insert)

        Args:
            employee_id (int): The ID of the employee.
            absence (Absence): The absence details to insert.

        Returns:
            int: The response status code indicating the success of the operation.
        """
        _absence = {
            "AbsenceCause": {"CauseId": absence.cause.id, "Cause": absence.cause.cause},
            "AbsenceId": absence.id,
            "Comment": absence.comment,
            "Percentage": absence.percentage,
            "Start": absence.start,
            "RegistrationStartDate": absence.registration_start_date,
            "End": absence.end,
            "RegistrationEndDate": absence.registration_end_date,
            "Dossier": absence.dossier,
            "Dossiernr": absence.dossier_number,
        }
        response = self.client.service.AbsenceNotification_Insert(
            EmployeeId=employee_id, Absence=_absence, _soapheaders=self.auth_manager.header
        )
        return response
