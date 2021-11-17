import cv2

def resize(res):
    video = cv2.VideoCapture("cut.mp4");
    ret, frame = video.read();
    if (res == 0):
        #ffmpeg - i input.jpg - vf scale = 320:240 output_320x240.png
    elif (res == 1):

    elif (res == 2):

    elif (res == 3):

    else:
        print("opcion no valida");
        exit();