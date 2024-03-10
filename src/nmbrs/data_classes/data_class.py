class DataClass:
    """
    A base class for data classes that automatically initializes instance variables from a dictionary.
    """

    def __init__(self, obj: dict) -> None:
        """
        Initializes instance variables based on the provided dictionary.

        Args:
            obj (dict): A dictionary containing data to initialize instance variables.
        """
        self.__dict__.update(obj)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return self.__dict__
