"""General classes used on multiple levels."""

from .data_class import DataClass


class CodeDescription(DataClass):
    """A class representing a code and a description."""

    def __init__(self, data: dict) -> None:
        if data is None:
            return  # pragma: no cover
        self.code: int = data.get("Code")
        self.description: str = data.get("Description")
