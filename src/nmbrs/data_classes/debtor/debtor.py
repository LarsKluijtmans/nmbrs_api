from nmbrs.data_classes.data_class import DataClass


class Debtor(DataClass):
    """
    A class representing a debtor.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for Debtor.

        Initializes Debtor instance with data from the provided dictionary.

        :param obj: A dictionary containing debtor data.
        """
        self.id: int | None = obj.get("Id", None)
        self.number: str | None = obj.get("Number", None)
        self.name: str | None = obj.get("Name", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the Debtor instance.
        """
        return {
            "id": self.id,
            "number": self.number,
            "name": self.name,
        }
