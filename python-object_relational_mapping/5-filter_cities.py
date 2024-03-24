#!/usr/bin/python3
"""Select cities from hbtn_0e_4_usa"""
import MySQLdb
import sys


def lists_city(username, password, database, state_name):
    """ Get states from database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY '{}'
    ORDER BY cities.id ASC
                   """.format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    lists_city(mysql_username, mysql_password, database_name, state_name)
