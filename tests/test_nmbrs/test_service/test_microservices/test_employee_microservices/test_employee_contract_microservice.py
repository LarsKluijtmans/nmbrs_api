"""Unit tests for the EmployeeContractService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from decimal import Decimal

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.contract import EmployeeContractService, Contract


class TestEmployeeContractService(unittest.TestCase):
    """Unit tests for the EmployeeContractService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.mock_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": "test_username",
                "Token": "test_token",
                "Domain": "test_domain",
            }
        }
        self.client = Mock()
        self.employee_contract_service = EmployeeContractService(self.auth_manager, self.client)

    def test_get_all(self):
        """Test getting all contracts for a given employee."""
        employee_id = 123
        self.client.service.Contract_GetAll.return_value = [
            {
                "ContractID": 1,
                "CreationDate": datetime(2023, 1, 1),
                "StartDate": datetime(2023, 1, 1),
                "TrialPeriod": datetime(2023, 1, 1),
                "EndDate": datetime(2023, 1, 1),
                "EmployementType": 1,
                "EmploymentSequenceTaxId": 1,
                "Indefinite": True,
                "PhaseClassification": 1,
                "WrittenContract": True,
                "HoursPerWeek": Decimal("40.0"),
            }
        ]

        result = self.employee_contract_service.get(employee_id)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].creation_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].start_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].trial_period, datetime(2023, 1, 1))
        self.assertEqual(result[0].end_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].employment_type, 1)
        self.assertEqual(result[0].employment_sequence_tax_id, 1)
        self.assertEqual(result[0].indefinite, True)
        self.assertEqual(result[0].phase_classification, 1)
        self.assertEqual(result[0].written_contract, True)
        self.assertEqual(result[0].hours_per_week, Decimal("40.0"))
        self.client.service.Contract_GetAll.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_current(self):
        """Test getting current contracts for a given employee."""
        employee_id = 123
        self.client.service.Contract_GetCurrentPeriod.return_value = {
            "EmployeeContracts": {
                "EmployeeContract": [
                    {
                        "ContractID": 1,
                        "CreationDate": datetime(2023, 1, 1),
                        "StartDate": datetime(2023, 1, 1),
                        "TrialPeriod": datetime(2023, 1, 1),
                        "EndDate": datetime(2023, 1, 1),
                        "EmployementType": 1,
                        "EmploymentSequenceTaxId": 1,
                        "Indefinite": True,
                        "PhaseClassification": 1,
                        "WrittenContract": True,
                        "HoursPerWeek": Decimal("40.0"),
                    }
                ]
            },
        }

        result = self.employee_contract_service.get_current(employee_id)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].creation_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].start_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].trial_period, datetime(2023, 1, 1))
        self.assertEqual(result[0].end_date, datetime(2023, 1, 1))
        self.assertEqual(result[0].employment_type, 1)
        self.assertEqual(result[0].employment_sequence_tax_id, 1)
        self.assertEqual(result[0].indefinite, True)
        self.assertEqual(result[0].phase_classification, 1)
        self.assertEqual(result[0].written_contract, True)
        self.assertEqual(result[0].hours_per_week, Decimal("40.0"))
        self.client.service.Contract_GetCurrentPeriod.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

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
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].start_date, datetime(2023, 6, 15))

        self.client.service.Contract_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyID=company_id, _soapheaders=self.mock_auth_header
        )

    def test_delete(self):
        """Test deleting a contract for a given employee."""
        employee_id = 123
        contract_id = 1
        self.client.service.Contract_Delete.return_value = "Success"

        result = self.employee_contract_service.delete(employee_id, contract_id)

        self.assertEqual(result, "Success")
        self.client.service.Contract_Delete.assert_called_once_with(
            EmployeeId=employee_id, Id=contract_id, _soapheaders=self.mock_auth_header
        )

    def test_update(self):
        """Test updating a contract for a given employee."""
        employee_id = 123
        contract_data = {
            "ContractID": 1,
            "CreationDate": datetime(2023, 1, 1),
            "StartDate": datetime(2023, 1, 1),
            "TrialPeriod": datetime(2023, 1, 1),
            "EndDate": datetime(2023, 1, 1),
            "EmployementType": 1,
            "EmploymentSequenceTaxId": 1,
            "Indefinite": True,
            "PhaseClassification": 1,
            "WrittenContract": True,
            "HoursPerWeek": Decimal("40.0"),
        }
        contract = Contract(employee_id=employee_id, data=contract_data)
        self.client.service.Contract_Update.return_value = "Success"

        result = self.employee_contract_service.update(employee_id, contract, unprotected_mode=True)

        self.assertEqual(result, "Success")
        self.client.service.Contract_Update.assert_called_once_with(
            EmployeeId=employee_id, EmployeeContract=contract_data, UnprotectedMode=True, _soapheaders=self.mock_auth_header
        )

    def test_insert(self):
        """Test inserting a contract for a given employee."""
        employee_id = 123
        contract_data = {
            "ContractID": 1,
            "CreationDate": datetime(2023, 1, 1),
            "StartDate": datetime(2023, 1, 1),
            "TrialPeriod": datetime(2023, 1, 1),
            "EndDate": datetime(2023, 1, 1),
            "EmployementType": 1,
            "EmploymentSequenceTaxId": 1,
            "Indefinite": True,
            "PhaseClassification": 1,
            "WrittenContract": True,
            "HoursPerWeek": Decimal("40.0"),
        }
        contract = Contract(employee_id=employee_id, data=contract_data)
        self.client.service.Contract_Update.return_value = "Success"

        result = self.employee_contract_service.post(employee_id, contract, unprotected_mode=True)

        self.assertEqual(result, "Success")
        self.client.service.Contract_Update.assert_called_once_with(
            EmployeeId=employee_id, EmployeeContract=contract_data, UnprotectedMode=True, _soapheaders=self.mock_auth_header
        )

    def test_insert_current(self):
        """Test inserting a contract for a given employee in the current period."""
        employee_id = 123
        contract_data = {
            "ContractID": 1,
            "CreationDate": datetime(2023, 1, 1),
            "StartDate": datetime(2023, 1, 1),
            "TrialPeriod": datetime(2023, 1, 1),
            "EndDate": datetime(2023, 1, 1),
            "EmployementType": 1,
            "EmploymentSequenceTaxId": 1,
            "Indefinite": True,
            "PhaseClassification": 1,
            "WrittenContract": True,
            "HoursPerWeek": Decimal("40.0"),
        }
        contract = Contract(employee_id=employee_id, data=contract_data)
        self.client.service.Contract_Update.return_value = "Success"

        result = self.employee_contract_service.post_current(employee_id, contract, unprotected_mode=True)

        self.assertEqual(result, "Success")
        self.client.service.Contract_Update.assert_called_once_with(
            EmployeeId=employee_id, EmployeeContract=contract_data, UnprotectedMode=True, _soapheaders=self.mock_auth_header
        )
