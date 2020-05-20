import cv2
import HogUtils

cascade_src = 'cars.xml'
img = cv2.imread('car1.jpg')
car_cascade = cv2.CascadeClassifier(cascade_src)
cars = car_cascade.detectMultiScale(img, 1.1, 1)
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('video', img)
cv2.waitKey(0)
