# pylint: disable=line-too-long
"""Microservice responsible for partner related actions on the employee level."""
from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list
from ....data_classes.employee import Partner


class EmployeePartnerService(MicroService):
    """Microservice responsible for partner related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Partner_Get")
    def get_current(self):
        """
        Get employee partner.

        For more information, refer to the official documentation:
            [Partner_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Partner_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Partner]:
        """
        Get employee partner.

        For more information, refer to the official documentation:
            [Partner_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Partner]: A list of Partner objects
        """
        partners = self.client.service.Partner_GetAll_AllEmployeesByCompany(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        partners = serialize_object(partners)
        _partners = []
        for employee in partners:
            _partners.append(Partner(employee_id=employee["EmployeeId"], data=employee["Partner"]))
        return _partners

    @nmbrs_exception_handler(resource="EmployeeService:Partner_Update")
    def update(self):
        """
        Update the employee partner info.

        For more information, refer to the official documentation:
            [Partner_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:Partner_Delete")
    def delete(self):
        """
        Delete employee's partner.

        For more information, refer to the official documentation:
            [Partner_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Partner_Delete)
        """
        raise NotImplementedError()  # pragma: no cover
