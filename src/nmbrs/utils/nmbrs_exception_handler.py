"""Exception Handling Decorators for Nmbrs SOAP API"""

import zeep.exceptions

from ..exceptions import (
    AuthenticationException,
    AuthorizationException,
    AuthorizationDataException,
    NoValidSubscriptionException,
    InvalidHourComponentException,
    InvalidWageComponentException,
    UnauthorizedEmployeeException,
    UnauthorizedCompanyException,
    InvalidPeriodException,
    UnauthorizedDebtorException,
    UnknownNmbrsException,
    UnknownException,
    LoginSecurityFailureException,
    MultipleEnvironmentAccountsException,
    DomainNotFoundException,
    InvalidCredentialsException,
    InvalidBankAccountIbanException,
    NotAvailableOnFreeTrialException,
    WageTaxDeclarationAlreadySentException,
    ProtectedModeException,
    InvalidLeaveTypeException,
    InvalidTaskResultException,
    TaskStatusNotAvailable2Exception,
    TaskStatusNotAvailableException,
    InvalidLeaveIdException,
    InvalidLabourAgreementIdException,
    InvalidBankAccountTypeException,
    InvalidBankAccountNumberException,
    TimeSlotsOverlapException,
    StartTimeAfterEndTimeException,
    InvalidTaxTypeException,
    TaxTypeRequiredException,
    BankAccountIbanRequiredException,
    InvalidSetOfValuesException,
    TaxFormRequiredException,
    FileTooLargeException,
    ProvideExtensionException,
    DuplicatedCostCenterCodeExceptionException,
    InvalidCostCenterCode,
    InvalidCostCenterIdException,
    InvalidTaxFormException,
    InvalidNameException,
    InvalidEndpointException,
    NotFoundException,
    InvalidDocumentTypeException,
)


def nmbrs_exception_handler(resource: str):
    """
    Decorator to handle exceptions raised by Nmbrs SOAP API.

    Args:
        resource (str): Resources being called.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except zeep.exceptions.Fault as e:
                error_map = {
                    1001: AuthenticationException,
                    1002: AuthorizationException,
                    1003: AuthorizationDataException,
                    1004: NoValidSubscriptionException,
                    1006: LoginSecurityFailureException,
                    2001: InvalidHourComponentException,
                    2002: InvalidWageComponentException,
                    2003: UnauthorizedEmployeeException,
                    2004: UnauthorizedCompanyException,
                    2006: InvalidPeriodException,
                    2009: UnauthorizedDebtorException,
                    2011: ProtectedModeException,
                    2012: WageTaxDeclarationAlreadySentException,
                    2013: NotAvailableOnFreeTrialException,
                    2014: InvalidBankAccountIbanException,
                    2015: InvalidBankAccountNumberException,
                    2016: InvalidBankAccountTypeException,
                    2017: InvalidLabourAgreementIdException,
                    2018: InvalidLeaveIdException,
                    2019: TaskStatusNotAvailableException,
                    2020: TaskStatusNotAvailable2Exception,
                    2021: InvalidTaskResultException,
                    2022: InvalidLeaveTypeException,
                    2028: StartTimeAfterEndTimeException,
                    2029: TimeSlotsOverlapException,
                    2030: InvalidSetOfValuesException,
                    2032: BankAccountIbanRequiredException,
                    2033: TaxTypeRequiredException,
                    2034: InvalidTaxTypeException,
                    2035: TaxFormRequiredException,
                    2036: InvalidTaxFormException,
                    2037: InvalidCostCenterIdException,
                    2038: InvalidCostCenterCode,
                    2039: DuplicatedCostCenterCodeExceptionException,
                    2040: ProvideExtensionException,
                    2041: FileTooLargeException,
                    2042: MultipleEnvironmentAccountsException,
                    2043: DomainNotFoundException,
                    2044: InvalidEndpointException,
                    2045: InvalidNameException,
                    2046: NotFoundException,
                    2047: InvalidDocumentTypeException,
                    9999: UnknownNmbrsException,
                }
                exception_str = str(e)

                # Exceptions without code
                if "---> Invalid combination email/password" in exception_str:
                    raise InvalidCredentialsException(resource=resource) from e

                for error_code, exception_class in error_map.items():
                    if f"---> {error_code}:" in exception_str:
                        raise exception_class(resource=resource) from e
                raise UnknownException(resource=resource) from e

        return wrapper

    return decorator
