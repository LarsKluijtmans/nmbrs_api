"""A base class for data classes that automatically initializes instance variables from a dictionary."""

import json
from abc import ABC, abstractmethod
from decimal import Decimal


def serialize(obj: any, target_cls=dict) -> float | dict | list[dict]:
    """Serialize DataClass objects to native python data structures"""
    if isinstance(obj, list):
        return [serialize(sub, target_cls) for sub in obj]

    if isinstance(obj, Decimal):
        return float(obj)

    if isinstance(obj, (dict, DataClass)):
        obj = obj.__dict__
        result = target_cls()
        for key in obj:
            result[key] = serialize(obj[key], target_cls)
        return result
    return obj


class DataClass(ABC):
    """A base class for data classes that automatically initializes instance variables from a dictionary."""

    @abstractmethod
    def __init__(self) -> None:
        """Initializes instance variables based on the provided dictionary."""

    def to_dict(self) -> dict:
        """Convert the instance to a dictionary."""
        return serialize(self)

    def __str__(self):
        """Returns a JSON representation of the instance."""
        obj = self.to_dict()
        return json.dumps(obj)

    def __getattr__(self, name):
        """Implement custom __getattr__ to access instance variables directly."""
        try:
            return self.__dict__[name]
        except KeyError as e:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'") from e

    def __setattr__(self, name, value):
        """Customize behavior when setting an attribute on an instance."""
        self.__dict__[name] = value

    def __delattr__(self, name):
        """Define behavior for when an attribute is deleted using the del statement."""
        try:
            del self.__dict__[name]
        except KeyError as e:  # pragma: no cover
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'") from e  # pragma: no cover

    def __eq__(self, other):
        """Specifies behavior for equality comparisons using the == operator."""
        if isinstance(other, type(self)):
            return self.to_dict() == other.to_dict()
        return False  # pragma: no cover

    def __repr__(self):
        """Defines the official string representation of the object."""
        return f"{type(self).__name__}({self.__dict__})"

    def __len__(self):
        """Returns the length of the object."""
        return len(self.__dict__)

    def __iter__(self):
        """Implement iteration behavior."""
        return iter(self.__dict__.items())
