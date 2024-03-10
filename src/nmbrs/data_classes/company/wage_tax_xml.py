"""
This module defines a data class representing wage tax XML.

Classes:
    WageTaxXML (DataClass): A class representing wage tax XML.

Dependencies:
    DataClass: An abstract base class defining common methods for data classes.
    parse_xml_to_dict: A function for parsing XML strings into dictionaries.
"""

from ...data_classes.data_class import DataClass
from ...data_classes.utils.xml import parse_xml_to_dict


class WageTaxXML(DataClass):
    """
    A class representing wage tax XML.
    """

    def __init__(self, obj: str) -> None:
        """
        Constructor method for wage tax XML.

        Initializes a wage tax XML instance with data from the provided dictionary.

        Args:
            obj (str): A string containing wage tax XML data.
        """
        self.xml: str | None = obj

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        Returns:
            dict: A dictionary representation of the wage tax XML instance.
        """
        return {
            "xml": parse_xml_to_dict(self.xml),
        }
