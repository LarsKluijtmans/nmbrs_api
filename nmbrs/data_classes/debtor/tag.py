from nmbrs.data_classes.data_class import DataClass


class Tag(DataClass):
    """
    A class representing debtor tag information.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for debtor tag.

        Initializes debtor tag instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing debtor tag data.
        """
        self.number: int | None = obj.get("Number", None)
        self.hex_color: str | None = obj.get("HexColor", None)
        self.tag: str | None = obj.get("Tag", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the debtor tag instance.
        """
        return {
            "number": self.number,
            "hex_color": self.hex_color,
            "tag": self.tag,
        }
