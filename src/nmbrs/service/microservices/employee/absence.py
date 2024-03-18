# pylint: disable=line-too-long
"""Microservice responsible for absence related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeAbsenceService(MicroService):
    """Microservice responsible for absence related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Absence_GetList"])
    def get(self):
        """
        Get a list of all absences.

        For more information, refer to the official documentation:
            [Absence_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence2_GetList"])
    def get_2(self):
        """
        Get a list of all absences with their respective cause.

        For more information, refer to the official documentation:
            [Absence2_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence2_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get a list of all absence of all company employees.

        For more information, refer to the official documentation:
            [Absence_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence_Insert"])
    def insert(self):
        """
        Insert an absence, this item will start from the given date in the object.

        For more information, refer to the official documentation:
            [Absence_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence2_Insert"])
    def insert_2(self):
        """
        Insert an absence with cause, this item will start from the given date in the object.

        For more information, refer to the official documentation:
            [Absence2_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence2_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence_PartialRecoveryInsert"])
    def insert_partial_recovery(self):
        """
        Insert an absence partial recovery message.

        For more information, refer to the official documentation:
            [Absence_PartialRecoveryInsert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_PartialRecoveryInsert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Absence_RecoveryInsert"])
    def insert_recovery(self):
        """
        Insert an absence recovery message.

        For more information, refer to the official documentation:
            [Absence_RecoveryInsert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Absence_RecoveryInsert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:AbsenceNotification_Insert"])
    def insert_notification(self):
        """
        Insert a new absence date, this item will start from the given date in the object to the requested absence dossier.

        For more information, refer to the official documentation:
            [AbsenceNotification_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=AbsenceNotification_Insert)
        """
        raise NotImplementedError()  # pragma: no cover
