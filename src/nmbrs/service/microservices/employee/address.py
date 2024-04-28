"""Microservice responsible for address related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Address
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeAddressService(MicroService):
    """Microservice responsible for address related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Address_GetList")
    def get(self, employee_id: int, period: int, year: int) -> list[Address]:
        """
        Get all addresses which are active in given period.

        For more information, refer to the official documentation:
            [Address_GetList](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetList)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period.
            year (int): The year.

        Returns:
            list[Address]: A list of Address objects representing the addresses.
        """
        addresses = self.client.service.Address_GetList(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return [Address(employee_id=employee_id, data=address) for address in serialize_object(addresses)]

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Address_GetListCurrent")
    def get_current(self, employee_id: int) -> list[Address]:
        """
        Get all currently active addresses.

        For more information, refer to the official documentation:
            [Address_GetListCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetListCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Address]: A list of Address objects representing the addresses.
        """
        addresses = self.client.service.Address_GetListCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return [Address(employee_id=employee_id, data=address) for address in serialize_object(addresses)]

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Address_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Address]:
        """
        Get all addresses of all employees.

        For more information, refer to the official documentation:
            [Address_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_GetAll_AllEmployeesByCompany)  # pylint: disable=line-too-long

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Address]: A list of Address objects representing the addresses.
        """
        addresses = self.client.service.Address_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_manager.header)

        _addresses = []
        for employee in serialize_object(addresses):
            for address in employee["EmployeeAddresses"]["EmployeeAddress_V2"]:
                _addresses.append(Address(employee_id=employee["EmployeeId"], data=address))
        return _addresses

    @nmbrs_exception_handler(resource="EmployeeService:Address_Delete")
    def delete(self, employee_id: int, address_id: int) -> bool:
        """
        Get all active bank accounts for given period.

        For more information, refer to the official documentation:
            [Address_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Delete)

        Args:
            employee_id (int): The ID of the employee.
            address_id (int): The ID of the address.

        Returns:
            bool: A boolean indicating the success of the operation.
        """
        response = self.client.service.Address_Delete(EmployeeId=employee_id, AddressID=address_id, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Address_Update")
    def update(self, employee_id: int, address: Address) -> bool:
        """
        Delete Employee Address.

        For more information, refer to the official documentation:
            [Address_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Update)

        Args:
            employee_id (int): The ID of the employee.
            address (Address): The Address object to update.

        Returns:
            bool: A boolean indicating the success of the operation.
        """
        _address = {
            "Id": address.id,
            "Default": address.default,
            "Street": address.street,
            "HouseNumber": address.house_number,
            "HouseNumberAddition": address.house_number_addition,
            "PostalCode": address.postcode,
            "City": address.city,
            "StateProvince": address.state_province,
            "CountryISOCode": address.country_iso_code,
            "Type": address.type,
        }
        response = self.client.service.Address_Update(EmployeeId=employee_id, Address=_address, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Address_Insert")
    def post(self, employee_id: int, address: Address, period: int, year: int, unprotected_mode: bool) -> int:
        """
        Insert given address to the specified period. If the period is before the company's current period,
        unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Address_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_Insert)

        Args:
            employee_id (int): The ID of the employee.
            address (Address): The Address object to insert.
            period (int): The period.
            year (int): The year.
            unprotected_mode (bool): Flag indicating whether unprotected mode is enabled.

        Returns:
            int: The response indicating the success of the operation.
        """
        _address = {
            "Id": address.id,
            "Default": address.default,
            "Street": address.street,
            "HouseNumber": address.house_number,
            "HouseNumberAddition": address.house_number_addition,
            "PostalCode": address.postcode,
            "City": address.city,
            "StateProvince": address.state_province,
            "CountryISOCode": address.country_iso_code,
            "Type": address.type,
        }
        response = self.client.service.Address_Insert(
            EmployeeId=employee_id,
            Address=_address,
            Period=period,
            Year=year,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Address_InsertCurrent")
    def post_current(self, employee_id: int, address: Address) -> int:
        """
        Insert given address to the current period.

        For more information, refer to the official documentation:
            [Address_InsertCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Address_InsertCurrent)

        Args:
            employee_id (int): The ID of the employee.
            address (Address): The Address object to insert.

        Returns:
            int: The response indicating the success of the operation.
        """
        _address = {
            "Id": address.id,
            "Default": address.default,
            "Street": address.street,
            "HouseNumber": address.house_number,
            "HouseNumberAddition": address.house_number_addition,
            "PostalCode": address.postcode,
            "City": address.city,
            "StateProvince": address.state_province,
            "CountryISOCode": address.country_iso_code,
            "Type": address.type,
        }
        response = self.client.service.Address_InsertCurrent(
            EmployeeId=employee_id, Address=_address, _soapheaders=self.auth_manager.header
        )
        return response
