"""
This module defines a data class representing Absence Verzuim data.

Classes:
    AbsenceVerzuim (DataClass): A class representing Absence Verzuim data.

Dependencies:
    DataClass: An abstract base class defining common methods for data classes.
    parse_xml_to_dict: A function for parsing XML strings into dictionaries.
"""
from ...data_classes.data_class import DataClass
from ...data_classes.utils.xml import parse_xml_to_dict


class AbsenceVerzuim(DataClass):
    """
    A class representing Absence Verzuim data.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for AbsenceVerzuim class.

        Initializes instance variables with default values from the provided dictionary.

        Args:
            obj (dict): A dictionary containing Absence Verzuim data.
        """
        self.debtor_id: int | None = obj.get("DebtorID", None)
        self.company_id: int | None = obj.get("CompanyID", None)
        self.employee_id: int | None = obj.get("EmployeeID", None)
        self.xml: str | None = obj.get("XML", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the Absence Verzuim data.
        """
        return {
            "debtor_id": self.debtor_id,
            "company_id": self.company_id,
            "employee_id": self.employee_id,
            "xml": parse_xml_to_dict(self.xml),
        }
