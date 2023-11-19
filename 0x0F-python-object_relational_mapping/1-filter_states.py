#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    UserName, UserPass, DataBaseName = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server using 'with' statement
    with MySQLdb.connect(host="localhost", port=3306, user=UserName, passwd=UserPass, db=DataBaseName) as conn:
        with conn.cursor() as cur:
            # Execute the query for states starting with 'N'
            cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
            query_rows = cur.fetchall()

            # Print results
            for row in query_rows:
                print(row)

