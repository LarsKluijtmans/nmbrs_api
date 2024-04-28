"""Test cases for the EmployeeAbsenceService class."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from src.nmbrs.auth.token_manager import AuthManager
from src.nmbrs.service.microservices.employee.absence import EmployeeAbsenceService, Absence


class TestEmployeeAbsenceService(unittest.TestCase):
    """Test cases for the EmployeeAbsenceService class."""

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
        self.employee_absence_service = EmployeeAbsenceService(self.auth_manager, self.client)

    def test_get(self):
        """Test the get method of EmployeeAbsenceService."""
        employee_id = 123
        expected_absences = [
            {"AbsenceId": 1, "Comment": "Sick leave", "Percentage": 100, "Start": datetime(2023, 1, 1), "End": datetime(2023, 1, 5)},
            {"AbsenceId": 2, "Comment": "Vacation", "Percentage": 100, "Start": datetime(2023, 2, 1), "End": datetime(2023, 2, 5)},
        ]
        self.client.service.Absence_GetList.return_value = expected_absences

        result = self.employee_absence_service.get_current(employee_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_absences))
        for item in result:
            self.assertIsInstance(item, Absence)
        self.client.service.Absence_GetList.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_2(self):
        """Test the get_2 method of EmployeeAbsenceService."""
        employee_id = 123
        expected_absences = [
            {
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
            },
            {
                "AbsenceId": 2,
                "Comment": "Vacation",
                "Percentage": 100,
                "Start": datetime(2023, 2, 1),
                "End": datetime(2023, 2, 5),
                "AbsenceCause": {"CauseId": 2, "Cause": "Vacation"},
            },
        ]
        self.client.service.Absence2_GetList.return_value = expected_absences

        result = self.employee_absence_service.get_current_2(employee_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_absences))
        for item in result:
            self.assertIsInstance(item, Absence)
        self.client.service.Absence2_GetList.assert_called_once_with(EmployeeId=employee_id, _soapheaders=self.mock_auth_header)

    def test_get_all_by_company(self):
        """Test the get_all_by_company method of EmployeeAbsenceService."""
        company_id = 456
        expected_absences = [
            {
                "EmployeeId": 123,
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
            },
            {
                "EmployeeId": 456,
                "AbsenceId": 2,
                "Comment": "Vacation",
                "Percentage": 100,
                "Start": datetime(2023, 2, 1),
                "End": datetime(2023, 2, 5),
            },
        ]
        self.client.service.Absence_GetAll_AllEmployeesByCompany.return_value = expected_absences

        result = self.employee_absence_service.get_all_by_company(company_id)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(expected_absences))
        for item in result:
            self.assertIsInstance(item, Absence)
        self.client.service.Absence_GetAll_AllEmployeesByCompany.assert_called_once_with(
            CompanyId=company_id, _soapheaders=self.mock_auth_header
        )

    def test_insert(self):
        """Test the insert method of EmployeeAbsenceService."""
        employee_id = 123
        absence = Absence(
            employee_id=employee_id,
            data={
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
            },
        )

        self.client.service.Absence_Insert.return_value = 200

        response = self.employee_absence_service.post(employee_id, absence)

        self.assertEqual(response, 200)
        self.client.service.Absence_Insert.assert_called_once_with(
            EmployeeId=employee_id,
            Absence={
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_2(self):
        """Test the insert_2 method of EmployeeAbsenceService."""
        employee_id = 123
        absence = Absence(
            employee_id=employee_id,
            data={
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
            },
        )

        self.client.service.Absence2_Insert.return_value = 200

        response = self.employee_absence_service.post_2(employee_id, absence)

        self.assertEqual(response, 200)
        self.client.service.Absence2_Insert.assert_called_once_with(
            EmployeeId=employee_id,
            Absence={
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
            },
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_partial_recovery(self):
        """Test the insert_partial_recovery method of EmployeeAbsenceService."""
        employee_id = 123
        response_status_code = 200
        absence_id = 1
        start_date = datetime(2023, 1, 1)
        report_date = datetime(2023, 1, 5)
        percentage = 50
        comment = "Partial recovery"

        self.client.service.Absence_PartialRecoveryInsert.return_value = response_status_code

        response = self.employee_absence_service.post_partial_recovery(
            employee_id, absence_id, start_date, report_date, percentage, comment
        )

        self.assertEqual(response, response_status_code)
        self.client.service.Absence_PartialRecoveryInsert.assert_called_once_with(
            EmployeeId=employee_id,
            AbsenceID=absence_id,
            StartDate=start_date,
            Reportdate=report_date,
            Percent=percentage,
            Comment=comment,
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_recovery(self):
        """Test the insert_recovery method of EmployeeAbsenceService."""
        employee_id = 123
        response_status_code = "200"
        absence_id = 1
        last_day_absence = datetime(2023, 1, 5)
        report_date = datetime(2023, 1, 10)
        comment = "Recovery"

        self.client.service.Absence_RecoveryInsert.return_value = response_status_code

        response = self.employee_absence_service.post_recovery(employee_id, absence_id, last_day_absence, report_date, comment)

        self.assertEqual(response, response_status_code)
        self.client.service.Absence_RecoveryInsert.assert_called_once_with(
            EmployeeId=employee_id,
            AbsenceID=absence_id,
            Lastdayabsence=last_day_absence,
            Reportdate=report_date,
            Comment=comment,
            _soapheaders=self.mock_auth_header,
        )

    def test_insert_notification(self):
        """Test the insert_notification  method of EmployeeAbsenceService."""
        employee_id = 123
        absence = Absence(
            employee_id=employee_id,
            data={
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
            },
        )

        self.client.service.AbsenceNotification_Insert.return_value = 200

        response = self.employee_absence_service.post_notification(employee_id, absence)

        self.assertEqual(response, 200)
        self.client.service.AbsenceNotification_Insert.assert_called_once_with(
            EmployeeId=employee_id,
            Absence={
                "AbsenceCause": {"CauseId": 1, "Cause": "Sickness"},
                "AbsenceId": 1,
                "Comment": "Sick leave",
                "Percentage": 100,
                "Start": datetime(2023, 1, 1),
                "RegistrationStartDate": datetime(2023, 1, 1),
                "End": datetime(2023, 1, 5),
                "RegistrationEndDate": datetime(2023, 1, 5),
                "Dossier": "Dossier001",
                "Dossiernr": 123456,
            },
            _soapheaders=self.mock_auth_header,
        )
