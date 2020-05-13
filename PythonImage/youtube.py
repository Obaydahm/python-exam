import cv2
import pafy

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

url = 'https://youtu.be/1AbfRENy3OQ'
#url = 'https://www.youtube.com/watch?v=mRe-514tGMg'

video = pafy.new(url)
print(video.title)

streams = video.streams
for s in streams:
    print(s)

best = video.getbest()
#best = video.getbest(preftype="webm")
print(best.resolution, best.extension)
print(best.url)
