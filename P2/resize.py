import cv2
import subprocess
def resize(res):
    video = cv2.VideoCapture("cut.mp4");
    ret, frame = video.read();
    if (res == 0):
        subprocess.call("-", "i","BBB.mp4", "-", "vf", "scale", "=" ,"1280:720", "scale_1280x720.mp4")
    elif (res == 1):
        subprocess.call("-", "i","BBB.mp4" ,"-", "vf" ,"scale", "=" ,"720:480", "scale_720x480.mp4")
    elif (res == 2):
        subprocess.call("-", "i", "BBB.mp4", "-" ,"vf" ,"scale", "=" ,"320:240", "scale_320x240.mp4")
    elif (res == 3):
        subprocess.call("-", "i", "BBB.mp4", "-" ,"vf" ,"scale", "=" ,"160:120" ,"scale_160x120.mp4")
    else:
        print("opcion no valida");
        exit();

if __name__ == '__main__':
    print("Escoge la resolucion a la que quieres cambiar:");
    print("0- 720p");
    print("1- 480p");
    print("2- 360x240");
    print("3- 160x120");
    scale = int(input())
    resize(scale)