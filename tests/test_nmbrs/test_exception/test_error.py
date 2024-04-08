"""Unit tests for the Error class."""

import unittest
from src.nmbrs.exceptions import NmbrsBaseException


class TestError(unittest.TestCase):
    """Unit tests for the Error class."""

    def test_repr(self):
        """Test the __repr__ method of the Error class."""
        error = NmbrsBaseException(1001, "test")
        self.assertEqual(error.error_code, 1001)
        self.assertEqual(error.resource, "test")
