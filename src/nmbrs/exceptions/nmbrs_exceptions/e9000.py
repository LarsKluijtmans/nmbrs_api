"""Nmbrs error 9000"""

from .nmbrs_base_exception import NmbrsBaseException


class UnknownNmbrsException(NmbrsBaseException):
    """Nmbrs error code: 9999"""

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(1001, resource=resource)


class UnknownException(NmbrsBaseException):
    """
    Custom exception in case the returned Nmbrs exception is unknown.
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(0, resource=resource)
