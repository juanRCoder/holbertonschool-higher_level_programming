#!/usr/bin/python3
""" list all State objects that contain the letter a from the database """

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    user = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    dbSQL = f'mysql+mysqldb://{user}:{psswd}@localhost:3306/{db}'
    engine = create_engine(dbSQL)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")

    session.close()
