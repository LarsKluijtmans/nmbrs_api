class InvalidAuthentication(Exception):
    """
    Exception raised for invalid authentication.

    [Nmbrs exceptions details](https://support.nmbrs.com/hc/en-us/articles/360015628919-API-error-1001-Invalid-Authentication)
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
