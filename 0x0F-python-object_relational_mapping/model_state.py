#!/usr/bin/python3
"""
python file that contains class definition of a state.
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class named state.
    (inherits from Base)

    Attributes:
    __tablename__(str): Table name of the class
    id(int): The state id of the class
    name(str): The state name of the class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
