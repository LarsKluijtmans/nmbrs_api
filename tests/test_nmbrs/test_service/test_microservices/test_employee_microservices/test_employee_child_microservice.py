"""Unit tests for the EmployeeChildService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from src.nmbrs.service.microservices.employee.child import EmployeeChildService, Child


class TestEmployeeChildService(unittest.TestCase):
    """Unit tests for the EmployeeChildService class."""

    def setUp(self):
        self.client = Mock()
        self.child_service = EmployeeChildService(self.client)
        self.mock_auth_header = Mock()
        self.child_service.set_auth_header(self.mock_auth_header)

    def test_get(self):
        """Test getting children for a given employee."""
        employee_id = 123
        self.client.service.Children_Get.return_value = {
            "EmployeeChildren": {
                "Child": [
                    {"Id": 1, "Name": "Alice", "FirstName": "Alice", "Initials": "A", "Gender": "Female", "Birthday": datetime(2010, 1, 1)}
                ]
            },
            "EmployeeId": employee_id,
        }

        result = self.child_service.get_current(employee_id)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, "Alice")
        self.assertEqual(result[0].first_name, "Alice")
        self.assertEqual(result[0].initials, "A")
        self.assertEqual(result[0].gender, "Female")
        self.assertEqual(result[0].birthday, datetime(2010, 1, 1))
        self.client.service.Children_Get.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting children for all employees in a company."""
        company_id = 456
        self.client.service.Children_GetAll_Employeesbycompany.return_value = [
            {
                "EmployeeChildren": {
                    "Child": [
                        {
                            "Id": 1,
                            "Name": "Alice",
                            "FirstName": "Alice",
                            "Initials": "A",
                            "Gender": "Female",
                            "Birthday": datetime(2010, 1, 1),
                        }
                    ]
                },
                "EmployeeId": 123,
            },
            {
                "EmployeeChildren": {
                    "Child": [
                        {"Id": 2, "Name": "Bob", "FirstName": "Bob", "Initials": "B", "Gender": "Male", "Birthday": datetime(2012, 2, 2)}
                    ]
                },
                "EmployeeId": 456,
            },
        ]

        result = self.child_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].name, "Bob")
        self.assertEqual(result[1].first_name, "Bob")
        self.assertEqual(result[1].initials, "B")
        self.assertEqual(result[1].gender, "Male")
        self.assertEqual(result[1].birthday, datetime(2012, 2, 2))
        self.client.service.Children_GetAll_Employeesbycompany.assert_called_once_with(
            CompanyId=company_id, _soapheaders=self.mock_auth_header
        )

    def test_delete(self):
        """Test deleting a child for a given employee."""
        employee_id = 123
        child_id = 1
        self.client.service.Child_Delete.return_value = "Success"

        result = self.child_service.delete(employee_id, child_id)

        self.assertEqual(result, "Success")
        self.client.service.Child_Delete.assert_called_once_with(
            EmployeeId=employee_id, ChildId=child_id, _soapheaders=self.mock_auth_header
        )

    def test_insert(self):
        """Test inserting a child for a given employee."""
        employee_id = 123
        child_data = {"Id": 1, "Name": "Alice", "FirstName": "Alice", "Initials": "A", "Gender": "Female", "Birthday": datetime(2010, 1, 1)}
        child = Child(employee_id=employee_id, data=child_data)
        self.client.service.Children_Insert.return_value = "Success"

        result = self.child_service.post(employee_id, child)

        self.assertEqual(result, "Success")
        _child = {
            "Id": child.id,
            "Name": child.name,
            "FirstName": child.first_name,
            "Initials": child.initials,
            "Gender": child.gender,
            "Birthday": child.birthday,
        }
        self.client.service.Children_Insert.assert_called_once_with(
            EmployeeId=employee_id, child=_child, _soapheaders=self.mock_auth_header
        )

    def test_insert_batch(self):
        """Test inserting multiple children for a given employee."""
        employee_id = 123
        children_data = [
            {"Id": 1, "Name": "Alice", "FirstName": "Alice", "Initials": "A", "Gender": "Female", "Birthday": datetime(2010, 1, 1)},
            {"Id": 2, "Name": "Bob", "FirstName": "Bob", "Initials": "B", "Gender": "Male", "Birthday": datetime(2012, 2, 2)},
        ]
        children = [Child(employee_id=employee_id, data=data) for data in children_data]
        self.client.service.Children_InsertBatch.return_value = "Success"

        result = self.child_service.post_batch(employee_id, children)

        self.assertEqual(result, "Success")
        _children = [
            {
                "Id": child.id,
                "Name": child.name,
                "FirstName": child.first_name,
                "Initials": child.initials,
                "Gender": child.gender,
                "Birthday": child.birthday,
            }
            for child in children
        ]
        self.client.service.Children_InsertBatch.assert_called_once_with(
            EmployeeId=employee_id, children=_children, _soapheaders=self.mock_auth_header
        )

    def test_update(self):
        """Test updating a child for a given employee."""
        employee_id = 123
        child_data = {"Id": 1, "Name": "Alice", "FirstName": "Alice", "Initials": "A", "Gender": "Female", "Birthday": datetime(2010, 1, 1)}
        child = Child(employee_id=employee_id, data=child_data)
        self.client.service.Children_Update.return_value = "Success"

        result = self.child_service.update(employee_id, child)

        self.assertEqual(result, "Success")
        _child = {
            "Id": child.id,
            "Name": child.name,
            "FirstName": child.first_name,
            "Initials": child.initials,
            "Gender": child.gender,
            "Birthday": child.birthday,
        }
        self.client.service.Children_Update.assert_called_once_with(
            EmployeeId=employee_id, child=_child, _soapheaders=self.mock_auth_header
        )
