"""Microservice responsible for svw related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeSvwService(MicroService):
    """Microservice responsible for svw related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_Get"])
    def get(self):
        """
        Get the active SVW settings for given period.

        For more information, refer to the official documentation:
            [SVW_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_GetCurrent"])
    def get_current(self):
        """
        Get the currently active SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_GetList"])
    def get_all(self):
        """
        Get a list of all SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all (historical) svw setting records for all employees that belong to the company.

        For more information, refer to the official documentation:
            [SVW_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_Update"])
    def update(self):
        """
        Update SVW settings starting from given period.

        For more information, refer to the official documentation:
            [SVW_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:SVW_UpdateCurrent"])
    def update_current(self):
        """
        Update SVW settings starting from the current period.

        For more information, refer to the official documentation:
            [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
