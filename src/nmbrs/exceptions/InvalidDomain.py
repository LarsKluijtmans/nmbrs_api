class InvalidDomain(Exception):
    """
    Exception raised when the specified domain (Nmbrs environment subdomain) does not exist.
    """

    def __init__(
        self,
        message: str = "Invalid domain: The specified domain does not exist. Resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for InvalidDomain class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        if resources is None:
            resources = []
        self.message = f"{message}{', '.join(resources)}"
        super().__init__(self.message)
