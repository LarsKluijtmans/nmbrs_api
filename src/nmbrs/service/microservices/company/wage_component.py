# pylint: disable=line-too-long
"""Microservice responsible for wage component related actions on the company level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyWageComponentService(MicroService):
    """Microservice responsible for wage component related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Get"])
    def fixed_get(self):
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_GetCurrent"])
    def fixed_get_current(self):
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Insert"])
    def fixed_insert(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_InsertCurrent"])
    def fixed_insert_current(self):
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Insert_Batch"])
    def fixed_insert_batch(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Stop"])
    def fixed_stop(self):
        """
        Stop a wage component ending after given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Stop)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Get"])
    def variable_get(self):
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_GetCurrent"])
    def variable_get_current(self):
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Insert"])
    def variable_insert(self):
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_InsertCurrent"])
    def variable_insert_current(self):
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_InsertCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Insert_Batch"])
    def variable_insert_batch(self):
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert_Batch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Clear"])
    def variable_clear(self):
        """
        Clear all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Clear)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_ClearCurrent"])
    def variable_clear_current(self):
        """
        Clear all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_ClearCurrent)
        """
        raise NotImplementedError()  # pragma: no cover
