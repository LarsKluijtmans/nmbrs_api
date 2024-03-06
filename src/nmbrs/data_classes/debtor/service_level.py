from datetime import datetime

from nmbrs.data_classes.data_class import DataClass


class ServiceLevel(DataClass):
    """
    A class representing service level information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for service level.

        Initializes service level instance with data from the provided dictionary.

        Args:
            obj (dict):  A dictionary containing service level data.
        """
        self.start_period: int | None = obj.get("StartPeriod", None)
        self.start_year: int | None = obj.get("StartYear", None)
        self.service_level: str | None = obj.get("ServiceLevel", None)
        self.start_contract: datetime | None = obj.get("StartContract", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the service level instance.
        """
        return {
            "start_period": self.start_period,
            "start_year": self.start_year,
            "service_level": self.service_level,
            "start_contract": self.start_contract,
        }
