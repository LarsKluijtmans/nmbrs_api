from datetime import datetime

from nmbrs.data_classes.data_class import DataClass


class WageTax(DataClass):
    """
    A class representing a wage tax.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for wage tax.

        Initializes wage tax instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing wage tax data.
        """
        self.loonaangifte_id: int | None = obj.get("LoonaangifteID", None)
        self.serial_number: int | None = obj.get("SerialNumber", None)
        self.payment_reference: str | None = obj.get("PaymentReference", None)
        self.total_general: int | None = obj.get("TotalGeneral", None)
        self.period: int | None = obj.get("Period", None)
        self.year: int | None = obj.get("Year", None)
        self.status: str | None = obj.get("Status", None)
        self.sent_at: datetime | None = obj.get("SentAt", None)
        self.tijdvak_start: datetime | None = obj.get("TijdvakStart", None)
        self.tijdvak_end: datetime | None = obj.get("TijdvakEnd", None)
        self.correction_tijdvak_start: datetime | None = obj.get(
            "CorrectionTijdvakStart", None
        )
        self.correction_tijdvak_end: datetime | None = obj.get(
            "CorrectionTijdvakEnd", None
        )

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the wage tax instance.
        """
        return {
            "loonaangifte_id": self.loonaangifte_id,
            "serial_number": self.serial_number,
            "payment_reference": self.payment_reference,
            "total_general": self.total_general,
            "period": self.period,
            "year": self.year,
            "status": self.status,
            "sent_at": self.sent_at,
            "tijdvak_start": self.tijdvak_start,
            "tijdvak_end": self.tijdvak_end,
            "correction_tijdvak_start": self.correction_tijdvak_start,
            "correction_tijdvak_end": self.correction_tijdvak_end,
        }
