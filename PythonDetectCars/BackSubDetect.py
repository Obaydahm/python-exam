import cv2
import imutils

# Initializing the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

backSub = cv2.createBackgroundSubtractorMOG2()

# cap = cv2.VideoCapture('1430inside.mp4')
# cap = cv2.VideoCapture('1422outside.mp4')
# cap = cv2.VideoCapture('1517outside.mp4')
cap = cv2.VideoCapture('1607outside.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars4.xml')

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frame = cap.read()
    # print(cap.get(3), cap.get(4)) # Print frame width, height

    frame = imutils.resize(frame, width=min(1000, frame.shape[1]))

    frame = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)

    fgMask = backSub.apply(frame)

    # Detecting all the regions in the image that has a pedestrians inside it
    # (regions, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.05)
    (regions, _) = hog.detectMultiScale(
        fgMask, winStride=(4, 4), padding=(4, 4), scale=1.05)

    # convert to gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    # cars = car_cascade.detectMultiScale(fgMask, 1.1, 1)
    # cars = car_cascade.detectMultiScale(fgMask, 1.03, 9)
    # cars = car_cascade.detectMultiScale(frame, 1.03, 9)
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)
    # cars1 = car_cascade.detectMultiScale(frame, 1.5, 2)

    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # Drawing the regions in the Image
    for (x, y, w, h) in regions:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('video1', frame)
    cv2.imshow('FG Mask', fgMask)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
