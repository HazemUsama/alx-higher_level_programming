#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':

    username, password, database, name = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM states
                WHERE name == %s
                ORDER BY id ASC""" % name)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
