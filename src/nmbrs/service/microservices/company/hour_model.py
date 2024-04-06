"""Microservice responsible for hour model related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....data_classes.company import HourCode
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class CompanyHourModelService(MicroService):
    """Microservice responsible for hour model related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:HourModel_GetHourCodes"])
    def get(self, company_id: int) -> list[HourCode]:
        """
        Get hour codes that belong to a company's hour model.

        For more information, refer to the official documentation:
            [HourModel_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel_GetHourCodes)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[HourCode]: A list of hour code objects.
        """
        hour_codes = self.client.service.HourModel_GetHourCodes(CompanyId=company_id, _soapheaders=self.auth_header)
        return [HourCode(company_id=company_id, data=hour_code) for hour_code in serialize_object(hour_codes)]

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:HourModel2_GetHourCodes"])
    def get_2(self, company_id: int) -> list[HourCode]:
        """
        Get hour codes that belong to a company's hour model 2.

        For more information, refer to the official documentation:
            [HourModel2_GetHourCodes](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=HourModel2_GetHourCodes)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[HourCode]: A list of hour code objects.
        """
        hour_codes = self.client.service.HourModel2_GetHourCodes(CompanyId=company_id, _soapheaders=self.auth_header)
        return [HourCode(company_id=company_id, data=hour_code) for hour_code in serialize_object(hour_codes)]
