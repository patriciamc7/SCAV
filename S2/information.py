import subprocess

def information():
    file = open("cont_info.txt", 'w+')
    subprocess.run(["ffmpeg" ,"-i","output.mp4"],stdout=file, stderr=subprocess.STDOUT)
    file.close()
    info = []
    file_r = open("cont_info.txt", 'r')
    vid_err = 0
    aud_err = 0
    for line in file_r:
        for word in line.split():
            info.append(word)

    for i in range (0, len(info)):
        if info[i] == 'Video:':
            print("Video codec "+ info[i+1])
            vid_err =+ 1
        elif info[i] == 'Audio:':
            print("Audio codec "+info[i+1])
            aud_err =+ 1
        elif info[i] == 'progressive),':
            print("Escaneo progressivo")
        elif info[i] == 'interlace),':
            print("Escaneo enterlazado")
        elif info[i] == 'fps,':
            print("Video a "+ info[i-1]+" fps")

    if vid_err == 0:
        print("ERROR, video codec no encontrado")
        exit()

    if aud_err == 0:
        print("ERROR, audio codec no encontrado")
        exit()