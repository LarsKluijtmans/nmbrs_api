"""
A base class for data classes that automatically initializes instance variables from a dictionary.
"""


class DataClass:
    """
    A base class for data classes that automatically initializes instance variables from a dictionary.
    """

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        return self.__dict__
