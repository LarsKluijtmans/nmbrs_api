"""Unit tests for the DataClass base class."""

import unittest
from decimal import Decimal
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

    def test_to_dict_decimal(self):
        """Test converting an instance with Decimal values to a dictionary."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, amount):
                """Test classs"""
                self.amount = amount

        amount = Decimal("123.45")  # Create a Decimal value
        obj = TestClass(amount)
        expected_dict = {"amount": float(amount)}  # Expected dictionary should have the Decimal value converted to float
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_getattr(self):
        """Test custom __getattr__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self):
                self.attribute = 42

        obj = TestClass()
        self.assertEqual(obj.attribute, 42)

        with self.assertRaises(AttributeError):
            _ = obj.non_existent_attribute

    def test_setattr(self):
        """Test custom __setattr__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self):
                self.attribute = 42

        obj = TestClass()
        obj.attribute = 99
        self.assertEqual(obj.attribute, 99)

    def test_delattr(self):
        """Test custom __delattr__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self):
                self.attribute = 42

        obj = TestClass()
        del obj.attribute

        with self.assertRaises(AttributeError):
            _ = obj.attribute

    def test_delattr_exception(self):
        """Test custom __delattr__ method, throwing an exception"""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self):
                self.attribute = 42

        obj = TestClass()
        self.assertTrue(obj.attribute == 42)
        del obj.attribute
        with self.assertRaises(AttributeError):
            getattr(obj, "attribute")  # Attempt to access the deleted attribute

    def test_eq(self):
        """Test custom __eq__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        obj1 = TestClass(42)
        obj2 = TestClass(42)
        obj3 = TestClass(99)

        self.assertTrue(obj1 == obj2)
        self.assertFalse(obj1 == obj3)

    def test_eq_not_equal(self):
        """Test inequality of objects with different attribute values."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, attribute1, attribute2):
                self.attribute1 = attribute1
                self.attribute2 = attribute2

        obj1 = TestClass("value1", "value2")
        obj2 = TestClass("value3", "value4")
        self.assertNotEqual(obj1, obj2)

    def test_repr(self):
        """Test custom __repr__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        obj = TestClass(42)
        self.assertEqual(repr(obj), "TestClass({'value': 42})")

    def test_len(self):
        """Test custom __len__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        obj = TestClass(42)
        self.assertEqual(len(obj), 1)

    def test_iter(self):
        """Test custom __iter__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        obj = TestClass(42)
        self.assertTrue(hasattr(obj, "__iter__"))
        self.assertTrue(hasattr(iter(obj), "__iter__"))

    def test_next(self):
        """Test custom __next__ method."""

        class TestClass(DataClass):
            """Test class"""

            def __init__(self, value):
                self.value = value

        obj = TestClass(42)
        self.assertEqual(next(iter(obj)), ("value", 42))
