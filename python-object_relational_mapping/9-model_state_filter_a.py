#!/usr/bin/python3
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State):
        for state in session.query(State).filter(State.name.contains('a'))\
                                        .order_by(State.id):
            print(state.id, state.name)
    else:
        print("Empty database")
    session.close()
