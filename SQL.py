import mysql.connector


def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                                  host='127.0.0.1',
                                  port='3307',
                                  database=database,
                                  use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx


def take3Variables():
    return 43, 22, 5


def insert_into_database():
    # this below could be any method, but it's these variables that are inserted into the database
    a, b, c = take3Variables()

    cursor, cnx = make_SQL_cursor('analysis')  # database

    # make a table named "analysis"
    query = ("INSERT INTO info VALUES (null, %s, %s, %s)")  # table

    cursor.execute(query, (a, b, c))

    cnx.commit()

    cursor.close()
    cnx.close()

    return 'færdig'


if __name__ == "__main__":
    insert_into_database()
