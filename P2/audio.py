import subprocess

def audio(modo):
   if (modo == 0):
    subprocess.call ([ "ffmpeg", "-i","cut.mp4", "-ac", "1", "mono_ac.flac"])
   elif(modo == 1):
    subprocess.call( ["ffmpeg", "-i", "cut.mp4", "-c:a", "aac", "mono_aac.aac"])
   else:
    print("opcion no valida")
    exit()
   print("se ha creado el audio en la carpeta")