"""Unit tests for the return_list decorator."""

import unittest

from src.nmbrs_soap.utils.return_list import return_list


class TestReturnListDecorator(unittest.TestCase):
    """Unit tests for the return_list decorator."""

    @return_list
    def return_none(self):
        """Function returns None."""
        return None

    @return_list
    def return_list_item(self):
        """Function returns a list."""
        return [1, 2, 3]

    @return_list
    def return_non_list(self):
        """Function returns a non-list item."""
        return "non_list_result"

    def test_return_none(self):
        """Test that the decorated function returns an empty list when the original function returns None."""
        self.assertEqual(self.return_none(), [])

    def test_return_list_item(self):
        """Test that the decorated function returns the same list when the original function returns a list."""
        self.assertEqual(self.return_list_item(), [1, 2, 3])

    def test_return_non_list(self):
        """Test that the decorated function wraps the non-list result in a list."""
        self.assertEqual(self.return_non_list(), ["non_list_result"])

    def test_raise_type_error(self):
        """Test that the decorated function raises TypeError when the original function raises TypeError."""

        @return_list
        def raise_type_error():
            """Faulty function trying to loop over None."""
            raise TypeError("'NoneType' object is not iterable")

        self.assertEqual(raise_type_error(), [])

    def test_raise_exception_on_other_error(self):
        """Test that the decorated function raises the original exception if it is not a TypeError."""

        @return_list
        def raise_custom_error():
            """Raise ValueError."""
            raise ValueError("Custom error message")

        with self.assertRaises(ValueError) as context:
            raise_custom_error()
        self.assertEqual(str(context.exception), "Custom error message")

    def test_raise_exception_when_type_error_not_caused_by_looping_none(self):
        """
        Test that the decorated function raises the original exception if the message was not:
            - "'NoneType' object is not iterable"
        """

        @return_list
        def raise_custom_error():
            """Raise TypeError with Custom error message."""
            raise TypeError("Custom error message")

        with self.assertRaises(TypeError) as context:
            raise_custom_error()
        self.assertEqual(str(context.exception), "Custom error message")
