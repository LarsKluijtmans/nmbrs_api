from datetime import datetime

from nmbrs_soap_api.data_classes.debtor.absence_verzuim import AbsenceVerzuim
from nmbrs_soap_api.services.service import Service
from zeep import Client
from zeep.helpers import serialize_object

from nmbrs_soap_api.global_variables import (
    nmbrs_base_uri,
    nmbrs_sandbox_base_uri,
    debtor_uri,
)


class DebtorService(Service):
    """
    A class representing Debtor Service for interacting with Nmbrs debtor-related functionalities.
    """

    def __init__(self, auth_header: dict, sandbox: bool) -> None:
        """
        Constructor method for DebtorService class.

        Initializes DebtorService instance with authentication and sandbox settings.

        :param auth_header: A dictionary containing authentication details.
        :param sandbox: A boolean indicating whether to use the sandbox environment.
        """
        self.auth_header = auth_header
        self.sandbox = sandbox

        # Initialize nmbrs services
        base_uri = nmbrs_base_uri
        if sandbox:
            base_uri = nmbrs_sandbox_base_uri
        self.debtor_service = Client(f"{base_uri}{debtor_uri}")

    def set_auth_header(self, auth_header: dict) -> None:
        """
        Method to set the authentication.

        :param auth_header: A dictionary containing authentication details.
        """
        self.auth_header = auth_header

    def get_absence_xml(
        self, debtor_id: int, start_date: datetime, end_date: datetime
    ) -> list[AbsenceVerzuim]:
        """
        Retrieve absence data for a debtor within a specified date range.

        This method calls the SOAP operation 'AbsenceXML_Get' from the Nmbrs API,
        which retrieves absence data for the specified debtor within the provided date range.

        For more information, refer to the official documentation:
        [Soap call AbsenceXML_Get](https://api.nmbrs.nl/soap/v3/DebtorService.asmx?op=AbsenceXML_Get)

        :param debtor_id: An integer representing the debtor's ID.
        :param start_date: A datetime representing the start date of the period to retrieve data.
        :param end_date: A datetime representing the end date of the period to retrieve data.
        :return: A list of AbsenceVerzuim objects representing the absence data.
        """
        data = {"DebtorId": debtor_id, "from": start_date, "to": end_date}
        absences = self.debtor_service.service.AbsenceXML_Get(
            **data, _soapheaders=self.auth_header
        )
        absences = [AbsenceVerzuim(absence) for absence in serialize_object(absences)]
        return absences
