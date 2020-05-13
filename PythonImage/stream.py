import cv2

cap = cv2.VideoCapture()
# cap.open('ped1.mp4')
cap.open('https://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1')

while (True):
    _, frame = cap.read()
    cv2.imshow("camCapture", frame)
    cv2.waitKey(1)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
