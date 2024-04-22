"""This module defines the Employee class, a subclass of DataClass, representing an employee entity."""

from datetime import datetime
from decimal import Decimal

from .data_class import DataClass


class Employee(DataClass):
    """A class representing an employee."""

    def __init__(self, data: dict):
        self.id: int = data.get("Id")
        self.number: int = data.get("Number")
        self.name: str = data.get("DisplayName")


class EmployeeTypes(DataClass):
    """A class representing an employee type."""

    def __init__(self, data: dict):
        self.id: int = data.get("Id")
        self.description: str = data.get("Description")


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
        self.id: int = data.get("ContractID")
        self.creation_date: datetime = data.get("CreationDate")
        self.start_date: datetime = data.get("StartDate")
        self.trial_period: datetime = data.get("TrialPeriod")
        self.end_date: datetime = data.get("EndDate")
        self.employment_type: int = data.get("EmployementType")
        self.employment_sequence_tax_id: int = data.get("EmploymentSequenceTaxId")
        self.indefinite: bool = data.get("Indefinite")
        self.phase_classification: int = data.get("PhaseClassification")
        self.written_contract: bool = data.get("WrittenContract")
        self.hours_per_week: Decimal = data.get("HoursPerWeek")


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


class Address(DataClass):
    """A class representing an address"""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id: int = employee_id
        self.id: int = data.get("Id")
        self.default: bool = data.get("Default")
        self.street: str = data.get("Street")
        self.house_number: str = data.get("HouseNumber")
        self.house_number_addition: str = data.get("HouseNumberAddition")
        self.postcode: str = data.get("PostalCode")
        self.city: str = data.get("City")
        self.state_province: str = data.get("StateProvince")
        self.country_iso_code: str = data.get("CountryISOCode")
        self.type: str = data.get("Type")


class BankAccount(DataClass):
    """A class representing a bank account."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.number: str = data.get("Number")
        self.description: str = data.get("Description")
        self.iban: str = data.get("IBAN")
        self.bic: str = data.get("BIC")
        self.city: str = data.get("City")
        self.name: str = data.get("Name")
        self.type: str = data.get("Type")


class Child(DataClass):
    """A class representing a child."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.name: str = data.get("Name")
        self.first_name: str = data.get("FirstName")
        self.initials: str = data.get("Initials")
        self.gender: str = data.get("Gender")
        self.birthday: datetime = data.get("Birthday")


class CostCenter(DataClass):
    """A class representing a cost center."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.code: str = data.get("Code")
        self.description: str = data.get("Description")


class DepartmentAll(DataClass):
    """A class representing a department."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id = data.get("Id")
        self.code = data.get("Code")
        self.description = data.get("Description")
        self.creation_date = data.get("CreationDate")
        self.start_period = data.get("StartPeriod")
        self.start_year = data.get("StartYear")


class Department(DataClass):
    """A class representing a department."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id = data.get("Id")
        self.code = data.get("Code")
        self.description = data.get("Description")


class Employment(DataClass):
    """A class representing an employment."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("EmploymentId")
        self.creation_date: datetime = data.get("CreationDate")
        self.start_date: datetime = data.get("StartDate")
        self.end_date: datetime = data.get("EndDate")
        self.initial_start_date: datetime = data.get("InitialStartDate")


class FunctionAll(DataClass):
    """A class representing a functions."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.record_id: int = data.get("RecordId")
        self.function_id: int = data.get("Function").get("Id")
        self.creation_date: datetime = data.get("CreationDate")
        self.start_period: datetime = data.get("StartPeriod")
        self.start_year: datetime = data.get("StartYear")


class Function(DataClass):
    """A class representing a functions."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class Manager(DataClass):
    """A class representing a manager."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.number: int = data.get("Number")
        self.first_name: str = data.get("FirstName")
        self.name: str = data.get("Name")
        self.department: str = data.get("Department")
        self.function: str = data.get("Function")
        self.phone_number: str = data.get("PhoneNumber")
        self.mobile: str = data.get("Mobile")
        self.fax: str = data.get("Fax")
        self.email: str = data.get("Email")


class LeaseCar(DataClass):
    """A class representing a lease car."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.brand: str = data.get("Brand")
        self.model: str = data.get("Model")
        self.additional_percentage: str = data.get("AdditionPercentage")
        self.contract_lease_company: str = data.get("ContractLeaseCompany")
        self.contract_number: str = data.get("ContractNumber")
        self.contract_duration: int = data.get("ContractDuration")
        self.leasing_price_month: Decimal = data.get("LeasingPriceMonth")
        self.max_mileage: int = data.get("MaxMileage")
        self.price_more_milage: Decimal = data.get("PriceMoreMileage")
        self.price_less_milage: Decimal = data.get("PriceLessMileage")
        self.first_registered: datetime = data.get("FirstResgistrationDate")
        self.co2_emissions: int = data.get("CO2Emissions")
        self.license_plate: str = data.get("LicensePlate")
        self.catalog_value: Decimal = data.get("CatalogValue")
        self.start_date: datetime = data.get("StartDate")
        self.end_date: datetime = data.get("EndDate")
        self.reason_no_contribution: int = data.get("ReasonNoContribution")
        self.contribution_private_percentage: int = data.get("ContributionPrivatePercentage")
        self.contribution_private_use: Decimal = data.get("ContributionPrivateUse")
        self.contribution_not_deductible: Decimal = data.get("ContributionNotDeductible")


