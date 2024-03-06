from nmbrs.data_classes.data_class import DataClass


class ContactInfo(DataClass):
    """
    A class representing a contact Info.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for accountant contact Info.

        Initializes contact Info instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing contact Info data.
        """
        self.email: str | None = obj.get("Email", None)
        self.name: str | None = obj.get("Name", None)
        self.phone: str | None = obj.get("Phone", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the contact Info instance.
        """
        return {
            "email": self.email,
            "name": self.name,
            "phone": self.phone,
        }
