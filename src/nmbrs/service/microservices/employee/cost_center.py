"""Microservice responsible for cost center related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import CostCenter
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeCostCenterService(MicroService):
    """Microservice responsible for cost center related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:CostCenter_Get")
    def get(self, employee_id: int, period: int, year: int) -> list[CostCenter]:
        """
        Get all cost center per employee.

        For more information, refer to the official documentation:
            [CostCenter_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            list[CostCenter]: a list of CostCenter objects
        """
        cost_centers = self.client.service.CostCenter_Get(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        cost_centers = [CostCenter(employee_id=employee_id, data=cost_center) for cost_center in serialize_object(cost_centers)]
        return cost_centers

    @nmbrs_exception_handler(resource="EmployeeService:CostCenter_GetCurrent")
    def get_current(self, employee_id: int) -> list[CostCenter]:
        """
        Get all active cost centers of a specific employee on the current period.

        For more information, refer to the official documentation:
            [CostCenter_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[CostCenter]: a list of CostCenter objects
        """
        cost_centers = self.client.service.CostCenter_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        cost_centers = [CostCenter(employee_id=employee_id, data=cost_center) for cost_center in serialize_object(cost_centers)]
        return cost_centers

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:CostCenter_GetAllEmployeesByCompany")
    def get_all_by_company(self, company_id: int, period: int, year: int) -> list[CostCenter]:
        """
        Get all cost centers of all employees per company.

        For more information, refer to the official documentation:
            [CostCenter_GetAllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_GetAllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.

        Returns:
            list[CostCenter]: a list of CostCenter objects
        """
        cost_centers = self.client.service.CostCenter_GetAllEmployeesByCompany(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        cost_centers = serialize_object(cost_centers)
        _cost_centers = []
        for employee in cost_centers:
            for cost_center in employee["CostCenters"]["EmployeeCostCenter"]:
                _cost_centers.append(CostCenter(employee_id=employee["EmployeeId"], data=cost_center))
        return _cost_centers

    @nmbrs_exception_handler(resource="EmployeeService:CostCenter_Update")
    def update(self):
        """
        Update cost center.

        For more information, refer to the official documentation:
            [CostCenter_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:CostCenter_UpdateCurrent")
    def update_current(self):
        """
        Update cost centers starting from the current period.

        For more information, refer to the official documentation:
            [CostCenter_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=CostCenter_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
