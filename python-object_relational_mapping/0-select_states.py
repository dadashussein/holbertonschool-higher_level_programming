#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='2343',
    db='hbtn_0d_usa',
    port=3306
)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
db.close()
