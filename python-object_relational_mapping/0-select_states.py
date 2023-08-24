#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb
aa
if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)

    pointer = db.cursor()
    pointer.execute("SELECT * FROM states;")
    states = pointer.fetchall()

    for state in states:
        print(state)
