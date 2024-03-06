from nmbrs.data_classes.data_class import DataClass


class Event(DataClass):
    """
    A class representing an event.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for event.

        Initializes event instance with data from the provided dictionary.

        :param obj: A dictionary containing event data.
        """
        self.event_id: int | None = obj.get("EventId", None)
        self.event_name: str | None = obj.get("EventName", None)
        self.active: bool | None = obj.get("Active", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the event instance.
        """
        return {
            "event_id": self.event_id,
            "event_name": self.event_name,
            "active": self.active,
        }

    def to_insert_dict(self) -> dict:
        """
        Convert the instance to a dictionary representing the XML insert format.

        :return: A dictionary representation of the event instance.
        """
        return {
            "EventId": self.event_id,
            "Active": self.active,
        }


class WebhookSetting(DataClass):
    """
    A class representing a webhook setting.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for webhook setting.

        Initializes webhook setting instance with data from the provided dictionary.

        :param obj: A dictionary containing webhook setting data.
        """
        self.webhook_setting_id: int | None = obj.get("WebhookSettingId", None)
        self.name: str | None = obj.get("Name", None)
        self.endpoint: str | None = obj.get("Endpoint", None)
        self.active: bool | None = obj.get("Active", None)
        self.events: list[Event] | None = [
            Event(event_data) for event_data in obj.get("Event", [])
        ]

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the webhook setting instance.
        """
        return {
            "webhook_setting_id": self.webhook_setting_id,
            "name": self.name,
            "endpoint": self.endpoint,
            "active": self.active,
            "events": [event.to_dict() for event in self.events] if self.events else [],
        }

    def to_insert_dict(self) -> dict:
        """
        Convert the instance to a dictionary representing the XML insert format.

        :return: A dictionary representation of the webhook setting instance in XML insert format.
        """
        event_dicts = (
            [event.to_insert_dict() for event in self.events] if self.events else []
        )
        return {
            "WebhookSetting": {
                "Name": self.name,
                "Endpoint": self.endpoint,
                "Active": self.active,
                "Events": event_dicts,
            }
        }
