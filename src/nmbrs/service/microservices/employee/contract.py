"""Microservice responsible for contract related actions on the employee level."""

from zeep import Client
from zeep.helpers import serialize_object

from ..micro_service import MicroService
from ....auth.token_manager import AuthManager
from ....data_classes.employee import Contract
from ....utils.nmbrs_exception_handler import nmbrs_exception_handler
from ....utils.return_list import return_list


class EmployeeContractService(MicroService):
    """Microservice responsible for contract related actions on the employee level."""

    def __init__(self, auth_manager: AuthManager, client: Client):
        super().__init__(auth_manager, client)

    @nmbrs_exception_handler(resource="EmployeeService:Contract_GetAll")
    def get(self, employee_id: int) -> list[Contract]:
        """
        Get all contracts for the specified employee.

        For more information, refer to the official documentation:
            [Contract_GetAll](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetAll)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Contract]: A list of Contract objects representing the employees contracts.
        """
        contracts = self.client.service.Contract_GetAll(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        return [Contract(employee_id=employee_id, data=contract) for contract in serialize_object(contracts)]

    @nmbrs_exception_handler(resource="EmployeeService:Contract_GetCurrentPeriod")
    def get_current(self, employee_id: int) -> list[Contract]:
        """
        Get a list of all active contracts for specified employee in current period.

        For more information, refer to the official documentation:
            [Contract_GetCurrentPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetCurrentPeriod)

        Args:
            employee_id (int): The ID of the employee.

        Returns:
            list[Contract]: A list of Contract objects representing the employees contracts.
        """
        contracts = self.client.service.Contract_GetCurrentPeriod(EmployeeId=employee_id, _soapheaders=self.auth_manager.header)
        contracts = serialize_object(contracts)

        _contracts = []
        for contract in contracts["EmployeeContracts"]["EmployeeContract"]:
            _contracts.append(Contract(employee_id=employee_id, data=contract))

        return _contracts

    @return_list
    @nmbrs_exception_handler(resource="EmployeeService:Contract_GetAll_AllEmployeesByCompany")
    def get_all_by_company(self, company_id: int) -> list[Contract]:
        """
        Get all contracts of all employees.

        For more information, refer to the official documentation:
            [Contract_GetAll_AllEmployeesByCompany](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_GetAll_AllEmployeesByCompany)  # pylint: disable=line-too-long

        Args:
            company_id (int): The ID of the company.

        Returns:
            list[Contract]: a list of contract objects
        """
        contracts = self.client.service.Contract_GetAll_AllEmployeesByCompany(CompanyID=company_id, _soapheaders=self.auth_manager.header)
        contracts = serialize_object(contracts)
        _contracts = []
        for employee in contracts:
            for contract in employee["EmployeeContracts"]["EmployeeContract"]:
                _contracts.append(Contract(employee_id=employee["EmployeeId"], data=contract))
        return _contracts

    @nmbrs_exception_handler(resource="EmployeeService:Contract_Delete")
    def delete(self, employee_id: int, contract_id: int):
        """
        Delete a contract from the system. This action can not be undone.

        For more information, refer to the official documentation:
            [Contract_Delete](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Delete)

        Args:
            employee_id (int): The ID of the employee.
            contract_id (int): The ID of the contract.
        """
        response = self.client.service.Contract_Delete(EmployeeId=employee_id, Id=contract_id, _soapheaders=self.auth_manager.header)
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Contract_Update")
    def update(self, employee_id: int, contract: Contract, unprotected_mode: bool):
        """
        Update the specified contract for specified employee. Contract start date can’t be updated, this field will be ignored.

        For more information, refer to the official documentation:
            [Contract_Update](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Update)

        Args:
            employee_id (int): The ID of the employee.
            contract (Contract): The Contract object to update.
            unprotected_mode (bool): Flag indicating whether unprotected mode is enabled.
        """
        _contract = {
            "ContractID": contract.id,
            "CreationDate": contract.creation_date,
            "StartDate": contract.start_date,
            "TrialPeriod": contract.trial_period,
            "EndDate": contract.end_date,
            "EmployementType": contract.employment_type,
            "EmploymentSequenceTaxId": contract.employment_sequence_tax_id,
            "Indefinite": contract.indefinite,
            "PhaseClassification": contract.phase_classification,
            "WrittenContract": contract.written_contract,
            "HoursPerWeek": contract.hours_per_week,
        }
        response = self.client.service.Contract_Update(
            EmployeeId=employee_id,
            EmployeeContract=_contract,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Contract_Insert")
    def post(self, employee_id: int, contract: Contract, unprotected_mode: bool) -> int:
        """
        Insert Contract. If the start date is before the company's current period, unprotected mode flag is required.

        For more information, refer to the official documentation:
            [Contract_Insert](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_Insert)

        Args:
            employee_id (int): The ID of the employee.
            contract (Contract): The Contract object to update.
            unprotected_mode (bool): Flag indicating whether unprotected mode is enabled.

        Returns:
            int: The response indicating the success of the operation.
        """
        _contract = {
            "ContractID": contract.id,
            "CreationDate": contract.creation_date,
            "StartDate": contract.start_date,
            "TrialPeriod": contract.trial_period,
            "EndDate": contract.end_date,
            "EmployementType": contract.employment_type,
            "EmploymentSequenceTaxId": contract.employment_sequence_tax_id,
            "Indefinite": contract.indefinite,
            "PhaseClassification": contract.phase_classification,
            "WrittenContract": contract.written_contract,
            "HoursPerWeek": contract.hours_per_week,
        }
        response = self.client.service.Contract_Update(
            EmployeeId=employee_id,
            EmployeeContract=_contract,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response

    @nmbrs_exception_handler(resource="EmployeeService:Contract_InsertCurrentPeriod")
    def post_current(self, employee_id: int, contract: Contract, unprotected_mode: bool) -> int:
        """
        Insert Contract in current period for specified employee.

        For more information, refer to the official documentation:
            [Contract_InsertCurrentPeriod](https://api.nmbrs.nl/soap/v3/EmployeeService.asmx?op=Contract_InsertCurrentPeriod)

        Args:
            employee_id (int): The ID of the employee.
            contract (Contract): The Contract object to update.
            unprotected_mode (bool): Flag indicating whether unprotected mode is enabled.

        Returns:
            int: The response indicating the success of the operation.
        """
        _contract = {
            "ContractID": contract.id,
            "CreationDate": contract.creation_date,
            "StartDate": contract.start_date,
            "TrialPeriod": contract.trial_period,
            "EndDate": contract.end_date,
            "EmployementType": contract.employment_type,
            "EmploymentSequenceTaxId": contract.employment_sequence_tax_id,
            "Indefinite": contract.indefinite,
            "PhaseClassification": contract.phase_classification,
            "WrittenContract": contract.written_contract,
            "HoursPerWeek": contract.hours_per_week,
        }
        response = self.client.service.Contract_Update(
            EmployeeId=employee_id,
            EmployeeContract=_contract,
            UnprotectedMode=unprotected_mode,
            _soapheaders=self.auth_manager.header,
        )
        return response
