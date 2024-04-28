"""Microservice responsible for wage component related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.company import WageComponent
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyWageComponentService(MicroService):
    """Microservice responsible for wage component related actions on the company level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_Get")
    def get_fixed(self, company_id: int, year: int, period: int) -> list[WageComponent]:
        """
        Retrieve all fixed wage components for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Get)

        Args:
            company_id (int): The ID of the company.
            year (int): The year.
            period (int): The period.

        Returns:
            list[WageComponent]: A list of fixed wage components.
        """
        wage_components = self.client.service.WageComponentFixed_Get(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        wage_components = [
            WageComponent(company_id=company_id, component_type="fixed", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_GetCurrent")
    def get_current_fixed(self, company_id: int):
        """
        Retrieve all fixed wage components for the current period of a specified company.

        For more information, refer to the official documentation:
            [WageComponentFixed_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[WageComponent]: A list of fixed wage components for the current period.
        """
        wage_components = self.client.service.WageComponentFixed_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        wage_components = [
            WageComponent(company_id=company_id, component_type="fixed", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_Insert")
    def post_fixed(
        self,
        wage_component: WageComponent,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> int:
        """
        Insert a fixed wage component for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert)

        Args:
            wage_component (WageComponent): The fixed wage component to insert.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            int: The ID of the inserted fixed wage component.
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentFixed_Insert(
            CompanyId=wage_component.company_id,
            WageComponent=new_wage_component,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_InsertCurrent")
    def post_current_fixed(self, wage_component: WageComponent) -> int:
        """
        Insert a fixed wage component for the current period of a specified company.

        For more information, refer to the official documentation:
            [WageComponentFixed_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_InsertCurrent)

        Args:
            wage_component (WageComponent): The fixed wage component to insert.

        Returns:
            int: The ID of the inserted fixed wage component.
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentFixed_InsertCurrent(
            CompanyId=wage_component.company_id, WageComponent=new_wage_component, _soapheaders=self.auth_manager.header
        )
        return response

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_Insert_Batch")
    def post_batch_fixed(
        self,
        wage_components: list[WageComponent],
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Insert multiple fixed wage components for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Insert_Batch)

        Args:
            wage_components (list[WageComponent]): The list of fixed wage components to insert.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            list[int]: The IDs of the inserted fixed wage components.
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
            WageComponents=new_wage_components,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="CompanyService:WageComponentFixed_Stop")
    def stop_fixed(
        self,
        company_id: int,
        component_id: int,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> None:
        """
        Stop a fixed wage component for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentFixed_Stop](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentFixed_Stop)

        Args:
            company_id (int): The ID of the company.
            component_id (int): The ID of the fixed wage component.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            None
        """
        self.client.service.WageComponentFixed_Stop(
            CompanyId=company_id,
            WageComponentId=component_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_Get")
    def get_variable(self, company_id: int, period: int, year: int) -> list[WageComponent]:
        """
        Retrieve all variable wage components for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentVar_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Get)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.

        Returns:
            list[WageComponent]: A list of variable wage components.
        """
        wage_components = self.client.service.WageComponentVar_Get(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.auth_manager.header
        )
        wage_components = [
            WageComponent(company_id=company_id, component_type="variable", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_GetCurrent")
    def get_current_variable(self, company_id: int) -> list[WageComponent]:
        """
        Retrieve all variable wage components for the current period of a specified company.

        For more information, refer to the official documentation:
            [WageComponentVar_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[WageComponent]: A list of variable wage components for the current period.
        """
        wage_components = self.client.service.WageComponentVar_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_manager.header)
        wage_components = [
            WageComponent(company_id=company_id, component_type="variable", data=wage_component)
            for wage_component in serialize_object(wage_components)
        ]
        return wage_components

    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_Insert")
    def post_variable(
        self,
        wage_component: WageComponent,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> int:
        """
        Insert a variable wage component for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert)

        Args:
            wage_component (WageComponent): The variable wage component to insert.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            int: The ID of the inserted variable wage component.
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentVar_Insert(
            CompanyId=wage_component.company_id,
            WageComponent=new_wage_component,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_InsertCurrent")
    def post_current_variable(self, wage_component: WageComponent) -> int:
        """
        Insert a variable wage component for the current period of a specified company.

        For more information, refer to the official documentation:
            [WageComponentVar_InsertCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_InsertCurrent)

        Args:
            wage_component (WageComponent): The variable wage component to insert.

        Returns:
            int: The ID of the inserted variable wage component.
        """
        new_wage_component = {"Id": wage_component.id, "Code": wage_component.code, "Value": wage_component.value}
        response = self.client.service.WageComponentVar_InsertCurrent(
            CompanyId=wage_component.company_id, WageComponent=new_wage_component, _soapheaders=self.auth_manager.header
        )
        return response

    @return_list
    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_Insert_Batch")
    def post_batch_variable(
        self,
        wage_components: list[WageComponent],
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Insert multiple variable wage components for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentVar_Insert_Batch](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Insert_Batch)

        Args:
            wage_components (list[WageComponent]): The list of variable wage components to insert.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            list[int]: The IDs of the inserted variable wage components.
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
            WageComponents=new_wage_components,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_Clear")
    def clear_variable(
        self,
        company_id: int,
        period: int,
        year: int,
        protected_mode: bool,
    ) -> list[int]:
        """
        Clear all variable wage components for a specified company, year, and period.

        For more information, refer to the official documentation:
            [WageComponentVar_Clear](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_Clear)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.
            protected_mode (bool): Flag indicating whether the operation is protected.

        Returns:
            list[int]: The IDs of the cleared variable wage components.
        """
        response = self.client.service.WageComponentVar_Clear(
            CompanyId=company_id,
            Period=period,
            Year=year,
            UnprotectedMode=protected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="CompanyService:WageComponentVar_ClearCurrent")
    def clear_current_variable(self, company_id: int) -> list[int]:
        """
        Clear all variable wage components for the current period of a specified company.

        For more information, refer to the official documentation:
            [WageComponentVar_ClearCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=WageComponentVar_ClearCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[int]: The IDs of the cleared variable wage components.
        """
        response = self.client.service.WageComponentVar_ClearCurrent(
            CompanyId=company_id,
            _soapheaders=self.auth_manager.header,
        )
        return response
