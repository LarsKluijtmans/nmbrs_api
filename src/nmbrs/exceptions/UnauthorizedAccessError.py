class UnauthorizedAccessError(Exception):
    """
    Exception raised when unauthorized access occurs.

    [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "Unauthorized access: You do not have the rights for the resources: ",
        resources: list[str] = None,
    ) -> None:
        """
        Constructor for UnauthorizedAccessError class.

        Args:
            message (str): Explanation of the error.
            resources (list[str]): List of resources causing the unauthorized access.
        """
        if resources is None:
            resources = []
        self.message = f"{message} {', '.join(resources)}"
        super().__init__(self.message)
