# pylint: disable=line-too-long
"""Microservice responsible for personal info related actions on the employee level."""
from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import PersonalInfo, PersonalInfoContractSalaryAddress
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeePersonalInfoService(MicroService):
    """Microservice responsible for personal info related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfo_Get")
    def get(self, employee_id: int, period: int, year: int) -> PersonalInfo | None:
        """
        Get the active personal info for given period.

        For more information, refer to the official documentation:
            [PersonalInfo_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_Get)

        Args:
            employee_id (int): The ID of the employee.
            period (int): The period for which personal information is retrieved.
            year (int): The year for which personal information is retrieved.

        Returns:
            PersonalInfo | None: The personal information of the employee for the specified period, or None if not found.
        """
        personal_info = self.client.service.PersonalInfo_Get(
            EmployeeId=employee_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        if not personal_info:
            return None
        return PersonalInfo(employee_id=employee_id, data=serialize_object(personal_info))

    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfo_GetCurrent")
    def get_current(self, employee_id: int) -> PersonalInfo | None:
        """
        Get the currently active personal info.

        For more information, refer to the official documentation:
            [PersonalInfo_GetCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_GetCurrent)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            PersonalInfo | None: The currently active personal information of the employee, or None if not found.
        """
        personal_info = self.client.service.PersonalInfo_GetCurrent(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        if not personal_info:
            return None
        return PersonalInfo(employee_id=employee_id, data=serialize_object(personal_info))

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfo_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[PersonalInfo]:
        """
        Get all personal infos of all employees.

        For more information, refer to the official documentation:
            [PersonalInfo_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[PersonalInfo]: A list of personal information objects of all employees within the company.
        """
        people_info = self.client.service.PersonalInfo_GetAll_AllEmployeesByCompany(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )

        _people_info = []
        for person in serialize_object(people_info):
            for info in person["EmployeePersonalInfos"]["PersonalInfo_V2"]:
                _people_info.append(PersonalInfo(employee_id=person["EmployeeId"], data=info))

        return _people_info

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany")
    def get_all_by_company_without_bsn(self, company_id: int) -> list[PersonalInfo]:
        """
        Get all personal infos of all employees, excluding the BSN.

        For more information, refer to the official documentation:
            [PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[PersonalInfo]: A list of personal information objects of all employees within the company, excluding the BSN.
        """
        people_info = self.client.service.PersonalInfoWithoutBSN_Get_GetAllEmployeesByCompany(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )

        _people_info = []
        for person in serialize_object(people_info):
            for info in person["EmployeePersonalInfos"]["PersonalInfo_V2"]:
                _people_info.append(PersonalInfo(employee_id=person["EmployeeId"], data=info))

        return _people_info

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany")
    def get_all_by_company_contract_address_salary(self, company_id: int) -> list[PersonalInfoContractSalaryAddress]:
        """
        Get all personal infos of all employees.

        For more information, refer to the official documentation:
            [PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[PersonalInfoContractSalaryAddress]: A list of personal information objects including contract and salary address of all employees within the company.
        """
        people_info = self.client.service.PersonalInfoContractSalaryAddress_GetAll_AllEmployeesByCompany(
            CompanyID=company_id, _soapheaders=self.auth_manager.header
        )
        return [
            PersonalInfoContractSalaryAddress(employee_id=person["EmployeeID"], data=person) for person in serialize_object(people_info)
        ]

    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfo_Update")
    def update(self, employee_id: int, personal_info: PersonalInfo, period: int, year: int):
        """
        Update personal info starting from the given period.

        For more information, refer to the official documentation:
            [PersonalInfo_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_Update)

        Args:
            employee_id (int): The ID of the employee.
            personal_info (PersonalInfo): The updated personal information.
            period (int): The period from which the update should take effect.
            year (int): The year from which the update should take effect.
        """
        new_personal_info = {
            "Id": employee_id,
            "Number": personal_info.employee_number,
            "EmployeeNumber": personal_info.employee_number,
            "BSN": personal_info.bsn,
            "Title": personal_info.title,
            "FirstName": personal_info.first_name,
            "Initials": personal_info.initials,
            "Prefix": personal_info.prefix,
            "LastName": personal_info.last_name,
            "Nickname": personal_info.nickname,
            "Gender": personal_info.gender,
            "NationalityCode": personal_info.nationality_code,
            "PlaceOfBirth": personal_info.place_of_birth,
            "CountryOfBirthISOCode": personal_info.country_of_birth_iso_code,
            "IdentificationNumber": personal_info.identification_number,
            "IdentificationType": personal_info.identification_type,
            "PartnerPrefix": personal_info.partner_prefix,
            "PartnerLastName": personal_info.partner_last_name,
            "TelephonePrivate": personal_info.telephone_private,
            "TelephoneWork": personal_info.telephone_work,
            "TelephoneMobilePrivate": personal_info.telephone_mobile_private,
            "TelephoneMobileWork": personal_info.telephone_mobile_work,
            "TelephoneOther": personal_info.telephone_other,
            "EmailPrivate": personal_info.email_private,
            "EmailWork": personal_info.email_work,
            "BurgerlijkeStaat": personal_info.burgerlijke_staat,
            "Naamstelling": personal_info.naamstelling,
            "Birthday": personal_info.birthday,
            "DeceasedDate": personal_info.deceased_date,
            "InCaseOfEmergency": personal_info.in_case_of_emergency,
            "InCaseOfEmergencyPhone": personal_info.in_case_of_emergency_phone,
            "InCaseOfEmergencyRelation": personal_info.in_case_of_emergency_relation,
            "TitleAfter": personal_info.title_after,
        }
        response = self.client.service.PersonalInfo_Update(
            EmployeeId=employee_id, PersonalInfo=new_personal_info, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:PersonalInfo_UpdateCurrent")
    def update_current(self, employee_id: int, personal_info: PersonalInfo):
        """
        Update personal info starting from the current period.

        For more information, refer to the official documentation:
            [PersonalInfo_UpdateCurrent](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=PersonalInfo_UpdateCurrent)

        Args:
            employee_id (int): The ID of the employee.
            personal_info (PersonalInfo): The updated personal information.
        """
        new_personal_info = {
            "Id": employee_id,
            "Number": personal_info.employee_number,
            "EmployeeNumber": personal_info.employee_number,
            "BSN": personal_info.bsn,
            "Title": personal_info.title,
            "FirstName": personal_info.first_name,
            "Initials": personal_info.initials,
            "Prefix": personal_info.prefix,
            "LastName": personal_info.last_name,
            "Nickname": personal_info.nickname,
            "Gender": personal_info.gender,
            "NationalityCode": personal_info.nationality_code,
            "PlaceOfBirth": personal_info.place_of_birth,
            "CountryOfBirthISOCode": personal_info.country_of_birth_iso_code,
            "IdentificationNumber": personal_info.identification_number,
            "IdentificationType": personal_info.identification_type,
            "PartnerPrefix": personal_info.partner_prefix,
            "PartnerLastName": personal_info.partner_last_name,
            "TelephonePrivate": personal_info.telephone_private,
            "TelephoneWork": personal_info.telephone_work,
            "TelephoneMobilePrivate": personal_info.telephone_mobile_private,
            "TelephoneMobileWork": personal_info.telephone_mobile_work,
            "TelephoneOther": personal_info.telephone_other,
            "EmailPrivate": personal_info.email_private,
            "EmailWork": personal_info.email_work,
            "BurgerlijkeStaat": personal_info.burgerlijke_staat,
            "Naamstelling": personal_info.naamstelling,
            "Birthday": personal_info.birthday,
            "DeceasedDate": personal_info.deceased_date,
            "InCaseOfEmergency": personal_info.in_case_of_emergency,
            "InCaseOfEmergencyPhone": personal_info.in_case_of_emergency_phone,
            "InCaseOfEmergencyRelation": personal_info.in_case_of_emergency_relation,
            "TitleAfter": personal_info.title_after,
        }
        response = self.client.service.PersonalInfo_UpdateCurrent(
            EmployeeId=employee_id, PersonalInfo=new_personal_info, _soapheaders=self.auth_manager.header
        )
        return response
