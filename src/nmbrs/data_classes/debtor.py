"""This module defines various data classes for representing different entities in the system."""

from datetime import datetime

from .data_class import DataClass
from .utils.xml import parse_xml_to_dict


class Domain(DataClass):
    """A class representing domain."""

    def __init__(self, data: dict) -> None:
        self.domain: int = data.get("Domain", None)
        self.sub_domain: int = data.get("SubDomain", None)


class AbsenceVerzuim(DataClass):
    """A class representing absence data."""

    def __init__(self, data: dict) -> None:
        self.debtor_id: int = data.get("DebtorID", None)
        self.company_id: int = data.get("CompanyID", None)
        self.employee_id: int = data.get("EmployeeID", None)
        self.xml: str = data.get("XML", None)

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
        self.id: int = data.get("Id", None)
        self.default: bool = data.get("Default", None)
        self.street: str = data.get("Street", None)
        self.house_number: str = data.get("HouseNumber", None)
        self.house_number_addition: str = data.get("HouseNumberAddition", None)
        self.postal_code: str = data.get("PostalCode", None)
        self.city: str = data.get("City", None)
        self.state_province: str = data.get("StateProvince", None)
        self.country_iso_code: str = data.get("CountryISOCode", None)


class BankAccount(DataClass):
    """A class representing a bank account."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id", None)
        self.number: str = data.get("Number", None)
        self.description: str = data.get("Description", None)
        self.iban: str = data.get("IBAN", None)
        self.bic: str = data.get("BIC", None)
        self.city: str = data.get("City", None)
        self.name: str = data.get("Name", None)
        self.type: str = data.get("Type", None)


class ContactInfo(DataClass):
    """A class representing a contact info."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.email: str = data.get("Email", None)
        self.name: str = data.get("Name", None)
        self.phone: str = data.get("Phone", None)


class Debtor(DataClass):
    """A class representing a debtor."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("Id", None)
        self.number: str = data.get("Number", None)
        self.name: str = data.get("Name", None)


class Department(DataClass):
    """A class representing a department."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id", None)
        self.code: int = data.get("Code", None)
        self.description: str = data.get("Description", None)


class Function(DataClass):
    """A class representing a function."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id", None)
        self.code: int = data.get("Code", None)
        self.description: str = data.get("Description", None)


class LabourAgreementSettings(DataClass):
    """A class representing labour agreement settings."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.id: int = data.get("Id", None)
        self.guid: str = data.get("Guid", None)
        self.int_number: int = data.get("IntNumber", None)
        self.str_name: str = data.get("StrName", None)
        self.debtor_id: int = data.get("IntDebiteurID", None)


class Manager(DataClass):
    """A class representing manager information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.number: int = data.get("Number", None)
        self.first_name: str = data.get("FirstName", None)
        self.name: str = data.get("Name", None)
        self.department: str = data.get("Department", None)
        self.function: str = data.get("Function", None)
        self.phone_number: str = data.get("PhoneNumber", None)
        self.mobile: str = data.get("Mobile", None)
        self.fax: str = data.get("Fax", None)
        self.email: str = data.get("Email", None)


class ServiceLevel(DataClass):
    """A class representing service level information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.start_period: int = data.get("StartPeriod", None)
        self.start_year: int = data.get("StartYear", None)
        self.service_level: str = data.get("ServiceLevel", None)
        self.start_contract: datetime = data.get("StartContract", None)


class Tag(DataClass):
    """A class representing debtor tag information."""

    def __init__(self, debtor_id: int, data: dict) -> None:
        self.debtor_id = debtor_id
        self.number: int = data.get("Number", None)
        self.hex_color: str = data.get("HexColor", None)
        self.tag: str = data.get("Tag", None)


class Event(DataClass):
    """A class representing an event."""

    def __init__(self, data: dict) -> None:
        self.event_id: int = data.get("EventId", None)
        self.event_name: str = data.get("EventName", None)
        self.active: bool = data.get("Active", None)

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
        self.webhook_setting_id: int = data.get("WebhookSettingId", None)
        self.name: str = data.get("Name", None)
        self.endpoint: str = data.get("Endpoint", None)
        self.active: bool = data.get("Active", None)
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
