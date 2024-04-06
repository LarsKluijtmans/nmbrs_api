"""Unit tests for the CompanySvwService class."""

import unittest
from unittest.mock import MagicMock
from src.nmbrs.data_classes.company import SVW
from src.nmbrs.service.microservices.company.svw import CompanySvwService


class TestCompanySvwService(unittest.TestCase):
    """Unit tests for the CompanySvwService class."""

    def setUp(self):
        """Set up test dependencies."""
        self.client = MagicMock()
        self.auth_header = {"Authorization": "Bearer token"}
        self.service = CompanySvwService(self.client)
        self.service.set_auth_header(self.auth_header)

    def test_get_current(self):
        """Test retrieving current SVW settings."""
        company_id = 123
        expected_result = {
            "SVWSettings": {
                "CodeCao": 456,
                "EigenrisicodragerGediffWGA": True,
                "EigenrisicodragerUniformeWAO": False,
                "EigenrisicodragerZiektewet": True,
                "RisicoGroep": 789,
                "Gediff_WGA_wn": 100.0,
                "Gediff_WGA_wg": 200.0,
                "Sector": 999,
            },
            "Sector": {"Code": "XYZ", "Description": "Sector XYZ"},
            "Risicogroep": {"Code": "ABC", "Description": "Risico Groep ABC"},
            "CAO": {"Code": "DEF", "Description": "CAO DEF"},
        }
        self.client.service.SVW_GetCurrent.return_value = expected_result

        result = self.service.get_current(company_id)

        self.assertIsInstance(result, SVW)
        self.assertEqual(result.settings.cao_code, 456)
        self.assertEqual(result.settings.eigenrisicodrager_gediff_wga, True)
        self.assertEqual(result.settings.eigenrisicodrager_uniforme_wao, False)
        self.assertEqual(result.settings.eigenrisicodrager_ziektewet, True)
        self.assertEqual(result.settings.risc_group, 789)
        self.assertEqual(result.settings.wga_wn, 100.0)
        self.assertEqual(result.settings.wga_wg, 200.0)
        self.assertEqual(result.settings.sector, 999)
        self.assertEqual(result.sector.code, "XYZ")
        self.assertEqual(result.sector.description, "Sector XYZ")
        self.assertEqual(result.risc_group.code, "ABC")
        self.assertEqual(result.risc_group.description, "Risico Groep ABC")
        self.assertEqual(result.cao.code, "DEF")
        self.assertEqual(result.cao.description, "CAO DEF")

    def test_insert_current(self):
        """Test inserting current SVW settings."""
        company_id = 123
        svw_data = {
            "SVWSettings": {
                "CodeCao": 456,
                "EigenrisicodragerGediffWGA": True,
                "EigenrisicodragerUniformeWAO": False,
                "EigenrisicodragerZiektewet": True,
                "RisicoGroep": 789,
                "Gediff_WGA_wn": 100.0,
                "Gediff_WGA_wg": 200.0,
                "Sector": 999,
            },
            "Sector": {"Code": "XYZ", "Description": "Sector XYZ"},
            "Risicogroep": {"Code": "ABC", "Description": "Risico Groep ABC"},
            "CAO": {"Code": "DEF", "Description": "CAO DEF"},
        }
        svw_obj = SVW(company_id, svw_data)
        expected_dict = svw_obj.insert_dict()

        self.service.insert_current(company_id, svw_obj)

        self.client.service.SVW_UpdateCurrent.assert_called_with(CompanyId=company_id, SVW=expected_dict, _soapheaders=self.auth_header)
