#!/usr/bin/python3
""" Lists all states with a name starting with 'N' """
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    HOST = 'localhost'

    db = MySQLdb.connect(host=HOST, user=user, passwd=passwd, db=db, port=3306)

    pointer = db.cursor()
    query = ("SELECT id, name FROM states \
    WHERE name LIKE 'N%' \
    ORDER BY id ASC; ")

    pointer.execute(query)
    states = pointer.fetchall()

    for state in states:
        print(state)

    pointer.close()
    db.close()
