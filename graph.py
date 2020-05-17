import mysql.connector


def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                                  host='127.0.0.1',
                                  port='3307',
                                  database=database,
                                  use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx

