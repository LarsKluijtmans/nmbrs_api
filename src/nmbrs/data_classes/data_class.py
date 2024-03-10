"""
This module provides an abstract base class defining common methods for data classes.

Classes:
    DataClass (ABC): An abstract base class for data classes.

Dependencies:
    ABC: Abstract base class support module.
    abstractmethod: Decorator for abstract methods.
"""

from abc import ABC, abstractmethod


class DataClass(ABC):
    """
    Abstract base class defining common methods for data classes.
    """

    @abstractmethod
    def __init__(self, obj: dict) -> None:
        """
        Constructor method for DataClass.

        Args:
            obj (dict): A dictionary containing data for initialization.
        """
        self.obj = obj

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Abstract method to convert the instance to a dictionary.

        Returns:
            dict: A dictionary representation of the instance.
        """
