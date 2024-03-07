from abc import ABC, abstractmethod


class DataClass(ABC):
    """
    Abstract base class defining common methods for data classes.
    """

    @abstractmethod
    def __init__(self, obj: dict) -> None:
        """
        Constructor method for DataClass.

        Args:
            obj (dict): A dictionary containing data for initialization.
        """
        self.obj = obj
        pass  # Abstract method, implementation expected in derived classes

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Abstract method to convert the instance to a dictionary.

        :return: A dictionary representation of the instance.
        """
        pass  # Abstract method, implementation expected in derived classes
