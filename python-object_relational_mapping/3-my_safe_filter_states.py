#!/usr/bin/python3
"""Select states from mysql db"""
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """ Get states from database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id
                   """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    filter_states(mysql_username, mysql_password, database_name, state_name)
