import subprocess

def create_container():

    subprocess.call(["ffmpeg","-ss","0", "-i","BBB.mp4", "-c", "copy", "-t",str(60), "cut60.mp4" ])
    subprocess.call( ["ffmpeg", "-i", "cut60.mp4", "-f", "mp3", "mono_mp3.mp3"])
    subprocess.call( ["ffmpeg", "-i", "cut60.mp4", "-c:a", "aac","-b:a", "32k","mono_aac.aac"])

    subprocess.call(["ffmpeg", "-i", "cut60.mp4", "-i","mono_mp3.mp3", "-i",
                     "mono_aac.aac", "-c:v","copy", "-c:a", "copy", "-map",
                     "0:v", "-map", "1:a","-map", "2:a", "output.mp4"])
    print("Creado como output.mp4")
