"""Unit tests for the Error class."""

import unittest
from src.nmbrs.exceptions import Error


class TestError(unittest.TestCase):
    """Unit tests for the Error class."""

    def test_repr(self):
        """Test the __repr__ method of the Error class."""
        error_message = "Test error message"
        error = Error(error_message)
        expected_repr = f"Error({error_message})"
        self.assertEqual(repr(error), expected_repr)
