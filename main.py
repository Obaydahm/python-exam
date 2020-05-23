import SQL
import DetectExam
import flaskserver

def main():
    #Download stream and start detection
    DetectExam

    #Insert result into database
    SQL.insert_detected_into_database()

    #Plot data
    SQL.detected_to_bar_chart()

if __name__ == "__main__":
    main()

