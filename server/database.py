import sqlite3
from sqlite3 import Error
import os
import json

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn


def select_all_data(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM peaches")

    rows = cur.fetchall()
    peaches = {}
    peaches['name'] = rows
    return peaches


def main():
    database = os.path.abspath("sqlite/database.db")

    # create a database connection
    conn = create_connection(database)
    if conn:
        print("Query all data")
        rows = select_all_data(conn)
        print(rows)
        return rows
    else:
        print('failed')


if __name__=='__main__':
    main()