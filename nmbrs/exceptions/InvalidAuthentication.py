class InvalidAuthentication(Exception):
    """
    Exception raised for invalid authentication.

    [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360013526891-Nmbrs-API-error-codes)
    """

    def __init__(
        self,
        message: str = "Invalid Authentication: The email address, API token or domain is not valid.",
    ) -> None:
        """
        Constructor for InvalidAuthentication class.

        Args:
            message (str): Explanation of the error.
        """
        super().__init__(message)
