#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
import hashlib
import uuid
import sys


USERNAME = ''
PASSWORD = ''


if len(sys.argv) < 3:
    exit(1)
else:
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_users(conn):
    """
    Query all rows in the users table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM app_proxy_users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 

def create_user(conn, user):
    """
    Create a new user
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO app_proxy_users(password,username,salt)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)

 
def main():
    database = "db.sqlite3"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        salt = uuid.uuid4().hex
        hashed_password = str(hashlib.sha512(PASSWORD.encode('utf-8') + salt.encode('utf-8')).hexdigest())
        new_user = (hashed_password, USERNAME, salt)
        create_user(conn, new_user)
        select_all_users(conn)
 
 
if __name__ == '__main__':
    main()
