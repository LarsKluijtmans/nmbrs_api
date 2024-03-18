"""Microservice responsible for child related actions on the employee level."""

from zeep import Client

from ..micro_service import MicroService
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler


class EmployeeChildService(MicroService):
    """Microservice responsible for child related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["EmployeeService:Children_Get"])
    def get(self):
        """
        Get employee childs.

        For more information, refer to the official documentation:
            [Children_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Get)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Children_GetAll_Employeesbycompany"])
    def get_all_by_company(self):
        """
        Get employee childs.

        For more information, refer to the official documentation:
            [Children_GetAll_Employeesbycompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_GetAll_Employeesbycompany)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Child_Delete"])
    def delete(self):
        """
        Delete's child.

        For more information, refer to the official documentation:
            [Child_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Child_Delete)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Children_Insert"])
    def insert(self):
        """
        Insert an employee child.

        For more information, refer to the official documentation:
            [Children_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Children_InsertBatch"])
    def insert_batch(self):
        """
        Insert employee children.

        For more information, refer to the official documentation:
            [Children_InsertBatch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_InsertBatch)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["EmployeeService:Children_Update"])
    def update(self):
        """
        Update employee child.

        For more information, refer to the official documentation:
            [Children_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Update)
        """
        raise NotImplementedError()  # pragma: no cover
