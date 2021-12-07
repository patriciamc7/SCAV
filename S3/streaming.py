import subprocess
def streaming():
    print("Introduce la IP a la que quieres hacer stream")
    ip = input()
    url  = "udp://@"+ip+"/5000"
    if(ip == ""):
        ip = "192.168.1.49"
    subprocess.call(["ffmpeg -re -i 1s.mp4 -vcodec copy -acodec copy -f mpegts "+url+":2222"])
