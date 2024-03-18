"""Microservice responsible for labour agreement related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeLabourAgreementService(MicroService):
    """Microservice responsible for labour agreement related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:LabourAgreements_Get"])
    def get(self):
        """
        Get the labour agreement settings to an employee.

        For more information, refer to the official documentation:
            [LabourAgreements_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LabourAgreements_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LabourAgreements_GetCurrent"])
    def get_current(self):
        """
        Get labour agreement settings to an employee for the current period.

        For more information, refer to the official documentation:
            [LabourAgreements_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LabourAgreements_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LabourAgreements_Update"])
    def update(self):
        """
        Update the labour agreement that is assigned to an employee. Unprotected mode flag activated.

        For more information, refer to the official documentation:
            [LabourAgreements_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LabourAgreements_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LabourAgreements_UpdateCurrent"])
    def update_current(self):
        """
        Update the labour agreement that is assigned to an employee for the current period.

        For more information, refer to the official documentation:
            [LabourAgreements_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LabourAgreements_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
