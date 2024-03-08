from nmbrs.data_classes.data_class import DataClass


class Employee(DataClass):
    """
    A class representing a employee.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for employee.

        Initializes employee instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing employee data.
        """
        self.id: int | None = obj.get("Id", None)
        self.number: str | None = obj.get("Number", None)
        self.name: str | None = obj.get("DisplayName", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the employee instance.
        """
        return {
            "id": self.id,
            "number": self.number,
            "name": self.name,
        }
