## Project overview

The project is our final delivery as part of our Python course at CPH, where we attempt to detect the moving objects - cars and pedestrians - using computer vision and deep learning in Python.

### Objectives

- Detect and count moving objects (pedestrians and cars) in a street from a live feed. (Recorded live feed.)
- Using different image detection algorithms - HOG (Histogram og Oriented Gradients) for detecting people, Cascade Classifier for detecting cars and image difference for detecting moving object.
- Showing the number of detected objects in a graph over time.

### Code and files

The project is our final delivery as part of our Python course at CPH:

- [DetectExam.py] is the main program that reads a record version of the live feed and applies the 3 differente computer vision algorithmes and mark them in the in boxes or conours in the frames. Finally to output the result into a new mp4-file and a csv-file with the findings.
- [car4.mp4] The recorded mp4-file of the live feed - https://www.youtube.com/watch?v=1EiC9bvVGnk.
- [car6.xml] An opencv-haar-classifier found on the internet, used to detect cars using OpenCV's CascadeClassifier. We chose not create our own classifier by training over many pictures. \*[graph.py] XXXX?

### Environment and dependencies

We used the following for the project:

- Python 3.7.6 (Anaconda 4.8.3)
  - numpy (1.18.1)
  - imutils (0.5.3)
  - csv
- OpenCV (opencv-python 4.2.0.34)

The project is quite generic, but we ran it on Windows 10.

We used the default HOG-descriptor that comes with OpenCV for people detection.

## Intermidiate transitions

By enabling the imshows (default commented out) for the different stages you,are able to follow how we narrow down the objects that we want to identify.

### Object detection

We tried tweaking the different parameters for all 3 methods of detection, to get an optimalt output.
The pedestrians images were very small and few in our chosen feed, which made it difficult for the HOG algorithme to detect them
