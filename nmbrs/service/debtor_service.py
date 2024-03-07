from datetime import datetime
from zeep import Client
from zeep.helpers import serialize_object

from service import Service
from nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler
from nmbrs.utils.return_list import return_list
from nmbrs.data_classes.debtor.absence_verzuim import AbsenceVerzuim
from nmbrs.data_classes.debtor.contact_info import ContactInfo
from nmbrs.data_classes.debtor.address import Address
from nmbrs.data_classes.debtor.bank_account import BankAccount
from nmbrs.data_classes.debtor.department import Department
from nmbrs.data_classes.debtor.function import Function
from nmbrs.data_classes.debtor.labour_agreement_settings import LabourAgreementSettings
from nmbrs.data_classes.debtor.manager import Manager
from nmbrs.data_classes.debtor.service_level import ServiceLevel
from nmbrs.data_classes.debtor.tag import Tag
from nmbrs.data_classes.debtor.webhook import WebhookSetting, Event
from nmbrs.data_classes.debtor.debtor import Debtor


class DebtorService(Service):
    """
    A class representing Debtor Service for interacting with Nmbrs debtor-related functionalities.

    Not implemented calls:
        [Converter_GetDebtors_IntToGuid](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Converter_GetDebtors_IntToGuid)
        [Environment_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Environment_Get)
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for DebtorService class.

        Initializes DebtorService instance with authentication and sandbox settings.

        Args:
            auth_header (dict): A dictionary containing authentication details.
            sandbox (bool): A boolean indicating whether to use the sandbox environment.
        """
        super().__init__()
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = self.nmbrs_base_uri
        if sandbox:
            base_uri = self.nmbrs_sandbox_base_uri
        self.debtor_service = Client(f"{base_uri}{self.debtor_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        Args:
            auth_header (dict): A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:List_GetAll"])
    def get_all(self) -> list[Debtor]:
        """
        Retrieve all debtors.

        For more information, refer to the official documentation:
            [Soap call List_GetAll](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=List_GetAll)

        Returns:
            list[Debtor]: A list of Debtor objects representing all debtors.
        """
        debtors = self.debtor_service.service.List_GetAll(_soapheaders=self.auth_header)
        debtors = [Debtor(debtor) for debtor in serialize_object(debtors)]
        return debtors

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:List_GetByNumber"])
    def get_all_by_number(self, number: str) -> list[Debtor]:
        """
        Retrieve all debtors by number.

        For more information, refer to the official documentation:
            [Soap call List_GetByNumber](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=List_GetByNumber)

        Args:
            number (str): The debtor number.

        Returns:
            list[Debtor]: A list of Debtor objects representing all debtors.
        """
        data = {"Number": number}
        debtors = self.debtor_service.service.List_GetByNumber(
            **data, _soapheaders=self.auth_header
        )
        debtors = [Debtor(debtor) for debtor in serialize_object(debtors)]
        return debtors

    @nmbrs_exception_handler(resources=["DebtorService:Debtor_Get"])
    def get(self, debtor_id: int) -> Debtor | None:
        """
        Retrieve a debtor by ID.

        For more information, refer to the official documentation:
            [Soap call Debtor_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Debtor_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            Debtor | None: A Debtor object representing the debtor if found, otherwise None.
        """
        data = {"DebtorId": debtor_id}
        debtor = self.debtor_service.service.Debtor_Get(
            **data, _soapheaders=self.auth_header
        )
        if debtor is None:
            return None
        return Debtor(serialize_object(debtor))

    @nmbrs_exception_handler(resources=["DebtorService:Debtor_Insert"])
    def insert(self, debtor_id: int, number: str, name: str) -> int:
        """
        Insert a new debtor.

        For more information, refer to the official documentation:
            [Soap call Debtor_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Debtor_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            number (str): The number of the debtor.
            name (str): The name of the debtor.

        Returns:
            int: The ID of the inserted debtor if successful.
        """
        data = {"Debtor": {"Id": debtor_id, "Number": number, "Name": name}}
        inserted = self.debtor_service.service.Debtor_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted

    @nmbrs_exception_handler(resources=["DebtorService:Debtor_Update"])
    def update(self, debtor_id: int, number: str, name: str) -> None:
        """
        Update an existing debtor.

        For more information, refer to the official documentation:
            [Soap call Debtor_Update](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Debtor_Update)

        Args:
            debtor_id (int): The ID of the debtor.
            number (str): The new number of the debtor.
            name (str): The new name of the debtor.
        """
        data = {"Debtor": {"Id": debtor_id, "Number": number, "Name": name}}
        self.debtor_service.service.Debtor_Update(**data, _soapheaders=self.auth_header)

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:AbsenceXML_Get"])
    def get_absence_xml(
        self, debtor_id: int, start_date: datetime, end_date: datetime
    ) -> list[AbsenceVerzuim]:
        """
        Retrieve absence data for a debtor within a specified date range.

        For more information, refer to the official documentation:
            [Soap call AbsenceXML_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=AbsenceXML_Get)

        Args:
            debtor_id (int): An integer representing the debtor's ID.
            start_date (datetime): A datetime representing the start date of the period to retrieve data.
            end_date (datetime): A datetime representing the end date of the period to retrieve data.

        Returns:
            list[AbsenceVerzuim]: A list of AbsenceVerzuim objects representing the absence data.
        """
        data = {"DebtorId": debtor_id, "from": start_date, "to": end_date}
        absences = self.debtor_service.service.AbsenceXML_Get(
            **data, _soapheaders=self.auth_header
        )
        absences = [AbsenceVerzuim(absence) for absence in serialize_object(absences)]
        return absences

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:AccountantContact_GetList"])
    def get_all_accountant_contact_info(self) -> list[ContactInfo]:
        """
        Retrieve all accountant contact information.

        For more information, refer to the official documentation:
            [Soap call AccountantContact_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=AccountantContact_GetList)

        Returns:
            list[ContactInfo]: A list of ContactInfo objects representing the accountant contact information.
        """
        accountants = self.debtor_service.service.AccountantContact_GetList(
            _soapheaders=self.auth_header
        )
        accountants = [
            ContactInfo(accountant) for accountant in serialize_object(accountants)
        ]
        return accountants

    @nmbrs_exception_handler(resources=["DebtorService:Address_Get"])
    def get_address(self, debtor_id: int) -> Address | None:
        """
        Retrieve address information for a debtor.

        For more information, refer to the official documentation:
            [Soap call Address_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Address_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            Address | None: An Address object representing the address if found, otherwise None.
        """
        data = {"DebtorId": debtor_id}
        address = self.debtor_service.service.Address_Get(
            **data, _soapheaders=self.auth_header
        )
        if address is None:
            return None
        return Address(serialize_object(address))

    @nmbrs_exception_handler(resources=["DebtorService:BankAccount_Get"])
    def get_bank_account(self, debtor_id: int) -> BankAccount | None:
        """
        Retrieve bank account information for a debtor.

        For more information, refer to the official documentation:
            [Soap call BankAccount_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=BankAccount_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            BankAccount | None: A BankAccount object representing the bank account if found, otherwise None.
        """
        data = {"DebtorId": debtor_id}
        bank_account = self.debtor_service.service.BankAccount_Get(
            **data, _soapheaders=self.auth_header
        )
        if bank_account is None:
            return None
        return BankAccount(serialize_object(bank_account))

    @nmbrs_exception_handler(resources=["DebtorService:ContactPerson_Get"])
    def get_contact_person(self, debtor_id: int) -> ContactInfo | None:
        """
        Retrieve contact person information for a debtor.

        For more information, refer to the official documentation:
            [Soap call ContactPerson_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=ContactPerson_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            ContactInfo | None: A ContactInfo object representing the contact person if found, otherwise None.
        """
        data = {"DebtorId": debtor_id}
        contact_person = self.debtor_service.service.ContactPerson_Get(
            **data, _soapheaders=self.auth_header
        )
        if contact_person is None:
            return None
        return ContactInfo(serialize_object(contact_person))

    @nmbrs_exception_handler(resources=["DebtorService:Debtor_IsOwner"])
    def is_owner(self) -> bool:
        """
        Check if the current user is the owner of the debtor.

        For more information, refer to the official documentation:
            [Soap call Debtor_IsOwner](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Debtor_IsOwner)

        Returns:
            bool: True if the current user is the owner of the debtor, otherwise False.
        """
        is_owner = self.debtor_service.service.Debtor_IsOwner(
            _soapheaders=self.auth_header
        )
        return is_owner

    @nmbrs_exception_handler(resources=["DebtorService:Department_Delete"])
    def delete_department(self, debtor_id: int, department_id: int) -> None:
        """
        Delete a department of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department to delete.
        """
        data = {"DebtorId": debtor_id, "id": department_id}
        self.debtor_service.service.Department_Delete(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Department_GetList"])
    def get_all_departments(self, debtor_id: int) -> list[Department]:
        """
        Retrieve all departments of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_GetList)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[Department]: A list of Department objects representing all departments of the debtor.
        """
        data = {"DebtorId": debtor_id}
        departments = self.debtor_service.service.Department_GetList(
            **data, _soapheaders=self.auth_header
        )
        departments = [
            Department(department) for department in serialize_object(departments)
        ]
        return departments

    @nmbrs_exception_handler(resources=["DebtorService:Department_Insert"])
    def insert_department(
        self, debtor_id: int, department_id: int, code: int, description: str
    ) -> int:
        """
        Insert a new department for a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department.
            code (int): The code of the department.
            description (str): The description of the department.

        Returns:
            int: The ID of the inserted department if successful.
        """
        data = {
            "DebtorId": debtor_id,
            "department": {
                "Id": department_id,
                "Code": code,
                "Description": description,
            },
        }
        inserted = self.debtor_service.service.Department_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted

    @nmbrs_exception_handler(resources=["DebtorService:Department_Update"])
    def update_department(
        self, debtor_id: int, department_id: int, code: int, description: str
    ) -> None:
        """
        Update an existing department of a debtor.

        For more information, refer to the official documentation:
            [Soap call Department_Update](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Department_Update)

        Args:
            debtor_id (int): The ID of the debtor.
            department_id (int): The ID of the department.
            code (int): The code of the department.
            description (str): The description of the department.
        """
        data = {
            "DebtorId": debtor_id,
            "department": {
                "Id": department_id,
                "Code": code,
                "Description": description,
            },
        }
        self.debtor_service.service.Department_Update(
            **data, _soapheaders=self.auth_header
        )

    @nmbrs_exception_handler(resources=["DebtorService:Function_Delete"])
    def delete_function(self, debtor_id: int, function_id: int) -> None:
        """
        Delete a function of a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function to be deleted.
        """
        data = {"DebtorId": debtor_id, "id": function_id}
        self.debtor_service.service.Function_Delete(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Function_GetList"])
    def get_all_functions(self, debtor_id: int, function_id: int) -> list[Function]:
        """
        Retrieve all functions of a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_GetList)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.

        Returns:
            list[Function]: A list of Function objects representing all functions of the debtor.
        """
        data = {"DebtorId": debtor_id, "id": function_id}
        functions = self.debtor_service.service.Function_GetList(
            **data, _soapheaders=self.auth_header
        )
        functions = [Function(function) for function in serialize_object(functions)]
        return functions

    @nmbrs_exception_handler(resources=["DebtorService:Function_Insert"])
    def insert_function(
        self, debtor_id: int, function_id: int, code: int, description: str
    ) -> int:
        """
        Insert a new function for a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.
            code (int): The code of the function.
            description (str): The description of the function.

        Returns:
            int: The ID of the inserted function if successful.
        """
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        inserted = self.debtor_service.service.Function_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted

    @nmbrs_exception_handler(resources=["DebtorService:Function_Update"])
    def update_function(
        self, debtor_id: int, function_id: int, code: int, description: str
    ) -> None:
        """
        Update a function for a debtor.

        For more information, refer to the official documentation:
            [Soap call Function_Update](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Function_Update)

        Args:
            debtor_id (int): The ID of the debtor.
            function_id (int): The ID of the function.
            code (int): The code of the function.
            description (str): The description of the function.
        """
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        self.debtor_service.service.Function_Update(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(
        resources=["DebtorService:LabourAgreementSettings_GetList"]
    )
    def get_all_labour_agreements(
        self, debtor_id: int, year: int, period: int
    ) -> list[LabourAgreementSettings]:
        """
        Retrieve all labour agreement settings for a debtor.

        For more information, refer to the official documentation:
            [Soap call LabourAgreementSettings_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=LabourAgreementSettings_GetList)

        Args:
            debtor_id (int): The ID of the debtor.
            year (int): The year for which to retrieve labour agreement settings.
            period (int): The period for which to retrieve labour agreement settings.

        Returns:
            list[LabourAgreementSettings]: A list of LabourAgreementSettings objects representing all labour
            agreement settings.
        """
        data = {"DebtorId": debtor_id, "Year": year, "Period": period}
        labour_agreements = self.debtor_service.service.LabourAgreementSettings_GetList(
            **data, _soapheaders=self.auth_header
        )
        labour_agreements = [
            LabourAgreementSettings(labour_agreement)
            for labour_agreement in serialize_object(labour_agreements)
        ]
        return labour_agreements

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Manager_GetList"])
    def get_all_managers(self, debtor_id: int) -> list[Manager]:
        """
        Retrieve all managers for a debtor.

        For more information, refer to the official documentation:
            [Soap call Manager_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Manager_GetList)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[Manager]: A list of Manager objects representing all managers for the debtor.
        """
        data = {"DebtorId": debtor_id}
        managers = self.debtor_service.service.Manager_GetList(
            **data, _soapheaders=self.auth_header
        )
        managers = [Manager(manager) for manager in serialize_object(managers)]
        return managers

    @nmbrs_exception_handler(resources=["DebtorService:ServiceLevel_Get"])
    def get_service_level(self, debtor_id: int) -> ServiceLevel | None:
        """
        Retrieve service level information for a debtor.

        For more information, refer to the official documentation:
            [Soap call ServiceLevel_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=ServiceLevel_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            ServiceLevel | None: A ServiceLevel object representing the service level information if found, otherwise
            None.
        """
        data = {"DebtorId": debtor_id}
        service_level = self.debtor_service.service.ServiceLevel_Get(
            **data, _soapheaders=self.auth_header
        )
        if service_level is None:
            return None
        return ServiceLevel(serialize_object(service_level))

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Tags_Get"])
    def get_tags(self, debtor_id: int) -> list[Tag]:
        """
        Retrieve all tags for a debtor.

        For more information, refer to the official documentation:
            [Soap call Tags_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Tags_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[Tag]: A list of Tag objects representing all tags associated with the debtor.
        """
        data = {"DebtorId": debtor_id}
        tags = self.debtor_service.service.Tags_Get(
            **data, _soapheaders=self.auth_header
        )
        tags = [Tag(tag) for tag in serialize_object(tags)]
        return tags

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:Title_GetList"])
    def get_all_titles(self, debtor_id: int) -> list[str]:
        """
        Retrieve all titles for a debtor.

        For more information, refer to the official documentation:
            [Soap call Title_GetList](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Title_GetList)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[str]: A list of strings representing all titles associated with the debtor.
        """
        data = {"DebtorId": debtor_id}
        titles = self.debtor_service.service.Title_GetList(
            **data, _soapheaders=self.auth_header
        )
        titles = [title["TitleName"] for title in serialize_object(titles)]
        return titles

    @nmbrs_exception_handler(resources=["DebtorService:Title_Insert"])
    def insert_titles(self, debtor_id: int, title: str) -> None:
        """
        Insert a title for a debtor.

        For more information, refer to the official documentation:
            [Soap call Title_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Title_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            title (str): The title to be inserted.
        """
        data = {"DebtorId": debtor_id, "title": {"TitleName": title}}
        self.debtor_service.service.Title_Insert(**data, _soapheaders=self.auth_header)

    @nmbrs_exception_handler(resources=["DebtorService:WebhookSettings_Delete"])
    def delete_webhook(self, debtor_id: int, webhook_id: int) -> bool:
        """
        Delete a webhook for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            webhook_id (int): The ID of the webhook to be deleted.

        Returns:
            bool: True if the webhook is successfully deleted, otherwise False.
        """
        data = {"DebtorId": debtor_id, "WebhookSettingId": webhook_id}
        deleted = self.debtor_service.service.WebhookSettings_Delete(
            **data, _soapheaders=self.auth_header
        )
        return deleted

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:WebhookSettings_Get"])
    def get_webhooks(self, debtor_id: int) -> list[WebhookSetting]:
        """
        Retrieve all webhooks for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[WebhookSetting]: A list of WebhookSetting objects representing all webhooks associated with the debtor.
        """
        data = {"DebtorId": debtor_id}
        webhooks = self.debtor_service.service.WebhookSettings_Get(
            **data, _soapheaders=self.auth_header
        )
        webhooks = [WebhookSetting(webhook) for webhook in serialize_object(webhooks)]
        return webhooks

    @return_list
    @nmbrs_exception_handler(resources=["DebtorService:WebhookSettings_GetEvents"])
    def get_webhook_events(self) -> list[Event]:
        """
        Retrieve all webhook events.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_GetEvents](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_GetEvents)

        Returns:
            list[Event]: A list of Event objects representing all webhook events.
        """
        events = self.debtor_service.service.WebhookSettings_GetEvents(
            _soapheaders=self.auth_header
        )
        events = [Event(event) for event in serialize_object(events)]
        return events

    @nmbrs_exception_handler(resources=["DebtorService:WebhookSettings_Insert"])
    def insert_webhook(
        self, debtor_id: int, insert_webhook_settings: WebhookSetting
    ) -> int:
        """
        Insert a webhook for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            insert_webhook_settings (WebhookSetting): The WebhookSetting object to be inserted.

        Returns:
            int: The ID of the inserted webhook.
        """
        data = {
            "DebtorId": debtor_id,
            "WebhookSetting": insert_webhook_settings.to_insert_dict(),
        }
        inserted = self.debtor_service.service.WebhookSettings_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted
