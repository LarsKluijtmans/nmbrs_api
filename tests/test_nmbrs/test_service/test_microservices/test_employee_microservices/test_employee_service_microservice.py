import unittest
from datetime import datetime
from unittest.mock import Mock
from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.service import EmployeeServiceService, Service


class TestEmployeeServiceService(unittest.TestCase):
    """Unit tests for the EmployeeServiceService class."""

    def setUp(self):
        self.auth_manager = AuthManager()
        self.auth_manager.set_auth_header("test_username", "test_token", "test_domain")
        self.mock_auth_header = {
            "AuthHeaderWithDomain": {
                "Username": "test_username",
                "Token": "test_token",
                "Domain": "test_domain",
            }
        }
        self.client = Mock()
        self.employee_service_service = EmployeeServiceService(self.auth_manager, self.client)

    def test_get_all(self):
        """Test retrieving all service intervals for a given employee."""
        employee_id = 123
        expected_services = [
            {
                "Start": datetime(2020, 1, 1),
                "End": datetime(2021, 1, 1),
                "SeniorityDate": datetime(2021, 1, 1),
                "EndServiceReason": "Resignation",
            },
            {
                "Start": datetime(2023, 1, 1),
                "End": datetime(2024, 1, 1),
                "SeniorityDate": datetime(2020, 1, 1),
                "EndServiceReason": "Resignation",
            },
        ]

        self.client.service.Service_GetList.return_value = expected_services

        result = self.employee_service_service.get_all(employee_id)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Service)
        self.assertEqual(result[0].employee_id, employee_id)
        self.assertEqual(result[0].end, datetime(2021, 1, 1))
        self.client.service.Service_GetList.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_post(self):
        """Test starting a new service interval for an employee."""
        employee_id = 456
        start_date = datetime(2023, 1, 1)
        unprotected_mode = True

        self.employee_service_service.post(employee_id, start_date, unprotected_mode)

        self.client.service.Service_Insert.assert_called_once_with(
            EmployeeId=employee_id, Start=start_date, UnprotectedMode=unprotected_mode, _soapheaders=self.mock_auth_header
        )

    def test_post_2(self):
        """Test starting a new service interval with a seniority date for an employee."""
        employee_id = 456
        start_date = datetime(2023, 1, 1)
        seniority_date = datetime(2022, 1, 1)
        unprotected_mode = False

        self.employee_service_service.post_2(employee_id, start_date, seniority_date, unprotected_mode)

        self.client.service.Service_Insert2.assert_called_once_with(
            EmployeeId=employee_id,
            Start=start_date,
            Ancienniteitsdatum=seniority_date,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_delete(self):
        """Test deleting a service interval for a specific employee."""
        employee_id = 789
        self.client.service.Service_Delete.return_value = True

        result = self.employee_service_service.delete(employee_id)

        self.assertTrue(result)
        self.client.service.Service_Delete.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_stop_current(self):
        """Test stopping the current service interval for an employee."""
        employee_id = 101
        end_date = datetime(2023, 12, 31)
        end_service_reason_id = 2
        unprotected_mode = True
        self.client.service.Service_StopCurrent.return_value = True

        result = self.employee_service_service.stop_current(employee_id, end_date, end_service_reason_id, unprotected_mode)

        self.assertTrue(result)
        self.client.service.Service_StopCurrent.assert_called_once_with(
            EmployeeId=employee_id,
            End=end_date,
            EndServiceReasonId=end_service_reason_id,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.mock_auth_header,
        )

    def test_remove_out_service(self):
        """Test removing the out of service date for an employee."""
        employee_id = 202
        unprotected_mode = False
        self.client.service.Service_RemoveOutService.return_value = True

        result = self.employee_service_service.remove_out_service(employee_id, unprotected_mode)

        self.assertTrue(result)
        self.client.service.Service_RemoveOutService.assert_called_once_with(
            EmployeeId=employee_id, UnprotectedMode=unprotected_mode, _soapheaders=self.mock_auth_header
        )
