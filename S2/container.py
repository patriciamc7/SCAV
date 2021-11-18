import subprocess

def create_container():
    subprocess.call(["ffmpeg","-ss","0", "-i","BBB.mp4", "-c", "copy", "-t",str(60), "cut60.mp4" ])
    subprocess.call( ["ffmpeg", "-i", "cut60.mp4", "-f", "mp3", "mono_mp3.mp3"])
    subprocess.call( ["ffmpeg", "-i", "cut60.mp4", "-c:a", "aac", "mono_aac.aac"])
    subprocess.call(["ffmpeg", "-i", "cut60.mp4" , "mono_aac.aac", "-c:v", "copy", "container.mp4"])
    subprocess.call(["ffmpeg", "-i", "container.mp4" , "mono_mp3.mp3", "-c:v", "copy", "container.mp4"])
    subprocess.call(["ffmpeg", "-i", "container.mp4"])
if __name__ == '__main__':
    create_container()