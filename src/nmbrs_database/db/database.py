"""Abstract base class for databases."""

from abc import ABC, abstractmethod

from nmbrs import Nmbrs
from nmbrs.data_classes.debtor import Debtor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database(ABC):
    """Abstract base class for databases."""

    def __init__(
        self,
        api: Nmbrs,
        db_url: str,
        base: declarative_base,
    ):
        """
        Initializes the Database.

        Args:
            api (Nmbrs): Nmbrs API used to request info from nmbrs.
            db_url (str): Database URL.
            base (declarative_base): Base used to create the database.
        """
        self.api = api
        self.engine = create_engine(db_url)

        # Create tables based on provided base
        base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    @abstractmethod
    def create(self, debtors: list[Debtor]):
        """
        Abstract method to create records in the database.

        Args:
            debtors Variable length argument list.
        """
