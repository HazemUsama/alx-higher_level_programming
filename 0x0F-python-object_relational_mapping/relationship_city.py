#!/usr/bin/python3
"""
The class definition of a City
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey


class City(Base):
    """
    Create the Class City
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

