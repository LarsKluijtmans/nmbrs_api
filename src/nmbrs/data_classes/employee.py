"""
This module defines the Employee class, a subclass of DataClass, representing an employee entity.

Classes:
- Employee: A class representing an employee.

Imported Module:
- DataClass: A base class for data classes.
"""

from .data_class import DataClass


class Employee(DataClass):
    """
    A class representing an employee.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            data (dict): A dictionary containing data to initialize instance variables.
        """
        self.id: int = data.get("Id", None)
        self.number: str = data.get("Number", None)
        self.name: str = data.get("DisplayName", None)
