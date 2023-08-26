#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    dbSQL = f'mysql+mysqldb://{user}:{psswd}@localhost:3306/{db}'
    engine = create_engine(dbSQL)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
