import subprocess
def resize(res):
    if (res == 0):
        subprocess.call(["ffmpeg", "-i","cut.mp4", "-s" ,"1280:720", "-c:a", "copy" , "scale_1280x720.mp4"])
    elif (res == 1):
        subprocess.call(["ffmpeg","-i","cut.mp4","-s","720:480", "-c:a","copy", "scale_720x480.mp4"])
    elif (res == 2):
        subprocess.call(["ffmpeg", "-i", "cut.mp4","-s" ,"320:240", "-c:a", "copy","scale_320x240.mp4"])
    elif (res == 3):
        subprocess.call(["ffmpeg","-i", "cut.mp4", "-s","160:120","-c:a", "copy","scale_160x120.mp4"])
    else:
        print("opcion no valida");
        exit();
    print("Se ha creado el fichero")