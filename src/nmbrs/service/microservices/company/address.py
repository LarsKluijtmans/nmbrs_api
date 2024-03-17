"""Microservice responsible for address-related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from src.nmbrs.data_classes.debtor import Address
from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyAddressService(MicroService):
    """
    Microservice responsible for address-related actions on the company level.

    Could not get working:
        - [Address_GetCurrentWithAddressType](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=Address_GetCurrentWithAddressType)
    """

    def __init__(self, client: Client) -> None:
        """
        Constructor method for CompanyAddressService.

        Args:
            client (Client): A Zeep Client object representing the connection to the Nmbrs API.
        """
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Set the authentication header for requests to the Nmbrs API.

        Args:
            auth_header (dict): The authentication header to be set.
        """
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:Address_GetCurrent"])
    def get(self, company_id: int) -> Address | None:
        """
        Get the current address of the company.

        This method fetches the current address of the specified company from the Nmbrs API.

        Args:
            company_id (int): The ID of the company.

        Returns:
            Address | None: An Address object if found, otherwise None.
        """
        address = self.client.service.Address_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_header)
        if address is None:
            return None
        return Address(serialize_object(address))

    @nmbrs_exception_handler(resources=["CompanyService:Address_Insert"])
    def insert(
        self,
        company_id: int,
        address_id: int,
        default: bool,
        street: str,
        house_number: str,
        house_number_addon: str,
        postal_code: str,
        city: str,
        state_province: str,
        country_iso_code: str,
    ) -> int:
        """
        Insert a new address for the company.

        This method inserts a new address for the specified company using the provided address data.

        Args:
            company_id (int): The ID of the company.
            address_id (int): The ID of the address.
            default (bool): Flag indicating if the address is default.
            street (str): Street name.
            house_number (str): House number.
            house_number_addon (str): House number addition (if any).
            postal_code (str): Postal code.
            city (str): City name.
            state_province (str): State or province name.
            country_iso_code (str): ISO code of the country.

        Returns:
            int: ID of the inserted address.
        """
        data = {
            "CompanyId": company_id,
            "Address": {
                "Id": address_id,
                "Default": default,
                "Street": street,
                "HouseNumber": house_number,
                "HouseNumberAddition": house_number_addon,
                "PostalCode": postal_code,
                "City": city,
                "StateProvince": state_province,
                "CountryISOCode": country_iso_code,
            },
        }
        response = self.client.service.Address_Insert(**data, _soapheaders=self.auth_header)
        return response

    @nmbrs_exception_handler(resources=["CompanyService:Address_Update"])
    def update(
        self,
        company_id: int,
        address_id: int,
        default: bool,
        street: str,
        house_number: str,
        house_number_addon: str,
        postal_code: str,
        city: str,
        state_province: str,
        country_iso_code: str,
    ) -> None:
        """
        Update an existing address for the company.

        This method updates an existing address for the specified company using the provided address data.

        Args:
            company_id (int): The ID of the company.
            address_id (int): The ID of the address.
            default (bool): Flag indicating if the address is default.
            street (str): Street name.
            house_number (str): House number.
            house_number_addon (str): House number addition (if any).
            postal_code (str): Postal code.
            city (str): City name.
            state_province (str): State or province name.
            country_iso_code (str): ISO code of the country.
        """
        data = {
            "CompanyId": company_id,
            "Address": {
                "Id": address_id,
                "Default": default,
                "Street": street,
                "HouseNumber": house_number,
                "HouseNumberAddition": house_number_addon,
                "PostalCode": postal_code,
                "City": city,
                "StateProvince": state_province,
                "CountryISOCode": country_iso_code,
            },
        }
        self.client.service.Address_Update(**data, _soapheaders=self.auth_header)
