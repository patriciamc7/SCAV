import subprocess

def converter():

    print("Escoge la resolucion a la que quieres cambiar:")
    print("0- 720p")
    print("1- 480p")
    print("2- 360x240")
    print("3- 160x120")
    res = int(input())
    if (res == 0):
        subprocess.call(["ffmpeg", "-i","cat.mp4", "-s" ,"1280:720", "-c:a", "copy" , "scale.mp4"])
    elif (res == 1):
        subprocess.call(["ffmpeg","-i","cat.mp4","-s","720:480", "-c:a","copy", "scale.mp4"])
    elif (res == 2):
        subprocess.call(["ffmpeg", "-i", "cat.mp4","-s" ,"320:240", "-c:a", "copy","scale.mp4"])
    elif (res == 3):
        subprocess.call(["ffmpeg","-i", "cat.mp4", "-s","160:120","-c:a", "copy","scale.mp4"])
    else:
        print("opcion no valida");
        exit();
    print("Seleciona el formato en el que quieres converitr el video:")
    print("1- VP8")
    print("2- VP9")
    print("3- h265")
    print("4- AV1")
    format = int(input())
    if (format == 0):
        subprocess.call(["ffmpeg", "-i","scale.mp4", "-c:v" ,"libvpx", "-b:v" , "1M", "-c:a", "libvorbis" , "vp8.webm"])
    elif (format == 1):
        subprocess.call(["ffmpeg", "-i", "scale.mp4", "-c:v", "libvpx", "-b:v", "2M", "vp9.webm"])
    elif (format == 2):
        subprocess.call(["ffmpeg", "-i", "scale.mp4", "-c:v", "libvpx265", "-c:a", "copy", "h265.mp4"])
    elif (format == 3):
        subprocess.call(["ffmpeg", "-i", "scale.mp4", "-c:v", "libaom-av1", "-crf","30","-b:v","0", "av1.mkv"])
    else:
        print("opcion no valida");
        exit();
