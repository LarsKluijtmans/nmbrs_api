"""
A base class for data classes that automatically initializes instance variables from a dictionary.
"""

import json
from abc import ABC


class DataClass(ABC):
    """
    A base class for data classes that automatically initializes instance variables from a dictionary.
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
                items = value
                new_list = []
                for obj in items:
                    if isinstance(obj, DataClass):
                        new_list.append(obj.to_dict())
                    else:
                        new_list.append(obj)
                new_item[key] = new_list
            else:
                new_item[key] = value
        return new_item

    def __str__(self):
        obj = self.to_dict()
        return json.dumps(obj)
