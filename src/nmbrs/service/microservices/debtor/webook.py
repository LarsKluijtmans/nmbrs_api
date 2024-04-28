"""Microservice responsible for webhooks related actions on the debtor level."""

from zeep import Client
from zeep.helpers import serialize_object

from ....auth.token_manager import AuthManager
from ....data_classes.debtor import WebhookSetting, Event
from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class DebtorWebHooksService(MicroService):
    """Microservice responsible for webhooks related actions on the debtor level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="DebtorService:WebhookSettings_Delete")
    def delete(self, debtor_id: int, webhook_id: int) -> bool:
        """
        Delete a webhook for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Delete](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Delete)

        Args:
            debtor_id (int): The ID of the debtor.
            webhook_id (int): The ID of the webhook to be deleted.

        Returns:
            bool: True if the webhook is successfully deleted, otherwise False.
        """
        deleted = self.client.service.WebhookSettings_Delete(
            DebtorId=debtor_id,
            WebhookSettingId=webhook_id,
            _soapheaders=self.auth_manager.header,
        )
        return deleted

    @return_list
    @nmbrs_exception_handler(resource="DebtorService:WebhookSettings_Get")
    def get_all(self, debtor_id: int) -> list[WebhookSetting]:
        """
        Retrieve all webhooks for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Get)

        Args:
            debtor_id (int): The ID of the debtor.

        Returns:
            list[WebhookSetting]: A list of WebhookSetting objects representing all webhooks associated with the debtor.
        """
        webhooks = self.client.service.WebhookSettings_Get(DebtorId=debtor_id, _soapheaders=self.auth_manager.header)
        webhooks = [WebhookSetting(debtor_id=debtor_id, data=webhook) for webhook in serialize_object(webhooks)]
        return webhooks

    @return_list
    @nmbrs_exception_handler(resource="DebtorService:WebhookSettings_GetEvents")
    def get_all_events(self) -> list[Event]:
        """
        Retrieve all webhook events.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_GetEvents](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_GetEvents)

        Returns:
            list[Event]: A list of Event objects representing all webhook events.
        """
        events = self.client.service.WebhookSettings_GetEvents(_soapheaders=self.auth_manager.header)
        events = [Event(event) for event in serialize_object(events)]
        return events

    @nmbrs_exception_handler(resource="DebtorService:WebhookSettings_Insert")
    def insert(self, debtor_id: int, insert_webhook_settings: WebhookSetting) -> int:
        """
        Insert a webhook for a debtor.

        For more information, refer to the official documentation:
            [Soap call WebhookSettings_Insert](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=WebhookSettings_Insert)

        Args:
            debtor_id (int): The ID of the debtor.
            insert_webhook_settings (WebhookSetting): The WebhookSetting object to be inserted.

        Returns:
            int: The ID of the inserted webhook.
        """
        data = {
            "DebtorId": debtor_id,
            "WebhookSetting": insert_webhook_settings.to_insert_dict(),
        }
        inserted = self.client.service.WebhookSettings_Insert(**data, _soapheaders=self.auth_manager.header)
        return inserted
