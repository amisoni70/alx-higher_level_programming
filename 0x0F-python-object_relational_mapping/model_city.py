#!/usr/bin/python3
"""
python file that contains definition of a class City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    A class named city.
    (inherits from Base)

    Attributes:
    __tablename__(str): Table name of the class
    id(int): The state id of the class
    name(str): The state name of the class
    state_id(int): represents the column of integer
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states_id'), nullable=False)
