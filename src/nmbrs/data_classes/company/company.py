from nmbrs.data_classes.data_class import DataClass


class Company(DataClass):
    """
    A class representing a company.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for company.

        Initializes company instance with data from the provided dictionary.

        :param obj: A dictionary containing company data.
        """
        self.id: int | None = obj.get("ID", None)
        self.number: int | None = obj.get("Number", None)
        self.name: str | None = obj.get("Name", None)
        self.phone_number: str | None = obj.get("PhoneNumber", None)
        self.fax_number: str | None = obj.get("FaxNumber", None)
        self.email: str | None = obj.get("Email", None)
        self.website: str | None = obj.get("Website", None)
        self.loonaangifte_tijdvak: str | None = obj.get("LoonaangifteTijdvak", None)
        self.kvk_number: str | None = obj.get("KvkNr", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the company instance.
        """
        return {
            "id": self.id,
            "number": self.number,
            "name": self.name,
            "phone_number": self.phone_number,
            "fax_number": self.fax_number,
            "email": self.email,
            "website": self.website,
            "loonaangifte_tijdvak": self.loonaangifte_tijdvak,
            "kvk_number": self.kvk_number,
        }
