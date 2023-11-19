#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    import sys

    UserName = sys.argv[1]
    UserPass = sys.argv[2]
    DataBaseName = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=UserName, passwd=UserPass, db=DataBaseName);
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
