"""This module defines various data classes for representing different entities in the system."""

from datetime import datetime
from decimal import Decimal
from .data_class import DataClass
from .general import CodeDescription
from .utils.xml import parse_xml_to_dict


class Company(DataClass):
    """A class representing a company."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("ID", None)
        self.number: int = data.get("Number", None)
        self.name: str = data.get("Name", None)
        self.phone_number: str = data.get("PhoneNumber", None)
        self.fax_number: str = data.get("FaxNumber", None)
        self.email: str = data.get("Email", None)
        self.website: str = data.get("Website", None)
        self.loonaangifte_tijdvak: str = data.get("LoonaangifteTijdvak", None)
        self.kvk_number: str = data.get("KvkNr", None)


class BankAccount(DataClass):
    """A class representing a bank account."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("Id", None)
        self.number: str = data.get("Number", None)
        self.description: str = data.get("Description", None)
        self.iban: str = data.get("IBAN", None)
        self.bic: str = data.get("BIC", None)
        self.city: str = data.get("City", None)
        self.name: str = data.get("Name", None)
        self.type: str = data.get("Type", None)


class Address(DataClass):
    """A class representing an address."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("Id", None)
        self.default: bool = data.get("Default", None)
        self.street: str = data.get("Street", None)
        self.house_number: str = data.get("HouseNumber", None)
        self.house_number_addition: str = data.get("HouseNumberAddition", None)
        self.postal_code: str = data.get("PostalCode", None)
        self.city: str = data.get("City", None)
        self.state_province: str = data.get("StateProvince", None)
        self.country_iso_code: str = data.get("CountryISOCode", None)


class LabourAgreement(DataClass):
    """A class representing a labour agreement."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("Id")
        self.guid: str = data.get("Guid")
        self.number: int = data.get("Number")
        self.description: str = data.get("Description")
        self.default: bool = data.get("Default")
        self.schedule_model: CodeDescription = CodeDescription(data.get("ScheduleModel"))
        self.wage_model: CodeDescription = CodeDescription(data.get("WageModel"))
        self.wage_model_2: CodeDescription = CodeDescription(data.get("WageModel2"))
        self.hours_model: CodeDescription = CodeDescription(data.get("HoursModel"))
        self.hours_model_2: CodeDescription = CodeDescription(data.get("HoursModel2"))
        self.industry: CodeDescription = CodeDescription(data.get("Industry"))
        self.industry_2: CodeDescription = CodeDescription(data.get("Industry2"))
        self.industry_3: CodeDescription = CodeDescription(data.get("Industry3"))
        self.leave_model: CodeDescription = CodeDescription(data.get("LeaveModel"))
        self.hours_reservation_model: CodeDescription = CodeDescription(data.get("HoursReservationModel"))
        self.reservation_model: CodeDescription = CodeDescription(data.get("ReservationModel"))
        self.salary_table: CodeDescription = CodeDescription(data.get("SalaryTable"))
        self.cao: CodeDescription = CodeDescription(data.get("CAO"))
        self.bln_use_provisional: bool = data.get("BlnUseProvisional")


class Period(DataClass):
    """A class representing a period of a company."""

    def __init__(self, company_id: int, data: str) -> None:
        parts = data.split("-")
        self.company_id = company_id
        self.year: int = int(parts[0])
        self.period: int = int(parts[1])
        self.type: str = parts[2]


class WageTax(DataClass):
    """A class representing a wage tax."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.loonaangifte_id: int = data.get("LoonaangifteID", None)
        self.serial_number: int = data.get("SerialNumber", None)
        self.payment_reference: str = data.get("PaymentReference", None)
        self.total_general: int = data.get("TotalGeneral", None)
        self.period: int = data.get("Period", None)
        self.year: int = data.get("Year", None)
        self.status: str = data.get("Status", None)
        self.sent_at: datetime = data.get("SentAt", None)
        self.tijdvak_start: datetime = data.get("TijdvakStart", None)
        self.tijdvak_end: datetime = data.get("TijdvakEnd", None)
        self.correction_tijdvak_start: datetime = data.get("CorrectionTijdvakStart", None)
        self.correction_tijdvak_end: datetime = data.get("CorrectionTijdvakEnd", None)


class WageTaxXML(DataClass):
    """A class representing wage tax XML."""

    def __init__(self, xml: str) -> None:
        self.xml: str = xml

    def to_dict(self) -> dict | str:
        """Convert the instance to a dictionary."""
        return parse_xml_to_dict(self.xml)


class ContactPerson(DataClass):
    """A class representing a contact person with their details."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.email: str = data.get("Email")
        self.name: str = data.get("Name")
        self.phone: str = data.get("Phone")
        self.gender: str = data.get("Gender")
        self.mobile_phone: str = data.get("MobilePhone")
        self.fax: str = data.get("Fax")
        self.function: str = data.get("Function")
        self.department: str = data.get("Department")
        self.number: int = data.get("Number")


