"""
Exception specifically related to the resource:
    - ReportService:Reports_BackgroundTask_Result
"""

from .nmbrs_base_exception import NmbrsBaseException


class BackgroundTaskException(NmbrsBaseException):
    """
    Error occurred when requesting a background report from nmbrs.

    The nmbrs API returned the status: "Error"
    """

    def __init__(self, resource: str = "ReportService:Reports_BackgroundTask_Result") -> None:
        super().__init__(10001, resource)


class UnknownBackgroundTaskException(NmbrsBaseException):
    """
    Unknown error occurred when requesting a background report from nmbrs.

    The nmbrs API returned the status: "Unknown"
    """

    def __init__(self, resource: str = "ReportService:Reports_BackgroundTask_Result") -> None:
        super().__init__(10002, resource)


class UnknownCall(Exception):
    """
    The selected call does not exist in the nmbrs report service.
    """

    def __init__(self, call: str):
        self.message = f"Call {call} does not exist in service."
        super(Exception, self).__init__(self.message)
