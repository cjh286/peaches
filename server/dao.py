import sqlite3
from sqlite3 import Error
import os
import json

def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    tasks = {}
    tasks['tasks'] = rows
    return tasks

def main():
    database = os.path.abspath("sqlite/peaches.db")

    # create a database connection
    conn = create_connection(database)
    if conn:
        print("Query all tasks")
        rows = select_all_tasks(conn)
        print(rows)
        return rows
    else:
        print('failed')


if __name__=='__main__':
    main()