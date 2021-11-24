import subprocess

def information():
    p = subprocess.run(["ffprobe" ,"-v" ,"error" ,"-select_streams" ,"v:0", "-show_entries" ,"stream=codec_name", "-of", "default=noprint_wrappers=1:nokey=1" ,"output.mp4"],stdout=subprocess.PIPE)#, stdout=file , stderr = subprocess.STDOUT])
    print(p.stdout.read())
    not_err = 0

    #if not_err == 0:
    #   print("ERROR, broadcasting standard no encontrado")
    #   exit()