class GuidConvertor(DataClass):
    """A class representing the mappings between integer IDs and GUIDs for a specific entity."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.entity: str = data.get("Entity")
        mappings_data = data.get("Mappings", [])
        mappings_data = mappings_data.get("Mapping", [])
        if not isinstance(mappings_data, list):
            mappings_data = [mappings_data]
        self.mappings: list[Mapping] = [Mapping(mapping_data) for mapping_data in mappings_data]


class Mapping(DataClass):
    """A class representing a mapping between an integer ID and a GUID."""

    def __init__(self, data: dict) -> None:
        self.id: int = data.get("IdInt")
        self.guid: str = data.get("IdGuid")


class CostCenter(DataClass):
    """A class representing a cost center."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class CostUnit(DataClass):
    """A class representing a cost unit."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class HourCode(DataClass):
    """A class representing an hour code."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class Pension(DataClass):
    """A class representing a pension exports information."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.pension_export_id: int = data.get("PensionExportID")
        self.serial_number: int = data.get("SerialNumber")
        self.period: int = data.get("Period")
        self.year: int = data.get("Year")
        self.status: str = data.get("Status")
        self.send_at: datetime = data.get("SentAt")
        self.correctie_tijdvak_start: datetime = data.get("CorrectionTijdvakStart")
        self.correctie_tijdvak_end: datetime = data.get("CorrectionTijdvakEnd")


class PensionXML(DataClass):
    """A class representing a pension export xml."""

    def __init__(self, xml: str) -> None:
        self.xml: str = xml

    def to_dict(self) -> dict | str:
        """Convert the instance to a dictionary."""
        return parse_xml_to_dict(self.xml)


class RunRequest(DataClass):
    """A class representing a run request."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id: company_id
        self.period: int = data.get("Period")
        self.year: int = data.get("Year")
        self.status: str = data.get("Status")
        self.handle_delete: datetime = data.get("HandledDate")


class RunInfo(DataClass):
    """A class representing a run info."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: int = data.get("ID")
        self.number: int = data.get("Number")
        self.year: int = data.get("Year")
        self.period_start: int = data.get("PeriodStart")
        self.period_end: int = data.get("PeriodEnd")
        self.description: int = data.get("Description")
        self.run_at: datetime = data.get("RunAt")
        self.locked: datetime = data.get("IsLocked")


class SalaryTable(DataClass):
    """A class representing a salary table."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")


class SalaryTableScale(DataClass):
    """A class representing a salary table scale."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.scale: str = data.get("Scale")
        self.description: str = data.get("Description")
        self.value: Decimal = data.get("ScaleValue")
        self.percentage_max: Decimal = data.get("ScalePercentageMax")
        self.percentage_min: Decimal = data.get("ScalePercentageMin")


class SalaryTableStep(DataClass):
    """A class representing a salary table scale."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.step: str = data.get("Step")
        self.description: str = data.get("StepDescription")
        self.value: Decimal = data.get("StepValue")


class SVWSettings(DataClass):
    """A class representing a svw settings."""

    def __init__(self, data: dict) -> None:
        self.cao_code: int = data.get("CodeCao")
        self.eigenrisicodrager_gediff_wga: bool = data.get("EigenrisicodragerGediffWGA")
        self.eigenrisicodrager_uniforme_wao: bool = data.get("EigenrisicodragerUniformeWAO")
        self.eigenrisicodrager_ziektewet: bool = data.get("EigenrisicodragerZiektewet")
        self.risc_group: int = data.get("RisicoGroep")
        self.wga_wn: Decimal = data.get("Gediff_WGA_wn")
        self.wga_wg: Decimal = data.get("Gediff_WGA_wg")
        self.sector: int = data.get("Sector")


