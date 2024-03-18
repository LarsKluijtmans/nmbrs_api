"""Microservice responsible for wage tax related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeWageTaxService(MicroService):
    """Microservice responsible for wage tax related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_Get"])
    def get(self):
        """
        Get the active loonheffing settings for given period.

        For more information, refer to the official documentation:
            [WageTax_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_GetCurrent"])
    def get_current(self):
        """
        Get the currently active loonheffing settings.

        For more information, refer to the official documentation:
            [WageTax_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_GetList"])
    def get_all(self):
        """
        Get a list of all loonheffing settings.

        For more information, refer to the official documentation:
            [WageTax_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_Get_SE"])
    def get_settings(self):
        """
        Get active wage tax settings for a specific period.

        For more information, refer to the official documentation:
            [WageTax_Get_SE](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_Get_SE)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_Update"])
    def update(self):
        """
        Update loonheffing settings starting from given period

        For more information, refer to the official documentation:
            [WageTax_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_UpdateCurrent"])
    def update_current(self):
        """
        Update loonheffing settings starting from the current period.

        For more information, refer to the official documentation:
            [WageTax_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:WageTax_Update_SE"])
    def update_settings(self):
        """
        Update loonheffing settings starting from given period.

        For more information, refer to the official documentation:
            [WageTax_Update_SE](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=WageTax_Update_SE)
        """
        raise NotImplementedError()  # pragma: no cover
