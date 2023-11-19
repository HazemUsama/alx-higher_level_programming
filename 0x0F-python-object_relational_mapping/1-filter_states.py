#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
with a name starting with N.
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE 'N%'
                ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