class SVW(DataClass):
    """A class representing a svw."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.settings: SVWSettings = SVWSettings(data.get("SVWSettings"))
        self.sector: CodeDescription = CodeDescription(data.get("Sector"))
        self.risc_group: CodeDescription = CodeDescription(data.get("Risicogroep"))
        self.cao: CodeDescription = CodeDescription(data.get("CAO"))

    def insert_dict(self) -> dict:
        """Method used in combination with the Insert methode in the company.svw service"""
        return {
            "SVWSettings": {
                "CodeCao": self.settings.cao_code,
                "EigenrisicodragerGediffWGA": self.settings.eigenrisicodrager_gediff_wga,
                "EigenrisicodragerUniformeWAO": self.settings.eigenrisicodrager_uniforme_wao,
                "EigenrisicodragerZiektewet": self.settings.eigenrisicodrager_ziektewet,
                "RisicoGroep": self.settings.risc_group,
                "Gediff_WGA_wn": self.settings.wga_wn,
                "Gediff_WGA_wg": self.settings.wga_wg,
                "Sector": self.settings.sector,
            },
            "Sector": {"Code": self.sector.code, "Description": self.sector.description},
            "Risicogroep": {
                "Code": self.risc_group.code,
                "Description": self.risc_group.description,
            },
            "CAO": {
                "Code": self.cao.code,
                "Description": self.cao.description,
            },
        }


class DefaultEmployeeTemplate(DataClass):
    """A class representing a default employee template scale."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.id: str = data.get("DefaultEmployeeTemplateId")
        self.description: str = data.get("Description")


class FulltimeSchedules(DataClass):
    """A class representing all fulltime schedules."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.schedule_one: FulltimeSchedule = FulltimeSchedule(data.get("FulltimeScheduleOne"))
        self.schedule_two: FulltimeSchedule = FulltimeSchedule(data.get("FulltimeScheduleTwo"))
        self.schedule_three: FulltimeSchedule = FulltimeSchedule(data.get("FulltimeScheduleThree"))
        self.schedule_four: FulltimeSchedule = FulltimeSchedule(data.get("FulltimeScheduleFour"))


class FulltimeSchedule(DataClass):
    """A class representing a fulltime schedule."""

    def __init__(self, data: dict) -> None:
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


class PayrollWorkflowAction(DataClass):
    """A class representing a payroll workflow action."""

    def __init__(self, data: dict) -> None:
        self.action_id: int = data.get("ActionId")
        self.action_name: str = data.get("ActionName")
        self.action_status_id: int = data.get("ActionStatusId")
        self.action_status: str = data.get("ActionStatus")
        self.run_at: datetime = data.get("RunAt")


class PayrollWorkflowTrack(DataClass):
    """A class representing a payroll workflow track."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.track_name: str = data.get("TrackName")
        self.track_status: str = data.get("TrackStatus")
        self.actions: list[PayrollWorkflowAction] = [PayrollWorkflowAction(action) for action in data.get("Actions", [])]


class LeaveTypeGroup(DataClass):
    """A class representing a leave type group."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.type: str = data.get("Type")
        self.description: str = data.get("Description")
        self.company_leave_balance: list[CompanyLeaveType] = [
            CompanyLeaveType(leave_type) for leave_type in data.get("CompanyLeaveBalance", [])
        ]


class CompanyLeaveType(DataClass):
    """A class representing a company leave type."""

    def __init__(self, data: dict) -> None:
        self.description_leave_balance: str = data.get("DescriptionLeaveBalance")
        self.full_time_balance: Decimal = data.get("FullTimeBalance")
        self.leave_rounding_method: str = data.get("LeaveRoundingMethod")


class WageComponent(DataClass):
    """A class representing a wage component."""

    def __init__(self, company_id: int, component_type: str, data: dict) -> None:
        self.company_id = company_id
        self.type = component_type
        self.id: int = data.get("Id")
        self.code: int = data.get("Code")
        self.value: str = data.get("Value")


class WageCost(DataClass):
    """A class representing a wage cost."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.period: int = data.get("Period")
        self.year: int = data.get("Year")
        self.payroll: Decimal = data.get("WorkCostPayroll")
        self.financial: Decimal = data.get("WorkCostFinancial")
        self.fiscal_wage: Decimal = data.get("FiscalWage")
        self.available_space: Decimal = data.get("WorkCostAvailableSpace")
        self.base: Decimal = data.get("WorkCostBase")
        self.to_pay: Decimal = data.get("WorkCostToPay")
        self.estimated: Decimal = data.get("WorkCostEstimated")
        self.paid: Decimal = data.get("WorkCostPaid")


class WageModel(DataClass):
    """A class representing a wage model."""

    def __init__(self, company_id: int, data: dict) -> None:
        self.company_id = company_id
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")
