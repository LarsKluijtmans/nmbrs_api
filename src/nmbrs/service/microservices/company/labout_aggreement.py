"""Microservice responsible for labour agreement related actions on the company level."""

from zeep import Client
from zeep.helpers import serialize_object

from src.nmbrs.data_classes.company import LabourAgreement
from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler
from src.nmbrs.utils.return_list import return_list


class CompanyLabourAgreementService(MicroService):
    """
    Microservice responsible for labour agreement related actions on the company level.
    """

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:LabourAgreements_Get"])
    def get(self, company_id: int, period: int, year: int):
        """
        Get a list of all the labour agreements that are assigned to a company.

        For more information, refer to the official documentation:
            [LabourAgreements_Get](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=LabourAgreements_Get)

        Args:
            company_id (int): The ID of the company.
            period (int): The period.
            year (int): The year.

        Returns:
            list[LabourAgreement]: A list of LabourAgreement objects.
        """
        labour_agreements = self.client.service.LabourAgreements_Get(
            CompanyId=company_id,
            Period=period,
            Year=year,
            _soapheaders=self.auth_header,
        )
        labour_agreements = [LabourAgreement(labour_agreement) for labour_agreement in serialize_object(labour_agreements)]
        return labour_agreements

    @return_list
    @nmbrs_exception_handler(resources=["CompanyService:LabourAgreements_GetCurrent"])
    def get_current(self, company_id: int):
        """
        Get a list of current labour agreements assigned to a company.

        For more information, refer to the official documentation:
            [LabourAgreements_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=LabourAgreements_GetCurrent)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[LabourAgreement]: A list of LabourAgreement objects representing the current labour agreements.
        """
        labour_agreements = self.client.service.LabourAgreements_GetCurrent(CompanyId=company_id, _soapheaders=self.auth_header)
        labour_agreements = [LabourAgreement(labour_agreement) for labour_agreement in serialize_object(labour_agreements)]
        return labour_agreements
