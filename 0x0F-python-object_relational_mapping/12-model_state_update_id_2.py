#!/usr/bin/python3

"""
A python script that changes the name of a state object
from the database hbtn_0e_6_usa

Takes 3 arguments: mysql username, mysql password and database name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(id="2").first()
    state.name = "New Mexico"
    session.commit()
    session.close()
