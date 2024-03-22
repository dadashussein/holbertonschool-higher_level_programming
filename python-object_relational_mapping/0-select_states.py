#!/usr/bin/python3
import MySQLdb
import sys


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(
    host='localhost',
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
    port=3306
)

cursor = db.cursor()
sql_query = "SELECT * FROM states ORDER BY states.id ASC"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
db.close()
