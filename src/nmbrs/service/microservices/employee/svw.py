"""Microservice responsible for svw related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import SVW
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeSvwService(MicroService):
    """Microservice responsible for svw related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:SVW_Get")
    def get(self):
        """
        Get the active SVW settings for given period.

        For more information, refer to the official documentation:
            [SVW_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:SVW_GetCurrent")
    def get_current(self):
        """
        Get the currently active SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:SVW_GetList")
    def get_all(self):
        """
        Get a list of all SVW settings.

        For more information, refer to the official documentation:
            [SVW_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:SVW_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[SVW]:
        """
        Get all (historical) svw setting records for all employees that belong to the company.

        For more information, refer to the official documentation:
            [SVW_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[SVW]: A list of SVW objects
        """
        svws = self.client.service.SVW_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_manager.header)
        svws = serialize_object(svws)
        _svw = []
        for employee in svws:
            for svw in employee["EmployeeSVWSettings"]["EmployeeSVWSettings"]:
                _svw.append(SVW(employee_id=employee["EmployeeId"], data=svw))
        return _svw

    @nmbrs_exception_handler(resource="EmployeeService:SVW_Update")
    def update(self):
        """
        Update SVW settings starting from given period.

        For more information, refer to the official documentation:
            [SVW_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:SVW_UpdateCurrent")
    def update_current(self):
        """
        Update SVW settings starting from the current period.

        For more information, refer to the official documentation:
            [SVW_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=SVW_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
