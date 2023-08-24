#!/usr/bin/python3
""" Lists all states that matches the argument 4"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]
    HOST = 'localhost'

    db = MySQLdb.connect(host=HOST, user=user, passwd=passwd, db=db, port=3306)

    pointer = db.cursor()
    query = ("SELECT id, name FROM states \
            WHERE name = '{}' \
            ORDER BY id ASC; ".format(search_name))
    pointer.execute(query)
    states = pointer.fetchall()

    for state in states:
        print(state)

    pointer.close()
    db.close()
