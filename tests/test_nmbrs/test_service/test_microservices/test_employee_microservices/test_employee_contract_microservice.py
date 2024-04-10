"""Unit tests for the EmployeeContractService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from src.nmbrs.service.microservices.employee.contract import EmployeeContractService, Contract


class TestEmployeeContractService(unittest.TestCase):
    """Unit tests for the EmployeeContractService class."""

    def setUp(self):
        self.client = Mock()
        self.employee_contract_service = EmployeeContractService(self.client)
        self.mock_auth_header = Mock()
        self.employee_contract_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test retrieving all contracts of all employees by company."""
        company_id = 123
        expected_contracts = [
            {
                "EmployeeId": 1,
                "EmployeeContracts": {
                    "EmployeeContract": [
                        {"ContractID": 1, "StartDate": datetime(2023, 6, 15)},
                        {"ContractID": 2, "StartDate": datetime(2023, 6, 16)},
                    ]
                },
            },
            {
                "EmployeeId": 2,
                "EmployeeContracts": {
                    "EmployeeContract": [
                        {"ContractID": 3, "StartDate": datetime(2023, 6, 17)},
                        {"ContractID": 4, "StartDate": datetime(2023, 6, 18)},
                    ]
                },
            },
        ]
        self.client.service.Contract_GetAll_AllEmployeesByCompany.return_value = expected_contracts

        result = self.employee_contract_service.get_all_by_company(company_id)

        self.assertEqual(len(result), 4)
        self.assertIsInstance(result[0], Contract)
        self.assertEqual(result[0].employee_id, 1)
        self.assertEqual(result[0].contract_id, 1)
        self.assertEqual(result[0].start_date, datetime(2023, 6, 15))

        self.client.service.Contract_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )
