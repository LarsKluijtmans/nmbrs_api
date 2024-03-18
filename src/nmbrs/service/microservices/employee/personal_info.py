# pylint: disable=line-too-long
"""Microservice responsible for personal info related actions on the employee level."""
from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeePersonalInfoService(MicroService):
    """Microservice responsible for personal info related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfo_Get"])
    def get(self):
        """
        Get the active personal info for given period.

        For more information, refer to the official documentation:
            [PersonalInfo_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfo_GetCurrent"])
    def get_current(self):
        """
        Get the currently active personal info.

        For more information, refer to the official documentation:
            [PersonalInfo_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfo_GetAll_AllEmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get all personal infos of all employees.

        For more information, refer to the official documentation:
            [PersonalInfo_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany"])
    def get_all_by_company_without_bsn(self):
        """
        Get all personal infos of all employees, excluding the BSN.

        For more information, refer to the official documentation:
            [PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany"])
    def get_all_by_company_contract_address_salary(self):
        """
        Get all personal infos of all employees.

        For more information, refer to the official documentation:
            [PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfo_Update"])
    def update(self):
        """
        Update personal info starting from the given period.

        For more information, refer to the official documentation:
            [PersonalInfo_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_Update)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:PersonalInfo_UpdateCurrent"])
    def update_current(self):
        """
        Update personal info starting from the current period.

        For more information, refer to the official documentation:
            [PersonalInfo_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_UpdateCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
