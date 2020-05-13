import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

#    orb = cv2.ORB()
#    kp = orb.detect(frame, None) # find the keypoints with ORB
#    kp, des = orb.compute(frame, kp) # compute the descriptors with ORB
#    img2 = cv2.drawKeypoints(img, kp, color=(0, 255, 0), flags=0) # draw only keypoints location,not size and orientation
#    plt.imshow(img2), plt.show()

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    gray = np.float32(gray)
#    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # result is dilated for marking the corners, not important
#    dst = cv2.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image.
#    frame[dst > 0.01*dst.max()] = [0, 0, 255]
#    cv2.imshow("test", frame)

#    img = cv2.medianBlur(frame, 5)
#    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#    cv2.imshow("test", cimg)
    cv2.imshow("test", cv2.Canny(frame, 50, 150))
#    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_frame_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_frame_name, frame)
        img_edge_name = "opencv_edge_{}.png".format(img_counter)
        edges = cv2.Canny(frame, 100, 200)
        cv2.imwrite(img_edge_name, edges)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
