from nmbrs.data_classes.data_class import DataClass


class LabourAgreementSettings(DataClass):
    """
    A class representing labour agreement settings.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for labour agreement settings.

        Initializes labour agreement settings instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing labour agreement settings data.
        """
        self.id: int | None = obj.get("Id", None)
        self.guid: str | None = obj.get("Guid", None)
        self.int_number: int | None = obj.get("IntNumber", None)
        self.str_name: str | None = obj.get("StrName", None)
        self.debtor_id: int | None = obj.get("IntDebiteurID", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the labour agreement settings instance.
        """
        return {
            "id": self.id,
            "guid": self.guid,
            "int_number": self.int_number,
            "str_name": self.str_name,
            "debtor_id": self.debtor_id,
        }
