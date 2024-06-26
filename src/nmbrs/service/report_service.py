"""
Service class for managing reports in Nmbrs.
"""

import logging
from time import sleep

import xmltodict
from zeep import Client

from ..auth.token_manager import AuthManager
from ..exceptions.nmbrs_exceptions.background_task import (
    BackgroundTaskException,
    UnknownBackgroundTaskException,
    UnknownCall,
)
from .service import Service
from ..utils.nmbrs_exception_handler import nmbrs_exception_handler

logger = logging.getLogger(__name__)


class ReportService(Service):
    """Service class for managing reports in Nmbrs."""

    def __init__(self, auth_manager: AuthManager, sandbox: bool = True):
        super().__init__(auth_manager, sandbox)

        # Initialize nmbrs services
        self.client = Client(f"{self.base_uri}{self.report_uri}")
        logger.info("ReportService initialized.")

    @nmbrs_exception_handler(resource="ReportService:Reports_BackgroundTask_Result")
    def background_task_result(self, task_id: str, wait_limit: int = 60) -> dict | None:
        """
        Retrieve the report generated by a background task.

        For more information, refer to the official documentation:
            [Reports_BackgroundTask_Result](https://api.nmbrs.nl/soap/v3/ReportService.asmx?op=Reports_BackgroundTask_Result)

        Args:
            task_id (str): The ID of the background task.
            wait_limit (int, optional): Time limit (in seconds) to wait for the task result. Defaults to 60 (1 minute).

        Returns:
            dict | None: The result of the background task, or None if the task did not complete within the specified time limit.
        """
        with self.client.settings(xml_huge_tree=True):
            for _ in range(wait_limit):
                result = self.client.service.Reports_BackgroundTask_Result(
                    TaskId=task_id,
                    _soapheaders=self.auth_manager.header,
                )
                if result["Status"] in ("Executing", "Enqueued"):
                    sleep(1)
                elif result["Status"] == "Unknown":
                    logger.error("Unknown status received for background task.")
                    raise UnknownBackgroundTaskException()
                elif result["Status"] == "Error":
                    logger.error("Background task encountered an error.")
                    raise BackgroundTaskException()
                elif result["Status"] == "Success":
                    logger.info("Background task completed successfully.")
                    return xmltodict.parse(result["Content"])
            return None

    @nmbrs_exception_handler(resource="ReportService")
    def get_task_id(self, task_name: str, task_args: dict) -> str:
        """
        Get the ID of a background task.

        Args:
            task_name (str): The name of the background task.
            task_args (dict): The arguments required for the background task.

        Returns:
            str: The ID of the background task.
        """
        try:
            response = self.client.service[task_name](
                **task_args,
                _soapheaders=self.auth_manager.header,
            )
            return response
        except AttributeError as e:
            logger.error("Unknown call made to the ReportService %s", task_name)
            raise UnknownCall(task_name) from e
