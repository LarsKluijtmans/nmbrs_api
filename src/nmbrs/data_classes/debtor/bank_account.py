from nmbrs.data_classes.data_class import DataClass


class BankAccount(DataClass):
    """
    A class representing a bank account.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for bank account.

        Initializes bank account instance with data from the provided dictionary.

        :param obj: A dictionary containing bank account data.
        """
        self.id: int | None = obj.get("Id", None)
        self.number: str | None = obj.get("Number", None)
        self.description: str | None = obj.get("Description", None)
        self.iban: str | None = obj.get("IBAN", None)
        self.bic: str | None = obj.get("BIC", None)
        self.city: str | None = obj.get("City", None)
        self.name: str | None = obj.get("Name", None)
        self.type: str | None = obj.get("Type", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the bank account instance.
        """
        return {
            "id": self.id,
            "number": self.number,
            "description": self.description,
            "iban": self.iban,
            "bic": self.bic,
            "city": self.city,
            "name": self.name,
            "type": self.type,
        }
