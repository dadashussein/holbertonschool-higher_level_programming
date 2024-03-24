#!/usr/bin/python3
"""Select cities from hbtn_0e_4_usa"""
import MySQLdb
import sys


def lists_city(username, password, database):
    """ Get states from database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities,
                states WHERE cities.state_id = states.id ORDER BY cities.id
                   """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    lists_city(mysql_username, mysql_password, database_name)
