"""
This module defines various data classes for representing different entities in the system.

Classes:
- Company: A class representing a company.
- WageTax: A class representing a wage tax.
- WageTaxXML: A class representing wage tax XML.

Dependencies:
- DataClass: A base class for data classes.
- datetime: Module providing classes for manipulating dates and times.
- parse_xml_to_dict: Function for parsing XML data into a dictionary.
"""

from datetime import datetime

from .data_class import DataClass
from .utils.xml import parse_xml_to_dict


class Company(DataClass):
    """
    A class representing a company.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = data.get("ID", None)
        self.number: int = data.get("Number", None)
        self.name: str = data.get("Name", None)
        self.phone_number: str = data.get("PhoneNumber", None)
        self.fax_number: str = data.get("FaxNumber", None)
        self.email: str = data.get("Email", None)
        self.website: str = data.get("Website", None)
        self.loonaangifte_tijdvak: str = data.get("LoonaangifteTijdvak", None)
        self.kvk_number: str = data.get("KvkNr", None)


class LabourAgreement(DataClass):
    """
    A class representing a labour agreement.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = data.get("Id")
        self.guid: str = data.get("Guid")
        self.number: int = data.get("Number")
        self.description: str = data.get("Description")
        self.default: bool = data.get("Default")
        self.schedule_model: CodeDescription = CodeDescription(data.get("ScheduleModel"))
        self.wage_model: CodeDescription = CodeDescription(data.get("WageModel"))
        self.wage_model_2: CodeDescription = CodeDescription(data.get("WageModel2"))
        self.hours_model: CodeDescription = CodeDescription(data.get("HoursModel"))
        self.hours_model_2: CodeDescription = CodeDescription(data.get("HoursModel2"))
        self.industry: CodeDescription = CodeDescription(data.get("Industry"))
        self.industry_2: CodeDescription = CodeDescription(data.get("Industry2"))
        self.industry_3: CodeDescription = CodeDescription(data.get("Industry3"))
        self.leave_model: CodeDescription = CodeDescription(data.get("LeaveModel"))
        self.hours_reservation_model: CodeDescription = CodeDescription(data.get("HoursReservationModel"))
        self.reservation_model: CodeDescription = CodeDescription(data.get("ReservationModel"))
        self.salary_table: CodeDescription = CodeDescription(data.get("SalaryTable"))
        self.cao: CodeDescription = CodeDescription(data.get("CAO"))
        self.bln_use_provisional: bool = data.get("BlnUseProvisional")


class CodeDescription(DataClass):
    """
    A class representing a code and a description.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        if data is None:
            return  # pragma: no cover
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class Period(DataClass):
    """
    A class representing a period of a company.
    """

    def __init__(self, data: str) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (str): A string containing data to initialize instance variables.
        """
        parts = data.split("-")
        self.year: int = int(parts[0])
        self.period: int = int(parts[1])
        self.type: str = parts[2]


class WageTax(DataClass):
    """
    A class representing a wage tax.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.loonaangifte_id: int = data.get("LoonaangifteID", None)
        self.serial_number: int = data.get("SerialNumber", None)
        self.payment_reference: str = data.get("PaymentReference", None)
        self.total_general: int = data.get("TotalGeneral", None)
        self.period: int = data.get("Period", None)
        self.year: int = data.get("Year", None)
        self.status: str = data.get("Status", None)
        self.sent_at: datetime = data.get("SentAt", None)
        self.tijdvak_start: datetime = data.get("TijdvakStart", None)
        self.tijdvak_end: datetime = data.get("TijdvakEnd", None)
        self.correction_tijdvak_start: datetime = data.get("CorrectionTijdvakStart", None)
        self.correction_tijdvak_end: datetime = data.get("CorrectionTijdvakEnd", None)


class WageTaxXML(DataClass):
    """
    A class representing wage tax XML.
    """

    def __init__(self, data: str) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.xml: str = data

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return parse_xml_to_dict(self.xml)


class ContactPerson(DataClass):
    """
    A class representing a contact person with their details.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.email: str = data.get("Email")
        self.name: str = data.get("Name")
        self.phone: str = data.get("Phone")
        self.gender: str = data.get("Gender")
        self.mobile_phone: str = data.get("MobilePhone")
        self.fax: str = data.get("Fax")
        self.function: str = data.get("Function")
        self.department: str = data.get("Department")
        self.number: int = data.get("Number")


class GuidConvertor(DataClass):
    """
    A class representing the mappings between integer IDs and GUIDs for a specific entity.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.entity: str = data.get("Entity")
        mappings_data = data.get("Mappings", [])
        mappings_data = mappings_data.get("Mapping", [])
        if not isinstance(mappings_data, list):
            mappings_data = [mappings_data]
        self.mappings: list[Mapping] = [Mapping(mapping_data) for mapping_data in mappings_data]


class Mapping(DataClass):
    """
    A class representing a mapping between an integer ID and a GUID.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = data.get("IdInt")
        self.guid: str = data.get("IdGuid")
