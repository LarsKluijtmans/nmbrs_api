"""Unit tests for the find_empty_params function."""
from unittest import TestCase

from src.nmbrs.utils.find_empty_params import find_empty_params


class TestFindEmptyParams(TestCase):
    """Unit tests for the find_empty_params function."""

    def test_empty_params(self):
        """Test when there are empty parameters."""
        kwargs = {"param1": None, "param2": "", "param3": "value", "param4": 0}
        expected_empty_params = ["param1", "param2"]
        self.assertEqual(find_empty_params(**kwargs), expected_empty_params)

    def test_no_empty_params(self):
        """Test when there are no empty parameters."""
        kwargs = {"param1": "value1", "param2": 123, "param3": [1, 2, 3]}
        self.assertEqual(find_empty_params(**kwargs), [])

    def test_mixed_params(self):
        """Test when there are mixed empty and non-empty parameters."""
        kwargs = {"param1": None, "param2": "value", "param3": "", "param4": "value"}
        expected_empty_params = ["param1", "param3"]
        self.assertEqual(find_empty_params(**kwargs), expected_empty_params)

    def test_empty_dict(self):
        """Test when an empty dictionary is passed."""
        kwargs = {}
        self.assertEqual(find_empty_params(**kwargs), [])

    def test_all_empty_params(self):
        """Test when all parameters are empty."""
        kwargs = {"param1": None, "param2": "", "param3": None}
        expected_empty_params = ["param1", "param2", "param3"]
        self.assertEqual(find_empty_params(**kwargs), expected_empty_params)

    def test_all_non_empty_params(self):
        """Test when all parameters are non-empty."""
        kwargs = {"param1": "value1", "param2": 123, "param3": [1, 2, 3]}
        self.assertEqual(find_empty_params(**kwargs), [])
