"""Microservice responsible for lease car related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeLeaseCarService(MicroService):
    """Microservice responsible for lease car related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_Get"])
    def get(self):
        """
        Get the active lease car contract for given period.

        For more information, refer to the official documentation:
            [LeaseCar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_GetCurrent"])
    def get_current(self):
        """
        Get currently active lease car contract.

        For more information, refer to the official documentation:
            [LeaseCar_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_GetList"])
    def get_all(self):
        """
        Get lease car contract list, until given period.

        For more information, refer to the official documentation:
            [LeaseCar_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_GetAll_EmployeesByCompany"])
    def get_all_by_company(self):
        """
        Get lease car contract list for all employee in company, until given period.

        For more information, refer to the official documentation:
            [LeaseCar_GetAll_EmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetAll_EmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar2_GetAll_EmployeesByCompany"])
    def get_all_by_company_2(self):
        """
        Get lease car contract list for all employee in company, until given period.

        For more information, refer to the official documentation:
            [LeaseCar2_GetAll_EmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar2_GetAll_EmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_Insert"])
    def insert(self):
        """
        Insert a new lease car contract, this contract will start from given date within the object.

        For more information, refer to the official documentation:
            [LeaseCar_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_InsertCurrent"])
    def insert_current(self):
        """
        Insert a new lease car contract, this contract will start from given date within the object.

        For more information, refer to the official documentation:
            [LeaseCar_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_Delete"])
    def delete(self):
        """
        Delete a lease car contract. This action can not be undone.

        For more information, refer to the official documentation:
            [LeaseCar_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:LeaseCar_Stop"])
    def stop(self):
        """
        Stop the currently active lease car contract.

        For more information, refer to the official documentation:
            [LeaseCar_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Stop)
        """
        raise NotImplementedError()  # pragma: no cover
