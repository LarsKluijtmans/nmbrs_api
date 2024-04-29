"""Unit tests for the serialize module."""

import unittest
from src.nmbrs.data_classes.serialize import serialize
from src.nmbrs.data_classes.data_class import DataClass


class TestSerialize(unittest.TestCase):
    """Unit tests for the serialize module."""

    def test_serialize_dict(self):
        """Test serializing a dictionary."""
        data = {"key1": "value1", "key2": {"nested_key": "nested_value"}}
        result = serialize(data)
        self.assertEqual(result, data)

    def test_serialize_data_class(self):
        """Test serializing a DataClass instance."""

        class ExampleDataClass(DataClass):
            """DataClass for testing purposes."""

            def __init__(self, key1, key2):
                self.key1 = key1
                self.key2 = key2

        data_class_instance = ExampleDataClass("value1", "value2")
        expected_result = {"key1": "value1", "key2": "value2"}
        result = serialize(data_class_instance)
        self.assertEqual(result, expected_result)

    def test_serialize_list(self):
        """Test serializing a list of objects."""
        data = [{"key1": "value1"}, {"key2": "value2"}]
        expected_result = [{"key1": "value1"}, {"key2": "value2"}]
        result = serialize(data)
        self.assertEqual(result, expected_result)