class Partner(DataClass):
    """A class representing a partner."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("Id")
        self.name: str = data.get("PartnerName")
        self.first_name: str = data.get("FirstName")
        self.initials: str = data.get("Initials")
        self.gender: str = data.get("Gender")
        self.birthday: datetime = data.get("Birthday")
        self.start_date: datetime = data.get("StartDate")
        self.telephone: str = data.get("Telephone")
        self.email: str = data.get("Email")


class Salary(DataClass):
    """A class representing a salary."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id: int = data.get("ID")
        self.value: Decimal = data.get("Value")
        self.type: int = data.get("Type")
        self.star_date: datetime = data.get("StartDate")
        self.creation_date: datetime = data.get("CreationDate")

        table = {} if not data.get("SalaryTable") else data.get("SalaryTable")
        self.table_code: int = table.get("Code")
        self.table_description: str = table.get("Description")

        scale = {} if not table.get("Schaal") else table.get("Schaal")
        self.scale: str = scale.get("Scale")
        self.scale_description: str = scale.get("SchaalDescription")
        self.scale_value: Decimal = scale.get("ScaleValue")
        self.scale_percentage_max: Decimal = scale.get("ScalePercentageMax")
        self.scale_percentage_min: Decimal = scale.get("ScalePercentageMin")

        step = {} if not table.get("Trede") else table.get("Trede")
        self.step: str = step.get("Step")
        self.step_description: str = step.get("StepDescription")
        self.step_value: Decimal = step.get("StepValue")


class SVW(DataClass):
    """A class representing a svw."""

    def __init__(self, employee_id: int, data: dict):
        self.employee_id = employee_id
        self.id = data.get("Id")
        self.create_date = data.get("CreateDate")
        self.start_year = data.get("StartYear")
        self.start_period = data.get("StartPeriod")
        self.influence_obliged_insurance = data.get("InfluenceObligedInsuranced")
        self.wao_wia = data.get("Wao_Wia")
        self.ww = data.get("Ww")
        self.zw = data.get("Zw")
        self.income_related_contribution_zvw = data.get("IncomeRelatedContributionZvw")
        self.code_zvw = data.get("CodeZvw")
        self.employment_type = data.get("EmploymentType")
        self.phase_classification = data.get("PhaseClassification")
        self.employment_sequence_tax_id = data.get("EmploymentSequenceTaxId")

        cao = data.get("CAO")
        self.cao_id = cao.get("CAOId")
        self.cao_code = cao.get("CAOCode")
        self.cao_description = cao.get("CAODescription")

        risk_group = data.get("RiskGroup")
        self.risk_group_id = risk_group.get("RiskGroupId")
        self.risk_group_code = risk_group.get("RiskGroupCode")
        self.risk_group_description = risk_group.get("RiskGroupDescription")

        sector = data.get("Sector")
        self.sector_id = sector.get("SectorId")
        self.sector_code = sector.get("SectorCode")
        self.sector_description = sector.get("SectorDescription")

        wage_cost_benefit = data.get("WageCostBenefit")
        self.wage_cost_benefit_code = wage_cost_benefit.get("WageCostBenefitCode")
        self.wage_cost_benefit_end_period = wage_cost_benefit.get("EndPeriod")
        self.wage_cost_benefit_end_year = wage_cost_benefit.get("EndYear")
