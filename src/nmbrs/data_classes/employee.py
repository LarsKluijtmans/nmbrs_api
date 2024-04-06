"""This module defines the Employee class, a subclass of DataClass, representing an employee entity."""

from datetime import datetime
from decimal import Decimal

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


class Period(DataClass):
    """A class representing a period of a company."""

    def __init__(self, employee_id: int, data: str) -> None:
        parts = data.split("-")
        self.employee_id = employee_id
        self.year: int = int(parts[0])
        self.period: int = int(parts[1])
        self.type: str = parts[2]


class Contract(DataClass):
    """A class representing a contract."""

    def __init__(self, data: dict, employee_id: int | None = None) -> None:
        self.employee_id = employee_id
        self.contract_id: int = data.get("ContractID", None)
        self.creation_date: datetime = data.get("CreationDate", None)
        self.start_date: datetime = data.get("StartDate", None)
        self.trial_period: datetime = data.get("TrialPeriod", None)
        self.end_date: datetime = data.get("EndDate", None)
        self.employment_type: int = data.get("EmployementType", None)
        self.employment_sequence_tax_id: int = data.get("EmploymentSequenceTaxId", None)
        self.indefinite: bool = data.get("Indefinite", None)
        self.phase_classification: int = data.get("PhaseClassification", None)
        self.written_contract: bool = data.get("WrittenContract", None)
        self.hours_per_week: Decimal = data.get("HoursPerWeek", None)


class Schedule(DataClass):
    """A class representing a schedule."""

    def __init__(self, data: dict, employee_id: int | None = None) -> None:
        self.employee_id = employee_id
        self.schedule_calc_method: str = data.get("ScheduleCalcMethod")
        self.hours_monday: Decimal = data.get("HoursMonday")
        self.hours_tuesday: Decimal = data.get("HoursTuesday")
        self.hours_wednesday: Decimal = data.get("HoursWednesday")
        self.hours_thursday: Decimal = data.get("HoursThursday")
        self.hours_friday: Decimal = data.get("HoursFriday")
        self.hours_saturday: Decimal = data.get("HoursSaturday")
        self.hours_sunday: Decimal = data.get("HoursSunday")
        self.hours_monday2: Decimal = data.get("HoursMonday2")
        self.hours_tuesday2: Decimal = data.get("HoursTuesday2")
        self.hours_wednesday2: Decimal = data.get("HoursWednesday2")
        self.hours_thursday2: Decimal = data.get("HoursThursday2")
        self.hours_friday2: Decimal = data.get("HoursFriday2")
        self.hours_saturday2: Decimal = data.get("HoursSaturday2")
        self.hours_sunday2: Decimal = data.get("HoursSunday2")
