"""This module defines custom exceptions related to parameter validation and authorization failures in nmbrs."""


class ParameterMissingError(Exception):
    """Exception raised when a required parameter is missing, empty or None."""

    def __init__(
        self,
        message: str = "Missing parameters: The following paramater are missing, empty, or None: ",
        params: list[str] = None,
    ) -> None:
        self.params = params
        self.message = f"{message}{', '.join(params)}"
        super().__init__(self.message)
