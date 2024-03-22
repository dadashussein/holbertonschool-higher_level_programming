#!/usr/bin/python3
"""Select states from mysql db"""
import MySQLdb
import sys


def get_states(username, password, database):
    """ Get states from database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    get_states(mysql_username, mysql_password, database_name)
