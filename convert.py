import os
import subprocess

for fn in os.listdir('.'):
    if os.path.isfile(fn):
        if fn.endswith(".mp4"):
            p = subprocess.run(
                ["ffmpeg",
                "-i", fn,
                "-acodec", "copy",
                "-vcodec", "copy",
                "-f", "mov", fn[:-4] + ".mov"], stderr=subprocess.STDOUT, shell=True)
            print (p)

