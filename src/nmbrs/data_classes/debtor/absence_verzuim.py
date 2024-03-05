import xmltodict

from nmbrs.data_classes.data_class import DataClass


class AbsenceVerzuim(DataClass):
    """
    A class representing Absence Verzuim data.

    Inherits from DataClass.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for AbsenceVerzuim class.

        Initializes instance variables with default values from the provided dictionary.

        :param obj: A dictionary containing Absence Verzuim data.
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
            "xml": self._parse_xml_to_dict(self.xml),
        }

    @staticmethod
    def _parse_xml_to_dict(xml: str) -> dict | str:
        """
        Try to parse the XML string into a dictionary.
        If parsing fails, return the original XML string.

        :param xml: A string that contains an XML document.
        :return: A dictionary representation of the XML or the original XML string.
        """
        try:
            return xmltodict.parse(xml)
        except Exception:
            return xml

    def get_xml(self) -> dict | None:
        """
        Method to retrieve XML data as a dictionary.

        :return: A dictionary representation of the XML data, or None if parsing fails.
        """
        xml = self._parse_xml_to_dict(self.xml)
        if type(xml) is not dict:
            return None
        return xml
