#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    HOST = 'localhost'

    db = MySQLdb.connect(host=HOST, user=user, passwd=passwd, db=db, port=3306)

    pointer = db.cursor()
    pointer.execute("SELECT * FROM states;")
    states = pointer.fetchall()

    for state in states:
        print(state)

    pointer.close()
    db.close()
