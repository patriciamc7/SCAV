import subprocess

def cut(N):
    subprocess.call(["ffmpeg","-ss","0", "-i","BBB.mp4", "-c", "copy", "-t",str(N), "cut.mp4" ])
    print("Video creado en la carpeta")

