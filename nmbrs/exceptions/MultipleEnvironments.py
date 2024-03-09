class MultipleEnvironments(Exception):
    """
    Exception raised when the sso service is used but the user has accounts in multiple environments.
    """

    def __init__(
        self,
        message: str = "Multiple environments: User has multiple envirnments use the call sso_auth_with_domain, to specify the envirnments you want to use.",
    ) -> None:
        """
        Constructor for MultipleEnvironments class.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)
