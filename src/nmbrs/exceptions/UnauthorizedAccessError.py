class UnauthorizedAccessError(Exception):
    """
    Exception raised when unauthorized access occurs.
    """

    def __init__(
        self,
        message: str = "Unauthorized access: You do not have the rights for the resources: ",
        resources: list[str] = None,
    ):
        if resources is None:
            resources = []
        self.message = f"{message} {', '.join(resources)}"
        super().__init__(self.message)
