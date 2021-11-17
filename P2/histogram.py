import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(frame):
    frame_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV);
    histogram, bin = np.histogram(frame_yuv);
    plt.figure();
    plt.title("Histogram YUV")
    plt.xlabel("YUV values")
    plt.ylabel("pixels")
    plt.plot(bin[0:-1],histogram);
    plt.show();
    plt.savefig("histogram.jpg");
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    video = cv2.VideoWriter("histogram.mp4", fourcc, 30, (1920, 1080))
    video.write(cv2.imread("histogram.jpg"));
def read_video():
    video = cv2.VideoCapture("cut.mp4");
    ret, frame = video.read();
    histogram(frame);

if __name__ == '__main__':
    read_video();
