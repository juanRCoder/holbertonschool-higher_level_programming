#!/usr/bin/python3
""" file similar to model_state.py named model_city.py """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    user = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    dbSQL = f'mysql+mysqldb://{user}:{psswd}@localhost:3306/{db}'
    engine = create_engine(dbSQL)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
