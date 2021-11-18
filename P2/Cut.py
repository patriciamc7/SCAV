import cv2
import moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import subprocess

def cut(N):
    subprocess.call(["ffmpeg","-ss","60", "-i","BBB.mp4", "-c", "copy", "-t",str(N), "cut.mp4", ])
    print("Video creado en la carpeta")
if __name__ == '__main__':
    cut(12)
