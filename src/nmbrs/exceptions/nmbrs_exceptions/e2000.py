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


class ProtectedModeException(NmbrsBaseException):
    """Nmbrs error code: 2011"""

    def __init__(self, resource: str) -> None:
        super().__init__(2011, resource)


class WageTaxDeclarationAlreadySentException(NmbrsBaseException):
    """Nmbrs error code: 2012"""

    def __init__(self, resource: str) -> None:
        super().__init__(2012, resource)


class NotAvailableOnFreeTrialException(NmbrsBaseException):
    """Nmbrs error code: 2013"""

    def __init__(self, resource: str) -> None:
        super().__init__(2013, resource)


class InvalidBankAccountIbanException(NmbrsBaseException):
    """Nmbrs error code: 2014"""

    def __init__(self, resource: str) -> None:
        super().__init__(2014, resource)


class InvalidBankAccountNumberException(NmbrsBaseException):
    """Nmbrs error code: 2015"""

    def __init__(self, resource: str) -> None:
        super().__init__(2015, resource)


class InvalidBankAccountTypeException(NmbrsBaseException):
    """Nmbrs error code: 2016"""

    def __init__(self, resource: str) -> None:
        super().__init__(2016, resource)


class InvalidLabourAgreementIdException(NmbrsBaseException):
    """Nmbrs error code: 2017"""

    def __init__(self, resource: str) -> None:
        super().__init__(2017, resource)


class InvalidLeaveIdException(NmbrsBaseException):
    """Nmbrs error code: 2018"""

    def __init__(self, resource: str) -> None:
        super().__init__(2018, resource)


class TaskStatusNotAvailableException(NmbrsBaseException):
    """Nmbrs error code: 2019"""

    def __init__(self, resource: str) -> None:
        super().__init__(2019, resource)


class TaskStatusNotAvailable2Exception(NmbrsBaseException):
    """Nmbrs error code: 2020"""

    def __init__(self, resource: str) -> None:
        super().__init__(2020, resource)


class InvalidTaskResultException(NmbrsBaseException):
    """Nmbrs error code: 2021"""

    def __init__(self, resource: str) -> None:
        super().__init__(2021, resource)


class InvalidLeaveTypeException(NmbrsBaseException):
    """Nmbrs error code: 2022"""

    def __init__(self, resource: str) -> None:
        super().__init__(2022, resource)


class StartTimeAfterEndTimeException(NmbrsBaseException):
    """Nmbrs error code: 2028"""

    def __init__(self, resource: str) -> None:
        super().__init__(2028, resource)


class TimeSlotsOverlapException(NmbrsBaseException):
    """Nmbrs error code: 2029"""

    def __init__(self, resource: str) -> None:
        super().__init__(2029, resource)


class InvalidSetOfValuesException(NmbrsBaseException):
    """Nmbrs error code: 2030"""

    def __init__(self, resource: str) -> None:
        super().__init__(2030, resource)


class BankAccountIbanRequiredException(NmbrsBaseException):
    """Nmbrs error code: 2032"""

    def __init__(self, resource: str) -> None:
        super().__init__(2032, resource)


class TaxTypeRequiredException(NmbrsBaseException):
    """Nmbrs error code: 2033"""

    def __init__(self, resource: str) -> None:
        super().__init__(2033, resource)


class InvalidTaxTypeException(NmbrsBaseException):
    """Nmbrs error code: 2034"""

    def __init__(self, resource: str) -> None:
        super().__init__(2034, resource)


class TaxFormRequiredException(NmbrsBaseException):
    """Nmbrs error code: 2035"""

    def __init__(self, resource: str) -> None:
        super().__init__(2035, resource)


class InvalidTaxFormException(NmbrsBaseException):
    """Nmbrs error code: 2036"""

    def __init__(self, resource: str) -> None:
        super().__init__(2036, resource)


class InvalidCostCenterIdException(NmbrsBaseException):
    """Nmbrs error code: 2037"""

    def __init__(self, resource: str) -> None:
        super().__init__(2037, resource)


class InvalidCostCenterCode(NmbrsBaseException):
    """Nmbrs error code: 2038"""

    def __init__(self, resource: str) -> None:
        super().__init__(2038, resource)


class DuplicatedCostCenterCodeExceptionException(NmbrsBaseException):
    """Nmbrs error code: 2039"""

    def __init__(self, resource: str) -> None:
        super().__init__(2039, resource)


class ProvideExtensionException(NmbrsBaseException):
    """Nmbrs error code: 2040"""

    def __init__(self, resource: str) -> None:
        super().__init__(2040, resource)


class FileTooLargeException(NmbrsBaseException):
    """Nmbrs error code: 2041"""

    def __init__(self, resource: str) -> None:
        super().__init__(2041, resource)


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


class InvalidEndpointException(NmbrsBaseException):
    """Nmbrs error code: 2044"""

    def __init__(self, resource: str) -> None:
        super().__init__(2044, resource)


class InvalidNameException(NmbrsBaseException):
    """Nmbrs error code: 2045"""

    def __init__(self, resource: str) -> None:
        super().__init__(2045, resource)


class NotFoundException(NmbrsBaseException):
    """Nmbrs error code: 2046"""

    def __init__(self, resource: str) -> None:
        super().__init__(2046, resource)


class InvalidDocumentTypeException(NmbrsBaseException):
    """Nmbrs error code: 2047"""

    def __init__(self, resource: str) -> None:
        super().__init__(2047, resource)
