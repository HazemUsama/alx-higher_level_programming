#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where name matches the argument (safe this time)
"""
import MySQLdb
import sys


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("""SELECT id, name FROM cities
                    ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
