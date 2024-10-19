# import datetime
# import mysql.connector

# __cnx = None

# def get_sql_connection():
#   print("Opening mysql connection")
#   global __cnx

#   if __cnx is None:
#     __cnx = mysql.connector.connect(user='root', password='mysql123', host='localhost', port='3306', database='grocery_store')

#   return __cnx


import mysql.connector
from mysql.connector import Error

__cnx = None

def get_sql_connection():
    print("Opening MySQL connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                user='root',
                password='mysql123',
                host='localhost',
                port='3306',
                database='grocery_store'
            )
            if __cnx.is_connected():
                print("Connection successful")

        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            __cnx = None

    return __cnx

