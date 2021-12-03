import os

def comparision():
    os.system("ffmpeg -i vp8.webm -i vp9.webm -filter_complex \"blend=all_mode=difference[blend];[0:v]pad=2*iw:2*ih[left];[left][1:v]overlay=w[tmp];[tmp][blend]overlay=0:h\" -c:v libx264 -crf 18 -c:a copy diff.mp4")

