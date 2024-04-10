"""Unit tests for the EmployeePartnerService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.employee.partner import EmployeePartnerService, Partner


class TestEmployeePartnerService(unittest.TestCase):
    """Unit tests for the EmployeePartnerService class."""

    def setUp(self):
        self.client = Mock()
        self.partner_service = EmployeePartnerService(self.client)
        self.mock_auth_header = Mock()
        self.partner_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all partners of all employees in a company."""
        company_id = 123
        self.client.service.Partner_GetAll_AllEmployeesByCompany.return_value = [
            {"EmployeeId": 1, "Partner": {"PartnerName": "John Doe", "Birthday": "1990-01-01", "Gender": "Male", "Initials": "JD"}},
            {"EmployeeId": 2, "Partner": {"PartnerName": "Jane Doe", "Birthday": "1992-05-15", "Gender": "Female", "Initials": "JD"}},
        ]

        result = self.partner_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 2)

        for item in result:
            self.assertIsInstance(item, Partner)

        partner_1 = result[0]
        self.assertEqual(partner_1.employee_id, 1)
        self.assertEqual(partner_1.name, "John Doe")
        self.assertEqual(partner_1.birthday, "1990-01-01")
        self.assertEqual(partner_1.gender, "Male")
        self.assertEqual(partner_1.initials, "JD")

        partner_2 = result[1]
        self.assertEqual(partner_2.employee_id, 2)
        self.assertEqual(partner_2.name, "Jane Doe")
        self.assertEqual(partner_2.birthday, "1992-05-15")
        self.assertEqual(partner_2.gender, "Female")
        self.assertEqual(partner_2.initials, "JD")

        self.client.service.Partner_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyId=company_id, _soapheaders=self.mock_auth_header
        )
