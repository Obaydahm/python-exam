# Import used libraries
import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression

# Initializing the HOG person detector from OpenCV used for our pedestrian detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open video file for detection
cap = cv2.VideoCapture('car3.mp4')

# Trained XML classifiers describes some features of cars we want detect
car_cascade = cv2.CascadeClassifier('cars6.xml')

# Image size we resize our vidoe frames
image_width = 1000

# Kernel matrix used for dilating our frames
kernel = np.ones((10, 10), np.uint8)

# Get the first frame of video - gray scale it and name it frame_prev and resize it - used for frame difference in contour detection
# and image_width, image_height
ret, frame_prev = cap.read()
frame_prev = imutils.resize(
    frame_prev, width=min(image_width, frame_prev.shape[1]))
image_height, image_width, layers = frame_prev.shape
size = (image_width, image_height)
gray_prev = cv2.cvtColor(frame_prev, cv2.COLOR_BGR2GRAY)

# Print image_width, image_height
print("size:", size)

# Specify output video name and frames per second and open for output
pathOut = 'cardet.mp4'
fps = 30.0
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

# Set detect_line_x and y to eliminate areas for detection
detect_line_x = int(image_width / 4)
detect_line_y = int(image_height / 3)

# Font style for text in output video
font = cv2.FONT_HERSHEY_SIMPLEX

# Loop all frames of video or until Esc is pressed
while True:

    # Reads frames from a video
    ret, frame = cap.read()

    # Resize frame to defined size
    frame = imutils.resize(frame, width=min(image_width, frame.shape[1]))
    # Convert frame to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find absdiff of current frame and previous gray_frame
    diff_image = cv2.absdiff(gray_prev, gray)
    # Uncomment to see result
    # cv2.imshow('diff_image', diff_image)

    # Perform image thresholding - NEED TO SEE IF THIS CAN IMPROVE DETECTION
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
    # Uncomment to see result
    # cv2.imshow('thresh', thresh)

    # Apply image dilation - make points thicker
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    # Uncomment to see result
    # cv2.imshow('dilated', thresh)

    # Find contours - CHAIN_APPROX_NONE to remove all redundant points and save memory
    contours, hierarchy = cv2.findContours(
        dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Select contours appearing in the detection zone that we want
    valid_cntrs = []
    for cntr in contours:
        x, y, w, h = cv2.boundingRect(cntr)
        # Discard the contours outside our detect lines and countours under a certain size
        if (x >= detect_line_x) & (y >= detect_line_y) & (cv2.contourArea(cntr) >= 600):
            valid_cntrs.append(cntr)
    print("Number of valid contours", len(valid_cntrs))

    # Draw the contours on the original frame using green color
    cv2.drawContours(frame, valid_cntrs, -1, (127, 200, 0), 2)

    # Draw lines defining moving object detection zone
    cv2.line(frame, (0, detect_line_y),
             (image_width, detect_line_y), (100, 255, 255))
    cv2.line(frame, (detect_line_x, 0),
             (detect_line_x, image_height), (100, 255, 255))

    # Print number of approved objects
    cv2.putText(frame, "Moving object detected: " + str(len(valid_cntrs)),
                (55, 55), font, 0.6, (200, 50, 50), 2)

    # ---
    # Using HOG (Histogram od Oriented Gradients) detect people in the image
    (rects, _) = hog.detectMultiScale(
        frame, winStride=(4, 4), padding=(4, 4), scale=1.8)

    # Detects cars of different sizes in the input image using chosen CascadeClassifier for cars
    # MAYBE TUNING THESE PARAMETERS CAN IMPROVE DETECTION
    cars = car_cascade.detectMultiScale(gray, 1.2, 2)

    # Pedestrians - Drawing the rectangles in the on frame
    for (x, y, w, h) in rects:
        # Apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping boxes that are still people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # Draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Cars - Draw a rectangle for each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Write frame to output video
        out.write(frame)

        # Show frame live
    cv2.imshow('After NMS', frame)

    # Set current fram as previous frame for next frame
    gray_prev = gray

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# Close out video
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
