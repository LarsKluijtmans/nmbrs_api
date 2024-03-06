from datetime import datetime
from zeep import Client
from zeep.helpers import serialize_object

from nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler
from nmbrs.utils.return_list import return_list
from nmbrs.service.service import Service
from nmbrs.data_classes.debtor.debtor import Debtor
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


class DebtorService(Service):
    """
    A class representing Debtor Service for interacting with Nmbrs debtor-related functionalities.

    Not implemented calls:

    (Converter_GetDebtors_IntToGuid)[https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Converter_GetDebtors_IntToGuid]
    (Environment_Get)[https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=Environment_Get]
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for DebtorService class.

        Initializes DebtorService instance with authentication and sandbox settings.

        :param auth_header: A dictionary containing authentication details.
        :param sandbox: A boolean indicating whether to use the sandbox environment.
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

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(["DebtorService:List_GetAll"])
    def get_all(self) -> list[Debtor]:
        """
        Retrieve all debtors.

        Calls the SOAP operation 'List_GetAll' from the debtor service with the provided authentication header.
        Converts the retrieved debtors into Debtor objects.

        For more information, refer to the official documentation:
        [Soap call AbsenceXML_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=List_GetAll)

        :return: A list of Debtor objects representing all debtors.
        """
        debtors = self.debtor_service.service.List_GetAll(_soapheaders=self.auth_header)
        debtors = [Debtor(debtor) for debtor in serialize_object(debtors)]
        return debtors

    @return_list
    @nmbrs_exception_handler(["DebtorService:List_GetByNumber"])
    def get_all_by_number(self, number: str) -> list[Debtor]:
        """
        Retrieve all debtors.

        Calls the SOAP operation 'List_GetByNumber' from the debtor service with the provided authentication header.
        Converts the retrieved debtors into Debtor objects.

        For more information, refer to the official documentation:
        [Soap call AbsenceXML_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=List_GetByNumber)

        :return: A list of Debtor objects representing all debtors.
        """
        data = {"Number": number}
        debtors = self.debtor_service.service.List_GetByNumber(
            **data, _soapheaders=self.auth_header
        )
        debtors = [Debtor(debtor) for debtor in serialize_object(debtors)]
        return debtors

    @nmbrs_exception_handler(["DebtorService:Debtor_Get"])
    def get(self, debtor_id: int) -> Debtor | None:
        data = {"DebtorId": debtor_id}
        debtor = self.debtor_service.service.Debtor_Get(
            **data, _soapheaders=self.auth_header
        )
        if debtor is None:
            return None
        return Debtor(debtor)

    @nmbrs_exception_handler(["DebtorService:Debtor_Insert"])
    def insert(self, debtor_id: int, number: str, name: str) -> int | None:
        data = {"Debtor": {"Id": debtor_id, "Number": number, "Name": name}}
        inserted = self.debtor_service.service.Debtor_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted

    @nmbrs_exception_handler(["DebtorService:Debtor_Update"])
    def update(self, debtor_id: int, number: str, name: str) -> None:
        data = {"Debtor": {"Id": debtor_id, "Number": number, "Name": name}}
        self.debtor_service.service.Debtor_Update(**data, _soapheaders=self.auth_header)

    @return_list
    @nmbrs_exception_handler(["DebtorService:AbsenceXML_Get"])
    def get_absence_xml(
        self, debtor_id: int, start_date: datetime, end_date: datetime
    ) -> list[AbsenceVerzuim]:
        """
        Retrieve absence data for a debtor within a specified date range.

        This method calls the SOAP operation 'AbsenceXML_Get' from the Nmbrs API,
        which retrieves absence data for the specified debtor within the provided date range.

        For more information, refer to the official documentation:
        [Soap call AbsenceXML_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=AbsenceXML_Get)

        :param debtor_id: An integer representing the debtor's ID.
        :param start_date: A datetime representing the start date of the period to retrieve data.
        :param end_date: A datetime representing the end date of the period to retrieve data.
        :return: A list of AbsenceVerzuim objects representing the absence data.
        """
        data = {"DebtorId": debtor_id, "from": start_date, "to": end_date}
        absences = self.debtor_service.service.AbsenceXML_Get(
            **data, _soapheaders=self.auth_header
        )
        absences = [AbsenceVerzuim(absence) for absence in serialize_object(absences)]
        return absences

    @return_list
    @nmbrs_exception_handler(["DebtorService:AccountantContact_GetList"])
    def get_all_accountant_contact_info(self) -> list[ContactInfo]:
        accountants = self.debtor_service.service.AccountantContact_GetList(
            _soapheaders=self.auth_header
        )
        accountants = [
            ContactInfo(accountant) for accountant in serialize_object(accountants)
        ]
        return accountants

    @nmbrs_exception_handler(["DebtorService:Address_Get"])
    def get_address(self, debtor_id: int) -> Address | None:
        data = {"DebtorId": debtor_id}
        address = self.debtor_service.service.Address_Get(
            **data, _soapheaders=self.auth_header
        )
        if address is None:
            return None
        return Address(address)

    @nmbrs_exception_handler(["DebtorService:BankAccount_Get"])
    def get_bank_account(self, debtor_id: int) -> BankAccount | None:
        data = {"DebtorId": debtor_id}
        bank_account = self.debtor_service.service.BankAccount_Get(
            **data, _soapheaders=self.auth_header
        )
        if bank_account is None:
            return None
        return BankAccount(bank_account)

    @nmbrs_exception_handler(["DebtorService:ContactPerson_Get"])
    def get_contact_person(self, debtor_id: int) -> ContactInfo | None:
        data = {"DebtorId": debtor_id}
        contact_person = self.debtor_service.service.ContactPerson_Get(
            **data, _soapheaders=self.auth_header
        )
        if contact_person is None:
            return None
        return ContactInfo(contact_person)

    @nmbrs_exception_handler(["DebtorService:Debtor_IsOwner"])
    def is_owner(self) -> bool | None:
        is_owner = self.debtor_service.service.Debtor_IsOwner(
            _soapheaders=self.auth_header
        )
        return is_owner

    @nmbrs_exception_handler(["DebtorService:Department_Delete"])
    def delete_department(self, debtor_id: int, department_id: int) -> None:
        data = {"DebtorId": debtor_id, "id": department_id}
        self.debtor_service.service.Department_Delete(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(["DebtorService:Department_GetList"])
    def get_all_departments(self, debtor_id: int) -> list[Department]:
        data = {"DebtorId": debtor_id}
        departments = self.debtor_service.service.Department_GetList(
            **data, _soapheaders=self.auth_header
        )
        departments = [
            Department(department) for department in serialize_object(departments)
        ]
        return departments

    @nmbrs_exception_handler(["DebtorService:Department_Insert"])
    def insert_department(
        self, debtor_id: int, department_id: int, code: int, description: str
    ) -> int | None:
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

    @nmbrs_exception_handler(["DebtorService:Department_Update"])
    def update_department(
        self, debtor_id: int, department_id: int, code: int, description: str
    ) -> None:
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

    @nmbrs_exception_handler(["DebtorService:Function_Delete"])
    def delete_function(self, debtor_id: int, function_id: int) -> None:
        data = {"DebtorId": debtor_id, "id": function_id}
        self.debtor_service.service.Function_Delete(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(["DebtorService:Function_GetList"])
    def get_all_functions(self, debtor_id: int, function_id: int) -> list[Function]:
        data = {"DebtorId": debtor_id, "id": function_id}
        functions = self.debtor_service.service.Function_GetList(
            **data, _soapheaders=self.auth_header
        )
        functions = [Function(function) for function in serialize_object(functions)]
        return functions

    @nmbrs_exception_handler(["DebtorService:Function_Insert"])
    def insert_function(
        self, debtor_id: int, function_id: int, code: int, description: str
    ) -> int | None:
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        inserted = self.debtor_service.service.Function_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted

    @nmbrs_exception_handler(["DebtorService:Function_Update"])
    def update_function(
        self, debtor_id: int, function_id: int, code: int, description: str
    ) -> None:
        data = {
            "DebtorId": debtor_id,
            "function": {"Id": function_id, "Code": code, "Description": description},
        }
        self.debtor_service.service.Function_Update(
            **data, _soapheaders=self.auth_header
        )

    @return_list
    @nmbrs_exception_handler(["DebtorService:LabourAgreementSettings_GetList"])
    def get_all_labour_agreements(
        self, debtor_id: int, year: int, period: int
    ) -> list[LabourAgreementSettings]:
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
    @nmbrs_exception_handler(["DebtorService:Manager_GetList"])
    def get_all_managers(self, debtor_id: int) -> list[Manager]:
        data = {"DebtorId": debtor_id}
        managers = self.debtor_service.service.Manager_GetList(
            **data, _soapheaders=self.auth_header
        )
        managers = [Manager(manager) for manager in serialize_object(managers)]
        return managers

    @nmbrs_exception_handler(["DebtorService:ServiceLevel_Get"])
    def get_service_level(self, debtor_id: int) -> ServiceLevel | None:
        data = {"DebtorId": debtor_id}
        service_level = self.debtor_service.service.ServiceLevel_Get(
            **data, _soapheaders=self.auth_header
        )
        if service_level is None:
            return None
        return ServiceLevel(service_level)

    @return_list
    @nmbrs_exception_handler(["DebtorService:Tags_Get"])
    def get_tags(self, debtor_id: int) -> list[Tag]:
        data = {"DebtorId": debtor_id}
        tags = self.debtor_service.service.Tags_Get(
            **data, _soapheaders=self.auth_header
        )
        tags = [Tag(tag) for tag in serialize_object(tags)]
        return tags

    @return_list
    @nmbrs_exception_handler(["DebtorService:Title_GetList"])
    def get_all_titles(self, debtor_id: int) -> list[str]:
        data = {"DebtorId": debtor_id}
        titles = self.debtor_service.service.Title_GetList(
            **data, _soapheaders=self.auth_header
        )
        titles = [title["TitleName"] for title in serialize_object(titles)]
        return titles

    @nmbrs_exception_handler(["DebtorService:Title_Insert"])
    def insert_titles(self, debtor_id: int, title: str) -> None:
        data = {"DebtorId": debtor_id, "title": {"TitleName": title}}
        self.debtor_service.service.Title_Insert(**data, _soapheaders=self.auth_header)

    @nmbrs_exception_handler(["DebtorService:WebhookSettings_Delete"])
    def delete_webhook(self, debtor_id: int, webhook_id: int) -> bool:
        data = {"DebtorId": debtor_id, "WebhookSettingId": webhook_id}
        deleted = self.debtor_service.service.WebhookSettings_Delete(
            **data, _soapheaders=self.auth_header
        )
        return deleted

    @return_list
    @nmbrs_exception_handler(["DebtorService:WebhookSettings_Get"])
    def get_webhooks(self, debtor_id: int) -> list[WebhookSetting]:
        data = {"DebtorId": debtor_id}
        webhooks = self.debtor_service.service.WebhookSettings_Get(
            **data, _soapheaders=self.auth_header
        )
        webhooks = [WebhookSetting(webhook) for webhook in serialize_object(webhooks)]
        return webhooks

    @return_list
    @nmbrs_exception_handler(["DebtorService:WebhookSettings_GetEvents"])
    def get_webhook_events(self) -> list[Event]:
        events = self.debtor_service.service.WebhookSettings_GetEvents(
            _soapheaders=self.auth_header
        )
        events = [Event(event) for event in serialize_object(events)]
        return events

    @nmbrs_exception_handler(["DebtorService:WebhookSettings_Insert"])
    def insert_webhook(
        self, debtor_id: int, insert_webhook_settings: WebhookSetting
    ) -> int:
        data = {
            "DebtorId": debtor_id,
            "WebhookSetting": insert_webhook_settings.to_insert_dict(),
        }
        inserted = self.debtor_service.service.WebhookSettings_Insert(
            **data, _soapheaders=self.auth_header
        )
        return inserted
