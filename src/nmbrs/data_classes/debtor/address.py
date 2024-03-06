from nmbrs.data_classes.data_class import DataClass


class Address(DataClass):
    """
    A class representing an address.
    """

    def __init__(self, obj: dict) -> None:
        """
        Constructor method for address.

        Initializes address instance with data from the provided dictionary.

        Args:
            obj (dict): A dictionary containing address data.
        """
        self.id: int | None = obj.get("Id", None)
        self.default: bool | None = obj.get("Default", None)
        self.street: str | None = obj.get("Street", None)
        self.house_number: str | None = obj.get("HouseNumber", None)
        self.house_number_addition: str | None = obj.get("HouseNumberAddition", None)
        self.postal_code: str | None = obj.get("PostalCode", None)
        self.city: str | None = obj.get("City", None)
        self.state_province: str | None = obj.get("StateProvince", None)
        self.country_iso_code: str | None = obj.get("CountryISOCode", None)

    def to_dict(self) -> dict:
        """
        Convert the instance to a dictionary.

        :return: A dictionary representation of the address instance.
        """
        return {
            "id": self.id,
            "default": self.default,
            "street": self.street,
            "house_number": self.house_number,
            "house_number_addition": self.house_number_addition,
            "postal_code": self.postal_code,
            "city": self.city,
            "state_province": self.state_province,
            "country_iso_code": self.country_iso_code,
        }
