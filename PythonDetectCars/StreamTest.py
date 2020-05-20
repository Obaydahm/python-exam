import cv2
import imutils
import streamlink

streams = streamlink.streams(
    'https://www.webcamtaxi.com/en/spain/alicante/benidorm-avenida-armada-espanola.html')
# streams = streamlink.streams('https://www.youtube.com/watch?v=1EiC9bvVGnk')
# print(list(streams))
# url = streams['best'].url
url = streams['480p'].url
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    cv2.imshow('video1', frame)
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
