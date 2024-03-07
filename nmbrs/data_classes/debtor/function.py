from nmbrs.data_classes.data_class import DataClass


class Function(DataClass):
    """
    A class representing a function.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for function.

        Initializes function instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing function data.
        """
        self.id: int | None = obj.get("Id", None)
        self.code: int | None = obj.get("Code", None)
        self.description: str | None = obj.get("Description", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the function instance.
        """
        return {
            "id": self.id,
            "code": self.code,
            "description": self.description,
        }
