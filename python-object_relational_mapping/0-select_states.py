#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    database_mySQL = MySQLdb.connect(user, password, db, port=3306)

    pointer = database_mySQL.cursor()
    pointer.execute("SELECT * FROM states;")
    states = pointer.fetchall()

    for state in states:
        print(state)
