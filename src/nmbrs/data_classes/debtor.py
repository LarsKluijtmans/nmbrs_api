"""This module defines various data classes for representing different entities in the system."""

from datetime import datetime

from .data_class import DataClass
from .utils.xml import parse_xml_to_dict


class Domain(DataClass):
    """A class representing domain."""

    def __init__(self, data: dict) -> None:
        self.domain: str = data.get("Domain")
        self.sub_domain: str = data.get("SubDomain")


class AbsenceVerzuim(DataClass):
    """A class representing absence data."""

    def __init__(self, data: dict) -> None:
        self.debtor_id: int = data.get("DebtorID")
        self.company_id: int = data.get("CompanyID")
        self.employee_id: int = data.get("EmployeeID")
        self.xml: str = data.get("XML")

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return {
            "debtor_id": self.debtor_id,
            "company_id": self.company_id,
            "employee_id": self.employee_id,
            "xml": parse_xml_to_dict(self.xml),
        }


class Address(DataClass):
    """A class representing an address."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id")
        self.default: bool = data.get("Default")
        self.street: str = data.get("Street")
        self.house_number: str = data.get("HouseNumber")
        self.house_number_addition: str = data.get("HouseNumberAddition")
        self.postal_code: str = data.get("PostalCode")
        self.city: str = data.get("City")
        self.state_province: str = data.get("StateProvince")
        self.country_iso_code: str = data.get("CountryISOCode")


class BankAccount(DataClass):
    """A class representing a bank account."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id")
        self.number: str = data.get("Number")
        self.description: str = data.get("Description")
        self.iban: str = data.get("IBAN")
        self.bic: str = data.get("BIC")
        self.city: str = data.get("City")
        self.name: str = data.get("Name")
        self.type: str = data.get("Type")


class ContactInfo(DataClass):
    """A class representing a contact info."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.email: str = data.get("Email")
        self.name: str = data.get("Name")
        self.phone: str = data.get("Phone")


class Debtor(DataClass):
    """A class representing a debtor."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("Id")
        self.number: str = data.get("Number")
        self.name: str = data.get("Name")


class Department(DataClass):
    """A class representing a department."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class Function(DataClass):
    """A class representing a function."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class LabourAgreementSettings(DataClass):
    """A class representing labour agreement settings."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id")
        self.guid: str = data.get("Guid")
        self.int_number: int = data.get("IntNumber")
        self.str_name: str = data.get("StrName")
        self.debtor_id: int = data.get("IntDebiteurID")


class Manager(DataClass):
    """A class representing manager information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.number: int = data.get("Number")
        self.first_name: str = data.get("FirstName")
        self.name: str = data.get("Name")
        self.department: str = data.get("Department")
        self.function: str = data.get("Function")
        self.phone_number: str = data.get("PhoneNumber")
        self.mobile: str = data.get("Mobile")
        self.fax: str = data.get("Fax")
        self.email: str = data.get("Email")


class ServiceLevel(DataClass):
    """A class representing service level information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.start_period: int = data.get("StartPeriod")
        self.start_year: int = data.get("StartYear")
        self.service_level: str = data.get("ServiceLevel")
        self.start_contract: datetime = data.get("StartContract")


class Tag(DataClass):
    """A class representing debtor tag information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.number: int = data.get("Number")
        self.hex_color: str = data.get("HexColor")
        self.tag: str = data.get("Tag")


class Event(DataClass):
    """A class representing an event."""

    def __init__(self, data: dict) -> None:
        self.event_id: int = data.get("EventId")
        self.event_name: str = data.get("EventName")
        self.active: bool = data.get("Active")

    def to_insert_dict(self) -> dict:
        """
        Convert the instance to a dictionary representing the XML insert format.

        :return: A dictionary representation of the event instance.
        """
        return {
            "EventId": self.event_id,
            "Active": self.active,
        }


class WebhookSetting(DataClass):
    """A class representing a webhook setting."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.webhook_setting_id: int = data.get("WebhookSettingId")
        self.name: str = data.get("Name")
        self.endpoint: str = data.get("Endpoint")
        self.active: bool = data.get("Active")
        events_data = data.get("Event", [])
        if not isinstance(events_data, list):
            events_data = [events_data]
        self.events: list[Event] = [Event(event_data) for event_data in events_data]

    def to_insert_dict(self) -> dict:
        """
        Convert the instance to a dictionary representing the XML insert format.

        :return: A dictionary representation of the webhook setting instance.
        """
        event_dicts = [event.to_insert_dict() for event in self.events] if self.events else []
        return {
            "WebhookSetting": {
                "Name": self.name,
                "Endpoint": self.endpoint,
                "Active": self.active,
                "Events": event_dicts,
            }
        }
