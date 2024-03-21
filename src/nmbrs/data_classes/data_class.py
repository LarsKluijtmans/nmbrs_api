"""A base class for data classes that automatically initializes instance variables from a dictionary."""

import json
from decimal import Decimal
from abc import ABC, abstractmethod


class DataClass(ABC):
    """A base class for data classes that automatically initializes instance variables from a dictionary."""

    @abstractmethod
    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        new_item = {}
        for key, value in self.__dict__.items():
            if isinstance(value, DataClass):
                new_item[key] = value.to_dict()
            elif isinstance(value, list):
                new_item[key] = [
                    obj.to_dict() if isinstance(obj, DataClass) else float(obj) if isinstance(obj, Decimal) else obj for obj in value
                ]
            elif isinstance(value, Decimal):
                new_item[key] = float(value)
            else:
                new_item[key] = value
        return new_item

    def __str__(self):
        obj = self.to_dict()
        return json.dumps(obj)
