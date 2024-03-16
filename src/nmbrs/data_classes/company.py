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

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = obj.get("ID", None)
        self.number: int = obj.get("Number", None)
        self.name: str = obj.get("Name", None)
        self.phone_number: str = obj.get("PhoneNumber", None)
        self.fax_number: str = obj.get("FaxNumber", None)
        self.email: str = obj.get("Email", None)
        self.website: str = obj.get("Website", None)
        self.loonaangifte_tijdvak: str = obj.get("LoonaangifteTijdvak", None)
        self.kvk_number: str = obj.get("KvkNr", None)


class WageTax(DataClass):
    """
    A class representing a wage tax.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.loonaangifte_id: int = obj.get("LoonaangifteID", None)
        self.serial_number: int = obj.get("SerialNumber", None)
        self.payment_reference: str = obj.get("PaymentReference", None)
        self.total_general: int = obj.get("TotalGeneral", None)
        self.period: int = obj.get("Period", None)
        self.year: int = obj.get("Year", None)
        self.status: str = obj.get("Status", None)
        self.sent_at: datetime = obj.get("SentAt", None)
        self.tijdvak_start: datetime = obj.get("TijdvakStart", None)
        self.tijdvak_end: datetime = obj.get("TijdvakEnd", None)
        self.correction_tijdvak_start: datetime = obj.get(
            "CorrectionTijdvakStart", None
        )
        self.correction_tijdvak_end: datetime = obj.get("CorrectionTijdvakEnd", None)


class WageTaxXML(DataClass):
    """
    A class representing wage tax XML.
    """

    def __init__(self, obj: str) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.xml: str = obj

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return parse_xml_to_dict(self.xml)
