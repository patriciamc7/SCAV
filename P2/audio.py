import subprocess

def audio(modo):
    if (modo == 0):
       subprocess.call ([ "ffmpeg", "-i"," stereo.flac", "-ac", "1", "mono_ac.flac"])# ac = audio chanel
    elif(modo == 1):
        subprocess.call( ["ffmpeg", "-i", " stereo.flac", "-c:a", "1", "mono_aac.aac"])#-c:a codec aac
    else:
        print("opcion no valida")
        exit()
    print("se ha creado el video en la carpeta")