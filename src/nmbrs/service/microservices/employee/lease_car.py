"""Microservice responsible for lease car related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import LeaseCar
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeLeaseCarService(MicroService):
    """Microservice responsible for lease car related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_Get")
    def get(self):
        """
        Get the active lease car contract for given period.

        For more information, refer to the official documentation:
            [LeaseCar_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_GetCurrent")
    def get_current(self):
        """
        Get currently active lease car contract.

        For more information, refer to the official documentation:
            [LeaseCar_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_GetList")
    def get_all(self):
        """
        Get lease car contract list, until given period.

        For more information, refer to the official documentation:
            [LeaseCar_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetList)
        """
        raise NotImplementedError()  # pragma: no cover

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_GetAll_EmployeesByCompany")
    def get_all_by_company(self, company_id: int, period: int, year: int) -> list[LeaseCar]:
        """
        Get lease car contract list for all employee in company, until given period.

        For more information, refer to the official documentation:
            [LeaseCar_GetAll_EmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_GetAll_EmployeesByCompany)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.

        Returns:
            list[LeaseCar]: a list of LeaseCar objects
        """
        lease_cars = self.client.service.LeaseCar_GetAll_EmployeesByCompany(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        lease_cars = serialize_object(lease_cars)
        _lease_cars = []
        for employee in lease_cars:
            for department in employee["LeaseCars"]["EmployeeLeaseCar"]:
                _lease_cars.append(LeaseCar(employee_id=employee["EmployeeId"], data=department))
        return _lease_cars

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar2_GetAll_EmployeesByCompany")
    def get_all_by_company_2(self):
        """
        Get lease car contract list for all employee in company, until given period.

        For more information, refer to the official documentation:
            [LeaseCar2_GetAll_EmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar2_GetAll_EmployeesByCompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_Insert")
    def post(self):
        """
        Insert a new lease car contract, this contract will start from given date within the object.

        For more information, refer to the official documentation:
            [LeaseCar_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_InsertCurrent")
    def post_current(self):
        """
        Insert a new lease car contract, this contract will start from given date within the object.

        For more information, refer to the official documentation:
            [LeaseCar_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_Delete")
    def delete(self):
        """
        Delete a lease car contract. This action can not be undone.

        For more information, refer to the official documentation:
            [LeaseCar_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:LeaseCar_Stop")
    def stop(self):
        """
        Stop the currently active lease car contract.

        For more information, refer to the official documentation:
            [LeaseCar_Stop](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=LeaseCar_Stop)
        """
        raise NotImplementedError()  # pragma: no cover
