import mysql.connector
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                                  host='127.0.0.1',
                                  port='3307',
                                  database=database,
                                  use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx


def make_plot():
    aList = retrieve_return()

    #bList = np.array(aList)

    # plt.bar


def take3Variables():
    return 12, 98, 27


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


def retrieve_from_database():
    cursor, cnx = make_SQL_cursor('analysis')

    query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    # for a in cursor:
    #    print("{}, {}, {} ".format(a, b, c))

    for (a, b, c) in cursor:
        print("{}, {}, {} ".format(a, b, c))

    cursor.close()
    cnx.close()


def retrieve_return_old():  # this works
    cursor, cnx = make_SQL_cursor('analysis')

    query = ("SELECT a FROM analysis.info")
    #query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    #bList = aList[0, 0:]
    #bList = np.array(aList)
    #cList = bList[:, :1].tolist()

    cursor.close()
    cnx.close()

    return aList  # cList


def retrieve_return(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    #query = ("SELECT a FROM " + database + "." + table)
    query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    bList = []

    for i in range(0, len(aList)):
        bList.append(aList[i][0])

    cursor.close()
    cnx.close()

    return bList


def make_graph(database, table):
    data_list = retrieve_return(database, table)
    id_list = retrieve_return_id(database, table)

    plt.bar(id_list, data_list)


def retrieve_return_id(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    query = ("SELECT id FROM " + database + "." + table)
    #query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    bList = []

    for i in range(0, len(aList)):
        bList.append(aList[i][0])

    cursor.close()
    cnx.close()

    return bList


def retrieve_specific_from_database():
    cursor, cnx = make_SQL_cursor('analysis')

    query = ("SELECT a, b, c FROM analysis.info WHERE id BETWEEN %s AND %s")

    cursor.execute(query, (3, 5))

    for (a, b, c) in cursor:
        print("{}, {}, {} ".format(a, b, c))

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    # insert_into_database()
    # insert_into_database(sys.argv[1:])  # method you run from bash
    retrieve_from_database()
    # retrieve_specific_from_database()
  # retrieve_return()
