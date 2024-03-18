"""Database class, capable of creating databases with nmbrs info."""

from nmbrs import Nmbrs
from nmbrs.data_classes.debtor import Debtor

from .db import Database, BasicDatabase


class NmbrsDatabase:
    """Database class, capable of creating databases with nmbrs info."""

    def __init__(
        self,
        api: Nmbrs,
        db_url: str = "sqlite:///nmbrs.db",
    ):
        """
        Args:
            api (Nmbrs): Nmbrs API used to request info from nmbrs.
            db_url (str (optional)): Username for Nmbrs.
        """
        self.api = api
        self.db_url = db_url
        self.database: Database | None = None

    def create_basic(self, debtors: list[Debtor] = None):
        """
        Create a basic database containing all the debtors, companies and employees.

        Args:
            debtors (list[Debtor] (optional)): List of debtors to include in the database, if None get all debtors.
        """

        if debtors is None:
            debtors = self.api.debtor.get_all()

        self.database = BasicDatabase(self.api, self.db_url)

        self.database.create(debtors)
