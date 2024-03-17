"""Unit tests for the DataClass base class."""

import unittest
from src.nmbrs.data_classes.data_class import DataClass


class TestDataClass(unittest.TestCase):
    """Unit tests for the DataClass base class."""

    def test_to_dict(self):
        """Test converting an instance to a dictionary."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, name, age, friends):
                self.name = name
                self.age = age
                self.friends = friends

        obj = TestClass("John", 30, ["Alice", "Bob"])
        expected_dict = {"name": "John", "age": 30, "friends": ["Alice", "Bob"]}
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_to_dict_nested(self):
        """Test converting an instance with nested DataClass objects to a dictionary."""

        class NestedClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, nested):
                self.nested = nested

        nested_obj = NestedClass("nested_value")
        obj = TestClass(nested_obj)
        expected_dict = {"nested": {"value": "nested_value"}}
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_to_dict_list(self):
        """Test converting an instance with a list of DataClass objects to a dictionary."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, items):
                self.items = items

        class Item(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        items = [Item("item1"), Item("item2")]
        obj = TestClass(items)
        expected_dict = {"items": [{"value": "item1"}, {"value": "item2"}]}
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_str(self):
        """Test converting an instance to a JSON string."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, name, age, friends):
                self.name = name
                self.age = age
                self.friends = friends

        obj = TestClass("John", 30, ["Alice", "Bob"])
        expected_str = '{"name": "John", "age": 30, "friends": ["Alice", "Bob"]}'
        self.assertEqual(str(obj), expected_str)
