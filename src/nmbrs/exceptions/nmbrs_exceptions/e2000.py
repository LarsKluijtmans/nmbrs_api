"""Nmbrs error 2000"""

from .nmbrs_base_exception import NmbrsBaseException


class InvalidHourComponentException(NmbrsBaseException):
    """Nmbrs error code: 2001"""

    def __init__(self, resource: str) -> None:
        super().__init__(2001, resource)


class InvalidWageComponentException(NmbrsBaseException):
    """Nmbrs error code: 2002"""

    def __init__(self, resource: str) -> None:
        super().__init__(2002, resource)


class UnauthorizedEmployeeException(NmbrsBaseException):
    """Nmbrs error code: 2003"""

    def __init__(self, resource: str) -> None:
        super().__init__(2003, resource)


class UnauthorizedCompanyException(NmbrsBaseException):
    """Nmbrs error code: 2004"""

    def __init__(self, resource: str) -> None:
        super().__init__(2004, resource)


class InvalidPeriodException(NmbrsBaseException):
    """Nmbrs error code: 2006"""

    def __init__(self, resource: str) -> None:
        super().__init__(2006, resource)


class UnauthorizedDebtorException(NmbrsBaseException):
    """Nmbrs error code: 2009"""

    def __init__(self, resource: str) -> None:
        super().__init__(2009, resource)


class MultipleEnvironmentAccountsException(NmbrsBaseException):
    """
    Nmbrs error code: 2042

    SSO (Single-Sign-On) only error.
    """

    def __init__(self, resource: str) -> None:
        super().__init__(2042, resource)


class DomainNotFoundException(NmbrsBaseException):
    """
    Nmbrs error code: 2043

    SSO (Single-Sign-On) only error.
    """

    def __init__(self, resource: str) -> None:
        super().__init__(2043, resource)
