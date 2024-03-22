"""General exceptions"""


class Error(Exception):
    """Base for errors"""

    def __init__(self, message=""):
        super(Exception, self).__init__(message)
        self.message = message

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message})"


class ParameterMissingError(Error):
    """Exception raised when a required parameter is missing, empty or None."""

    def __init__(
        self,
        message: str = "Missing parameters: The following paramater are missing, empty, or None: ",
        params: list[str] = None,
    ) -> None:
        self.params = params
        self.message = f"{message}{', '.join(params)}"
        super().__init__(message)
