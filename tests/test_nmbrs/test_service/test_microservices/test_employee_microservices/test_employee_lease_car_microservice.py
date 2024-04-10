"""Unit tests for the EmployeeLeaseCarService class."""

import unittest
from unittest.mock import Mock
from datetime import datetime
from decimal import Decimal
from src.nmbrs.service.microservices.employee.lease_car import EmployeeLeaseCarService, LeaseCar


class TestEmployeeLeaseCarService(unittest.TestCase):
    """Unit tests for the EmployeeLeaseCarService class."""

    def setUp(self):
        self.client = Mock()
        self.lease_car_service = EmployeeLeaseCarService(self.client)
        self.mock_auth_header = Mock()
        self.lease_car_service.set_auth_header(self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test getting all lease cars of all employees in a company."""
        company_id = 123
        period = 3
        year = 2024
        self.client.service.LeaseCar_GetAll_EmployeesByCompany.return_value = [
            {
                "EmployeeId": 1,
                "LeaseCars": {
                    "EmployeeLeaseCar": [
                        {
                            "Id": 1,
                            "Brand": "Brand 1",
                            "Model": "Model 1",
                            "AdditionPercentage": "5%",
                            "ContractLeaseCompany": "Company 1",
                            "ContractNumber": "123",
                            "ContractDuration": 24,
                            "LeasingPriceMonth": Decimal("500.00"),
                            "MaxMileage": 10000,
                            "PriceMoreMileage": Decimal("0.10"),
                            "PriceLessMileage": Decimal("0.05"),
                            "FirstResgistrationDate": datetime.now(),
                            "CO2Emissions": 120,
                            "LicensePlate": "ABC123",
                            "CatalogValue": Decimal("25000.00"),
                            "StartDate": datetime.now(),
                            "EndDate": datetime.now(),
                            "ReasonNoContribution": 1,
                            "ContributionPrivatePercentage": 50,
                            "ContributionPrivateUse": Decimal("250.00"),
                            "ContributionNotDeductible": Decimal("50.00"),
                        }
                    ]
                },
            }
        ]

        result = self.lease_car_service.get_all_by_company(company_id, period, year)

        self.assertEqual(len(result), 1)

        for item in result:
            self.assertIsInstance(item, LeaseCar)

        lease_car = result[0]
        self.assertEqual(lease_car.employee_id, 1)
        self.assertEqual(lease_car.id, 1)
        self.assertEqual(lease_car.brand, "Brand 1")
        self.assertEqual(lease_car.model, "Model 1")
        self.assertEqual(lease_car.additional_percentage, "5%")
        self.assertEqual(lease_car.contract_lease_company, "Company 1")
        self.assertEqual(lease_car.contract_number, "123")
        self.assertEqual(lease_car.contract_duration, 24)
        self.assertEqual(lease_car.leasing_price_month, Decimal("500.00"))
        self.assertEqual(lease_car.max_mileage, 10000)
        self.assertEqual(lease_car.price_more_milage, Decimal("0.10"))
        self.assertEqual(lease_car.price_less_milage, Decimal("0.05"))
        self.assertIsInstance(lease_car.first_registered, datetime)
        self.assertEqual(lease_car.co2_emissions, 120)
        self.assertEqual(lease_car.license_plate, "ABC123")
        self.assertEqual(lease_car.catalog_value, Decimal("25000.00"))
        self.assertIsInstance(lease_car.start_date, datetime)
        self.assertIsInstance(lease_car.end_date, datetime)
        self.assertEqual(lease_car.reason_no_contribution, 1)
        self.assertEqual(lease_car.contribution_private_percentage, 50)
        self.assertEqual(lease_car.contribution_private_use, Decimal("250.00"))
        self.assertEqual(lease_car.contribution_not_deductible, Decimal("50.00"))

        self.client.service.LeaseCar_GetAll_EmployeesByCompany.assert_called_once_with(
            CompanyId=company_id, Period=period, Year=year, _soapheaders=self.mock_auth_header
        )
