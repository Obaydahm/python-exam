import mysql.connector
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime


def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                                  host='127.0.0.1',
                                  port='3307',
                                  database=database,
                                  use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx

def insert_detected_into_database():
    cursor, cnx = make_SQL_cursor("pyexam")
    csv = pd.read_csv("./detected.csv")
    df = [tuple(int(col) for col in row) for row in csv.to_numpy()]

    #Tømmer tabellen hver gang, så vi ikke får for meget data med når vi plotter. Dette er jo kun et proof of concept.
    cursor.execute("TRUNCATE TABLE detected")

    query = "INSERT INTO detected (frame, moving_obj, cars, pedestrians) VALUES (%s,%s,%s,%s)"
    cursor.executemany(query, df)

    cnx.commit()
    
    cursor.close()
    cnx.close()
    print("inserted")

def get_detected():
    cursor, cnx = make_SQL_cursor("pyexam")
    cursor.execute("SELECT * FROM detected")
    res = cursor.fetchall()
    return res

def detected_to_bar_chart():
    print("plot")
    detected = get_detected()
    df = pd.DataFrame(detected, columns=["frames", "moving_obj", "cars", "pedestrians"])
    
    frames = df.iloc[:,0]
    frames_indices = np.arange(len(frames))
    moving_obj = df['moving_obj'].values.tolist()
    cars = df['cars'].values.tolist()
    pedestrians = df['pedestrians'].values.tolist()

    plt.plot(frames, moving_obj, "-b", label="Moving objects")
    plt.plot(frames, cars, "-r", label="Cars")
    plt.plot(frames, pedestrians, "-g", label="Pedestrians")

    plt.xticks(ticks=frames_indices, labels=frames, rotation="vertical")
    plt.legend()
    plt.title("Detected cars and pedestrains")
    plt.xlabel("Frames")
    plt.ylabel("Occourrences")

    plt.tight_layout()
    plt.savefig("./static/barchart.png")
    plt.show()


def insert_into_database(database, table, a, b, c):
    cursor, cnx = make_SQL_cursor(database)

    #localtime = time.asctime( time.localtime(time.time()) )
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    query = ("INSERT INTO " + table + " VALUES (null, %s, %s, %s, %s)")

    cursor.execute(query, (a, b, c, current_time))

    cnx.commit()

    cursor.close()
    cnx.close()

    return 'færdig'


def retrieve_return(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    #query = ("SELECT a FROM " + database + "." + table)
    query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    #aList = [value for value in cursor]
    fList = [value for value in cursor]

    aList = []
    bList = []
    cList = []

    for i in range(0, len(fList)):
        aList.append(fList[i][0])
        bList.append(fList[i][1])
        cList.append(fList[i][2])

    cursor.close()
    cnx.close()

    aList = list(map(int, aList))
    bList = list(map(int, bList))
    cList = list(map(int, cList))

    return aList, bList, cList


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


def retrieve_return_time(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    query = ("SELECT time FROM " + database + "." + table)
    #query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    bList = []

    for i in range(0, len(aList)):
        bList.append(aList[i][0])

    cursor.close()
    cnx.close()

    return bList


def make_graph(database, table):
    data_list1, data_list2, data_list3 = retrieve_return(database, table)
    id_list = retrieve_return_id(database, table)
    time_list = retrieve_return_time(database, table)

    f, ax = plt.subplots()

    plt.plot(id_list, data_list1, "-b", label="data1")
    plt.plot(id_list, data_list2, "-r", label="data2")
    plt.plot(id_list, data_list3, "-g", label="data3")
    plt.legend(loc="upper left")

    ax.set_xticks(id_list)
    ax.set_xticklabels(time_list)

    plt.show()


##########################################################
############ Functions below aren't used ################
##########################################################

def take3Variables():
    return 12, 98, 27


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
    # query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    # bList = aList[0, 0:]
    # bList = np.array(aList)
    # cList = bList[:, :1].tolist()

    cursor.close()
    cnx.close()

    return aList  # cList


def make_graph(database, table):
    data_list = retrieve_return(database, table)
    id_list = retrieve_return_id(database, table)

    plt.bar(id_list, data_list)


def retrieve_specific_from_database():
    cursor, cnx = make_SQL_cursor('analysis')

    query = ("SELECT a, b, c FROM analysis.info WHERE id BETWEEN %s AND %s")

    cursor.execute(query, (3, 5))

    for (a, b, c) in cursor:
        print("{}, {}, {} ".format(a, b, c))

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    #insert_detected_into_database()
    detected_to_bar_chart()
    # insert_into_database()
    # insert_into_database(sys.argv[1:])  # method you run from bash
    #retrieve_from_database()
    # retrieve_specific_from_database()
  # retrieve_return()
