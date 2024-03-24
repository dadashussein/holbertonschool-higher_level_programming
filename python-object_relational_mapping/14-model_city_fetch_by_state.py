#!/usr/bin/python3
"""Prints all city objects"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        for state in session.query(State).all():
            if state.id == city.state_id:
                print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
