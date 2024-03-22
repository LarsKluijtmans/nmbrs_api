"""General classes used on multiple levels."""

from .data_class import DataClass


class CodeDescription(DataClass):
    """A class representing a code and a description."""

    def __init__(self, data: dict) -> None:
        self.code: int | None = None
        self.description: str | None = None

        if data is None:
            return  # pragma: no cover

        self.code = data.get("Code")
        self.description = data.get("Description")
