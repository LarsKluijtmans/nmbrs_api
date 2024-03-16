"""Unit tests for the DataClass base class."""

import unittest
from src.nmbrs.data_classes.data_class import DataClass


class TestDataClass(DataClass):
    """A subclass of DataClass for testing purposes."""

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.key1: str = obj.get("Key1", None)
        self.key2: str = obj.get("Key2", None)


class TestDataClassMethods(unittest.TestCase):
    """Unit tests for the DataClass base class."""

    def test_to_dict(self):
        """Test the to_dict method of the DataClass."""
        # Create an instance of TestDataClass
        obj = {"Key1": "value1", "Key2": "value2"}
        test_instance = TestDataClass(obj)

        # Expected result
        expected_result = {"key1": "value1", "key2": "value2"}

        # Check if the to_dict method returns the expected result
        self.assertEqual(test_instance.to_dict(), expected_result)
