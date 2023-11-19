#!/usr/bin/python3
import MySQLdb

DataBaseName = 'hbtn_0e_0_usa'
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db=DataBaseName);
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
