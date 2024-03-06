from nmbrs.data_classes.data_class import DataClass


class Manager(DataClass):
    """
    A class representing manager information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for manager.

        Initializes manager instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing manager data.
        """
        self.number: int | None = obj.get("Number", None)
        self.first_name: str | None = obj.get("FirstName", None)
        self.name: str | None = obj.get("Name", None)
        self.department: str | None = obj.get("Department", None)
        self.function: str | None = obj.get("Function", None)
        self.phone_number: str | None = obj.get("PhoneNumber", None)
        self.mobile: str | None = obj.get("Mobile", None)
        self.fax: str | None = obj.get("Fax", None)
        self.email: str | None = obj.get("Email", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the manager instance.
        """
        return {
            "number": self.number,
            "first_name": self.first_name,
            "name": self.name,
            "department": self.department,
            "function": self.function,
            "phone_number": self.phone_number,
            "mobile": self.mobile,
            "fax": self.fax,
            "email": self.email,
        }
