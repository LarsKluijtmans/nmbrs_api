"""
Unit tests for the Nmbrs class.
"""
import unittest

from src.nmbrs import Nmbrs
from src.nmbrs.exceptions.MissingParams import MissingParams


class TestNmbrs(unittest.TestCase):
    """
    Unit tests for the Nmbrs class.
    """

    def test_empty_initializer(self):
        """
        Test initialization of Nmbrs class with default parameters.
        """
        nmbrs = Nmbrs()

        self.assertIsNotNone(nmbrs.sso_service)
        self.assertIsNotNone(nmbrs.debtor_service)
        self.assertIsNotNone(nmbrs.company_service)
        self.assertIsNotNone(nmbrs.employee_service)

    def test_standard_auth_with_missing_params(self):
        """
        Test standard authentication with missing parameters.
        """
        with self.assertRaises(MissingParams):
            # Missing token parameter should raise MissingParams
            Nmbrs(username="test_user", auth_type="token")
