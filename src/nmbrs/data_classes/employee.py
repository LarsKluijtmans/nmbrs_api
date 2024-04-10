"""This module defines the Employee class, a subclass of DataClass, representing an employee entity."""

from datetime import datetime
from decimal import Decimal

from .data_class import DataClass


class Employee(DataClass):
    """A class representing an employee."""

    def __init__(self, data: dict):
        self.id: int = data.get("Id", None)
        self.number: int = data.get("Number", None)
        self.name: str = data.get("DisplayName", None)


class EmployeeTypes(DataClass):
    """A class representing an employee type."""

    def __init__(self, data: dict):
        self.id: int = data.get("Id", None)
        self.description: str = data.get("Description", None)


class Period(DataClass):
    """A class representing a period of a company."""

    def __init__(self, employee_id: int, data: str):
        parts = data.split("-")
        self.employee_id = employee_id
        self.year: int = int(parts[0])
        self.period: int = int(parts[1])
        self.type: str = parts[2]


class Contract(DataClass):
    """A class representing a contract."""

    def __init__(self, employee_id: int, data: dict):
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

    def __init__(self, employee_id: int, data: dict):
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


class PersonalInfo(DataClass):
    """A class representing an employee's personal information."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.employee_number: int = data.get("EmployeeNumber")
        self.bsn: str = data.get("BSN")
        self.title: str = data.get("Title")
        self.first_name: str = data.get("FirstName")
        self.initials: str = data.get("Initials")
        self.prefix: str = data.get("Prefix")
        self.last_name: str = data.get("LastName")
        self.nickname: str = data.get("Nickname")
        self.gender: str = data.get("Gender")
        self.nationality_code: int = data.get("NationalityCode")
        self.place_of_birth: str = data.get("PlaceOfBirth")
        self.country_of_birth_iso_code: str = data.get("CountryOfBirthISOCode")
        self.identification_number: str = data.get("IdentificationNumber")
        self.identification_type: int = data.get("IdentificationType")
        self.partner_prefix: str = data.get("PartnerPrefix")
        self.partner_last_name: str = data.get("PartnerLastName")
        self.telephone_private: str = data.get("TelephonePrivate")
        self.telephone_work: str = data.get("TelephoneWork")
        self.telephone_mobile_private: str = data.get("TelephoneMobilePrivate")
        self.telephone_mobile_work: str = data.get("TelephoneMobileWork")
        self.telephone_other: str = data.get("TelephoneOther")
        self.email_private: str = data.get("EmailPrivate")
        self.email_work: str = data.get("EmailWork")
        self.burgerlijke_staat: str = data.get("BurgerlijkeStaat")
        self.naamstelling: str = data.get("Naamstelling")
        self.birthday: datetime = data.get("Birthday")
        self.deceased_date: datetime = data.get("DeceasedDate")
        self.in_case_of_emergency: str = data.get("InCaseOfEmergency")
        self.in_case_of_emergency_phone: str = data.get("InCaseOfEmergencyPhone")
        self.in_case_of_emergency_relation: str = data.get("InCaseOfEmergencyRelation")
        self.title_after: str = data.get("TitleAfter")


class PersonalInfoContractSalaryAddress(DataClass):
    """A class representing personal, contract, salary, and address information."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id: int = employee_id
        self.employee_number: int = data.get("EmployeeNumber")
        self.first_name: str = data.get("FirstName")
        self.birthday: datetime = data.get("Birthday")
        self.prefix: str = data.get("Prefix")
        self.last_name: str = data.get("LastName")
        self.gender: str = data.get("Gender")
        self.bsn: str = data.get("BSN")
        self.city: str = data.get("City")
        self.telephone_work: str = data.get("TelephoneWork")
        self.telephone_mobile_work: str = data.get("TelephoneMobileWork")
        self.email_work: str = data.get("EmailWork")
        self.contract_start_date: datetime = data.get("ContractStartDate")
        self.contract_end_date: datetime = data.get("ContractEndDate")
        self.email_private: str = data.get("EmailPrivate")
        self.telephone_private: str = data.get("TelephonePrivate")
        self.telephone_mobile_private: str = data.get("TelephoneMobilePrivate")
        self.salary_type: str = data.get("SalaryType")
        self.salary_value: Decimal = data.get("SalaryValue")
        self.street: str = data.get("Street")
        self.house_number: str = data.get("HouseNumber")
        self.house_number_addition: str = data.get("HouseNumberAddition")
        self.post_code: str = data.get("PostCode")
        self.hourly_wage: Decimal = data.get("HourlyWage")
        self.contract_hours: Decimal = data.get("ContractHours")


class Absence(DataClass):
    """A class representing absence"""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id: int = employee_id
        self.id: int = data.get("AbsenceId")
        self.comment: str = data.get("Comment")
        self.percentage: int = data.get("Percentage")
        self.start: datetime = data.get("Start")
        self.registration_start_date: datetime = data.get("RegistrationStartDate")
        self.end: datetime = data.get("End")
        self.registration_end_date: datetime = data.get("RegistrationEndDate")
        self.dossier: str = data.get("Dossier")
        self.dossier_number: int = data.get("Dossiernr")
        self.cause: AbsenceCause = AbsenceCause(data.get("AbsenceCause"))


class AbsenceCause(DataClass):
    """A class representing the cause of an absence"""

    def __init__(self, data: dict | None):
        if data is None:
            return
        self.id: int = data.get("CauseId")
        self.cause: str = data.get("Cause")
