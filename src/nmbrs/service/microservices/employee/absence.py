"""Microservice responsible for absence related actions on the employee level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService


class EmployeeAbsenceService(MicroService):
    """Microservice responsible for absence related actions on the employee level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header
