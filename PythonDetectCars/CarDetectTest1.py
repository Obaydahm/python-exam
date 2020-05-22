import cv2
import time
import numpy as np
import imutils

# Create our body classifier
# car_classifier = cv2.CascadeClassifier('Haarcascades\haarcascade_car.xml')
car_classifier = cv2.CascadeClassifier('cars4.xml')

# Initiate video capture for video file
# cap = cv2.VideoCapture('image_examples/cars.avi')
cap = cv2.VideoCapture('car.mp4')


# Loop once video is successfully loaded
while cap.isOpened():

    time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.2, 2)

    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
