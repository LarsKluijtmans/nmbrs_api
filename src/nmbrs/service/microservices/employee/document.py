"""Microservice responsible for document related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeDocumentService(MicroService):
    """Microservice responsible for document related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:EmployeeDocument_UploadDocument")
    def upload(self):
        """
        Uploads document for employee.

        For more information, refer to the official documentation:
            [EmployeeDocument_UploadDocument](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeDocument_UploadDocument)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resource="EmployeeService:EmployeeDocument_UploadDocumentFull")
    def upload_full(self):
        """
        Uploads document for employee with all the fields.

        For more information, refer to the official documentation:
            [EmployeeDocument_UploadDocumentFull](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=EmployeeDocument_UploadDocumentFull)
        """
        raise NotImplementedError()  # pragma: no cover
