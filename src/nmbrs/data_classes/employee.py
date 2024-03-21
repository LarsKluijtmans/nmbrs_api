"""This module defines the Employee class, a subclass of DataClass, representing an employee entity."""

from .data_class import DataClass


class Employee(DataClass):
    """A class representing an employee."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("Id", None)
        self.number: int = data.get("Number", None)
        self.name: str = data.get("DisplayName", None)


class EmployeeTypes(DataClass):
    """A class representing an employee type."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("Id", None)
        self.description: str = data.get("Description", None)
