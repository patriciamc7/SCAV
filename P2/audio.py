import subprocess


def audio(modo):
    subprocess.call ([ "ffmpeg", "-","i"," stereo.flac", "-"," ac", "1", "mono.flac"])