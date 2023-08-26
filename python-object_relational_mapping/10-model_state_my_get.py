#!/usr/bin/python3
""" prints the State object with the name passed as argument """

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    user = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]

    dbSQL = f'mysql+mysqldb://{user}:{psswd}@localhost:3306/{db}'
    engine = create_engine(dbSQL)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == search_name).first()

    if not states:
        print("Not found")

    else:
        print(f"{states.id}")

    session.close()
