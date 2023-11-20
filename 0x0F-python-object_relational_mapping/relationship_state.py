#!/usr/bin/python3
"""
The class definition of a State
"""
from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """
    Create the Class State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
