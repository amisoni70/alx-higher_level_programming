#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY 'N%'\
             ORDER BY states.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()