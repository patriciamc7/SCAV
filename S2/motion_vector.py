import subprocess

def motion_vectors():
    subprocess.call(["ffmpeg", "-flags2", "+export_mvs" ,"-i", "cut.mp4", "-vf" ,"codecview=mv=pf+bf+bb", "motion_vec.mp4"])
    print("Video creado")