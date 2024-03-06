class InvalidAuthentication(Exception):
    def __init__(
        self,
        message: str = "Invalid Authentication: The email address, API token or domain is not valid.",
    ):
        super().__init__(message)
