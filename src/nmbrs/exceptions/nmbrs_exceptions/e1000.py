"""Nmbrs error 1000"""

from .nmbrs_base_exception import NmbrsBaseException


class InvalidCredentialsException(NmbrsBaseException):
    """
    Nmbrs error code: 1000 (This error does not have a code)

    SSO (Single-Sign-On) only error.
    """

    def __init__(self, resource: str) -> None:
        super().__init__(1000, resource)


class AuthenticationException(NmbrsBaseException):
    """
    Nmbrs error code: 1001
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(1001, resource=resource)


class AuthorizationException(NmbrsBaseException):
    """
    Nmbrs error code: 1002
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(1002, resource=resource)


class AuthorizationDataException(NmbrsBaseException):
    """
    Nmbrs error code: 1003
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(1003, resource=resource)


class NoValidSubscriptionException(NmbrsBaseException):
    """
    Nmbrs error code: 1004
    """

    def __init__(
        self,
        resource: str,
    ) -> None:
        super().__init__(1004, resource=resource)


class LoginSecurityFailureException(NmbrsBaseException):
    """
    Nmbrs error code: 1006

    SSO (Single-Sign-On) only error.
    """

    def __init__(self, resource: str) -> None:
        super().__init__(1006, resource)
