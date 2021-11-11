import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut(N):
    #video = cv2.VideoCapture("BBB.mp4");
    #while(video.isOpened()):
     #       ret, image = video.read(); #

    ffmpeg_extract_subclip("video1.mp4", 0, N,targetname="BBB.mp4");


if __name__ == '__main__':
    cut(12);