from nmbrs.data_classes.data_class import DataClass
from nmbrs.data_classes.utils.xml import parse_xml_to_dict


class WageTaxXML(DataClass):
    """
    A class representing a wage tax xml.
    """

    def __init__(self, obj: str) -> None:
        """
        Constructor method for wage tax xml.

        Initializes wage tax xml instance with data from the provided dictionary.

        :param obj: A dictionary containing wage tax xml data.
        """
        self.xml: str | None = obj

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the wage tax xml instance.
        """
        return {
            "xml": parse_xml_to_dict(self.xml),
        }
