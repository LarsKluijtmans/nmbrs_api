"""Microservice responsible for document related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeDocumentService(MicroService):
    """Microservice responsible for document related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:EmployeeDocument_UploadDocument"])
    def upload(self):
        """
        Uploads document for employee.

        For more information, refer to the official documentation:
            [EmployeeDocument_UploadDocument](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeDocument_UploadDocument)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:EmployeeDocument_UploadDocumentFull"])
    def upload_full(self):
        """
        Uploads document for employee with all the fields.

        For more information, refer to the official documentation:
            [EmployeeDocument_UploadDocumentFull](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeDocument_UploadDocumentFull)
        """
        raise NotImplementedError()  # pragma: no cover
