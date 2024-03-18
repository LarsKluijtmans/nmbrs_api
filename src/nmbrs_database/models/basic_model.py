"""Base for the basic nmbrs database"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BasicBase = declarative_base()


class DebtorDB(BasicBase):
    """Debtor Database Table Representation

    Represents debtors in the database.

    Attributes:
        id (int): The unique identifier for the debtor.
        name (str): The name of the debtor.
        number (str): The debtor's number.
        companies (relationship): Relationship with CompanyDB.
    """

    __tablename__ = "debtors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    companies = relationship("CompanyDB", back_populates="debtor")


class CompanyDB(BasicBase):
    """Company Database Table Representation

    Represents companies in the database.

    Attributes:
        id (int): The unique identifier for the company.
        debtor_id (int): Foreign key referencing debtors.
        number (str): The company's number.
        name (str): The name of the company.
        phone_number (str): The phone number of the company.
        fax_number (str): The fax number of the company.
        email (str): The email address of the company.
        website (str): The website of the company.
        loonaangifte_tijdvak (str): The loonaangifte tijdvak of the company.
        kvk_number (str): The kvk number of the company.
        debtor (relationship): Relationship with DebtorDB.
    """

    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    debtor_id = Column(Integer, ForeignKey("debtors.id"))
    number = Column(String)
    name = Column(String)
    phone_number = Column(String)
    fax_number = Column(String)
    email = Column(String)
    website = Column(String)
    loonaangifte_tijdvak = Column(String)
    kvk_number = Column(String)
    debtor = relationship("DebtorDB", back_populates="companies")
