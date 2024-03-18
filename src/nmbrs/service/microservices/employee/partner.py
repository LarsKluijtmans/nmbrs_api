# pylint: disable=line-too-long
"""Microservice responsible for partner related actions on the employee level."""
from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeePartnerService(MicroService):
    """Microservice responsible for partner related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Partner_Get"])
    def get(self):
        """
        Get employee partner.

        For more information, refer to the official documentation:
            [Partner_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Partner_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get employee partner.

        For more information, refer to the official documentation:
            [Partner_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Partner_Update"])
    def update(self):
        """
        Update the employee partner info.

        For more information, refer to the official documentation:
            [Partner_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Partner_Delete"])
    def delete(self):
        """
        Delete employee's partner.

        For more information, refer to the official documentation:
            [Partner_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Delete)
        """
        raise NotImplementedError()  # pragma: no cover
