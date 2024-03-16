"""
This module defines various data classes for representing different entities in the system.

Classes:
- AbsenceVerzuim: A class representing absence data.
- Address: A class representing an address.
- BankAccount: A class representing a bank account.
- ContactInfo: A class representing contact information.
- Debtor: A class representing a debtor.
- Department: A class representing a department.
- Function: A class representing a function.
- LabourAgreementSettings: A class representing labour agreement settings.
- Manager: A class representing manager information.
- ServiceLevel: A class representing service level information.
- Tag: A class representing debtor tag information.
- Event: A class representing an event.
- WebhookSetting: A class representing a webhook setting.

Dependencies:
- DataClass: A base class for data classes.
- datetime: Module providing classes for manipulating dates and times.
- parse_xml_to_dict: Function for parsing XML data into a dictionary.
"""

from datetime import datetime

from .data_class import DataClass
from .utils.xml import parse_xml_to_dict


class AbsenceVerzuim(DataClass):
    """
    A class representing absence data.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.debtor_id: int = obj.get("DebtorID", None)
        self.company_id: int = obj.get("CompanyID", None)
        self.employee_id: int = obj.get("EmployeeID", None)
        self.xml: str = obj.get("XML", None)

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
    """
    A class representing an address.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.default: bool = obj.get("Default", None)
        self.street: str = obj.get("Street", None)
        self.house_number: str = obj.get("HouseNumber", None)
        self.house_number_addition: str = obj.get("HouseNumberAddition", None)
        self.postal_code: str = obj.get("PostalCode", None)
        self.city: str = obj.get("City", None)
        self.state_province: str = obj.get("StateProvince", None)
        self.country_iso_code: str = obj.get("CountryISOCode", None)


class BankAccount(DataClass):
    """
    A class representing a bank account.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.number: str = obj.get("Number", None)
        self.description: str = obj.get("Description", None)
        self.iban: str = obj.get("IBAN", None)
        self.bic: str = obj.get("BIC", None)
        self.city: str = obj.get("City", None)
        self.name: str = obj.get("Name", None)
        self.type: str = obj.get("Type", None)


class ContactInfo(DataClass):
    """
    A class representing a contact info.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.email: str = obj.get("Email", None)
        self.name: str = obj.get("Name", None)
        self.phone: str = obj.get("Phone", None)


class Debtor(DataClass):
    """
    A class representing a debtor.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.number: str = obj.get("Number", None)
        self.name: str = obj.get("Name", None)


class Department(DataClass):
    """
    A class representing a department.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.code: int = obj.get("Code", None)
        self.description: str = obj.get("Description", None)


class Function(DataClass):
    """
    A class representing a function.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.code: int = obj.get("Code", None)
        self.description: str = obj.get("Description", None)


class LabourAgreementSettings(DataClass):
    """
    A class representing labour agreement settings.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("Id", None)
        self.guid: str = obj.get("Guid", None)
        self.int_number: int = obj.get("IntNumber", None)
        self.str_name: str = obj.get("StrName", None)
        self.debtor_id: int = obj.get("IntDebiteurID", None)


class Manager(DataClass):
    """
    A class representing manager information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.number: int = obj.get("Number", None)
        self.first_name: str = obj.get("FirstName", None)
        self.name: str = obj.get("Name", None)
        self.department: str = obj.get("Department", None)
        self.function: str = obj.get("Function", None)
        self.phone_number: str = obj.get("PhoneNumber", None)
        self.mobile: str = obj.get("Mobile", None)
        self.fax: str = obj.get("Fax", None)
        self.email: str = obj.get("Email", None)


class ServiceLevel(DataClass):
    """
    A class representing service level information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.start_period: int = obj.get("StartPeriod", None)
        self.start_year: int = obj.get("StartYear", None)
        self.service_level: str = obj.get("ServiceLevel", None)
        self.start_contract: datetime = obj.get("StartContract", None)


class Tag(DataClass):
    """
    A class representing debtor tag information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.number: int = obj.get("Number", None)
        self.hex_color: str = obj.get("HexColor", None)
        self.tag: str = obj.get("Tag", None)


class Event(DataClass):
    """
    A class representing an event.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.event_id: int = obj.get("EventId", None)
        self.event_name: str = obj.get("EventName", None)
        self.active: bool = obj.get("Active", None)

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
    """
    A class representing a webhook setting.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.webhook_setting_id: int = obj.get("WebhookSettingId", None)
        self.name: str = obj.get("Name", None)
        self.endpoint: str = obj.get("Endpoint", None)
        self.active: bool = obj.get("Active", None)
        events_data = obj.get("Event", [])
        if not isinstance(events_data, list):
            events_data = [events_data]
        self.events: list[Event] = [Event(event_data) for event_data in events_data]

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return {
            "webhook_setting_id": self.webhook_setting_id,
            "name": self.name,
            "endpoint": self.endpoint,
            "active": self.active,
            "events": [event.to_dict() for event in self.events] if self.events else [],
        }

    def to_insert_dict(self) -> dict:
        """
        Convert the instance to a dictionary representing the XML insert format.

        :return: A dictionary representation of the webhook setting instance.
        """
        event_dicts = (
            [event.to_insert_dict() for event in self.events] if self.events else []
        )
        return {
            "WebhookSetting": {
                "Name": self.name,
                "Endpoint": self.endpoint,
                "Active": self.active,
                "Events": event_dicts,
            }
        }
