"""Unit tests for the CompanySalaryTableService class."""

import unittest
from unittest.mock import Mock
from src.nmbrs.service.microservices.company.salary_table import CompanySalaryTableService, SalaryTable, SalaryTableScale, SalaryTableStep


class TestCompanySalaryTableService(unittest.TestCase):
    """Unit tests for the CompanySalaryTableService class."""

    def setUp(self):
        self.client = Mock()
        self.salary_table_service = CompanySalaryTableService(self.client)
        self.mock_auth_header = Mock()
        self.salary_table_service.set_auth_header(self.mock_auth_header)

    def test_get_salary_tables(self):
        """Test retrieving salary tables associated with a company."""
        mock_salary_tables = [{"Code": 1, "Description": "Salary Table 1"}, {"Code": 2, "Description": "Salary Table 2"}]
        self.client.service.SalaryTable_Get.return_value = mock_salary_tables
        result = self.salary_table_service.get(1, 6, 2023)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], SalaryTable)
        self.assertEqual(result[0].code, 1)
        self.assertEqual(result[0].description, "Salary Table 1")
        self.client.service.SalaryTable_Get.assert_called_once_with(CompanyId=1, Period=6, Year=2023, _soapheaders=self.mock_auth_header)

    def test_get_salary_table_guids(self):
        """Test retrieving salary table guids associated with a company."""
        mock_salary_tables = [{"GuidSalaryTable": "guid1"}, {"GuidSalaryTable": "guid2"}]
        self.client.service.SalaryTable2_Get.return_value = mock_salary_tables
        result = self.salary_table_service.get_2(1, 6, 2023)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["guid1", "guid2"])
        self.client.service.SalaryTable2_Get.assert_called_once_with(CompanyId=1, Period=6, Year=2023, _soapheaders=self.mock_auth_header)

    def test_get_salary_table_scales(self):
        """Test retrieving salary table scales associated with a company."""
        mock_scales = [
            {"Scale": "Scale1", "Description": "Scale 1", "ScaleValue": 1000, "ScalePercentageMax": 10, "ScalePercentageMin": 5},
            {"Scale": "Scale2", "Description": "Scale 2", "ScaleValue": 2000, "ScalePercentageMax": 15, "ScalePercentageMin": 8},
        ]
        self.client.service.SalaryTable_GetScales.return_value = mock_scales
        result = self.salary_table_service.get_scale(1, 6, 2023)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], SalaryTableScale)
        self.assertEqual(result[0].scale, "Scale1")
        self.assertEqual(result[0].description, "Scale 1")
        self.assertEqual(result[0].value, 1000)
        self.assertEqual(result[0].percentage_max, 10)
        self.assertEqual(result[0].percentage_min, 5)
        self.client.service.SalaryTable_GetScales.assert_called_once_with(
            CompanyId=1, Period=6, Year=2023, _soapheaders=self.mock_auth_header
        )

    def test_get_salary_table_scale_guids(self):
        """Test retrieving salary table scale guids associated with a company."""
        mock_scales = [{"GuidSalaryTableScale": "guid1"}, {"GuidSalaryTableScale": "guid2"}]
        self.client.service.SalaryTable2_GetScales.return_value = mock_scales
        result = self.salary_table_service.get_scale_2(1, 6, 2023)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["guid1", "guid2"])
        self.client.service.SalaryTable2_GetScales.assert_called_once_with(
            CompanyId=1, Period=6, Year=2023, _soapheaders=self.mock_auth_header
        )

    def test_get_salary_table_steps(self):
        """Test retrieving salary table steps associated with a company."""
        mock_steps = [
            {"Step": "Step1", "StepDescription": "Step 1", "StepValue": 1000},
            {"Step": "Step2", "StepDescription": "Step 2", "StepValue": 2000},
        ]
        mock_scale = SalaryTableScale(
            1, {"Scale": "Scale1", "Description": "Scale 1", "ScaleValue": 1000, "ScalePercentageMax": 10, "ScalePercentageMin": 5}
        )
        self.client.service.SalaryTable_GetSteps.return_value = mock_steps
        result = self.salary_table_service.get_step(1, 6, 2023, mock_scale)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], SalaryTableStep)
        self.assertEqual(result[0].step, "Step1")
        self.assertEqual(result[0].description, "Step 1")
        self.assertEqual(result[0].value, 1000)
        self.client.service.SalaryTable_GetSteps.assert_called_once_with(
            CompanyId=1,
            Period=6,
            Year=2023,
            Scale={
                "Scale": "Scale1",
                "SchaalDescription": "Scale 1",
                "ScaleValue": 1000,
                "ScalePercentageMax": 10,
                "ScalePercentageMin": 5,
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_get_salary_table_step_guids(self):
        """Test retrieving salary table step guids associated with a company."""
        mock_steps = [{"GuidSalaryTableStep": "guid1"}, {"GuidSalaryTableStep": "guid2"}]
        self.client.service.SalaryTable2_GetSteps.return_value = mock_steps
        result = self.salary_table_service.get_step_2(1, 6, 2023)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["guid1", "guid2"])
        self.client.service.SalaryTable2_GetSteps.assert_called_once_with(
            CompanyId=1, Period=6, Year=2023, _soapheaders=self.mock_auth_header
        )
