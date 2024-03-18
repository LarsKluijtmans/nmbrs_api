"""Microservice responsible for cost center related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeCostCenterService(MicroService):
    """Microservice responsible for cost center related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:CostCenter_Get"])
    def get(self):
        """
        Get all cost center per employee.

        For more information, refer to the official documentation:
            [CostCenter_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:CostCenter_GetCurrent"])
    def get_current(self):
        """
        Get all active cost centers of a specific employee on the current period.

        For more information, refer to the official documentation:
            [CostCenter_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:CostCenter_GetAllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all cost centers of all employees per company.

        For more information, refer to the official documentation:
            [CostCenter_GetAllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_GetAllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:CostCenter_Update"])
    def update(self):
        """
        Update cost center.

        For more information, refer to the official documentation:
            [CostCenter_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:CostCenter_UpdateCurrent"])
    def update_current(self):
        """
        Update cost centers starting from the current period.

        For more information, refer to the official documentation:
            [CostCenter_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
