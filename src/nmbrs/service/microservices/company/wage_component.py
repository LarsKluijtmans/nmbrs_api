# pylint: disable=line-too-long
"""Microservice responsible for wage component related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import WageComponent
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyWageComponentService(MicroService):
    """Microservice responsible for wage component related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Get"])
    def fixed_get(self, company_id: int, year: int, period: int) -> list[WageComponent]:
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Get)
        """
        wage_components = self.client.service.WageComponentFixed_Get(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header
        )
        wage_components = [
            WageComponent(company_id=company_id, component_type="fixed", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_GetCurrent"])
    def fixed_get_current(self, company_id: int):
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_GetCurrent)
        """
        wage_components = self.client.service.WageComponentFixed_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_header)
        wage_components = [
            WageComponent(company_id=company_id, component_type="fixed", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Insert"])
    def fixed_insert(
        self,
        wage_component: WageComponent,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> int:
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert)
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentFixed_Insert(
            CompanyId=wage_component.company_id,
            WageComponent=new_wage_component,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_header,
        )
        return response

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_InsertCurrent"])
    def fixed_insert_current(self, wage_component: WageComponent) -> int:
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_InsertCurrent)
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentFixed_InsertCurrent(
            CompanyId=wage_component.company_id, WageComponent=new_wage_component, _soapheaders=self.auth_header
        )
        return response

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Insert_Batch"])
    def fixed_insert_batch(
        self,
        wage_components: list[WageComponent],
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert_Batch)
        """
        new_wage_components = []
        for wage_component in wage_components:
            new_wage_components.append(
                {
                    "CompanyId": wage_component.company_id,
                    "Id": wage_component.id,
                    "Code": wage_component.code,
                    "Value": wage_component.value,
                }
            )
        response = self.client.service.WageComponentFixed_Insert_Batch(
            WageComponents=new_wage_components, Period=period, Year=year, UnprotectedMode=protected_mode, _soapheaders=self.auth_header
        )
        return response

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentFixed_Stop"])
    def fixed_stop(
        self,
        company_id: int,
        component_id: int,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> None:
        """
        Stop a wage component ending after given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Stop)
        """
        self.client.service.WageComponentFixed_Stop(
            CompanyId=company_id,
            WageComponentId=component_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_header,
        )

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Get"])
    def variable_get(self, company_id: int, year: int, period: int) -> list[WageComponent]:
        """
        Get all fixed wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Get)
        """
        wage_components = self.client.service.WageComponentVar_Get(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_header
        )
        wage_components = [
            WageComponent(company_id=company_id, component_type="variable", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_GetCurrent"])
    def variable_get_current(self, company_id: int) -> list[WageComponent]:
        """
        Get all fixed wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_GetCurrent)
        """
        wage_components = self.client.service.WageComponentVar_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_header)
        wage_components = [
            WageComponent(company_id=company_id, component_type="variable", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Insert"])
    def variable_insert(
        self,
        wage_component: WageComponent,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> int:
        """
        Insert a wage component to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert)
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentVar_Insert(
            CompanyId=wage_component.company_id,
            WageComponent=new_wage_component,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_header,
        )
        return response

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_InsertCurrent"])
    def variable_insert_current(self, wage_component: WageComponent) -> int:
        """
        Insert a wage component to the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_InsertCurrent)
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentVar_InsertCurrent(
            CompanyId=wage_component.company_id, WageComponent=new_wage_component, _soapheaders=self.auth_header
        )
        return response

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Insert_Batch"])
    def variable_insert_batch(
        self,
        wage_components: list[WageComponent],
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Insert a batch of wage components to given period. If the period is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert_Batch)
        """
        new_wage_components = []
        for wage_component in wage_components:
            new_wage_components.append(
                {
                    "CompanyId": wage_component.company_id,
                    "Id": wage_component.id,
                    "Code": wage_component.code,
                    "Value": wage_component.value,
                }
            )
        response = self.client.service.WageComponentVar_Insert_Batch(
            WageComponents=new_wage_components, Period=period, Year=year, UnprotectedMode=protected_mode, _soapheaders=self.auth_header
        )
        return response

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_Clear"])
    def variable_clear(
        self,
        company_id: int,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Clear all variable wage components for given period.

        For more information, refer to the official documentation:
            [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Clear)
        """
        response = self.client.service.WageComponentVar_Clear(
            CompanyId=company_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_header,
        )
        return response

    @nmbrs_exception_handler(resources=["CompanyService:WageComponentVar_ClearCurrent"])
    def variable_clear_current(
        self,
        company_id: int,
    ) -> list[int]:
        """
        Clear all variable wage components for the current period.

        For more information, refer to the official documentation:
            [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_ClearCurrent)
        """
        response = self.client.service.WageComponentVar_ClearCurrent(
            CompanyId=company_id,
            _soapheaders=self.auth_header,
        )
        return response
