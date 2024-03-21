"""Unit tests for the Company level data classes."""

import unittest

from src.nmbrs.data_classes.company import WageTaxXML, PensionXML


class TestCompanyClasses(unittest.TestCase):
    """Unit tests for the Company level data classes."""

    def test_wage_tax_xml_class_to_dict(self):
        """Test the to_dict method of the WageTaxXML class."""
        xml_data = "<root><name>John</name><age>30</age></root>"
        wage_tax_xml = WageTaxXML(xml_data)
        expected_result = {"root": {"name": "John", "age": "30"}}
        self.assertEqual(wage_tax_xml.to_dict(), expected_result)

    def tests_pension_xml_to_dict(self):
        """Test the to_dict method of the PensionXML class."""
        xml_data = "<root><name>John</name><age>30</age></root>"
        pension_xml = PensionXML(xml_data)
        expected_result = {"root": {"name": "John", "age": "30"}}
        self.assertEqual(pension_xml.to_dict(), expected_result)
