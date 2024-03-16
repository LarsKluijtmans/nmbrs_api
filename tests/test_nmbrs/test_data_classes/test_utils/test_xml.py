"""Unit tests for the  parse_xml_to_dict and get_xml functions."""

import unittest

from src.nmbrs.data_classes.utils.xml import parse_xml_to_dict, get_xml


class TestXMLParser(unittest.TestCase):
    """Unit tests for the  parse_xml_to_dict and get_xml functions."""

    def test_parse_xml_to_dict_valid_xml(self):
        """Test parsing valid XML string."""
        xml_string = "<root><name>John</name><age>30</age></root>"
        expected_result = {"root": {"name": "John", "age": "30"}}
        self.assertEqual(parse_xml_to_dict(xml_string), expected_result)

    def test_parse_xml_to_dict_invalid_xml(self):
        """Test parsing invalid XML string."""
        xml_string = "<root><name>John</name><age>30</age>"
        self.assertEqual(parse_xml_to_dict(xml_string), xml_string)

    def test_get_xml_valid_xml(self):
        """Test retrieving XML data as a dictionary with valid XML."""
        xml_string = "<root><name>John</name><age>30</age></root>"
        expected_result = {"root": {"name": "John", "age": "30"}}
        self.assertEqual(get_xml(xml_string), expected_result)

    def test_get_xml_invalid_xml(self):
        """Test retrieving XML data as a dictionary with invalid XML."""
        xml_string = "<root><name>John</name><age>30</age>"
        self.assertIsNone(get_xml(xml_string))
