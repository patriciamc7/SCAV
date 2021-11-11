import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def histogram(frame):
    histogram = np.histogram(frame);
    #plt.plot(histogram);

def read_video():
    video = cv2.VideoCapture("cut.mp4");
    ret, frame = video.read()
    histogram(frame);

if __name__ == '__main__':
    read_video();


    #while cap.isOpened():
     #   ret, frame = cap.read()

      #  cv2.imshow('frame', frame)
       # if cv2.waitKey(25) & 0xFF == ord('q'):
        #    break

    #cap.release()
    #cv2.destroyAllWindows()