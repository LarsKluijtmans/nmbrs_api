"""Microservice responsible for child related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Child
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeChildService(MicroService):
    """Microservice responsible for child related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Children_Get")
    def get_current(self, employee_id: int) -> list[Child]:
        """
        Get employee childs.

        For more information, refer to the official documentation:
            [Children_Get](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Get)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Child]: A list of Child objects representing the children.
        """
        children = self.client.service.Children_Get(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        children = serialize_object(children)

        _children = []
        for child in children["EmployeeChildren"]["Child"]:
            _children.append(Child(employee_id=children["EmployeeId"], data=child))
        return _children

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Children_GetAll_Employeesbycompany")
    def get_all_by_company(self, company_id: int) -> list[Child]:
        """
        Get employee childs.

        For more information, refer to the official documentation:
            [Children_GetAll_Employeesbycompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_GetAll_Employeesbycompany)

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Child]: A list of Child objects representing the children.
        """
        children = self.client.service.Children_GetAll_Employeesbycompany(CompanyId=company_id, _soapheaders=self.auth_manager.header)

        _children = []
        for employee in serialize_object(children):
            for child in employee["EmployeeChildren"]["Child"]:
                _children.append(Child(employee_id=employee["EmployeeId"], data=child))
        return _children

    @nmbrs_exception_handler(resource="EmployeeService:Child_Delete")
    def delete(self, employee_id: int, child_id: int) -> str:
        """
        Deletes child.

        For more information, refer to the official documentation:
            [Child_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Child_Delete)

        Args:
            employee_id (int): The ID of the employee.
            child_id (int): The ID of the child.

        Returns:
            str: The response indicating the success of the operation.
        """
        response = self.client.service.Child_Delete(EmployeeId=employee_id, ChildId=child_id, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Children_Insert")
    def post(self, employee_id: int, child: Child) -> str:
        """
        Insert an employee child.

        For more information, refer to the official documentation:
            [Children_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Insert)

        Args:
            employee_id (int): The ID of the employee.
            child (Child): The Child object to insert.

        Returns:
            str: A str indicating the success of the operation.
        """
        _child = {
            "Id": child.id,
            "Name": child.name,
            "FirstName": child.first_name,
            "Initials": child.initials,
            "Gender": child.gender,
            "Birthday": child.birthday,
        }
        response = self.client.service.Children_Insert(
            EmployeeId=employee_id,
            child=_child,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Children_InsertBatch")
    def post_batch(self, employee_id: int, children: list[Child]) -> str:
        """
        Insert employee children.

        For more information, refer to the official documentation:
            [Children_InsertBatch](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_InsertBatch)

        Args:
            employee_id (int): The ID of the employee.
            children (list[Child]): The list of Child objects to insert.

        Returns:
            str: A str indicating the success of the operation.
        """
        _children = []
        for child in children:
            _children.append(
                {
                    "Id": child.id,
                    "Name": child.name,
                    "FirstName": child.first_name,
                    "Initials": child.initials,
                    "Gender": child.gender,
                    "Birthday": child.birthday,
                }
            )
        response = self.client.service.Children_InsertBatch(
            EmployeeId=employee_id,
            children=_children,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Children_Update")
    def update(self, employee_id: int, child: Child) -> str:
        """
        Update employee child.

        For more information, refer to the official documentation:
            [Children_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Children_Update)

        Args:
            employee_id (int): The ID of the employee.
            child (Child): The Child object to insert.

        Returns:
            str: A str indicating the success of the operation.
        """
        _child = {
            "Id": child.id,
            "Name": child.name,
            "FirstName": child.first_name,
            "Initials": child.initials,
            "Gender": child.gender,
            "Birthday": child.birthday,
        }
        response = self.client.service.Children_Update(
            EmployeeId=employee_id,
            child=_child,
            _soapheaders=self.auth_manager.header,
        )
        return response
