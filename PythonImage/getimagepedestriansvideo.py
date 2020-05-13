import cv2
import imutils

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cam = cv2.VideoCapture('ped1.mp4')

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    # Resizing the Image
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))

    # Detecting all the regions in the
    # Image that has a pedestrians inside it
    (regions, _) = hog.detectMultiScale(frame,
                                        winStride=(4, 4),
                                        padding=(4, 4),
                                        scale=1.05)

    # Drawing the regions in the Image
    for (x, y, w, h) in regions:
        cv2.rectangle(frame, (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)

    # Showing the output Image
    cv2.imshow("Image", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()
