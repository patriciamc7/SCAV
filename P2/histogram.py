import subprocess

def histogram():
    subprocess.call(["ffmpeg", "-i", "cut.mp4", "-vf", "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay", "histogram.mp4"])
    print("Se ha creado el video histogram.mp4")
