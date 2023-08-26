#!/usr/bin/python3
""" print the first State object from the database 'hbtn_0e_6_usa """

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

    states = session.query(State).order_by(State.id).first()

    if not states:
        print("Nothing")

    else:
        print(f"{states.id}: {states.name}")

    session.close()
