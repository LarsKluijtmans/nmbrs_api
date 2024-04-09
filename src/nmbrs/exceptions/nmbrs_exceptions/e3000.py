"""Nmbrs error 3000"""

from .nmbrs_base_exception import NmbrsBaseException


class AuthenticationException(NmbrsBaseException):
    """
    Nmbrs error code: 3001
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(3001, resource=resource)
