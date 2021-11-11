import cv2
import moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut(N):
    ffmpeg_extract_subclip("BBB.mp4", 0, N,targetname="cut.mp4");

if __name__ == '__main__':
    cut(12);